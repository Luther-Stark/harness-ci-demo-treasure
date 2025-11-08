# 🏴‍☠️ Treasure Island — Harness CI/CD Demo

This is a simple **Python text adventure game** used to demonstrate a full CI/CD workflow using **Harness Cloud**.

---

## ⚙️ Features

- CI pipeline builds, tests, and pushes a Docker image to DockerHub.  
- CD pipeline deploys the game as a **Kubernetes Job** in a demo cluster.  
- Uses a reusable **Build & Push Docker Template (v1)** for portability and speed.  
- Includes **Docker Layer Caching** and **automatic tagging** with `<+pipeline.sequenceId>`.

---

## 🧱 Project Structure
app/            # Treasure Island Python source
tests/          # Simple pytest validation
k8s/job.yaml    # K8s Job manifest (runs the game)
.harness/       # Harness pipeline YAML
Dockerfile
requirements.txt

---

## 🚀 Run Locally

```bash
python app/treasure.py