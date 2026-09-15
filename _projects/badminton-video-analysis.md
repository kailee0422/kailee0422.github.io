---
layout: page
title: "AI-Based Video Analysis for Badminton Strategy"
description: "A computer-vision capstone that analyzes badminton actions and player posture using YOLOv7 and OpenPose."
importance: 5
category: applied-ai
github: https://github.com/kailee0422/badminton-posture
---

## Overview

This undergraduate capstone investigates **AI-based video content analysis for badminton match strategy**. The system uses **YOLOv7** for action/shot-related detection and **OpenPose** for human-joint extraction, then compares posture patterns across processed datasets to support strategy-oriented analysis.

The project demonstrates an end-to-end computer-vision workflow spanning video preprocessing, detection, pose estimation, model training, and strategy-focused analysis.

It received **First Place** and the **Most Popular Award** in the graduation capstone competition of the Department of Computer Science and Information Engineering at the **National University of Tainan**.

**Topics:** Computer Vision · YOLOv7 · OpenPose · Video Analysis · Sports Analytics

[GitHub repository](https://github.com/kailee0422/badminton-posture) · [First Place certificate]({{ '/assets/pdf/NUTN_Capstone_First_Place.pdf' | relative_url }}) · [Most Popular Award certificate]({{ '/assets/pdf/NUTN_Capstone_Most_Popular_Award.pdf' | relative_url }})

## System pipeline

<figure style="margin: 1.25rem 0;">
  <img
    src="{{ '/assets/img/projects/badminton-pipeline.png' | relative_url }}"
    alt="Badminton hitting-posture detection pipeline from rally video through YOLOv7 and OpenPose to posture classification."
    style="width:100%;height:auto;border-radius:12px;border:1px solid var(--global-divider-color);"
    loading="lazy">
  <figcaption style="margin-top:0.6rem;color:var(--global-text-color-light);font-size:0.85rem;line-height:1.55;">
    The pipeline detects the hitting event and player, crops the hitter frame, extracts 25 body keypoints with OpenPose,
    and compares six training-data representations. In the shown evaluation, Normalized Vector + Z-score achieved the
    highest average accuracy at 67.1%.
  </figcaption>
</figure>
