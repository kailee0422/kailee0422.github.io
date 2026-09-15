---
layout: page
title: projects
permalink: /projects/
description: "Software, AI, IoT, and systems projects with implementation links and selected demos."
nav: true
nav_order: 2
---

<div class="portfolio-projects">

  <div class="projects-intro">
    <p>
      Selected projects spanning <strong>software engineering, AI systems, IoT/edge integration,
      automation, and computer vision</strong>. Source code is linked directly from each project,
      so a separate Code page is not necessary.
    </p>
  </div>

  <article class="project-card">
    <div class="project-heading">
      <div>
        <span class="project-kicker">SOFTWARE & AI SYSTEMS · 2025–2026</span>
        <h2>Multi-Source Attack Path Reconstruction with Weighted Attack Graphs</h2>
      </div>
      <div class="project-links">
        <a href="https://github.com/kailee0422/network-threat-detection-deploy" target="_blank" rel="noopener">GitHub ↗</a>
      </div>
    </div>

    <p>
      An end-to-end threat-analysis platform integrating <strong>Zeek/NetFlow, Suricata, Wazuh,
      VirusTotal CTI, transformer-based threat scoring, and weighted attack graphs</strong>.
      The system reconstructs time-ordered attack paths and was deployed on TWCC with Docker Compose.
    </p>

    <div class="tech-tags">
      <span>Python</span><span>Transformers</span><span>Docker</span><span>Linux</span>
      <span>Data Pipelines</span><span>Networking</span>
    </div>

    <div class="project-video">
      <iframe
        src="https://www.youtube-nocookie.com/embed/eyanoGjfy2g"
        title="NICS project demo"
        loading="lazy"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen>
      </iframe>
    </div>
  </article>

  <article class="project-card">
    <div class="project-heading">
      <div>
        <span class="project-kicker">AI SOFTWARE ENGINEERING · 2025</span>
        <h2>NYCU-Bot — Multi-Agent Award Announcement & Social Media Automation</h2>
      </div>
      <div class="project-links">
        <a href="https://github.com/kailee0422/automatic-social-media-post" target="_blank" rel="noopener">GitHub ↗</a>
      </div>
    </div>

    <p>
      A hierarchical multi-agent software system that monitors award announcements and produces
      bilingual social-media content. The implementation combines coordinator agents,
      platform-specific agents, an internal message bus, LangChain, and a locally hosted
      DeepSeek-R1 model through Ollama.
    </p>

    <div class="tech-tags">
      <span>Python</span><span>Multi-Agent Systems</span><span>LangChain</span>
      <span>Ollama</span><span>Automation</span>
    </div>
  </article>

  <article class="project-card">
    <div class="project-heading">
      <div>
        <span class="project-kicker">AI SYSTEMS · 2025</span>
        <h2>Intelligent Research Companion</h2>
      </div>
      <div class="project-links">
        <a href="https://github.com/kailee0422/RNN-Transformer/tree/main/Final%20Project%20-IRC" target="_blank" rel="noopener">GitHub ↗</a>
      </div>
    </div>

    <p>
      A multi-agent academic paper analysis workflow combining <strong>Mistral OCR, citation extraction,
      automated reference retrieval, RAG, LangChain, and local LLMs</strong>. The system decomposes
      literature-review tasks through orchestrator, coordinator, and task-specific agents.
    </p>

    <div class="tech-tags">
      <span>Python</span><span>RAG</span><span>OCR</span><span>LangChain</span>
      <span>Ollama</span><span>LLM Agents</span>
    </div>

    <div class="project-video">
      <iframe
        src="https://www.youtube-nocookie.com/embed/uRMtMFvGOTo"
        title="Intelligent Research Companion demo"
        loading="lazy"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen>
      </iframe>
    </div>
  </article>

  <article class="project-card">
    <div class="project-heading">
      <div>
        <span class="project-kicker">IOT / EDGE AI · 2024</span>
        <h2>Agrivoltaics Smart Micro-grid for Leisure Farms</h2>
      </div>
      <div class="project-links">
        <a href="https://github.com/Lonelypheonix/TaiZhi/tree/main/TaiZhi" target="_blank" rel="noopener">GitHub ↗</a>
      </div>
    </div>

    <p>
      An AI- and IoT-enabled smart micro-grid integrating <strong>real-time solar monitoring,
      MQTT communication, sensor data, anomaly detection, automated LED control, and ML-based
      yield prediction</strong>. This project is especially relevant to my interest in
      software-to-device and edge-system integration.
    </p>

    <div class="tech-tags">
      <span>IoT</span><span>MQTT</span><span>Sensor Integration</span>
      <span>Machine Learning</span><span>Web Systems</span>
    </div>

    <div class="project-video">
      <iframe
        src="https://www.youtube-nocookie.com/embed/WWejlb_-U-Q"
        title="Agrivoltaics Smart Micro-grid for Leisure Farms"
        loading="lazy"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen>
      </iframe>
    </div>
  </article>

  <article class="project-card">
    <div class="project-heading">
      <div>
        <span class="project-kicker">COMPUTER VISION SOFTWARE · 2023</span>
        <h2>AI-Based Video Analysis for Badminton Strategy</h2>
      </div>
      <div class="project-links">
        <a href="https://github.com/kailee0422/badminton-posture" target="_blank" rel="noopener">GitHub ↗</a>
      </div>
    </div>

    <p>
      An undergraduate capstone using <strong>YOLOv7 and OpenPose</strong> for badminton video analysis,
      action detection, joint extraction, posture comparison, and strategy-oriented analysis.
      The project received <strong>First Place</strong> and the <strong>Most Popular Award</strong>.
    </p>

    <div class="tech-tags">
      <span>Python</span><span>YOLOv7</span><span>OpenPose</span>
      <span>Computer Vision</span><span>Video Processing</span>
    </div>
  </article>

</div>

<style>
  .portfolio-projects {
    --project-border: var(--global-divider-color, #d8d8d8);
    --project-muted: var(--global-text-color-light, #767676);
  }

  .projects-intro {
    max-width: 820px;
    margin: 0 0 1.5rem;
    color: var(--project-muted);
    font-size: 1rem;
    line-height: 1.75;
  }

  .project-card {
    border: 1px solid var(--project-border);
    border-radius: 16px;
    padding: 1.4rem;
    margin-bottom: 1.25rem;
    background: var(--global-card-bg-color, transparent);
  }

  .project-heading {
    display: flex;
    justify-content: space-between;
    gap: 1rem;
    align-items: flex-start;
    margin-bottom: 0.85rem;
  }

  .project-kicker {
    display: block;
    margin-bottom: 0.35rem;
    font-size: 0.74rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    color: var(--global-theme-color);
  }

  .project-card h2 {
    margin: 0;
    font-size: 1.35rem;
    line-height: 1.35;
  }

  .project-card p {
    line-height: 1.75;
  }

  .project-links {
    flex: 0 0 auto;
  }

  .project-links a {
    display: inline-block;
    border: 1px solid var(--project-border);
    border-radius: 999px;
    padding: 0.45rem 0.75rem;
    text-decoration: none !important;
    white-space: nowrap;
  }

  .tech-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    margin: 0.9rem 0 1rem;
  }

  .tech-tags span {
    border: 1px solid var(--project-border);
    border-radius: 999px;
    padding: 0.28rem 0.58rem;
    font-size: 0.76rem;
    color: var(--project-muted);
  }

  .project-video {
    position: relative;
    width: 100%;
    aspect-ratio: 16 / 9;
    overflow: hidden;
    border-radius: 12px;
    margin-top: 1.1rem;
    background: #000;
  }

  .project-video iframe {
    width: 100%;
    height: 100%;
    border: 0;
    display: block;
  }

  @media (max-width: 680px) {
    .project-heading {
      flex-direction: column;
    }
  }
</style>
