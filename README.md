# Bantu AI — Technical Documentation

## Executive Summary
**Bantu AI** is a localized, privacy-focused desktop AI assistant system designed exclusively for household interaction, initially configured for **my family**. Utilizing voice biometric authentication and email-based authorization, Bantu AI acts as a personal intelligent agent tailored to the communication style, schedule, and privacy needs of individual families.

---

## Vision & Core Objectives
* **Voice Security & Biometrics:** Establish voice profile verification as the primary security layer to validate authorized household speakers.
* **Family Access Control:** Restrict interaction exclusively to invited family members authenticated via email login.
* **Custom Household Personalities:** Support multi-tenant customization, enabling unique AI personalities tailored to fit different family environments.
* **Local Computer Execution:** Guarantee user data privacy by executing core processing and logic locally on personal hardware.

---

## Tech Stack & Architecture Structure

### System Modules & File Architecture
* **`Voice_Agent.py`:** Manages real-time voice sessions, low-latency audio streaming, and live speech execution.
* **`coreAI.py` / `conv.py`:** Core conversational engines handling prompt processing, dialogue history, and context management.
* **`tool_registry.py`:** Central registry for registering and dispatching tool functions to the AI agent.
* **`tools/` Directory:** Modular function library containing integrations for dynamic features:
  * `app_tools.py`: Desktop application control and automation.
  * `morning_tools.py`: Aggregates calendar events, weather summaries, and task deadlines into a morning schedule.
  * `news_tools.py`: Dynamic news fetchers and web content scrapers.
  * `time_tools.py`: Timezone, date, and schedule calculation utilities.
  * `web_tools.py`: Web browsing automation and search queries.
* **`config.py` & `paths.py`:** Central environment configuration, API key handling, and file system path resolution.

### Languages & Frameworks
* **Language:** Python (CPython 3.12 / 3.13)
* **Real-Time Voice Infrastructure:** LiveKit Agent Framework (full-duplex streaming)
* **Pre-Trained Models:** Microsoft DialoGPT-medium (early baseline) & Advanced LLM integrations
* **Environment & Tools:** PyCharm IDE (`.idea` configuration), Virtual Environments, and standard modular dependencies (`requirements.txt`)

---

## System Evolution & Development Milestones

### 1. Foundation & Basic Conversational Architecture
* Implemented initial response handlers using Microsoft’s **DialoGPT-medium** model.
* Configured basic user prompt execution and foundational dialogue loops.

### 2. Audio Engineering & Dynamic Input Routing
* Transitioned from static manual audio file loading to dynamic microphone input routing.
* Debugged system-level audio streaming errors, device selection conflicts, and input capture limitations.

### 3. Modular System Restructuring
* Rebuilt code structure following clean-code principles, modular separation, and design patterns inspired by advanced open-source architectures.
* Added browser automation modules and external integration interfaces.

### 4. Context & Real-Time Data Services
* Built dynamic tools for real-time news retrieval, calendar scheduling, and time-aware response generation.

### 5. Advanced Real-Time Infrastructure & Briefing Tools
* **LiveKit Integration:** Upgraded voice architecture to LiveKit for sub-second real-time streaming voice interactions.
* **Interruptible Voice Pipeline:** Implemented full-duplex speech capability, allowing users to interrupt the AI mid-response.
* **Tool-Based Morning Briefing Engine:** Built an automated briefing system using `morning_tools.py` to aggregate weather, news, events, and task deadlines into a single dynamic voice report.
* **Workflow Architecture:** Restructured event triggers to align with workflow-driven architectures (n8n design patterns).

---

## Technical Acknowledgments
* **Development Assistance:** Microsoft Copilot was utilized as a primary learning tool to explore AI system design, syntax optimization, and architectural strategies.

---

## Roadmap & Future Enhancements
* [X] Complete voiceprint biometric security layer for authenticating family members.
* [ ] Deploy email-based sign-in access control for multi-family sharing.
* [X] Introduce customizable household personality profiles.
* [X] Expand background automation triggers using workflow orchestration.
