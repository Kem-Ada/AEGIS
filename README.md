# AEGIS — AI Ethics & Governance Integrated System

> Open source Python framework for AI security, governance, human-in-the-loop controls, explainability, and regulatory compliance across EU AI Act, GDPR Article 35, and ISO/IEC 42001.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

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

```bash
pip install aegis-framework
```

```python
from aegis import RiskClassifier, ModelCardGenerator, HITLController

# Classify an AI system under EU AI Act
classifier = RiskClassifier()
result = classifier.classify(
    system_name="Customer Credit Scoring Model",
    domain="financial_services",
    automated_decision=True
)
print(result.risk_tier)        # "HIGH"
print(result.obligations)      # List of applicable EU AI Act obligations

# Generate a model card
card = ModelCardGenerator()
card.generate(model_name="credit-scorer-v2", output_format="markdown")

# Define human-in-the-loop controls
hitl = HITLController()
hitl.define_checkpoint(
    decision_type="credit_denial",
    required_reviewer="human",
    escalation_threshold=0.85
)
```

---

## Features

| Feature | Status |
|---|---|
| EU AI Act risk classification engine | ✅ Available |
| Model card generator (Markdown + JSON) | ✅ Available |
| GDPR Article 35 DPIA mapping | ✅ Available |
| AI security threat assessment module | 🔄 In progress |
| Human-in-the-loop control framework | 🔄 In progress |
| Explainability & transparency reporting | 🔄 In progress |
| AI system inventory tracker | 🔄 In progress |
| Streamlit dashboard UI | 📅 Planned |
| AWS / Azure / GCP integration docs | 📅 Planned |

---

## Installation

**Requirements:** Python 3.9+, pandas, pydantic, streamlit

```bash
git clone https://github.com/aegis-framework/aegis.git
cd aegis
pip install -r requirements.txt
```

---

## Contributing

AEGIS is community-driven. We welcome contributions from AI security professionals, AI governance practitioners, machine learning engineers, and anyone working at the intersection of security, ethics, and responsible AI.

See [CONTRIBUTING.md](CONTRIBUTING.md) to get started. Good first issues are labelled `good-first-issue`.

Areas where we especially welcome help:
- AI security threat modelling and adversarial risk frameworks
- Human-in-the-loop patterns and oversight mechanisms
- Explainability and interpretability tooling
- Additional regulatory mappings (NIST AI RMF, ISO 42001, UK AI Code of Practice)
- Cloud platform integration examples (AWS, Azure, GCP)

---

## Community & Support

- 💬 [GitHub Discussions](https://github.com/aegis-framework/aegis/discussions) — questions, ideas, show and tell
- 🐛 [Issues](https://github.com/aegis-framework/aegis/issues) — bug reports and feature requests
- 📣 Follow project updates on [LinkedIn](https://linkedin.com/in/kem-a-695462101)

---

## License

MIT License — see [LICENSE](LICENSE) for details.

Free to use, modify, and distribute. Attribution appreciated.

---

## About

AEGIS was created by [Kem Ada](https://linkedin.com/in/kem-a-695462101), a Cybersecurity GRC & AI Risk Specialist with global experience across EMEA, North America, and APAC. The project grew out of real-world enterprise AI security and governance work and the absence of accessible, open source tooling that treats AI security and AI governance as two sides of the same problem.

---

*AEGIS is not legal advice. It is a practical framework to support AI security and governance workflows.*

