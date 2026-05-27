
from modules.module1_risk_estimation import expected_claims



def expected_claim_cost(n, p, claim_amount):
    claims = expected_claims(n, p)
    return claims * claim_amount


def reserve_amount(total_claim_cost, reserve_percent):
    return total_claim_cost * (reserve_percent / 100)


def total_required_fund(total_claim_cost, reserve):
    return total_claim_cost + reserve


def premium_per_customer(total_required, n):
    return total_required / n