"""
AEGIS — AI Ethics & Governance Integrated System
EU AI Act Risk Classification Engine

Classifies AI systems by risk tier based on EU AI Act requirements.
Author: Kem Ada | https://linkedin.com/in/kem-a-695462101
"""

from dataclasses import dataclass
from typing import List


# --- Risk Tier Definitions ---

RISK_TIERS = {
    "UNACCEPTABLE": {
        "label": "🚫 Unacceptable Risk",
        "description": "This AI system is prohibited under the EU AI Act.",
        "obligations": [
            "This system must NOT be deployed in the EU.",
            "Deployment constitutes a breach of EU AI Act Article 5.",
        ]
    },
    "HIGH": {
        "label": "🔴 High Risk",
        "description": "This AI system is subject to strict obligations before deployment.",
        "obligations": [
            "Register in the EU AI Act database before deployment.",
            "Conduct a conformity assessment.",
            "Implement a risk management system.",
            "Ensure human oversight mechanisms are in place.",
            "Maintain technical documentation and logs.",
            "Ensure transparency and provide clear user information.",
            "Data governance: training data must be relevant, representative, and free of errors.",
        ]
    },
    "LIMITED": {
        "label": "🟡 Limited Risk",
        "description": "This AI system has transparency obligations.",
        "obligations": [
            "Inform users they are interacting with an AI system.",
            "Disclose AI-generated content where applicable.",
            "Ensure users can opt out of AI interaction where possible.",
        ]
    },
    "MINIMAL": {
        "label": "🟢 Minimal Risk",
        "description": "This AI system carries minimal regulatory risk.",
        "obligations": [
            "No mandatory obligations under EU AI Act.",
            "Best practice: follow voluntary codes of conduct.",
            "Document system purpose and intended use.",
        ]
    }
}


# --- Classification Logic ---

@dataclass
class ClassificationResult:
    system_name: str
    risk_tier: str
    label: str
    description: str
    obligations: List[str]
    rationale: str


def classify_ai_system(
    system_name: str,
    makes_automated_decisions_about_people: bool,
    sector: str,
    is_biometric: bool = False,
    is_social_scoring: bool = False,
    manipulates_behaviour: bool = False,
    is_chatbot_or_generated_content: bool = False,
) -> ClassificationResult:
    """
    Classifies an AI system under the EU AI Act risk framework.

    Args:
        system_name: Name or description of the AI system
        makes_automated_decisions_about_people: Does the system make or assist
            in decisions that affect individuals?
        sector: The sector the system operates in
        is_biometric: Does the system process biometric data?
        is_social_scoring: Does the system score or rank people based on behaviour?
        manipulates_behaviour: Does the system subliminally manipulate user behaviour?
        is_chatbot_or_generated_content: Is this a chatbot or generative AI system?

    Returns:
        ClassificationResult with risk tier, obligations, and rationale
    """

    HIGH_RISK_SECTORS = [
        "employment", "recruitment", "hr",
        "education", "vocational training",
        "credit", "financial services", "insurance",
        "healthcare", "medical",
        "law enforcement", "border control", "immigration",
        "critical infrastructure", "energy", "water", "transport",
        "justice", "legal", "democratic processes",
    ]

    # Step 1: Check for unacceptable risk
    if is_social_scoring:
        return ClassificationResult(
            system_name=system_name,
            risk_tier="UNACCEPTABLE",
            rationale="System performs social scoring of individuals, which is prohibited under EU AI Act Article 5.",
            **{k: v for k, v in RISK_TIERS["UNACCEPTABLE"].items()}
        )

    if manipulates_behaviour:
        return ClassificationResult(
            system_name=system_name,
            risk_tier="UNACCEPTABLE",
            rationale="System uses subliminal techniques to manipulate behaviour, prohibited under EU AI Act Article 5.",
            **{k: v for k, v in RISK_TIERS["UNACCEPTABLE"].items()}
        )

    if is_biometric and sector.lower() in ["law enforcement", "border control", "public spaces"]:
        return ClassificationResult(
            system_name=system_name,
            risk_tier="UNACCEPTABLE",
            rationale="Real-time remote biometric identification in public spaces by law enforcement is prohibited under EU AI Act Article 5.",
            **{k: v for k, v in RISK_TIERS["UNACCEPTABLE"].items()}
        )

    # Step 2: Check for high risk
    sector_lower = sector.lower()
    in_high_risk_sector = any(s in sector_lower for s in HIGH_RISK_SECTORS)

    if makes_automated_decisions_about_people and in_high_risk_sector:
        return ClassificationResult(
            system_name=system_name,
            risk_tier="HIGH",
            rationale=f"System makes automated decisions affecting individuals in a high-risk sector ({sector}). "
                      f"Classified as High Risk under EU AI Act Annex III.",
            **{k: v for k, v in RISK_TIERS["HIGH"].items()}
        )

    if is_biometric:
        return ClassificationResult(
            system_name=system_name,
            risk_tier="HIGH",
            rationale="System processes biometric data for identification or categorisation purposes.",
            **{k: v for k, v in RISK_TIERS["HIGH"].items()}
        )

    # Step 3: Check for limited risk
    if is_chatbot_or_generated_content:
        return ClassificationResult(
            system_name=system_name,
            risk_tier="LIMITED",
            rationale="System is a chatbot or generates synthetic content — transparency obligations apply under EU AI Act Article 52.",
            **{k: v for k, v in RISK_TIERS["LIMITED"].items()}
        )

    # Step 4: Minimal risk
    return ClassificationResult(
        system_name=system_name,
        risk_tier="MINIMAL",
        rationale="System does not meet criteria for higher risk tiers under the EU AI Act.",
        **{k: v for k, v in RISK_TIERS["MINIMAL"].items()}
    )


def print_result(result: ClassificationResult):
    """Prints a formatted classification report."""
    print("\n" + "="*60)
    print(f"  AEGIS — EU AI Act Risk Classification Report")
    print("="*60)
    print(f"  System:      {result.system_name}")
    print(f"  Risk Tier:   {result.label}")
    print(f"  Summary:     {result.description}")
    print(f"\n  Rationale:\n  {result.rationale}")
    print(f"\n  Obligations:")
    for i, obligation in enumerate(result.obligations, 1):
        print(f"  {i}. {obligation}")
    print("="*60 + "\n")


# --- Example Usage ---

if __name__ == "__main__":

    # Example 1: CV screening tool
    result1 = classify_ai_system(
        system_name="Automated CV Screening Tool",
        makes_automated_decisions_about_people=True,
        sector="recruitment",
    )
    print_result(result1)

    # Example 2: Customer service chatbot
    result2 = classify_ai_system(
        system_name="Customer Service Chatbot",
        makes_automated_decisions_about_people=False,
        sector="retail",
        is_chatbot_or_generated_content=True,
    )
    print_result(result2)

    # Example 3: Fraud detection
    result3 = classify_ai_system(
        system_name="Fraud Detection Model",
        makes_automated_decisions_about_people=True,
        sector="financial services",
    )
    print_result(result3)

