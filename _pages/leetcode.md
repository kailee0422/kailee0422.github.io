---
layout: page
title: LeetCode
permalink: /leetcode/
description: Automated LeetCode problem-solving statistics.
nav: true
nav_order: 5
---

{% assign lc = site.data.leetcode %}

<div class="lc-dashboard">

  <div class="lc-hero">
    <div>
      <div class="lc-eyebrow">PROBLEM SOLVING</div>
      <h2 class="lc-title">LeetCode Progress</h2>
      <p class="lc-subtitle">
        A continuously updated snapshot of my algorithmic problem-solving progress.
      </p>
    </div>

    <a class="lc-profile-button" href="{{ lc.profile_url }}" target="_blank" rel="noopener noreferrer">
      View LeetCode Profile
      <span aria-hidden="true">↗</span>
    </a>
  </div>

  <div class="lc-stat-grid">
    <div class="lc-stat-card lc-total-card">
      <span class="lc-stat-label">Solved Problems</span>
      <span class="lc-stat-value">{{ lc.solved.total }}</span>
      <span class="lc-stat-caption">@{{ lc.username }}</span>
    </div>

    <div class="lc-stat-card">
      <span class="lc-stat-dot lc-easy-dot"></span>
      <span class="lc-stat-label">Easy</span>
      <span class="lc-stat-value">{{ lc.solved.easy }}</span>
      <span class="lc-stat-caption">{{ lc.distribution.easy_pct }}% of solved</span>
    </div>

    <div class="lc-stat-card">
      <span class="lc-stat-dot lc-medium-dot"></span>
      <span class="lc-stat-label">Medium</span>
      <span class="lc-stat-value">{{ lc.solved.medium }}</span>
      <span class="lc-stat-caption">{{ lc.distribution.medium_pct }}% of solved</span>
    </div>

    <div class="lc-stat-card">
      <span class="lc-stat-dot lc-hard-dot"></span>
      <span class="lc-stat-label">Hard</span>
      <span class="lc-stat-value">{{ lc.solved.hard }}</span>
      <span class="lc-stat-caption">{{ lc.distribution.hard_pct }}% of solved</span>
    </div>
  </div>

  <div class="lc-chart-grid">

    <section class="lc-panel">
      <div class="lc-panel-heading">
        <div>
          <h3>Difficulty Distribution</h3>
          <p>Composition of accepted problems by difficulty.</p>
        </div>
      </div>

      {% if lc.solved.total > 0 %}
      <div class="lc-donut-wrap">
        <div
          class="lc-donut"
          style="
            --easy-end: {{ lc.distribution.easy_pct }}%;
            --medium-end: {{ lc.distribution.easy_plus_medium_pct }}%;
          "
          aria-label="Difficulty distribution chart"
        >
          <div class="lc-donut-center">
            <strong>{{ lc.solved.total }}</strong>
            <span>Solved</span>
          </div>
        </div>

        <div class="lc-legend">
          <div class="lc-legend-row">
            <div><span class="lc-legend-swatch lc-easy-bg"></span>Easy</div>
            <strong>{{ lc.solved.easy }}</strong>
          </div>
          <div class="lc-legend-row">
            <div><span class="lc-legend-swatch lc-medium-bg"></span>Medium</div>
            <strong>{{ lc.solved.medium }}</strong>
          </div>
          <div class="lc-legend-row">
            <div><span class="lc-legend-swatch lc-hard-bg"></span>Hard</div>
            <strong>{{ lc.solved.hard }}</strong>
          </div>
        </div>
      </div>
      {% else %}
      <div class="lc-empty-state">
        Statistics will appear automatically after the first synchronization.
      </div>
      {% endif %}
    </section>

    <section class="lc-panel">
      <div class="lc-panel-heading">
        <div>
          <h3>Primary Languages</h3>
          <p>Top languages based on solved problems.</p>
        </div>
      </div>

      {% if lc.languages.size > 0 %}
      <div class="lc-language-list">
        {% for language in lc.languages limit:3 %}
        <div class="lc-language-item">
          <div class="lc-language-meta">
            <span>{{ language.name }}</span>
            <strong>{{ language.problems_solved }}</strong>
          </div>
          <div class="lc-language-track">
            <div class="lc-language-fill" style="width: {{ language.relative_pct }}%;"></div>
          </div>
        </div>
        {% endfor %}
      </div>
      {% else %}
      <div class="lc-empty-state">
        Language statistics will appear automatically after the first synchronization.
      </div>
      {% endif %}
    </section>

  </div>

  <section class="lc-panel lc-bars-panel">
    <div class="lc-panel-heading">
      <div>
        <h3>Solved by Difficulty</h3>
        <p>Relative distribution across Easy, Medium, and Hard problems.</p>
      </div>
    </div>

    {% if lc.solved.total > 0 %}
    <div class="lc-difficulty-bars">
      <div class="lc-bar-row">
        <div class="lc-bar-label">
          <span>Easy</span>
          <strong>{{ lc.solved.easy }}</strong>
        </div>
        <div class="lc-bar-track">
          <div class="lc-bar-fill lc-easy-bg" style="width: {{ lc.distribution.easy_pct }}%;"></div>
        </div>
      </div>

      <div class="lc-bar-row">
        <div class="lc-bar-label">
          <span>Medium</span>
          <strong>{{ lc.solved.medium }}</strong>
        </div>
        <div class="lc-bar-track">
          <div class="lc-bar-fill lc-medium-bg" style="width: {{ lc.distribution.medium_pct }}%;"></div>
        </div>
      </div>

      <div class="lc-bar-row">
        <div class="lc-bar-label">
          <span>Hard</span>
          <strong>{{ lc.solved.hard }}</strong>
        </div>
        <div class="lc-bar-track">
          <div class="lc-bar-fill lc-hard-bg" style="width: {{ lc.distribution.hard_pct }}%;"></div>
        </div>
      </div>
    </div>
    {% else %}
    <div class="lc-empty-state">
      Waiting for the first synchronization.
    </div>
    {% endif %}
  </section>

  <div class="lc-footer-note">
    Data is synchronized automatically from the public LeetCode profile.
    {% if lc.last_updated %}
      Last updated: {{ lc.last_updated }} UTC.
    {% endif %}
  </div>

</div>

<style>
  .lc-dashboard {
    --lc-easy: #00b8a3;
    --lc-medium: #ffc01e;
    --lc-hard: #ff375f;
    --lc-card: var(--global-card-bg-color, rgba(127, 127, 127, 0.06));
    --lc-border: var(--global-divider-color, rgba(127, 127, 127, 0.22));
    --lc-muted: var(--global-text-color-light, #777);
    margin-top: 1.25rem;
  }

  .lc-hero {
    display: flex;
    justify-content: space-between;
    gap: 1.5rem;
    align-items: flex-end;
    margin-bottom: 1.5rem;
  }

  .lc-eyebrow {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    color: var(--global-theme-color);
    margin-bottom: 0.45rem;
  }

  .lc-title {
    margin: 0;
    font-size: clamp(1.8rem, 4vw, 2.55rem);
    letter-spacing: -0.03em;
  }

  .lc-subtitle {
    margin: 0.55rem 0 0;
    max-width: 650px;
    color: var(--lc-muted);
  }

  .lc-profile-button {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    white-space: nowrap;
    border: 1px solid var(--lc-border);
    border-radius: 999px;
    padding: 0.72rem 1rem;
    text-decoration: none !important;
    transition: transform 0.18s ease, border-color 0.18s ease;
  }

  .lc-profile-button:hover {
    transform: translateY(-2px);
    border-color: var(--global-theme-color);
  }

  .lc-stat-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 0.9rem;
    margin-bottom: 0.9rem;
  }

  .lc-stat-card,
  .lc-panel {
    border: 1px solid var(--lc-border);
    background: var(--lc-card);
    border-radius: 16px;
  }

  .lc-stat-card {
    min-height: 142px;
    padding: 1.15rem;
    display: flex;
    flex-direction: column;
  }

  .lc-total-card {
    background:
      linear-gradient(135deg, color-mix(in srgb, var(--global-theme-color) 11%, transparent), transparent 60%),
      var(--lc-card);
  }

  .lc-stat-label {
    font-size: 0.82rem;
    color: var(--lc-muted);
    font-weight: 600;
  }

  .lc-stat-value {
    font-size: 2.05rem;
    font-weight: 750;
    line-height: 1.05;
    margin-top: auto;
    letter-spacing: -0.035em;
  }

  .lc-stat-caption {
    margin-top: 0.3rem;
    font-size: 0.76rem;
    color: var(--lc-muted);
  }

  .lc-stat-dot {
    width: 9px;
    height: 9px;
    border-radius: 50%;
    margin-bottom: 0.8rem;
  }

  .lc-easy-dot,
  .lc-easy-bg { background: var(--lc-easy); }

  .lc-medium-dot,
  .lc-medium-bg { background: var(--lc-medium); }

  .lc-hard-dot,
  .lc-hard-bg { background: var(--lc-hard); }

  .lc-chart-grid {
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 0.9rem;
    margin-bottom: 0.9rem;
  }

  .lc-panel {
    padding: 1.25rem;
  }

  .lc-panel-heading h3 {
    margin: 0;
    font-size: 1rem;
  }

  .lc-panel-heading p {
    margin: 0.3rem 0 0;
    color: var(--lc-muted);
    font-size: 0.8rem;
  }

  .lc-donut-wrap {
    display: grid;
    grid-template-columns: minmax(190px, 230px) 1fr;
    gap: 1.5rem;
    align-items: center;
    padding-top: 1.25rem;
  }

  .lc-donut {
    aspect-ratio: 1;
    width: 100%;
    max-width: 220px;
    margin: 0 auto;
    border-radius: 50%;
    position: relative;
    background:
      conic-gradient(
        var(--lc-easy) 0 var(--easy-end),
        var(--lc-medium) var(--easy-end) var(--medium-end),
        var(--lc-hard) var(--medium-end) 100%
      );
  }

  .lc-donut::after {
    content: "";
    position: absolute;
    inset: 22%;
    border-radius: 50%;
    background: var(--global-bg-color, #fff);
    border: 1px solid var(--lc-border);
  }

  .lc-donut-center {
    position: absolute;
    inset: 0;
    z-index: 1;
    display: grid;
    place-content: center;
    text-align: center;
    pointer-events: none;
  }

  .lc-donut-center strong {
    font-size: 1.8rem;
    line-height: 1;
  }

  .lc-donut-center span {
    margin-top: 0.25rem;
    color: var(--lc-muted);
    font-size: 0.76rem;
  }

  .lc-legend {
    display: grid;
    gap: 0.78rem;
  }

  .lc-legend-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 1rem;
    padding-bottom: 0.68rem;
    border-bottom: 1px solid var(--lc-border);
  }

  .lc-legend-row > div {
    display: flex;
    align-items: center;
    gap: 0.55rem;
  }

  .lc-legend-swatch {
    width: 10px;
    height: 10px;
    border-radius: 3px;
    display: inline-block;
  }

  .lc-language-list {
    display: grid;
    gap: 1.15rem;
    padding-top: 1.35rem;
  }

  .lc-language-meta,
  .lc-bar-label {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    gap: 1rem;
    margin-bottom: 0.42rem;
  }

  .lc-language-meta span,
  .lc-bar-label span {
    font-size: 0.85rem;
    font-weight: 600;
  }

  .lc-language-meta strong,
  .lc-bar-label strong {
    font-size: 0.78rem;
    color: var(--lc-muted);
  }

  .lc-language-track,
  .lc-bar-track {
    height: 8px;
    border-radius: 999px;
    background: color-mix(in srgb, var(--global-text-color) 9%, transparent);
    overflow: hidden;
  }

  .lc-language-fill {
    height: 100%;
    border-radius: inherit;
    background: var(--global-theme-color);
  }

  .lc-bars-panel {
    margin-bottom: 0.75rem;
  }

  .lc-difficulty-bars {
    display: grid;
    gap: 1rem;
    padding-top: 1.2rem;
  }

  .lc-bar-fill {
    height: 100%;
    border-radius: inherit;
    min-width: 2px;
  }

  .lc-empty-state {
    margin-top: 1.2rem;
    padding: 1rem;
    border: 1px dashed var(--lc-border);
    border-radius: 12px;
    color: var(--lc-muted);
    font-size: 0.85rem;
  }

  .lc-footer-note {
    font-size: 0.75rem;
    color: var(--lc-muted);
    text-align: right;
    margin-top: 0.7rem;
  }

  @media (max-width: 900px) {
    .lc-stat-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .lc-chart-grid {
      grid-template-columns: 1fr;
    }
  }

  @media (max-width: 620px) {
    .lc-hero {
      flex-direction: column;
      align-items: flex-start;
    }

    .lc-stat-grid {
      grid-template-columns: 1fr 1fr;
    }

    .lc-donut-wrap {
      grid-template-columns: 1fr;
    }

    .lc-profile-button {
      width: 100%;
      justify-content: center;
    }
  }
</style>
