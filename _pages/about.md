---
layout: about
title: about
permalink: /
subtitle: "Software & AI Engineering · Embedded Systems"

profile:
  align: right
  image: prof_pic.jpg
  image_circular: false
  more_info: >
    <p>National Yang Ming Chiao Tung University</p>
    <p>Taiwan</p>

selected_papers: false
social: true

announcements:
  enabled: false
  scrollable: false
  limit: 5
---

Hi! I am **Chong-Kai Li**, a master's student at the **Institute of Artificial Intelligence, National Yang Ming Chiao Tung University (NYCU)**.

My career interests are centered on **software engineering, embedded and edge systems, and AI engineering**. I enjoy building reliable end-to-end systems that connect systems software, networking or IoT components with intelligent applications. My technical experience spans **C/C++, Python, Linux and Shell, Docker, networking, MQTT/IoT integration, computer vision, LLM/RAG systems, and deployable machine learning**.

My projects cover several engineering layers, including multi-source data pipelines, distributed monitoring, multi-agent automation, IoT-enabled smart energy systems, academic research assistants, and computer-vision applications. I am especially interested in the **engineering process behind robust software and intelligent systems**, from data collection and system integration to model deployment and user-facing applications.

I have also worked as an **AI Engineer Intern**, where I developed an intelligent question-answering system for manufacturing operations and applied **RAG, SFT, and LoRA** for domain-specific LLM adaptation.

[**View Projects**]({{ '/projects/' | relative_url }}) ·
[**View CV**]({{ '/cv/' | relative_url }}) ·
[**Awards & Honors**]({{ '/awards/' | relative_url }}) ·
[**LeetCode**]({{ '/leetcode/' | relative_url }}) ·
[**Download Résumé**]({{ '/assets/pdf/Chong-Kai_Li_Resume.pdf' | relative_url }})

## Engineering focus

- **Software & Systems** — C/C++, Python, Linux, Shell, Docker, networking, data pipelines, and deployable services.
- **Embedded & Edge Systems** — MQTT, IoT sensing, real-time monitoring, device-to-service integration, and edge-facing software workflows.
- **AI Engineering** — PyTorch, Transformers, RAG, LLM agents, computer vision, model integration, and application deployment.

## Selected projects

<div class="home-project-grid">
  <a class="home-project-card" href="{{ '/projects/#attack-path' | relative_url }}">
    <span>Software & AI Systems</span>
    <strong>Multi-Source Attack Path Reconstruction</strong>
    <small>Data pipelines · Networking · Transformers · Docker</small>
  </a>

  <a class="home-project-card" href="{{ '/projects/#agrivoltaics' | relative_url }}">
    <span>Embedded / IoT</span>
    <strong>Agrivoltaics Smart Micro-grid</strong>
    <small>MQTT · Sensors · Real-time monitoring · ML</small>
  </a>

  <a class="home-project-card" href="{{ '/projects/#irc' | relative_url }}">
    <span>AI Engineering</span>
    <strong>Intelligent Research Companion</strong>
    <small>RAG · OCR · LangChain · Local LLMs</small>
  </a>
</div>

<style>
  .home-project-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 0.8rem;
    margin-top: 1rem;
  }

  .home-project-card {
    display: flex;
    flex-direction: column;
    gap: 0.45rem;
    padding: 1rem;
    border: 1px solid var(--global-divider-color);
    border-radius: 14px;
    text-decoration: none !important;
    background: var(--global-card-bg-color, transparent);
    transition: transform 0.18s ease, border-color 0.18s ease;
  }

  .home-project-card:hover {
    transform: translateY(-2px);
    border-color: var(--global-theme-color);
  }

  .home-project-card span {
    color: var(--global-theme-color);
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
  }

  .home-project-card strong {
    color: var(--global-text-color);
    line-height: 1.4;
  }

  .home-project-card small {
    color: var(--global-text-color-light);
    line-height: 1.5;
  }

  @media (max-width: 760px) {
    .home-project-grid {
      grid-template-columns: 1fr;
    }
  }
</style>
