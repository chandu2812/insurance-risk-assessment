
from modules.module1_risk_estimation import cumulative_probability


def probability_more_than(n, threshold, p):
    return 1 - cumulative_probability(n, threshold, p)


def policy_decision(n, threshold, p):
    risk_probability = probability_more_than(n, threshold, p)

    if risk_probability < 0.10:
        return {
            "decision": "ACCEPT",
            "risk_level": "Low Risk",
            "probability": round(risk_probability, 4)
        }

    elif risk_probability < 0.25:
        return {
            "decision": "REVIEW",
            "risk_level": "Medium Risk",
            "probability": round(risk_probability, 4)
        }

    else:
        return {
            "decision": "REJECT",
            "risk_level": "High Risk",
            "probability": round(risk_probability, 4)
        }