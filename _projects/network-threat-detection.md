---
layout: page
title: "Extracting Attack Path Based on Multiple Sightings Using Graph-based Algorithms"
description: "A NICS-sponsored, graph-based attack-path reconstruction system that fuses multiple sightings from NIDS, HIDS, network-flow, and CTI sources into a weighted attack graph."
importance: 1
category: research
github: https://github.com/kailee0422/network-threat-detection-deploy
github_stars: kailee0422/network-threat-detection-deploy
---

## Overview

This project reconstructs attack paths by combining **multiple independent sightings** of each network event — captured via **Zeek/NetFlow**, **Suricata NIDS**, **Wazuh HIDS**, and **VirusTotal CTI** — into a single weighted threat score, rather than relying on any one detection source.

I designed a dual-stream **MaliciousFlowTransformer + SecureBERT 2.0** threat-scoring pipeline and a **multi-source weighted attack graph** with reverse beam search to reconstruct temporally ordered attack paths from a known victim host. The system was deployed on **Taiwan Computing Cloud (TWCC)** using Docker Compose.

On the evaluated benchmark scenarios, the system achieved **F1 = 1.0000** on DARPA 2000 and a custom TWCC testbed, and **F1 = 0.9730** on the full six-day ISCXIDS2012 dataset.

**Topics:** Cybersecurity · Attack Path Reconstruction · Attack Graphs · Multi-Source Data Fusion · Transformers · Beam Search · Cyber Threat Intelligence · Docker

[GitHub repository](https://github.com/kailee0422/network-threat-detection-deploy) · [Project video](https://youtu.be/eyanoGjfy2g)

<div style="width:100%;aspect-ratio:16/9;margin-top:1rem;">
  <iframe src="https://www.youtube-nocookie.com/embed/eyanoGjfy2g" title="NICS Project" style="width:100%;height:100%;border:0;border-radius:12px;" loading="lazy" allowfullscreen></iframe>
</div>
