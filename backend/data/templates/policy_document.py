"""
Template-based generator for MYBank internal policy documents.
Produces 7 policy documents with realistic Malaysian banking compliance content.
"""

from datetime import datetime


def generate_policy_documents() -> list[dict]:
    """Generate 7 policy documents with full metadata."""
    policies = []

    # ── Overdraft Policy (Jan 2024) - CURRENT ───────────────────────────
    policies.append({
        "title": "MYBank Overdraft Policy (Effective January 2024)",
        "sections": [
            {
                "heading": "Policy Objective and Scope",
                "content": (
                    "This Overdraft Policy establishes the principles, governance framework, and "
                    "operational guidelines for the origination, management, and monitoring of overdraft "
                    "facilities extended by MYBank Berhad and its banking subsidiaries. The policy applies "
                    "to all overdraft products across consumer banking, business banking, and corporate "
                    "banking segments.\n\n"
                    "This policy is issued in compliance with Bank Negara Malaysia's Policy Document on "
                    "Credit Risk (BNM/RH/PD 030-12), the Financial Services Act 2013, and the Guidelines "
                    "on Responsible Financing (BNM/RH/GL 018-3). It supersedes the MYBank Overdraft Policy "
                    "effective March 2021 and reflects updates to credit assessment standards, digital "
                    "lending practices, and BNM's revised guidelines on credit risk management.\n\n"
                    "All staff involved in the origination, approval, and management of overdraft facilities "
                    "must familiarise themselves with this policy and its associated operational procedures. "
                    "Non-compliance with this policy may result in disciplinary action in accordance with "
                    "the MYBank Staff Handbook and Code of Conduct."
                ),
            },
            {
                "heading": "Credit Assessment and Approval",
                "content": (
                    "Credit assessment for overdraft facilities must be conducted in accordance with "
                    "MYBank's Credit Risk Assessment Framework and the principles of responsible financing "
                    "as prescribed by Bank Negara Malaysia.\n\n"
                    "For Consumer Overdraft Facilities:\n"
                    "- Minimum borrower age: 21 years\n"
                    "- Minimum annual income: RM36,000 (salaried) or RM48,000 (self-employed)\n"
                    "- Maximum facility amount: RM150,000 (unsecured) or RM500,000 (secured)\n"
                    "- Debt Service Ratio (DSR): Must not exceed 70% of net income, inclusive of all "
                    "existing debt obligations\n"
                    "- CCRIS and CTOS checks are mandatory for all applications\n"
                    "- Internal credit scoring must achieve a minimum score of 650 on the MYBank Credit "
                    "Scoring Model v4.2\n\n"
                    "For Business/SME Overdraft Facilities:\n"
                    "- Minimum business operating history: 2 years\n"
                    "- Financial statements for the latest 2 financial years must be reviewed\n"
                    "- Clean (unsecured) facilities up to RM250,000 are available under the Credit "
                    "Guarantee Corporation (CGC) Portfolio Guarantee scheme\n"
                    "- Secured facilities require collateral valued at a minimum of 120% of the facility "
                    "limit (property) or 100% (fixed deposits)\n\n"
                    "Approval Authority:\n"
                    "- Up to RM100,000: Branch Manager (Grade M2 and above)\n"
                    "- RM100,001 to RM500,000: Regional Credit Centre\n"
                    "- RM500,001 to RM2,000,000: Group Credit Approval Committee\n"
                    "- Above RM2,000,000: Board Credit Committee"
                ),
            },
            {
                "heading": "Facility Monitoring and Review",
                "content": (
                    "All overdraft facilities are subject to annual review, regardless of facility size. "
                    "The review must assess the borrower's continued creditworthiness, facility utilisation "
                    "patterns, and compliance with facility conditions.\n\n"
                    "Key monitoring indicators include:\n"
                    "- Utilisation rate: Facilities with consistently low utilisation (below 10% for 6 "
                    "consecutive months) should be reviewed for reduction or cancellation\n"
                    "- Hard-core utilisation: Overdraft facilities where the outstanding balance has not "
                    "fallen below 85% of the limit for 6 consecutive months must be flagged for assessment. "
                    "Where hard-core utilisation is identified, the relationship manager must propose "
                    "conversion to a term loan facility.\n"
                    "- Excess utilisation: Any utilisation beyond the approved limit must be reported to "
                    "the Credit Monitoring Unit within 24 hours. Excess utilisation is subject to penalty "
                    "interest of Base Rate + 5.00% per annum.\n\n"
                    "Overdraft facilities classified as impaired under MFRS 9 must be transferred to the "
                    "Group Special Assets Management (GSAM) division for recovery action. The classification "
                    "follows Bank Negara Malaysia's impairment classification guidelines, with facilities "
                    "being classified as Stage 2 when 30 days past due and Stage 3 when 90 days past due."
                ),
            },
            {
                "heading": "Digital Overdraft Origination",
                "content": (
                    "MYBank's digital overdraft origination channel enables eligible customers to apply "
                    "for and receive overdraft facilities entirely online through the MYBank GO mobile "
                    "application. Digital origination is available for consumer overdraft facilities up to "
                    "RM50,000 (unsecured).\n\n"
                    "The digital origination process incorporates:\n"
                    "- eKYC verification using MYBank's proprietary facial recognition technology, "
                    "compliant with BNM's eKYC Policy Document (BNM/RH/PD 035-8)\n"
                    "- Automated credit decisioning using the MYBank AI Credit Engine, which analyses "
                    "bank statements, CCRIS data, and alternative data sources\n"
                    "- Digital document signing via qualified electronic signatures\n"
                    "- Real-time facility activation upon approval\n\n"
                    "All digital overdraft approvals are subject to the same credit assessment standards "
                    "as branch-originated facilities. The AI Credit Engine's decisioning logic is subject "
                    "to semi-annual model validation by the Group Model Risk Management team."
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank Overdraft Policy (Effective January 2024)",
                "document_type": "policy_document",
                "entity": "MYBank Group",
                "published_date": datetime(2024, 1, 1),
                "version": "4.0",
                "status": "current",
                "superseded_by": None,
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": "MYBank Overdraft Policy (Effective March 2021)",
                "related_documents": [
                    "MYBank Credit Risk Assessment Framework",
                    "MYBank SME Overdraft Facility Product Disclosure Sheet 2024",
                ],
                "amendment_history": [
                    {"version": "3.0", "date": datetime(2021, 3, 1), "changes": "Post-COVID updates, revised DSR thresholds"},
                    {"version": "4.0", "date": datetime(2024, 1, 1), "changes": "Digital origination, AI credit engine, revised approval limits"},
                ],
            },
            "approvals": [
                {"approver": "Encik Azman bin Mohd Yusof", "role": "Group CRO", "date": datetime(2023, 12, 15)},
                {"approver": "Lim Siew Hua", "role": "Group CEO", "date": datetime(2023, 12, 18)},
            ],
            "regulatory": {
                "bnm_circulars": ["BNM/RH/PD 030-12", "BNM/RH/GL 018-3", "BNM/RH/PD 035-8"],
                "compliance_categories": ["credit_risk", "responsible_financing", "digital_banking"],
                "data_classification": "internal",
            },
            "people_mentioned": [
                {"name": "Encik Azman bin Mohd Yusof", "role": "Group CRO", "entity": "MYBank Group",
                 "tenure_start": datetime(2020, 4, 1), "tenure_end": None},
            ],
            "distribution": {
                "target_audience": ["staff_credit", "staff_branches", "management"],
                "regions": ["Malaysia"],
            },
        },
    })

    # ── Overdraft Policy (March 2021) - SUPERSEDED ──────────────────────
    policies.append({
        "title": "MYBank Overdraft Policy (Effective March 2021)",
        "sections": [
            {
                "heading": "Policy Objective and Scope",
                "content": (
                    "This Overdraft Policy governs the origination and management of overdraft facilities "
                    "by MYBank Berhad. It applies to consumer, business, and corporate overdraft products. "
                    "This policy is issued in compliance with BNM/RH/PD 030-12 and the Financial Services "
                    "Act 2013.\n\n"
                    "The policy has been updated to reflect the post-COVID-19 operating environment, "
                    "incorporating revised credit assessment standards for borrowers affected by the "
                    "pandemic and the transition from BNM's blanket moratorium to targeted repayment "
                    "assistance programmes."
                ),
            },
            {
                "heading": "Credit Assessment Standards",
                "content": (
                    "Consumer Overdraft Facilities:\n"
                    "- Minimum borrower age: 21 years\n"
                    "- Minimum annual income: RM30,000 (salaried) or RM42,000 (self-employed)\n"
                    "- Maximum unsecured facility: RM100,000\n"
                    "- DSR must not exceed 65% of net income\n"
                    "- CCRIS/CTOS checks mandatory\n"
                    "- Internal credit score minimum: 600 (MYBank Credit Scoring Model v3.8)\n\n"
                    "Business/SME Overdraft Facilities:\n"
                    "- Minimum 3 years business operating history\n"
                    "- Clean facilities up to RM150,000 under CGC Portfolio Guarantee\n"
                    "- Secured facilities require collateral at minimum 130% coverage\n\n"
                    "COVID-19 Transition Provisions:\n"
                    "- Borrowers who participated in BNM's loan moratorium or targeted repayment "
                    "assistance must demonstrate 6 consecutive months of regular repayment before "
                    "new facility origination\n"
                    "- Enhanced income verification required for industries most affected by the "
                    "pandemic (tourism, hospitality, aviation, retail)\n\n"
                    "Approval Authority:\n"
                    "- Up to RM50,000: Branch Manager\n"
                    "- RM50,001 to RM300,000: Regional Credit Centre\n"
                    "- Above RM300,000: Group Credit Approval Committee"
                ),
            },
            {
                "heading": "Monitoring and Hard-Core Assessment",
                "content": (
                    "All overdraft facilities are subject to annual review. Hard-core utilisation is "
                    "defined as outstanding balance not falling below 90% of limit for 6 consecutive "
                    "months. Facilities showing hard-core utilisation must be assessed for conversion "
                    "to term loan within 30 days of identification.\n\n"
                    "Impaired facilities are classified per BNM guidelines: Stage 2 at 30 days past "
                    "due, Stage 3 at 90 days past due. Stage 3 facilities are transferred to GSAM.\n\n"
                    "This policy supersedes the MYBank Overdraft Policy effective January 2019."
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank Overdraft Policy (Effective March 2021)",
                "document_type": "policy_document",
                "entity": "MYBank Group",
                "published_date": datetime(2021, 3, 1),
                "version": "3.0",
                "status": "superseded",
                "superseded_by": "MYBank Overdraft Policy (Effective January 2024)",
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": "MYBank Overdraft Policy (Effective January 2019)",
                "related_documents": [
                    "MYBank SME Overdraft Facility Product Disclosure Sheet 2021",
                ],
                "amendment_history": [
                    {"version": "3.0", "date": datetime(2021, 3, 1), "changes": "Post-COVID updates, moratorium transition provisions"},
                ],
            },
            "approvals": [
                {"approver": "Encik Azman bin Mohd Yusof", "role": "Group CRO", "date": datetime(2021, 2, 20)},
                {"approver": "Tan Wei Ming", "role": "Group CEO", "date": datetime(2021, 2, 22)},
            ],
            "regulatory": {
                "bnm_circulars": ["BNM/RH/PD 030-12", "BNM/RH/GL 018-3"],
                "compliance_categories": ["credit_risk", "responsible_financing"],
                "data_classification": "internal",
            },
            "people_mentioned": [],
            "distribution": {
                "target_audience": ["staff_credit", "staff_branches", "management"],
                "regions": ["Malaysia"],
            },
        },
    })

    # ── Late Payment Policy (July 2023) - CURRENT ───────────────────────
    policies.append({
        "title": "MYBank Late Payment Policy (Effective July 2023)",
        "sections": [
            {
                "heading": "Policy Objective",
                "content": (
                    "This Late Payment Policy establishes the framework for the management of late "
                    "payments across all consumer and business credit products offered by MYBank Berhad, "
                    "including credit cards, personal loans, hire purchase, housing loans, and overdraft "
                    "facilities. The policy is designed to ensure consistent and fair treatment of borrowers "
                    "while maintaining the Group's credit quality standards.\n\n"
                    "This policy is issued in compliance with Bank Negara Malaysia's Policy Document on "
                    "Debt Management and Operations (BNM/RH/PD 031-7), the Guidelines on Responsible "
                    "Financing (BNM/RH/GL 018-3), and the Financial Services Act 2013. The policy also "
                    "incorporates the principles of BNM's Fair Treatment of Financial Consumers policy."
                ),
            },
            {
                "heading": "Late Payment Charges and Grace Periods",
                "content": (
                    "Credit Cards:\n"
                    "- Grace period: Payment is due 25 days from the statement date\n"
                    "- Gold Card: RM50 or 1% of total outstanding balance, whichever is higher\n"
                    "- Platinum Card: RM75 or 1% of total outstanding balance, whichever is higher\n"
                    "- Maximum late payment charge per billing cycle: RM100\n\n"
                    "Personal Loans and Hire Purchase:\n"
                    "- Grace period: 7 days from instalment due date\n"
                    "- Late payment charge: 1% per annum on the overdue instalment amount, calculated "
                    "on a daily basis from the due date until full payment is received\n\n"
                    "Housing Loans:\n"
                    "- Grace period: 7 days from instalment due date\n"
                    "- Late payment charge: 1% per annum on the overdue instalment amount\n\n"
                    "Overdraft Facilities:\n"
                    "- Excess utilisation beyond approved limit is subject to penalty interest of "
                    "Base Rate + 5.00% per annum on the excess amount\n"
                    "- Facilities that remain in excess for more than 30 consecutive days will be "
                    "subject to facility review and potential recall\n\n"
                    "MYBank will not compound late payment charges. Late payment charges are applied "
                    "only to the overdue amount, not the total outstanding balance, in line with "
                    "BNM's fair treatment principles."
                ),
            },
            {
                "heading": "Collection Procedures and Escalation",
                "content": (
                    "Day 1-14 Past Due: Automated SMS and email reminders are sent to the borrower. "
                    "Push notifications via MYBank GO app are also triggered.\n\n"
                    "Day 15-30 Past Due: Telephone collection by MYBank's internal collection team. "
                    "All collection calls must be made between 8:00 AM and 9:00 PM, Monday to Saturday. "
                    "No calls are permitted on Sundays and public holidays. Collection staff must comply "
                    "with the MYBank Collection Code of Conduct, which prohibits threatening language, "
                    "harassment, and contact with third parties regarding the borrower's debt.\n\n"
                    "Day 31-60 Past Due: Formal demand letter issued to the borrower. The borrower is "
                    "offered the option to restructure or reschedule the debt through MYBank's Debt "
                    "Management Programme.\n\n"
                    "Day 61-90 Past Due: Second demand letter with notice of potential legal action. "
                    "The account is escalated to the Group Special Assets Management (GSAM) division.\n\n"
                    "Day 91+ Past Due: The facility is classified as impaired (Stage 3 under MFRS 9). "
                    "GSAM initiates recovery action, which may include legal proceedings, engagement "
                    "of external collection agencies, or referral to the Agensi Kaunseling dan Pengurusan "
                    "Kredit (AKPK) for debt counselling.\n\n"
                    "All collection activities are conducted in accordance with BNM's Debt Management and "
                    "Operations policy and the Personal Data Protection Act 2010 (PDPA)."
                ),
            },
            {
                "heading": "Hardship Provisions",
                "content": (
                    "MYBank recognises that borrowers may experience financial difficulties due to "
                    "circumstances beyond their control, including job loss, medical emergencies, or "
                    "natural disasters. The following hardship provisions are available:\n\n"
                    "Temporary Payment Reduction: Monthly instalments may be reduced by up to 50% for "
                    "a period of 3 to 6 months, subject to documentation of financial hardship.\n\n"
                    "Tenure Extension: Loan tenure may be extended to reduce monthly instalment amounts, "
                    "subject to maximum tenure limits for each product type.\n\n"
                    "Debt Consolidation: Multiple credit facilities may be consolidated into a single "
                    "term loan at a reduced interest rate, simplifying the borrower's repayment obligations.\n\n"
                    "AKPK Referral: Borrowers who are unable to manage their debt obligations independently "
                    "are referred to AKPK for professional debt counselling and management. MYBank "
                    "participates in AKPK's Debt Management Programme (DMP) and will honour approved "
                    "DMP repayment plans.\n\n"
                    "All hardship applications must be assessed within 14 working days of receipt of "
                    "complete documentation."
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank Late Payment Policy (Effective July 2023)",
                "document_type": "policy_document",
                "entity": "MYBank Group",
                "published_date": datetime(2023, 7, 1),
                "version": "2.0",
                "status": "current",
                "superseded_by": None,
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": "MYBank Late Payment Policy (Effective January 2020)",
                "related_documents": [
                    "MYBank Collection Code of Conduct",
                    "MYBank Debt Management Programme Guidelines",
                ],
                "amendment_history": [
                    {"version": "2.0", "date": datetime(2023, 7, 1), "changes": "Updated collection hours, added digital notification channels, enhanced hardship provisions"},
                ],
            },
            "approvals": [
                {"approver": "Puan Norashikin binti Ahmad", "role": "Head of Consumer Banking Products", "date": datetime(2023, 6, 20)},
                {"approver": "Encik Razif bin Mohd Salleh", "role": "Chief Compliance Officer", "date": datetime(2023, 6, 22)},
            ],
            "regulatory": {
                "bnm_circulars": ["BNM/RH/PD 031-7", "BNM/RH/GL 018-3"],
                "compliance_categories": ["debt_management", "consumer_protection", "fair_treatment"],
                "data_classification": "internal",
            },
            "people_mentioned": [],
            "distribution": {
                "target_audience": ["staff_collections", "staff_branches", "management"],
                "regions": ["Malaysia"],
            },
        },
    })

    # ── KYC/AML Compliance Guidelines (2024 revision) - CURRENT ────────
    policies.append({
        "title": "MYBank KYC/AML Compliance Guidelines (2024 Revision)",
        "sections": [
            {
                "heading": "Purpose and Regulatory Framework",
                "content": (
                    "These KYC/AML Compliance Guidelines establish the standards and procedures for "
                    "Know Your Customer (KYC), Customer Due Diligence (CDD), and Anti-Money Laundering "
                    "(AML) compliance across MYBank Berhad and its subsidiaries. The guidelines are "
                    "issued in compliance with:\n\n"
                    "- Anti-Money Laundering, Anti-Terrorism Financing and Proceeds of Unlawful "
                    "Activities Act 2001 (AMLA)\n"
                    "- Bank Negara Malaysia's Policy Document on Anti-Money Laundering and Counter "
                    "Financing of Terrorism (AML/CFT) — Specified Entities (BNM/RH/PD 034-5)\n"
                    "- BNM's Policy Document on Customer Due Diligence (CDD) (BNM/RH/PD 027-16)\n"
                    "- Financial Action Task Force (FATF) Recommendations\n"
                    "- Labuan Financial Services Authority (LFSA) guidelines for Labuan operations\n\n"
                    "The 2024 revision incorporates enhanced requirements for digital customer "
                    "onboarding (eKYC), updated Politically Exposed Persons (PEP) screening procedures, "
                    "beneficial ownership identification standards aligned with the Companies Act 2016 "
                    "amendments, and the integration of AI-powered transaction monitoring systems."
                ),
            },
            {
                "heading": "Customer Due Diligence Requirements",
                "content": (
                    "Standard CDD (Individual Customers):\n"
                    "- Verify identity using original MyKad (Malaysian citizens) or passport (non-citizens)\n"
                    "- Verify residential address using utility bill, bank statement, or government "
                    "correspondence dated within 3 months\n"
                    "- Screen against internal watchlists, BNM sanctions list, UN Security Council "
                    "sanctions list, OFAC SDN list, and EU consolidated sanctions list\n"
                    "- Determine customer risk rating using the MYBank Customer Risk Assessment Matrix\n"
                    "- Record source of funds and purpose of account/transaction\n\n"
                    "Enhanced Due Diligence (EDD) is required for:\n"
                    "- Politically Exposed Persons (PEPs) and their family members and close associates\n"
                    "- Customers from FATF high-risk jurisdictions (grey list and black list countries)\n"
                    "- Non-face-to-face business relationships (including digital onboarding)\n"
                    "- Correspondent banking relationships\n"
                    "- Customers in high-risk industries: money services business, casino/gaming, "
                    "precious metals/stones, real estate agents, lawyers, and accountants\n"
                    "- Transactions above RM50,000 (single or cumulative within 24 hours)\n\n"
                    "EDD procedures include senior management approval, enhanced source of wealth "
                    "verification, enhanced ongoing monitoring, and annual review of the business "
                    "relationship."
                ),
            },
            {
                "heading": "eKYC and Digital Onboarding",
                "content": (
                    "MYBank's eKYC system enables remote customer identification and verification "
                    "through the MYBank GO mobile application, in compliance with BNM's eKYC Policy "
                    "Document (BNM/RH/PD 035-8).\n\n"
                    "The eKYC process comprises:\n"
                    "1. Document capture: High-resolution scan of MyKad (front and back) using the "
                    "device camera, with optical character recognition (OCR) for data extraction\n"
                    "2. Biometric verification: Facial recognition with liveness detection, matching "
                    "against the MyKad photo and Jabatan Pendaftaran Negara (JPN) database\n"
                    "3. OTP verification: One-time password sent to the registered mobile number\n"
                    "4. Risk assessment: Automated screening against sanctions lists and internal watchlists\n\n"
                    "eKYC is currently approved for: savings accounts, current accounts, fixed deposits, "
                    "credit cards, and personal financing up to RM50,000. Higher-risk products and "
                    "corporate accounts require face-to-face verification.\n\n"
                    "All eKYC records are retained for a minimum of 6 years from the date of account "
                    "closure, in compliance with AMLA record-keeping requirements."
                ),
            },
            {
                "heading": "Suspicious Transaction Reporting",
                "content": (
                    "All staff are required to report any suspicious transactions or activities to "
                    "the Group Compliance Division's Financial Intelligence Unit (FIU) immediately. "
                    "Suspicious Transaction Reports (STRs) must be filed with Bank Negara Malaysia's "
                    "Financial Intelligence and Enforcement Department (FIED) within 5 working days "
                    "of identification.\n\n"
                    "Red flags that may indicate suspicious activity include:\n"
                    "- Cash transactions at or above RM50,000 (or currency equivalent)\n"
                    "- Structuring of transactions to avoid reporting thresholds\n"
                    "- Transactions inconsistent with the customer's known profile or business\n"
                    "- Use of multiple accounts to funnel funds\n"
                    "- Transactions involving sanctioned countries or designated persons\n"
                    "- Rapid movement of funds through accounts with no apparent business purpose\n\n"
                    "MYBank's AI-powered transaction monitoring system (TMS) generates automated alerts "
                    "based on rule-based and machine learning models. All alerts must be investigated "
                    "and dispositioned within 10 working days. The TMS system is validated annually by "
                    "the Group Model Risk Management team.\n\n"
                    "Tipping off — informing the customer or any third party that a STR has been or "
                    "will be filed — is a criminal offence under Section 22 of AMLA and may result in "
                    "imprisonment and/or fine."
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank KYC/AML Compliance Guidelines (2024 Revision)",
                "document_type": "policy_document",
                "entity": "MYBank Group",
                "published_date": datetime(2024, 1, 15),
                "version": "5.0",
                "status": "current",
                "superseded_by": None,
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": "MYBank KYC/AML Compliance Guidelines (2022 Revision)",
                "related_documents": [
                    "MYBank Sanctions Screening Policy",
                    "MYBank eKYC Operational Procedures",
                ],
                "amendment_history": [
                    {"version": "4.0", "date": datetime(2022, 4, 1), "changes": "eKYC integration, enhanced PEP screening"},
                    {"version": "5.0", "date": datetime(2024, 1, 15), "changes": "AI transaction monitoring, beneficial ownership, updated sanctions lists"},
                ],
            },
            "approvals": [
                {"approver": "Encik Razif bin Mohd Salleh", "role": "Chief Compliance Officer", "date": datetime(2024, 1, 10)},
                {"approver": "Lim Siew Hua", "role": "Group CEO", "date": datetime(2024, 1, 12)},
            ],
            "regulatory": {
                "bnm_circulars": ["BNM/RH/PD 034-5", "BNM/RH/PD 027-16", "BNM/RH/PD 035-8"],
                "compliance_categories": ["aml_cft", "kyc", "sanctions_screening", "ekyc"],
                "data_classification": "confidential",
            },
            "people_mentioned": [
                {"name": "Encik Razif bin Mohd Salleh", "role": "Chief Compliance Officer", "entity": "MYBank Group",
                 "tenure_start": datetime(2019, 9, 1), "tenure_end": None},
            ],
            "distribution": {
                "target_audience": ["staff_compliance", "staff_branches", "staff_operations", "management"],
                "regions": ["Malaysia", "ASEAN"],
            },
        },
    })

    # ── KYC/AML Compliance Guidelines (2022 revision) - SUPERSEDED ─────
    policies.append({
        "title": "MYBank KYC/AML Compliance Guidelines (2022 Revision)",
        "sections": [
            {
                "heading": "Purpose and Regulatory Framework",
                "content": (
                    "These guidelines govern KYC, CDD, and AML/CFT compliance for MYBank Berhad and "
                    "subsidiaries, issued under AMLA 2001, BNM/RH/PD 034-5, and FATF Recommendations. "
                    "The 2022 revision introduces eKYC procedures for digital onboarding and updated "
                    "PEP screening requirements following BNM's revised CDD policy document.\n\n"
                    "All staff handling customer onboarding, account management, and transaction "
                    "processing must complete the annual AML/CFT training programme. Non-compliance "
                    "may result in regulatory sanctions and disciplinary action."
                ),
            },
            {
                "heading": "CDD and EDD Requirements",
                "content": (
                    "Standard CDD requires: identity verification via original MyKad/passport, "
                    "address verification, sanctions screening (BNM, UN, OFAC lists), customer risk "
                    "rating, and source of funds declaration.\n\n"
                    "EDD is required for: PEPs, high-risk jurisdictions, non-face-to-face relationships, "
                    "correspondent banking, transactions above RM25,000 (single or cumulative).\n\n"
                    "STRs must be filed with BNM FIED within 7 working days of identification. "
                    "Cash transactions at or above RM25,000 trigger Cash Transaction Reports (CTRs).\n\n"
                    "Record retention: Minimum 6 years from account closure per AMLA requirements."
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank KYC/AML Compliance Guidelines (2022 Revision)",
                "document_type": "policy_document",
                "entity": "MYBank Group",
                "published_date": datetime(2022, 4, 1),
                "version": "4.0",
                "status": "superseded",
                "superseded_by": "MYBank KYC/AML Compliance Guidelines (2024 Revision)",
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": "MYBank KYC/AML Compliance Guidelines (2020 Revision)",
                "related_documents": [],
                "amendment_history": [],
            },
            "approvals": [
                {"approver": "Encik Razif bin Mohd Salleh", "role": "Chief Compliance Officer", "date": datetime(2022, 3, 25)},
            ],
            "regulatory": {
                "bnm_circulars": ["BNM/RH/PD 034-5", "BNM/RH/PD 027-16"],
                "compliance_categories": ["aml_cft", "kyc"],
                "data_classification": "confidential",
            },
            "people_mentioned": [],
            "distribution": {
                "target_audience": ["staff_compliance", "staff_branches", "management"],
                "regions": ["Malaysia"],
            },
        },
    })

    # ── Credit Card Dispute Resolution Procedure (2024) - CURRENT ──────
    policies.append({
        "title": "MYBank Credit Card Dispute Resolution Procedure (2024)",
        "sections": [
            {
                "heading": "Scope and Objectives",
                "content": (
                    "This procedure establishes the framework for handling credit card transaction "
                    "disputes raised by MYBank credit cardholders, including unauthorised transactions, "
                    "merchant disputes, duplicate charges, and billing errors. The procedure ensures "
                    "compliance with Bank Negara Malaysia's Guidelines on Dispute Resolution for Payment "
                    "Instruments (BNM/RH/GL 019-2), the Financial Services Act 2013, and the rules and "
                    "regulations of Visa International and Mastercard Worldwide.\n\n"
                    "MYBank is committed to resolving all disputes fairly, transparently, and within "
                    "the prescribed timelines. Cardholders are advised to report disputes as soon as "
                    "possible, and in any event within 60 calendar days from the statement date on which "
                    "the disputed transaction appears."
                ),
            },
            {
                "heading": "Dispute Categories and Timelines",
                "content": (
                    "Category 1 — Unauthorised Transactions (including fraud, stolen card, skimming):\n"
                    "- Provisional credit: Within 5 working days of receiving the dispute form\n"
                    "- Investigation timeline: 45 calendar days (domestic) or 90 calendar days (cross-border)\n"
                    "- Cardholder liability: Maximum RM250 if reported within 24 hours of discovery; "
                    "unlimited if not reported within 60 days\n\n"
                    "Category 2 — Merchant Disputes (goods not received, defective goods, service not rendered):\n"
                    "- Provisional credit: Not automatic; assessed case-by-case\n"
                    "- Investigation: 30 working days from receipt of supporting documentation\n"
                    "- Chargeback raised with acquirer within applicable card scheme timelines\n\n"
                    "Category 3 — Duplicate or Incorrect Charges:\n"
                    "- Provisional credit: Within 5 working days if preliminary review confirms duplication\n"
                    "- Resolution: Within 14 working days\n\n"
                    "Category 4 — Recurring Charge Disputes (subscription cancellations):\n"
                    "- Cardholder must provide evidence of cancellation request to the merchant\n"
                    "- Resolution: Within 30 working days\n\n"
                    "If a dispute cannot be resolved within the prescribed timelines, MYBank will "
                    "provide the cardholder with a written update on the investigation status and "
                    "revised expected resolution date."
                ),
            },
            {
                "heading": "Escalation and External Resolution",
                "content": (
                    "If the cardholder is not satisfied with MYBank's resolution, the dispute may be "
                    "escalated through the following channels:\n\n"
                    "Level 1: MYBank Card Centre Manager (response within 7 working days)\n"
                    "Level 2: MYBank Customer Experience Head (response within 14 working days)\n"
                    "Level 3: Ombudsman for Financial Services (OFS Malaysia) — free dispute resolution "
                    "for claims up to RM250,000. Website: www.ofs.org.my\n"
                    "Level 4: Bank Negara Malaysia BNMLINK — for regulatory complaints\n\n"
                    "MYBank will cooperate fully with OFS investigations and will comply with OFS "
                    "decisions that are accepted by the complainant."
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank Credit Card Dispute Resolution Procedure (2024)",
                "document_type": "policy_document",
                "entity": "MYBank Group",
                "published_date": datetime(2024, 2, 1),
                "version": "3.0",
                "status": "current",
                "superseded_by": None,
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": "MYBank Credit Card Dispute Resolution Procedure (2021)",
                "related_documents": [
                    "MYBank Gold Credit Card Product Disclosure Sheet v2.1",
                    "MYBank Platinum Credit Card Product Disclosure Sheet v3.0",
                ],
                "amendment_history": [
                    {"version": "3.0", "date": datetime(2024, 2, 1), "changes": "Updated timelines, added recurring charge disputes, enhanced provisional credit policy"},
                ],
            },
            "approvals": [
                {"approver": "Puan Norashikin binti Ahmad", "role": "Head of Consumer Banking Products", "date": datetime(2024, 1, 25)},
                {"approver": "Encik Razif bin Mohd Salleh", "role": "Chief Compliance Officer", "date": datetime(2024, 1, 28)},
            ],
            "regulatory": {
                "bnm_circulars": ["BNM/RH/GL 019-2"],
                "compliance_categories": ["dispute_resolution", "consumer_protection", "card_operations"],
                "data_classification": "internal",
            },
            "people_mentioned": [],
            "distribution": {
                "target_audience": ["staff_card_operations", "staff_customer_service", "staff_branches"],
                "regions": ["Malaysia"],
            },
        },
    })

    # ── Branch Operations Manual — Account Opening (2024) - CURRENT ────
    policies.append({
        "title": "MYBank Branch Operations Manual — Account Opening (2024)",
        "sections": [
            {
                "heading": "Account Opening Procedures",
                "content": (
                    "This chapter of the MYBank Branch Operations Manual establishes the standardised "
                    "procedures for opening deposit accounts (savings, current, and fixed deposit) at "
                    "MYBank branches nationwide. All branch staff involved in account opening must "
                    "complete the mandatory training programme and obtain certification from the MYBank "
                    "Academy before processing any account opening applications.\n\n"
                    "Account opening procedures must comply with:\n"
                    "- BNM's Policy Document on Customer Due Diligence (BNM/RH/PD 027-16)\n"
                    "- Anti-Money Laundering, Anti-Terrorism Financing and Proceeds of Unlawful "
                    "Activities Act 2001 (AMLA)\n"
                    "- Personal Data Protection Act 2010 (PDPA)\n"
                    "- Financial Services Act 2013\n\n"
                    "Standard Processing Time:\n"
                    "- Individual savings account: 30 minutes\n"
                    "- Individual current account: 45 minutes\n"
                    "- Corporate/business account: 2-3 working days (subject to document verification)\n"
                    "- Fixed deposit placement: 20 minutes"
                ),
            },
            {
                "heading": "Documentation Requirements",
                "content": (
                    "Individual Accounts (Malaysian Citizens):\n"
                    "- Original MyKad for identity verification (photocopy to be retained)\n"
                    "- Proof of address (utility bill, bank statement, or government letter within 3 months) "
                    "— required only if residential address differs from MyKad address\n"
                    "- Initial deposit: Savings account RM250 minimum, current account RM500 minimum\n"
                    "- Completed account opening form with specimen signature card\n"
                    "- Declaration of source of funds and purpose of account\n\n"
                    "Individual Accounts (Non-Malaysian Residents):\n"
                    "- Original passport with valid visa\n"
                    "- Employment pass, student pass, or valid work permit\n"
                    "- Letter of employment or university enrolment letter\n"
                    "- Proof of local address\n"
                    "- Initial deposit: Savings account RM1,000 minimum\n\n"
                    "Corporate/Business Accounts:\n"
                    "- Certificate of incorporation (Companies Commission of Malaysia, SSM)\n"
                    "- Memorandum and Articles of Association (or Constitution under Companies Act 2016)\n"
                    "- Board resolution authorising account opening and signatories\n"
                    "- MyKad/passport copies of all directors and authorised signatories\n"
                    "- Form 24 (list of shareholders) and Form 49 (list of directors)\n"
                    "- Business profile from SSM (not older than 3 months)\n"
                    "- Beneficial ownership declaration form (per Companies Act 2016, Section 60)\n"
                    "- Initial deposit: Current account RM1,000 minimum"
                ),
            },
            {
                "heading": "KYC Verification and Risk Assessment",
                "content": (
                    "All account opening applications must undergo the following KYC checks before "
                    "account activation:\n\n"
                    "1. Identity Verification: MyKad chip reading using the branch's MyKad reader device. "
                    "The biometric data on the MyKad chip must match the applicant. For non-Malaysians, "
                    "passport details must be verified against the Immigration Department database.\n\n"
                    "2. Sanctions Screening: The applicant's name, date of birth, and nationality must be "
                    "screened against BNM's designated lists, UN Security Council sanctions lists, OFAC "
                    "SDN list, and MYBank's internal watchlist. Screening is performed via the MYBank "
                    "Compliance Screening System (CSS).\n\n"
                    "3. Customer Risk Rating: The MYBank Customer Risk Assessment Matrix assigns a risk "
                    "rating (Low, Medium, High) based on factors including customer type, nationality, "
                    "occupation, source of funds, and expected transaction volume. High-risk customers "
                    "require Enhanced Due Diligence and Branch Manager approval.\n\n"
                    "4. PEP Screening: All applicants are screened against the MYBank PEP database, "
                    "which covers domestic and foreign PEPs, their family members, and close associates. "
                    "PEP accounts require Regional Compliance Officer approval.\n\n"
                    "5. Adverse Media Screening: Automated screening against news databases for any "
                    "negative media coverage related to financial crime, fraud, or regulatory action."
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank Branch Operations Manual — Account Opening (2024)",
                "document_type": "policy_document",
                "entity": "MYBank Group",
                "published_date": datetime(2024, 1, 2),
                "version": "6.0",
                "status": "current",
                "superseded_by": None,
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": "MYBank Branch Operations Manual — Account Opening (2022)",
                "related_documents": [
                    "MYBank KYC/AML Compliance Guidelines (2024 Revision)",
                    "MYBank eKYC Operational Procedures",
                ],
                "amendment_history": [
                    {"version": "6.0", "date": datetime(2024, 1, 2), "changes": "Updated KYC procedures, beneficial ownership requirements, processing times"},
                ],
            },
            "approvals": [
                {"approver": "Encik Mohd Hafiz bin Kamaruddin", "role": "Head of Branch Operations", "date": datetime(2023, 12, 20)},
                {"approver": "Encik Razif bin Mohd Salleh", "role": "Chief Compliance Officer", "date": datetime(2023, 12, 22)},
            ],
            "regulatory": {
                "bnm_circulars": ["BNM/RH/PD 027-16"],
                "compliance_categories": ["branch_operations", "kyc", "account_opening"],
                "data_classification": "internal",
            },
            "people_mentioned": [],
            "distribution": {
                "target_audience": ["staff_branches", "staff_operations"],
                "regions": ["Malaysia"],
            },
        },
    })

    return policies
