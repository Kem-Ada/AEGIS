# AEGIS — AI Ethics & Governance Integrated System

> Founded and maintained by Kem Ada
>
> AEGIS is an independent open source project created by Kem Ada to support practical AI governance and AI security workflows
> 
> Open source Python framework for AI security, governance, human-in-the-loop controls, explainability, and regulatory compliance across EU AI Act, GDPR Article 35, and ISO/IEC 42001.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-kem--ada.github.io%2FAEGIS-10b9a8)](https://kem-ada.github.io/AEGIS/)
[![Python demo](https://img.shields.io/badge/Python%20demo-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://aegis-classifier.streamlit.app)
---

## What is AEGIS?

AEGIS is an open source framework that helps organisations operationalise AI governance and security. It translates complex regulatory requirements such as EU AI Act, GDPR Article 35, and ISO/IEC 42001 into executable, auditable workflows that security and risk teams can actually use.

**AEGIS automates:**
- 🔴 **EU AI Act risk classification** — classify AI systems by risk tier with documented rationale
- 📋 **Model card generation** — produce standardised model documentation for transparency and accountability
- 🗺️ **AI system inventory mapping** — map AI assets against GDPR Article 35 DPIA requirements
- 🔐 **AI security risk assessment** — identify adversarial threats, model vulnerabilities, and data integrity risks
- 👁️ **Human-in-the-loop (HITL) controls** — document and enforce meaningful human oversight checkpoints for high-risk AI decisions
- 💡 **Explainability & transparency reporting** — generate structured outputs that make AI decision-making auditable and interpretable
- 📊 **Governance gap reporting** — produce structured reports for security teams, DPOs, and regulators

Built for organisations that need to govern AI responsibly not just tick boxes.

---

## Why AEGIS?

Most enterprises are adopting AI faster than their security and governance frameworks can keep up. Teams face:

- No standardised way to classify AI risk across business units
- AI systems deployed without security threat modelling or adversarial risk assessment
- Human oversight that exists on paper but isn't operationalised
- Model documentation that doesn't hold up to regulatory or audit scrutiny
- DPIA processes that weren't designed with AI systems in mind

AEGIS bridges the gap between AI deployment and AI accountability with security and explainability built in from the start, not bolted on after.

---

## Core Principles

**Security-first governance** — AI risk isn't just regulatory. AEGIS treats adversarial robustness, data poisoning, model inversion, and supply chain risk as first-class governance concerns.

**Human-in-the-loop by design** — High-risk AI decisions require meaningful human oversight, not just a log entry. AEGIS helps organisations define, document, and enforce HITL checkpoints that satisfy both regulatory and ethical standards.

**Transparency and explainability** — Stakeholders whether regulators, users, or internal audit deserve to understand how AI systems reach decisions. AEGIS generates explainability outputs that go beyond model cards into operational transparency.

**Governance as code** — Policies and controls should be versioned, testable, and auditable. AEGIS treats governance artefacts the same way engineering teams treat infrastructure.

---

## Quick Start

Clone the repository and run the Streamlit app from source:

```bash
git clone https://github.com/Kem-Ada/AEGIS.git
cd AEGIS
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

### Python API examples

Classify an AI system under the EU AI Act:

```python
from classifier import classify_ai_system

result = classify_ai_system(
    system_name="Customer Credit Scoring Model",
    makes_automated_decisions_about_people=True,
    sector="financial services",
)

print(result.risk_tier)
print(result.rationale)
```

Assess whether a DPIA is required:

```python
from dpia_mapper import assess_dpia_requirement

result = assess_dpia_requirement(
    system_name="Customer Credit Scoring Model",
    automated_decisions=True,
    large_scale=True,
    novel_technology=True,
)

print(result.dpia_required)
print(result.requirement_rationale)
```

Generate a model card:

```python
from model_card import ModelCard, generate_model_card
```

A Streamlit build also runs at [aegis-classifier.streamlit.app](https://aegis-classifier.streamlit.app).

---

## Installation

Requirements:

- Python 3.9+
- Streamlit

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

---

## Contributing

AEGIS welcomes contributions from AI security professionals, AI governance practitioners, machine learning engineers, and anyone working at the intersection of security, ethics, and responsible AI.

See [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

Useful contribution areas include:

- AI security threat modelling and adversarial risk frameworks
- Human-in-the-loop patterns and oversight mechanisms
- Explainability and interpretability tooling
- Additional regulatory mappings
- Cloud platform integration examples
- Tests and documentation improvements

---

## Community & Support

- [GitHub Discussions](https://github.com/Kem-Ada/AEGIS/discussions)
- [Issues](https://github.com/Kem-Ada/AEGIS/issues)
- [LinkedIn](https://linkedin.com/in/kem-a-695462101)

---

## License

MIT License — see [LICENSE](LICENSE) for details.

Free to use, modify, and distribute. Attribution appreciated.

---

## About

AEGIS is an independent open source project founded and maintained by [Kem Ada](https://linkedin.com/in/kem-a-695462101), a Cybersecurity GRC & AI Risk Specialist with global experience across EMEA, North America, and APAC. The project grew out of real-world enterprise AI security and governance work and the absence of accessible, open source tooling that treats AI security and AI governance as two sides of the same problem.

---

*AEGIS is not legal advice. It is a practical framework to support AI security and governance workflows.*

