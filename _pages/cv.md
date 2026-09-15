---
layout: page
title: cv
permalink: /cv/
description: "Curriculum vitae of Chong-Kai Li."
nav: true
nav_order: 4
---

<div class="cv-page">

  <div class="cv-heading">
    <div>
      <h1>Chong-Kai Li</h1>
      <p>Software & AI Engineering · Embedded Systems</p>
    </div>
  </div>

  <section class="cv-section">
    <h2>Education</h2>

    <div class="cv-item">
      <div>
        <h3>National Yang Ming Chiao Tung University</h3>
        <p>Master's Program, Institute of Artificial Intelligence</p>
      </div>
      <div class="cv-date">Sep 2024 – Aug 2026</div>
    </div>

    <div class="cv-item">
      <div>
        <h3>National University of Tainan</h3>
        <p>Bachelor's Program, Department of Computer Science and Information Engineering</p>
      </div>
      <div class="cv-date">Sep 2019 – Jul 2024</div>
    </div>

    <div class="cv-item">
      <div>
        <h3>Taichung Second Senior High School</h3>
        <p>Mathematics and Science Gifted Program</p>
      </div>
      <div class="cv-date">2017 – 2019</div>
    </div>
  </section>

  <section class="cv-section">
    <h2>Experience</h2>

    <div class="cv-item">
      <div>
        <h3>AI Engineer Intern</h3>
        <p>Industry Internship</p>
        <ul>
          <li>Developed an intelligent question-answering workflow for manufacturing operations and factory-floor inquiries.</li>
          <li>Applied RAG, SFT, and LoRA for domain-specific LLM adaptation.</li>
          <li>Studied contemporary post-training and reinforcement-learning methods including PPO and GRPO.</li>
        </ul>
      </div>
      <div class="cv-date">Jun 2025 – Aug 2025</div>
    </div>
  </section>

  <section class="cv-section">
    <h2>Projects</h2>

    <div class="cv-item">
      <div>
        <h3><a href="{{ '/projects/#attack-path' | relative_url }}">Multi-Source Attack Path Reconstruction with Weighted Attack Graphs</a></h3>
        <p>
          Integrated Zeek/NetFlow, Suricata, Wazuh, VirusTotal CTI, transformer-based threat scoring,
          and weighted attack graphs in a Docker-based deployment.
        </p>
      </div>
      <div class="cv-date">2025 – 2026</div>
    </div>

    <div class="cv-item">
      <div>
        <h3><a href="{{ '/projects/#nycu-bot' | relative_url }}">NYCU-Bot — Multi-Agent Award Announcement & Social Media Automation</a></h3>
        <p>
          Built a hierarchical multi-agent automation system with LangChain, Ollama, local LLMs,
          web monitoring, and platform-specific publishing agents.
        </p>
      </div>
      <div class="cv-date">2025</div>
    </div>

    <div class="cv-item">
      <div>
        <h3><a href="{{ '/projects/#irc' | relative_url }}">Intelligent Research Companion</a></h3>
        <p>
          Developed an academic-paper analysis workflow combining OCR, citation extraction,
          automated reference retrieval, RAG, and local LLMs.
        </p>
      </div>
      <div class="cv-date">2025</div>
    </div>

    <div class="cv-item">
      <div>
        <h3><a href="{{ '/projects/#agrivoltaics' | relative_url }}">Agrivoltaics Smart Micro-grid for Leisure Farms</a></h3>
        <p>
          Integrated MQTT-based monitoring, IoT sensing, anomaly detection, automated control,
          and ML-based yield prediction in a smart-energy application.
        </p>
      </div>
      <div class="cv-date">2024</div>
    </div>

    <div class="cv-item">
      <div>
        <h3><a href="{{ '/projects/#badminton' | relative_url }}">AI-Based Video Analysis for Badminton Strategy</a></h3>
        <p>
          Built a computer-vision pipeline using YOLOv7 and OpenPose for badminton video,
          action, posture, and strategy analysis.
        </p>
      </div>
      <div class="cv-date">2023</div>
    </div>
  </section>

  <section class="cv-section">
    <h2>Technical Skills</h2>

    <div class="cv-skill-grid">
      <div class="cv-skill-card">
        <h3>Programming</h3>
        <p>C, C++, Python, Java, SQL</p>
      </div>
      <div class="cv-skill-card">
        <h3>Systems</h3>
        <p>Linux, Shell, Docker, networking, data pipelines</p>
      </div>
      <div class="cv-skill-card">
        <h3>Embedded & Edge</h3>
        <p>MQTT, IoT integration, sensor data, real-time monitoring, device-to-service workflows</p>
      </div>
      <div class="cv-skill-card">
        <h3>AI / Machine Learning</h3>
        <p>PyTorch, Transformers, scikit-learn, OpenCV, RAG, LangChain, Ollama</p>
      </div>
    </div>
  </section>

  <section class="cv-section">
    <h2>Awards</h2>

    <div class="cv-compact-row">
      <span>College-level Outstanding Student Award — NYCU</span>
      <span>2025</span>
    </div>
    <div class="cv-compact-row">
      <span>Certificate of Excellence / Honor Student Award — NYCU</span>
      <span>2025</span>
    </div>
    <div class="cv-compact-row">
      <span>Honorable Mention — Mobile Communications Practice Competition</span>
      <span>2024</span>
    </div>
    <div class="cv-compact-row">
      <span>First Place & Most Popular Award — NUTN Graduation Capstone Competition</span>
      <span>2023</span>
    </div>
  </section>

  <div class="cv-download-wrap">
    <a class="cv-download-button"
       href="{{ '/assets/pdf/Chong-Kai_Li_Resume.pdf' | relative_url }}"
       download>
      Download Résumé (PDF)
    </a>
  </div>

</div>

<style>
  .cv-page {
    --cv-border: var(--global-divider-color, #d7d7d7);
    --cv-muted: var(--global-text-color-light, #767676);
  }

  .cv-heading {
    border-bottom: 1px solid var(--cv-border);
    padding-bottom: 1rem;
    margin-bottom: 1.6rem;
  }

  .cv-heading h1 {
    margin: 0;
    font-size: 2rem;
  }

  .cv-heading p {
    margin: 0.4rem 0 0;
    color: var(--cv-muted);
  }

  .cv-section {
    margin-bottom: 2rem;
  }

  .cv-section > h2 {
    font-size: 1.35rem;
    margin: 0 0 0.9rem;
  }

  .cv-item {
    display: grid;
    grid-template-columns: minmax(0, 1fr) auto;
    gap: 1.2rem;
    padding: 1rem 0;
    border-top: 1px solid var(--cv-border);
  }

  .cv-item h3 {
    margin: 0;
    font-size: 1rem;
    line-height: 1.45;
  }

  .cv-item p {
    margin: 0.32rem 0 0;
    color: var(--cv-muted);
    line-height: 1.65;
    font-size: 0.9rem;
  }

  .cv-item ul {
    margin: 0.65rem 0 0 1.15rem;
    padding: 0;
  }

  .cv-item li {
    margin: 0.3rem 0;
    line-height: 1.55;
    font-size: 0.9rem;
  }

  .cv-date {
    color: var(--cv-muted);
    font-size: 0.86rem;
    white-space: nowrap;
    padding-top: 0.05rem;
  }

  .cv-skill-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.8rem;
  }

  .cv-skill-card {
    border: 1px solid var(--cv-border);
    border-radius: 12px;
    padding: 1rem;
  }

  .cv-skill-card h3 {
    margin: 0;
    font-size: 0.95rem;
  }

  .cv-skill-card p {
    margin: 0.45rem 0 0;
    color: var(--cv-muted);
    font-size: 0.86rem;
    line-height: 1.6;
  }

  .cv-compact-row {
    display: flex;
    justify-content: space-between;
    gap: 1rem;
    padding: 0.7rem 0;
    border-top: 1px solid var(--cv-border);
    font-size: 0.9rem;
  }

  .cv-compact-row span:last-child {
    color: var(--cv-muted);
    white-space: nowrap;
  }

  .cv-download-wrap {
    display: flex;
    justify-content: center;
    padding-top: 0.8rem;
  }

  .cv-download-button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border-radius: 999px;
    padding: 0.78rem 1.2rem;
    background: var(--global-theme-color);
    color: #fff !important;
    font-weight: 650;
    text-decoration: none !important;
  }

  @media (max-width: 760px) {
    .cv-item {
      grid-template-columns: 1fr;
      gap: 0.35rem;
    }

    .cv-date {
      grid-row: 1;
    }

    .cv-skill-grid {
      grid-template-columns: 1fr;
    }

    .cv-compact-row {
      flex-direction: column;
      gap: 0.2rem;
    }
  }
</style>
