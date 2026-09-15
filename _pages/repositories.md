---
layout: page
permalink: /repositories/
title: code
nav: true
nav_order: 5
description: "Selected public repositories and implementation work."
---

{% if site.data.repositories.github_users %}
## GitHub profile
{% for user in site.data.repositories.github_users %}
{% include repository/repo_user.liquid username=user %}
{% endfor %}
{% endif %}

{% if site.data.repositories.github_repos %}
## Selected repositories
{% for repo in site.data.repositories.github_repos %}
{% include repository/repo.liquid repository=repo %}
{% endfor %}
{% endif %}
