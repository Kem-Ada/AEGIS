"""
AEGIS — AI Ethics & Governance Integrated System
# Copyright (c) 2026 Kem Ada. Licensed under the MIT License.
GDPR Article 35 DPIA Mapper

Maps AI systems against GDPR Article 35 DPIA requirements.
Author: Kem Ada | https://linkedin.com/in/kem-a-695462101
"""

from dataclasses import dataclass
from typing import List


@dataclass
class DPIAResult:
    system_name: str
    dpia_required: bool
    requirement_rationale: str
    triggered_criteria: List[str]
    data_categories: List[str]
    risks_to_individuals: List[str]
    recommended_mitigations: List[str]
    residual_risk_level: str
    dpo_consultation_required: bool
    summary: str


# GDPR Article 35 high-risk criteria
DPIA_CRITERIA = {
    "automated_decisions": {
        "label": "Automated decision-making with significant effects (Art. 35(3)(a))",
        "triggered_by": "automated_decisions"
    },
    "large_scale_special": {
        "label": "Large-scale processing of special category data (Art. 35(3)(b))",
        "triggered_by": "special_category_data"
    },
    "systematic_monitoring": {
        "label": "Systematic monitoring of publicly accessible areas (Art. 35(3)(c))",
        "triggered_by": "systematic_monitoring"
    },
    "vulnerable_subjects": {
        "label": "Processing data of vulnerable individuals (children, employees, patients)",
        "triggered_by": "vulnerable_subjects"
    },
    "biometric_data": {
        "label": "Processing biometric data for unique identification",
        "triggered_by": "biometric_data"
    },
    "large_scale_processing": {
        "label": "Large-scale processing affecting many individuals",
        "triggered_by": "large_scale"
    },
    "novel_technology": {
        "label": "Use of novel or innovative technology",
        "triggered_by": "novel_technology"
    }
}

RISK_MITIGATIONS = {
    "automated_decisions": [
        "Implement human review for all significant automated decisions",
        "Provide clear opt-out mechanism for automated processing",
        "Document decision logic and ensure explainability",
        "Establish appeals process for individuals",
        "Comply with GDPR Article 22 requirements"
    ],
    "special_category_data": [
        "Identify explicit legal basis under Article 9",
        "Implement data minimisation — collect only what is strictly necessary",
        "Apply pseudonymisation or anonymisation where possible",
        "Restrict access to authorised personnel only",
        "Conduct regular data audits"
    ],
    "biometric_data": [
        "Obtain explicit consent or establish alternative legal basis",
        "Implement strong encryption for biometric data at rest and in transit",
        "Define and enforce strict retention periods",
        "Ensure data is not used beyond its original purpose"
    ],
    "vulnerable_subjects": [
        "Apply enhanced safeguards for vulnerable data subjects",
        "Ensure parental consent mechanisms where children are involved",
        "Conduct regular reviews of processing activities",
        "Appoint dedicated data protection contact"
    ],
    "large_scale": [
        "Implement robust data governance framework",
        "Conduct regular privacy impact reviews",
        "Ensure data subject rights mechanisms are scalable",
        "Document retention and deletion schedules"
    ],
    "novel_technology": [
        "Document technology assessment and risk evaluation",
        "Engage DPO early in technology deployment",
        "Monitor regulatory guidance on emerging technology",
        "Plan for iterative privacy reviews as technology evolves"
    ]
}


def assess_dpia_requirement(
    system_name: str,
    automated_decisions: bool = False,
    special_category_data: bool = False,
    systematic_monitoring: bool = False,
    vulnerable_subjects: bool = False,
    biometric_data: bool = False,
    large_scale: bool = False,
    novel_technology: bool = False,
    data_categories: List[str] = None,
    estimated_data_subjects: int = 0,
) -> DPIAResult:
    """
    Assesses whether a DPIA is required under GDPR Article 35
    and maps applicable risks and mitigations.
    """

    triggered_criteria = []
    recommended_mitigations = []
    risks = []

    inputs = {
        "automated_decisions": automated_decisions,
        "special_category_data": special_category_data,
        "systematic_monitoring": systematic_monitoring,
        "vulnerable_subjects": vulnerable_subjects,
        "biometric_data": biometric_data,
        "large_scale": large_scale,
        "novel_technology": novel_technology,
    }

    for key, triggered in inputs.items():
        if triggered:
            criteria_info = next(
                (v for v in DPIA_CRITERIA.values() if v["triggered_by"] == key), None
            )
            if criteria_info:
                triggered_criteria.append(criteria_info["label"])
            if key in RISK_MITIGATIONS:
                recommended_mitigations.extend(RISK_MITIGATIONS[key])

    # Determine if DPIA is required (2+ criteria = mandatory)
    dpia_required = len(triggered_criteria) >= 2 or biometric_data or special_category_data or automated_decisions

    # Build risk list
    if automated_decisions:
        risks.append("Risk of unfair or discriminatory automated decisions affecting individuals")
        risks.append("Risk of lack of transparency in decision-making process")
    if special_category_data or biometric_data:
        risks.append("Risk of sensitive data breach with severe impact on individuals")
        risks.append("Risk of unauthorised access to special category or biometric data")
    if large_scale:
        risks.append("Risk of large-scale data breach affecting many individuals simultaneously")
    if vulnerable_subjects:
        risks.append("Heightened risk of harm to vulnerable individuals including children")
    if novel_technology:
        risks.append("Risk of unforeseen consequences from novel or untested technology")

    if not risks:
        risks.append("No significant risks identified based on provided information")

    # Remove duplicate mitigations
    recommended_mitigations = list(dict.fromkeys(recommended_mitigations))

    # Residual risk
    if len(triggered_criteria) >= 3 or (biometric_data and automated_decisions):
        residual_risk = "HIGH — DPO consultation and supervisory authority prior consultation may be required"
    elif len(triggered_criteria) >= 2:
        residual_risk = "MEDIUM — DPIA mandatory, implement mitigations before deployment"
    elif len(triggered_criteria) == 1:
        residual_risk = "LOW-MEDIUM — DPIA recommended, monitor processing activities"
    else:
        residual_risk = "LOW — Standard data protection measures sufficient"

    dpo_required = len(triggered_criteria) >= 3 or (biometric_data and large_scale)

    if dpia_required:
        rationale = f"DPIA is mandatory. {len(triggered_criteria)} high-risk criteria identified under GDPR Article 35."
        summary = f"This AI system requires a full DPIA before deployment. {len(triggered_criteria)} Article 35 criteria were triggered. Implement all recommended mitigations and consult your DPO."
    elif len(triggered_criteria) == 1:
        rationale = "DPIA is recommended but not strictly mandatory based on current criteria. Monitor and review."
        summary = "One high-risk criterion was identified. A DPIA is recommended as best practice. Review processing activities regularly."
    else:
        rationale = "No high-risk criteria triggered. Standard data protection measures apply."
        summary = "No DPIA required based on provided information. Ensure standard GDPR compliance measures are in place."

    return DPIAResult(
        system_name=system_name,
        dpia_required=dpia_required,
        requirement_rationale=rationale,
        triggered_criteria=triggered_criteria,
        data_categories=data_categories or [],
        risks_to_individuals=risks,
        recommended_mitigations=recommended_mitigations,
        residual_risk_level=residual_risk,
        dpo_consultation_required=dpo_required,
        summary=summary
    )


def print_dpia_result(result: DPIAResult):
    print("\n" + "="*60)
    print("  AEGIS — GDPR Article 35 DPIA Assessment")
    print("="*60)
    print(f"  System: {result.system_name}")
    print(f"  DPIA Required: {'YES ⚠️' if result.dpia_required else 'NOT MANDATORY'}")
    print(f"  Rationale: {result.requirement_rationale}")

    if result.triggered_criteria:
        print(f"\n  Triggered Criteria:")
        for c in result.triggered_criteria:
            print(f"  • {c}")

    print(f"\n  Risks to Individuals:")
    for r in result.risks_to_individuals:
        print(f"  • {r}")

    print(f"\n  Recommended Mitigations:")
    for i, m in enumerate(result.recommended_mitigations, 1):
        print(f"  {i}. {m}")

    print(f"\n  Residual Risk: {result.residual_risk_level}")
    print(f"  DPO Consultation Required: {'YES' if result.dpo_consultation_required else 'NO'}")
    print(f"\n  Summary: {result.summary}")
    print("="*60 + "\n")


if __name__ == "__main__":
    result = assess_dpia_requirement(
        system_name="Customer Credit Scoring Model",
        automated_decisions=True,
        large_scale=True,
        novel_technology=True,
        data_categories=["Financial data", "Credit history", "Transaction data"],
        estimated_data_subjects=50000
    )
    print_dpia_result(result)
