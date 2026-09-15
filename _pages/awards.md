---
layout: page
title: awards
permalink: /awards/
description: "Academic honors and competition awards with certificate previews."
nav: true
nav_order: 3
---

<div class="awards-page">

  <section class="award-section">
    <h2>Academic Honors</h2>

    <article class="award-card">
      <div class="award-copy">
        <span class="award-type">ACADEMIC HONOR</span>
        <h3>College-level Outstanding Student Award — Semester 2</h3>
        <p class="award-org">National Yang Ming Chiao Tung University · College of Smart Science and Green Energy</p>
        <p class="award-description">
          Recognized for outstanding academic performance in the second semester of Academic Year 2024–2025.
        </p>
        <p class="award-date">November 24, 2025</p>
      </div>
      <iframe class="award-pdf" loading="lazy"
        src="{{ '/assets/pdf/NYCU_Outstanding_Student_Award_Semester_2.pdf' | relative_url }}#view=FitH"
        title="College-level Outstanding Student Award certificate"></iframe>
      <div class="award-actions"><a class="award-pdf-link" href="{{ '/assets/pdf/NYCU_Outstanding_Student_Award_Semester_2.pdf' | relative_url }}" target="_blank">Open full PDF ↗</a><a class="award-pdf-link" href="{{ '/assets/pdf/NYCU_Outstanding_Student_Award_Semester_2.pdf' | relative_url }}" download>Download PDF</a></div>
    </article>

    <article class="award-card">
      <div class="award-copy">
        <span class="award-type">ACADEMIC HONOR</span>
        <h3>Certificate of Excellence / Honor Student Award — Semester 1</h3>
        <p class="award-org">National Yang Ming Chiao Tung University</p>
        <p class="award-description">
          Recognized as an honor student in the first semester of Academic Year 2024–2025.
        </p>
        <p class="award-date">May 5, 2025</p>
      </div>
      <iframe class="award-pdf" loading="lazy"
        src="{{ '/assets/pdf/NYCU_Certificate_of_Excellence_Semester_1.pdf' | relative_url }}#view=FitH"
        title="Certificate of Excellence certificate"></iframe>
      <div class="award-actions"><a class="award-pdf-link" href="{{ '/assets/pdf/NYCU_Certificate_of_Excellence_Semester_1.pdf' | relative_url }}" target="_blank">Open full PDF ↗</a><a class="award-pdf-link" href="{{ '/assets/pdf/NYCU_Certificate_of_Excellence_Semester_1.pdf' | relative_url }}" download>Download PDF</a></div>
    </article>
  </section>

  <section class="award-section">
    <h2>Competition Awards</h2>

    <article class="award-card">
      <div class="award-copy">
        <span class="award-type">COMPETITION</span>
        <h3>Honorable Mention — 2024 Mobile Communications Practice Competition</h3>
        <p class="award-org">Smart Energy & Internet of Things Applications Track</p>
        <p class="award-description">
          Awarded for <strong>Agrivoltaics Smart Micro-grid for Leisure Farms</strong>.
        </p>
        <p class="award-date">December 7, 2024</p>
      </div>
      <iframe class="award-pdf" loading="lazy"
        src="{{ '/assets/pdf/Mobile_Communications_Practice_Competition_2024.pdf' | relative_url }}#view=FitH"
        title="Mobile Communications Practice Competition certificate"></iframe>
      <div class="award-actions"><a class="award-pdf-link" href="{{ '/assets/pdf/Mobile_Communications_Practice_Competition_2024.pdf' | relative_url }}" target="_blank">Open full PDF ↗</a><a class="award-pdf-link" href="{{ '/assets/pdf/Mobile_Communications_Practice_Competition_2024.pdf' | relative_url }}" download>Download PDF</a></div>
    </article>

    <article class="award-card">
      <div class="award-copy">
        <span class="award-type">CAPSTONE AWARD</span>
        <h3>First Place — Graduation Capstone Project Competition</h3>
        <p class="award-org">Department of Computer Science and Information Engineering · National University of Tainan</p>
        <p class="award-description">
          Project: <strong>AI-Based Video Content Analysis for Badminton Match Strategy Analysis</strong>.
        </p>
        <p class="award-date">December 16, 2023</p>
      </div>
      <iframe class="award-pdf" loading="lazy"
        src="{{ '/assets/pdf/NUTN_Capstone_First_Place.pdf' | relative_url }}#view=FitH"
        title="First Place capstone certificate"></iframe>
      <div class="award-actions"><a class="award-pdf-link" href="{{ '/assets/pdf/NUTN_Capstone_First_Place.pdf' | relative_url }}" target="_blank">Open full PDF ↗</a><a class="award-pdf-link" href="{{ '/assets/pdf/NUTN_Capstone_First_Place.pdf' | relative_url }}" download>Download PDF</a></div>
    </article>

    <article class="award-card">
      <div class="award-copy">
        <span class="award-type">CAPSTONE AWARD</span>
        <h3>Most Popular Award — Graduation Capstone Project Competition</h3>
        <p class="award-org">Department of Computer Science and Information Engineering · National University of Tainan</p>
        <p class="award-description">
          Awarded to the same badminton video-analysis capstone project.
        </p>
        <p class="award-date">December 16, 2023</p>
      </div>
      <iframe class="award-pdf" loading="lazy"
        src="{{ '/assets/pdf/NUTN_Capstone_Most_Popular_Award.pdf' | relative_url }}#view=FitH"
        title="Most Popular Award capstone certificate"></iframe>
      <div class="award-actions"><a class="award-pdf-link" href="{{ '/assets/pdf/NUTN_Capstone_Most_Popular_Award.pdf' | relative_url }}" target="_blank">Open full PDF ↗</a><a class="award-pdf-link" href="{{ '/assets/pdf/NUTN_Capstone_Most_Popular_Award.pdf' | relative_url }}" download>Download PDF</a></div>
    </article>
  </section>

</div>

<style>
  .awards-page {
    --award-border: var(--global-divider-color, #d7d7d7);
    --award-muted: var(--global-text-color-light, #767676);
  }

  .award-section {
    margin-bottom: 2.25rem;
  }

  .award-section > h2 {
    font-size: 1.45rem;
    margin: 0 0 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid var(--award-border);
  }

  .award-card {
    border: 1px solid var(--award-border);
    border-radius: 16px;
    padding: 1.25rem;
    margin-bottom: 1.25rem;
    background: var(--global-card-bg-color, transparent);
  }

  .award-type {
    display: block;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.09em;
    color: var(--global-theme-color);
    margin-bottom: 0.35rem;
  }

  .award-card h3 {
    font-size: 1.18rem;
    line-height: 1.4;
    margin: 0;
  }

  .award-org {
    margin: 0.4rem 0 0;
    font-size: 0.92rem;
    font-weight: 600;
  }

  .award-description {
    margin: 0.65rem 0 0;
    font-size: 0.92rem;
    line-height: 1.65;
    color: var(--award-muted);
  }

  .award-date {
    margin: 0.6rem 0 0;
    font-size: 0.8rem;
    color: var(--award-muted);
  }

  .award-pdf {
    display: block;
    width: 100%;
    height: 540px;
    border: 1px solid var(--award-border);
    border-radius: 10px;
    margin-top: 1rem;
    background: #fff;
  }

  .award-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 0.8rem;
    margin-top: 0.75rem;
  }

  .award-pdf-link {
    display: inline-block;
    font-size: 0.86rem;
  }

  @media (max-width: 680px) {
    .award-pdf {
      height: 430px;
    }
  }
</style>
