---
layout: page
title: projects
permalink: /projects/
description: "Software, embedded/edge, and AI engineering projects with source code, demos, and outcomes."
nav: true
nav_order: 2
---

<div class="portfolio-projects">

  <div class="projects-intro">
    <p>
      Selected projects spanning <strong>software engineering, embedded/edge systems,
      AI engineering, automation, and computer vision</strong>. Each project highlights
      what I built, the technologies used, and the resulting outcome. Source code is linked
      directly from each project.
    </p>
  </div>

  <article class="project-card" id="attack-path">
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

    <div class="project-facts">
      <div><span>Contribution</span><strong>Built the multi-source processing, scoring, graph-reconstruction, and deployment workflow.</strong></div>
      <div><span>Outcome</span><strong>F1 = 1.0000 on DARPA 2000 and a custom TWCC testbed; F1 = 0.9730 on the full six-day ISCXIDS2012 evaluation.</strong></div>
    </div>

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

  <article class="project-card" id="nycu-bot">
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

    <div class="project-facts">
      <div><span>Contribution</span><strong>Designed the hierarchical agent architecture and platform-specific publishing workflow.</strong></div>
      <div><span>Outcome</span><strong>Supports both one-shot execution and continuous polling with configurable update intervals.</strong></div>
    </div>

    <div class="tech-tags">
      <span>Python</span><span>Multi-Agent Systems</span><span>LangChain</span>
      <span>Ollama</span><span>Automation</span>
    </div>

    <figure class="project-figure">
      <img
        src="{{ '/assets/img/projects/nycu-bot-architecture.png' | relative_url }}"
        alt="Architecture diagram of NYCU-Bot showing InformationAgent, FatherAgent, MotherAgent, ContentAgent, social platform agents, and a local LLM via Ollama."
        loading="lazy">
      <figcaption>
        Architecture of NYCU-Bot. The workflow starts from award news monitoring, passes through
        coordinator agents, and then routes generated content to platform-specific posting agents.
      </figcaption>
    </figure>
  </article>

  <article class="project-card" id="irc">
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

    <div class="project-facts">
      <div><span>Contribution</span><strong>Implemented the hierarchical agent workflow for OCR, citation extraction, retrieval, and structured analysis.</strong></div>
      <div><span>Outcome</span><strong>Automates literature-review preparation and structured knowledge extraction from academic papers.</strong></div>
    </div>

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

  <article class="project-card" id="agrivoltaics">
    <div class="project-heading">
      <div>
        <span class="project-kicker">EMBEDDED / EDGE AI · 2024</span>
        <h2>Agrivoltaics Smart Micro-grid for Leisure Farms</h2>
      </div>
      <div class="project-links">
        <a href="https://github.com/Lonelypheonix/TaiZhi/tree/main/TaiZhi" target="_blank" rel="noopener">GitHub ↗</a>
      </div>
    </div>

    <p>
      An AI- and IoT-enabled smart micro-grid integrating <strong>real-time solar monitoring,
      MQTT communication, sensor data, anomaly detection, automated LED control, and ML-based
      yield prediction</strong>. The project connects device-facing sensing and control with
      web-based monitoring and AI analysis.
    </p>

    <div class="project-facts">
      <div><span>Contribution</span><strong>Integrated sensing, MQTT communication, monitoring, automated control, and ML-based prediction into one application workflow.</strong></div>
      <div><span>Outcome</span><strong>Received Honorable Mention in the 2024 Mobile Communications Practice Competition.</strong></div>
    </div>

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

  <article class="project-card" id="badminton">
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
    </p>

    <div class="project-facts">
      <div><span>Contribution</span><strong>Built the video-to-posture pipeline from event detection and player detection to OpenPose keypoint extraction and posture classification.</strong></div>
      <div><span>Outcome</span><strong>First Place and Most Popular Award; the best evaluated representation reached 67.1% average classification accuracy.</strong></div>
    </div>

    <div class="tech-tags">
      <span>Python</span><span>YOLOv7</span><span>OpenPose</span>
      <span>Computer Vision</span><span>Video Processing</span>
    </div>

    <figure class="project-figure">
      <img
        src="{{ '/assets/img/projects/badminton-pipeline.png' | relative_url }}"
        alt="Badminton hitting-posture detection pipeline from rally video to six training-data representations."
        loading="lazy">
      <figcaption>
        Badminton hitting-posture detection pipeline. The evaluated representations include two image-based
        variants and four vector-based variants; Normalized Vector + Z-score achieved the highest average
        accuracy in this comparison.
      </figcaption>
    </figure>
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
    scroll-margin-top: 90px;
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

  .project-facts {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.7rem;
    margin: 1rem 0;
  }

  .project-facts > div {
    border-left: 3px solid var(--global-theme-color);
    background: color-mix(in srgb, var(--global-theme-color) 6%, transparent);
    border-radius: 0 10px 10px 0;
    padding: 0.75rem 0.85rem;
  }

  .project-facts span {
    display: block;
    color: var(--project-muted);
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin-bottom: 0.25rem;
  }

  .project-facts strong {
    display: block;
    color: var(--global-text-color);
    font-size: 0.86rem;
    font-weight: 500;
    line-height: 1.55;
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

  .project-video,
  .project-figure {
    width: 100%;
    margin: 1.1rem 0 0;
  }

  .project-video {
    position: relative;
    aspect-ratio: 16 / 9;
    overflow: hidden;
    border-radius: 12px;
    background: #000;
  }

  .project-video iframe {
    width: 100%;
    height: 100%;
    border: 0;
    display: block;
  }

  .project-figure img {
    width: 100%;
    height: auto;
    display: block;
    border: 1px solid var(--project-border);
    border-radius: 12px;
  }

  .project-figure figcaption {
    color: var(--project-muted);
    font-size: 0.8rem;
    line-height: 1.55;
    margin-top: 0.55rem;
  }

  @media (max-width: 680px) {
    .project-heading {
      flex-direction: column;
    }

    .project-facts {
      grid-template-columns: 1fr;
    }
  }
</style>
