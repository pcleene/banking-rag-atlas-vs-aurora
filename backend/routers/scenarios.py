"""GET /api/scenarios -- predefined killer test scenarios."""

from __future__ import annotations

from fastapi import APIRouter

from backend.models.schemas import Scenario

router = APIRouter()

SCENARIOS: list[Scenario] = [
    Scenario(
        id=1,
        title="CEO Identification",
        query="Who is the CEO of MYBank?",
        description=(
            "Tests whether retrieval surfaces the most recent annual report and "
            "correctly identifies the current CEO despite older documents naming "
            "a different person."
        ),
        expected_correct="Lim Siew Hua (from 2024 Annual Report)",
        expected_failure=(
            "May return a former CEO from an older annual report if status "
            "filtering or recency preference is missing."
        ),
        suggested_filters={"status": "current"},
        suggested_options={"use_reranking": True, "embedding_mode": "contextual"},
    ),
    Scenario(
        id=2,
        title="Late Payment Fee on Gold Credit Card",
        query="What is the late payment fee on the Gold Credit Card?",
        description=(
            "Tests precise retrieval from the current Product Disclosure Sheet "
            "(PDS). The 2024 PDS states RM50; older versions may differ."
        ),
        expected_correct="RM50 (from 2024 Gold Credit Card PDS)",
        expected_failure=(
            "May return outdated fee amount from a superseded PDS version."
        ),
        suggested_filters={"status": "current", "document_type": "pds"},
        suggested_options={"use_reranking": True, "embedding_mode": "contextual"},
    ),
    Scenario(
        id=3,
        title="Gold vs Platinum Card Eligibility",
        query="Compare the Gold and Platinum card eligibility criteria",
        description=(
            "Requires retrieval from two separate product sheets for a fair "
            "comparison. Both must be current versions."
        ),
        expected_correct="Current eligibility criteria from both Gold and Platinum card PDS documents",
        expected_failure=(
            "May mix current and superseded product info, giving an inaccurate "
            "comparison."
        ),
        suggested_filters={"status": "current"},
        suggested_options={
            "use_hybrid_search": True,
            "use_reranking": True,
            "embedding_mode": "contextual",
        },
    ),
    Scenario(
        id=4,
        title="SME Overdraft Limits",
        query="What are the overdraft limits for SME customers?",
        description=(
            "Tests retrieval of the current overdraft policy. The 2024 policy "
            "has different limits from the 2021 version."
        ),
        expected_correct="2024 overdraft limits from the current policy document",
        expected_failure=(
            "May return 2021 limits if the superseded version is not filtered out."
        ),
        suggested_filters={"status": "current"},
        suggested_options={"use_reranking": True, "embedding_mode": "contextual"},
    ),
    Scenario(
        id=5,
        title="Current Fixed Deposit Rates",
        query="What are the current fixed deposit rates?",
        description=(
            "Tests whether retrieval picks the latest rate sheet. Rates change "
            "quarterly and only the Q1 2024 sheet should be surfaced."
        ),
        expected_correct="Q1 2024 fixed deposit rates",
        expected_failure=(
            "May return rates from an older quarter if date-based ranking is weak."
        ),
        suggested_filters={"status": "current"},
        suggested_options={"use_reranking": True, "embedding_mode": "standard"},
    ),
    Scenario(
        id=6,
        title="KYC Process for New Account Opening",
        query="What is the KYC process for new account opening?",
        description=(
            "Tests cross-document retrieval: the answer should combine the 2024 "
            "KYC policy with the branch operations manual for a complete picture."
        ),
        expected_correct="2024 KYC policy combined with branch operations manual",
        expected_failure=(
            "May return only one source, giving an incomplete answer."
        ),
        suggested_filters={"status": "current"},
        suggested_options={
            "use_hybrid_search": True,
            "use_reranking": True,
            "embedding_mode": "contextual",
        },
    ),
    Scenario(
        id=7,
        title="Board Members of MYBank Group",
        query="Who are the board members of MYBank Group?",
        description=(
            "Tests entity-level filtering. Board member lists differ between "
            "MYBank Group and subsidiary entities."
        ),
        expected_correct="2024 board members of MYBank Group from current annual report",
        expected_failure=(
            "May return board members from a subsidiary or from an older report."
        ),
        suggested_filters={"status": "current", "entity": "MYBank Group"},
        suggested_options={"use_reranking": True, "embedding_mode": "contextual"},
    ),
    Scenario(
        id=8,
        title="Overdraft Policy Changes 2021-2024",
        query="What changed in the overdraft policy between 2021 and 2024?",
        description=(
            "Control scenario: intentionally requires BOTH the superseded (2021) "
            "and current (2024) policy documents for a meaningful comparison. "
            "Filtering to 'current' only would miss half the answer."
        ),
        expected_correct=(
            "Comparison of both 2021 (superseded) and 2024 (current) overdraft "
            "policy versions"
        ),
        expected_failure=(
            "Returns only one version if status filter is too restrictive."
        ),
        suggested_filters={},
        suggested_options={
            "use_hybrid_search": True,
            "use_reranking": True,
            "embedding_mode": "contextual",
        },
    ),
]


@router.get("/scenarios", response_model=list[Scenario])
async def list_scenarios():
    """Return the predefined killer test scenarios for the demo."""
    return SCENARIOS
