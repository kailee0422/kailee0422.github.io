#!/usr/bin/env python3
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

USERNAME = os.environ.get("LEETCODE_USERNAME", "KevinLee777")
OUTPUT = Path("_data/leetcode.json")
ENDPOINT = "https://leetcode.com/graphql"

QUERY = r"""
query portfolioLeetCodeStats($username: String!) {
  matchedUser(username: $username) {
    username
    profile {
      ranking
    }
    submitStatsGlobal {
      acSubmissionNum {
        difficulty
        count
        submissions
      }
    }
    languageProblemCount {
      languageName
      problemsSolved
    }
  }
}
"""

payload = json.dumps(
    {
        "operationName": "portfolioLeetCodeStats",
        "variables": {"username": USERNAME},
        "query": QUERY,
    }
).encode("utf-8")

request = Request(
    ENDPOINT,
    data=payload,
    method="POST",
    headers={
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (compatible; GitHub-Actions-LeetCode-Portfolio/1.0)",
        "Referer": f"https://leetcode.com/u/{USERNAME}/",
        "Origin": "https://leetcode.com",
    },
)

with urlopen(request, timeout=30) as response:
    result = json.loads(response.read().decode("utf-8"))

if result.get("errors"):
    raise RuntimeError(f"LeetCode GraphQL error: {result['errors']}")

user = result.get("data", {}).get("matchedUser")
if not user:
    raise RuntimeError(f"LeetCode user '{USERNAME}' was not found.")

counts = {
    row["difficulty"]: int(row["count"])
    for row in user["submitStatsGlobal"]["acSubmissionNum"]
}

total = counts.get("All", 0)
easy = counts.get("Easy", 0)
medium = counts.get("Medium", 0)
hard = counts.get("Hard", 0)

def pct(value: int) -> float:
    return round((value / total) * 100, 1) if total else 0.0

raw_languages = sorted(
    user.get("languageProblemCount") or [],
    key=lambda item: int(item.get("problemsSolved", 0)),
    reverse=True,
)

top_languages = raw_languages[:3]
top_language_count = max(
    [int(item.get("problemsSolved", 0)) for item in top_languages] or [0]
)

languages = []
for item in top_languages:
    solved = int(item.get("problemsSolved", 0))
    relative_pct = round((solved / top_language_count) * 100, 1) if top_language_count else 0.0
    languages.append(
        {
            "name": item.get("languageName", "Unknown"),
            "problems_solved": solved,
            "relative_pct": relative_pct,
        }
    )

new_data = {
    "username": user.get("username", USERNAME),
    "profile_url": f"https://leetcode.com/u/{USERNAME}/",
    "solved": {
        "total": total,
        "easy": easy,
        "medium": medium,
        "hard": hard,
    },
    "distribution": {
        "easy_pct": pct(easy),
        "medium_pct": pct(medium),
        "hard_pct": pct(hard),
        "easy_plus_medium_pct": round(pct(easy) + pct(medium), 1),
    },
    "languages": languages,
    "ranking": user.get("profile", {}).get("ranking"),
}

old_data = {}
if OUTPUT.exists():
    try:
        old_data = json.loads(OUTPUT.read_text(encoding="utf-8"))
    except Exception:
        old_data = {}

old_comparable = {k: v for k, v in old_data.items() if k != "last_updated"}
if old_comparable == new_data:
    print("LeetCode statistics are unchanged; no file update needed.")
else:
    new_data["last_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(new_data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        f"Updated {OUTPUT}: total={total}, easy={easy}, "
        f"medium={medium}, hard={hard}"
    )
