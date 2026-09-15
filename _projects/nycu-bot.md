---
layout: page
title: "NYCU-Bot: Multi-Agent Award Announcement & Social Media Automation"
description: "A hierarchical multi-agent system that detects new award announcements and publishes bilingual posts across multiple social platforms."
importance: 2
category: agents
github: https://github.com/kailee0422/automatic-social-media-post
github_stars: kailee0422/automatic-social-media-post
---

## Overview

NYCU-Bot is a **multi-agent automation system** that monitors an NYCU institute website for new award announcements and automatically prepares bilingual congratulatory content for social media.

The system uses a hierarchical agent architecture with an **InformationAgent**, **Father/Mother coordinator agents**, and **platform-specific publishing agents** connected through an internal message bus. A LangChain-based **ContentAgent** uses a locally hosted **DeepSeek-R1 7B** model through Ollama to generate localized captions and hashtags.

The workflow supports both **one-shot execution** and **continuous polling**, and targets platforms including **X/Twitter, Facebook, Instagram, LinkedIn, and Reddit**.

**Topics:** Multi-Agent Systems · LLMs · LangChain · Ollama · Social Media Automation · Web Monitoring

[GitHub repository](https://github.com/kailee0422/automatic-social-media-post)
