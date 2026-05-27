# =====================================================
# APP.PY
# Insurance Risk Assessment and Premium Pricing
# =====================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =====================================================
# IMPORT MODULES
# =====================================================

from modules.module1_risk_estimation import (
    binomial_probability,
    expected_claims,
    variance_claims,
    standard_deviation,
)

from modules.module2_group_pricing import (
    expected_claim_cost,
    reserve_amount,
    total_required_fund,
    premium_per_customer,
)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Insurance Risk Assessment",
    page_icon="📊",
    layout="wide"
)

# =====================================================
# UI DESIGN
# =====================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg,#020617,#0f172a,#1e293b);
}

h1, h2, h3 {
    color: white !important;
}

label {
    color: white !important;
}

section[data-testid="stSidebar"] {
    background: #020617;
}

[data-testid="stMetric"] {
    background: white;
    padding: 18px;
    border-radius: 18px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.2);
}

[data-testid="stMetricLabel"] {
    color: #111827 !important;
    font-size: 18px !important;
    font-weight: 700 !important;
}

[data-testid="stMetricValue"] {
    color: #111827 !important;
    font-size: 36px !important;
    font-weight: 800 !important;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

st.title("📊 Insurance Risk Assessment and Premium Pricing")

st.write(
    "This project uses Binomial Distribution to estimate insurance claim risk "
    "and calculate premium pricing for policyholders."
)

# =====================================================
# SIDEBAR INPUTS
# =====================================================

st.sidebar.title("⚙ Input Parameters")

n = st.sidebar.number_input(
    "Number of Policyholders (n)",
    min_value=1,
    value=100
)

p = st.sidebar.slider(
    "Probability of One Claim (p)",
    min_value=0.01,
    max_value=0.99,
    value=0.08
)

k = st.sidebar.number_input(
    "Exact Number of Claims (k)",
    min_value=0,
    max_value=int(n),
    value=2
)

claim_amount = st.sidebar.number_input(
    "Average Claim Amount (₹)",
    min_value=1000,
    value=50000
)

reserve_percent = st.sidebar.slider(
    "Reserve Percentage (%)",
    min_value=0,
    max_value=100,
    value=20
)

# =====================================================
# MODULE 1
# Risk Probability Estimation
# =====================================================

st.markdown("---")

st.header("📌 MODULE 1 — Risk Probability Estimation")

st.info(
    "This module calculates insurance claim probability "
    "using Binomial Distribution."
)

# CALCULATIONS

exact_prob = binomial_probability(n, k, p)

exp_claims = expected_claims(n, p)

variance = variance_claims(n, p)

std_dev = standard_deviation(n, p)

# DISPLAY

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Expected Claims",
        f"{exp_claims:.2f}"
    )

with col2:
    st.metric(
        "Variance",
        f"{variance:.2f}"
    )

with col3:
    st.metric(
        "Standard Deviation",
        f"{std_dev:.2f}"
    )

with col4:
    st.metric(
        "Exact Probability",
        f"{exact_prob:.4f}"
    )

# =====================================================
# CHART
# =====================================================

st.markdown("---")

st.subheader("📈 Claim Distribution")

x_values = list(range(0, min(int(n), 30) + 1))

y_values = [
    binomial_probability(n, x, p)
    for x in x_values
]

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(x_values, y_values)

ax.set_xlabel("Number of Claims")

ax.set_ylabel("Probability")

ax.set_title("Binomial Distribution of Insurance Claims")

st.pyplot(fig)

# =====================================================
# MODULE 2
# Premium Pricing & Reserve Fund Management
# =====================================================

st.markdown("---")

st.header("📌 MODULE 2 — Premium Pricing and Reserve Fund Management")

st.success(
    "This module calculates premium pricing and reserve forecasting."
)

# CALCULATIONS

total_claim_cost = expected_claim_cost(
    n,
    p,
    claim_amount
)

reserve = reserve_amount(
    total_claim_cost,
    reserve_percent
)

total_fund = total_required_fund(
    total_claim_cost,
    reserve
)

premium = premium_per_customer(
    total_fund,
    n
)

# DISPLAY

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Claim Cost",
        f"₹ {total_claim_cost:,.0f}"
    )

with c2:
    st.metric(
        "Reserve Amount",
        f"₹ {reserve:,.0f}"
    )

with c3:
    st.metric(
        "Total Fund",
        f"₹ {total_fund:,.0f}"
    )

with c4:
    st.metric(
        "Premium Per Customer",
        f"₹ {premium:,.0f}"
    )

# =====================================================
# FINAL REPORT
# =====================================================

st.markdown("---")

st.header("📋 Final Summary Report")

summary_df = pd.DataFrame({
    "Metric": [
        "Policyholders",
        "Expected Claims",
        "Variance",
        "Standard Deviation",
        "Premium Per Customer",
        "Reserve Amount"
    ],

    "Value": [
        str(n),
        str(round(exp_claims, 2)),
        str(round(variance, 2)),
        str(round(std_dev, 2)),
        f"₹ {round(premium, 2)}",
        f"₹ {round(reserve, 2)}"
    ]
})

st.dataframe(summary_df, width="stretch")

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.caption(
    "Final Year Project — Insurance Risk Assessment and Premium Pricing Using Binomial Distribution"
)