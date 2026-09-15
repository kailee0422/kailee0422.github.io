---
layout: page
title: "Multi-Source Attack Path Reconstruction with Weighted Attack Graphs"
description: "A NICS-sponsored cyber threat analysis system that fuses network, host, and CTI signals to reconstruct time-ordered attack paths."
importance: 1
category: research
github: https://github.com/kailee0422/network-threat-detection-deploy
github_stars: kailee0422/network-threat-detection-deploy
---

## Overview

This project develops a multi-source attack-path reconstruction system for cyber threat investigation. The pipeline integrates **Zeek/NetFlow**, **Suricata NIDS**, **Wazuh HIDS**, and **VirusTotal CTI** to combine network, endpoint, and threat-intelligence evidence.

I designed a dual-stream **MaliciousFlowTransformer + SecureBERT 2.0** threat-scoring pipeline and a **multi-source weighted attack graph** with reverse beam search to reconstruct temporally ordered attack paths from a known victim host. The system was deployed on **Taiwan Computing Cloud (TWCC)** using Docker Compose.

On the evaluated benchmark scenarios, the system achieved **F1 = 1.0000** on DARPA 2000 and a custom TWCC testbed, and **F1 = 0.9730** on the full six-day ISCXIDS2012 dataset.

**Topics:** Cybersecurity · Attack Graphs · Transformers · NIDS/HIDS · CTI · Docker · TWCC

[GitHub repository](https://github.com/kailee0422/network-threat-detection-deploy) · [Project video](https://youtu.be/eyanoGjfy2g)

<div style="width:100%;aspect-ratio:16/9;margin-top:1rem;">
  <iframe src="https://www.youtube-nocookie.com/embed/eyanoGjfy2g" title="NICS Project" style="width:100%;height:100%;border:0;border-radius:12px;" loading="lazy" allowfullscreen></iframe>
</div>
