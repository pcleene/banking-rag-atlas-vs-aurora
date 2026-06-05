"""
Template-based generator for MYBank FAQ documents.
Produces 4 FAQ documents with realistic Malaysian banking Q&A content.
"""

from datetime import datetime


def generate_faqs() -> list[dict]:
    """Generate 4 FAQ documents with full metadata."""
    faqs = []

    # ── Credit Card FAQ (Dec 2023) ──────────────────────────────────────
    faqs.append({
        "title": "MYBank Credit Card Frequently Asked Questions (Updated December 2023)",
        "sections": [
            {
                "heading": "Application and Eligibility",
                "content": (
                    "Q: What are the eligibility requirements for the MYBank Gold Credit Card?\n"
                    "A: To apply for the MYBank Gold Credit Card, you must be at least 21 years old, "
                    "a Malaysian citizen or permanent resident, and earn a minimum annual income of "
                    "RM36,000 (salaried) or RM48,000 (self-employed). You must also have a satisfactory "
                    "credit record as assessed by CCRIS and CTOS. Non-residents with a valid employment "
                    "pass may apply with a minimum annual income of RM60,000.\n\n"
                    "Q: How do I apply for a MYBank credit card?\n"
                    "A: You can apply through: (1) MYBank GO mobile app — instant application with eKYC "
                    "verification; (2) MYBank Online Banking — complete the online application form; "
                    "(3) Any MYBank branch — bring your MyKad, latest 3 months' salary slips, and latest "
                    "EA form; (4) MYBank Direct Sales representatives. Processing time is typically 5-7 "
                    "working days for branch applications and 3-5 working days for digital applications.\n\n"
                    "Q: Can I apply for a supplementary card?\n"
                    "A: Yes, you can apply for supplementary cards for family members aged 18 and above. "
                    "The supplementary card annual fee for Gold cards is RM100, and supplementary "
                    "cardholders share the principal cardholder's credit limit. You can apply for up to "
                    "5 supplementary cards."
                ),
            },
            {
                "heading": "Fees, Interest and Payments",
                "content": (
                    "Q: What is the annual fee for the MYBank Gold Credit Card?\n"
                    "A: The annual fee for the Gold Credit Card is RM200 for the principal card and RM100 "
                    "for a supplementary card. The first year's annual fee is waived for new cardholders. "
                    "In subsequent years, the annual fee is waived if your total annual retail spend "
                    "exceeds RM30,000.\n\n"
                    "Q: What is the interest rate on my credit card?\n"
                    "A: The interest rate for retail purchases on the Gold Credit Card is 15% per annum. "
                    "Cash advance transactions are charged at 18% per annum. If you pay your total "
                    "outstanding balance in full by the payment due date, you will enjoy an interest-free "
                    "period of up to 20 days. The Platinum Credit Card offers a lower retail rate of "
                    "13.5% per annum.\n\n"
                    "Q: What happens if I miss my payment due date?\n"
                    "A: A late payment charge of RM50 or 1% of total outstanding balance (whichever is "
                    "higher) will be applied. For Platinum cardholders, the late payment charge is RM75 "
                    "or 1% (whichever is higher). Late payments may also affect your credit score as "
                    "reported to CCRIS. We strongly encourage you to set up auto-debit through MYBank GO "
                    "to avoid missing payments.\n\n"
                    "Q: What is the minimum payment amount?\n"
                    "A: The minimum monthly payment is 5% of your total outstanding balance or RM50, "
                    "whichever is higher. However, we strongly encourage you to pay the full balance "
                    "each month to avoid interest charges. Paying only the minimum amount may result in "
                    "a significantly longer debt repayment period."
                ),
            },
            {
                "heading": "Rewards, Benefits and Disputes",
                "content": (
                    "Q: How does the MYBank Rewards Points programme work?\n"
                    "A: You earn rewards points on eligible retail transactions. Gold Card: 5x points per "
                    "RM1 on dining, 3x points on online transactions, 1x point on all other retail. "
                    "Platinum Card: 8x points on dining, 5x on travel, 4x on online, 1.5x on all other. "
                    "Points can be redeemed for statement credits, air miles, gift items, or cashback "
                    "through the MYBank GO app.\n\n"
                    "Q: How do I dispute a transaction on my credit card statement?\n"
                    "A: To dispute a transaction, please: (1) Call MYBank Card Centre at 1-300-88-6922; "
                    "(2) Submit a dispute form through MYBank GO app under 'Card Services > Dispute'; "
                    "or (3) Visit any MYBank branch. You must report disputes within 60 days of the "
                    "statement date. For unauthorised transactions, report immediately and your liability "
                    "is limited to RM250 if reported within 24 hours.\n\n"
                    "Q: What insurance coverage comes with my card?\n"
                    "A: The Gold Credit Card includes complimentary travel accident insurance up to "
                    "RM500,000 (when full fare is charged to the card), purchase protection up to RM5,000 "
                    "per item (within 90 days of purchase), and extended warranty of 12 months beyond "
                    "the manufacturer's warranty. The Platinum Card offers enhanced coverage with travel "
                    "insurance up to RM1,000,000 and purchase protection up to RM10,000 per item."
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank Credit Card Frequently Asked Questions (Updated December 2023)",
                "document_type": "faq",
                "entity": "MYBank Group",
                "published_date": datetime(2023, 12, 15),
                "version": "2023.12",
                "status": "current",
                "superseded_by": None,
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": None,
                "related_documents": [
                    "MYBank Gold Credit Card Product Disclosure Sheet v2.1",
                    "MYBank Platinum Credit Card Product Disclosure Sheet v3.0",
                    "MYBank Credit Card Dispute Resolution Procedure (2024)",
                ],
                "amendment_history": [],
            },
            "approvals": [
                {"approver": "Puan Norashikin binti Ahmad", "role": "Head of Consumer Banking Products", "date": datetime(2023, 12, 10)},
            ],
            "regulatory": {
                "bnm_circulars": [],
                "compliance_categories": ["consumer_education"],
                "data_classification": "public",
            },
            "people_mentioned": [],
            "distribution": {
                "target_audience": ["retail_customers", "prospective_customers"],
                "regions": ["Malaysia"],
            },
        },
    })

    # ── Home Loan FAQ (Jan 2024) ────────────────────────────────────────
    faqs.append({
        "title": "MYBank Home Loan Frequently Asked Questions (Updated January 2024)",
        "sections": [
            {
                "heading": "Eligibility and Application",
                "content": (
                    "Q: Am I eligible for a MYBank home loan?\n"
                    "A: You are eligible if you are a Malaysian citizen or permanent resident aged 18 to "
                    "65 years, with a minimum monthly income of RM3,000 (salaried) or RM4,000 "
                    "(self-employed). Your total debt service ratio (DSR) must not exceed 70% of your net "
                    "income, including all existing debt obligations. You must have a satisfactory credit "
                    "record with CCRIS and CTOS.\n\n"
                    "Q: What documents do I need to apply?\n"
                    "A: For salaried applicants: MyKad, latest 3 months' salary slips, latest EA form or "
                    "income tax return (Form BE), Sale and Purchase Agreement (SPA), and property valuation "
                    "report (for sub-sale properties). For self-employed applicants: additional documents "
                    "include latest 2 years' income tax returns (Form B), audited financial statements, and "
                    "6 months' bank statements.\n\n"
                    "Q: What is the maximum loan amount I can get?\n"
                    "A: MYBank offers home loans from RM100,000 to RM5,000,000. The maximum margin of "
                    "finance is 90% of the property value for your first two residential properties, "
                    "subject to Bank Negara Malaysia's loan-to-value (LTV) limits. For your third property "
                    "and above, the maximum margin is 70%."
                ),
            },
            {
                "heading": "Interest Rates and Costs",
                "content": (
                    "Q: What is the current home loan interest rate?\n"
                    "A: Our standard variable rate is Base Rate (BR) + 1.75%, which is currently 5.75% "
                    "per annum based on MYBank's BR of 4.00%. For new applications of RM300,000 and above, "
                    "we offer a promotional rate of BR + 1.50% (5.50% p.a.) for the first 3 years, "
                    "reverting to the standard rate thereafter.\n\n"
                    "Q: What fees are involved in a home loan?\n"
                    "A: The main costs include: Stamp duty on the loan agreement (0.5% of loan amount), "
                    "stamp duty on the Memorandum of Transfer (tiered rates), legal fees for loan agreement "
                    "and property transfer (based on Solicitors' Remuneration Order 2005), and valuation "
                    "fee (typically RM500 to RM2,000). MYBank waives the processing fee for all home loan "
                    "applications.\n\n"
                    "Q: Is there an early settlement penalty?\n"
                    "A: Yes, if you settle or refinance your home loan within the 3-year lock-in period, "
                    "an early settlement penalty of 2% of the outstanding balance applies. After the "
                    "lock-in period, there is no penalty for early settlement or additional repayments.\n\n"
                    "Q: What is Mortgage Reducing Term Assurance (MRTA)?\n"
                    "A: MRTA is an optional insurance policy that pays off your remaining home loan balance "
                    "in the event of death or total permanent disability. While not mandatory, MYBank "
                    "strongly recommends MRTA or equivalent coverage to protect your family. MRTA premiums "
                    "can be financed as part of the home loan (subject to margin of finance limits)."
                ),
            },
            {
                "heading": "Government Schemes and First-Time Buyers",
                "content": (
                    "Q: Are there special schemes for first-time home buyers?\n"
                    "A: Yes, first-time buyers of properties priced RM500,000 and below may benefit from "
                    "stamp duty exemptions under the government's Home Ownership Campaign. MYBank also "
                    "offers the MYBank First Home programme with reduced documentation requirements and a "
                    "special promotional rate for first-time buyers.\n\n"
                    "Q: Does MYBank participate in the Skim Rumah Pertamaku (SRP) scheme?\n"
                    "A: Yes, MYBank is a participating financial institution under Skim Rumah Pertamaku, "
                    "a government initiative by Cagamas Berhad that provides up to 110% financing for "
                    "first-time home buyers purchasing properties priced up to RM500,000. The scheme is "
                    "open to Malaysian citizens earning a gross monthly household income of up to RM10,000.\n\n"
                    "Q: Can I use my PensionFund savings for a down payment?\n"
                    "A: Yes, you can withdraw from your PensionFund Account 2 for "
                    "property purchase. The withdrawal covers the property purchase price (minus any "
                    "financing obtained), stamp duty, legal fees, and other approved costs. Application "
                    "is made directly through PensionFund. MYBank's branch staff can assist you with the "
                    "necessary documentation."
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank Home Loan Frequently Asked Questions (Updated January 2024)",
                "document_type": "faq",
                "entity": "MYBank Group",
                "published_date": datetime(2024, 1, 20),
                "version": "2024.01",
                "status": "current",
                "superseded_by": None,
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": None,
                "related_documents": [
                    "MYBank Home Loan Package Product Disclosure Sheet 2024",
                ],
                "amendment_history": [],
            },
            "approvals": [
                {"approver": "Encik Rizal bin Ibrahim", "role": "Head of Mortgage Lending", "date": datetime(2024, 1, 15)},
            ],
            "regulatory": {
                "bnm_circulars": [],
                "compliance_categories": ["consumer_education"],
                "data_classification": "public",
            },
            "people_mentioned": [],
            "distribution": {
                "target_audience": ["retail_customers", "prospective_home_buyers"],
                "regions": ["Malaysia"],
            },
        },
    })

    # ── Digital Banking FAQ (Feb 2024) ──────────────────────────────────
    faqs.append({
        "title": "MYBank Digital Banking Frequently Asked Questions (Updated February 2024)",
        "sections": [
            {
                "heading": "MYBank GO Mobile App",
                "content": (
                    "Q: What is MYBank GO?\n"
                    "A: MYBank GO is MYBank's mobile banking application, available on iOS (App Store) and "
                    "Android (Google Play). The app allows you to manage your accounts, make payments and "
                    "transfers, apply for products, track rewards, and access customer support — all from "
                    "your smartphone. MYBank GO has over 18 million registered users and was rated the "
                    "number one banking app in Malaysia in 2023.\n\n"
                    "Q: How do I register for MYBank GO?\n"
                    "A: Download MYBank GO from the App Store or Google Play. You will need your MYBank "
                    "debit or credit card number, MyKad number, and registered mobile number. If you are a "
                    "new-to-bank customer, you can open a savings account directly through the app using "
                    "eKYC verification — just have your MyKad ready for the photo verification process.\n\n"
                    "Q: What can I do on MYBank GO?\n"
                    "A: Key features include: balance enquiry and transaction history, fund transfers "
                    "(within MYBank, interbank via IBG/InstantTransfer, international via SWIFT), bill payments "
                    "(250+ billers), QR payments (InstantTransfer QR), FPX payments, fixed deposit placement and "
                    "withdrawal, credit card management and rewards redemption, loan and financing "
                    "applications, investment (unit trusts, gold), insurance purchase, budgeting tools, and "
                    "24/7 live chat support.\n\n"
                    "Q: Is MYBank GO secure?\n"
                    "A: Yes. MYBank GO uses bank-grade security including 256-bit SSL encryption, biometric "
                    "authentication (fingerprint and Face ID), Secure2u push authentication for transaction "
                    "verification, device binding, and real-time fraud monitoring. We comply with BNM's "
                    "Risk Management in Technology policy (BNM/RH/PD 028-18)."
                ),
            },
            {
                "heading": "InstantTransfer and Digital Payments",
                "content": (
                    "Q: What is InstantTransfer?\n"
                    "A: InstantTransfer is Malaysia's national addressing scheme operated by Payments Network "
                    "Malaysia (PayNet). It allows you to send and receive money using your mobile number, "
                    "MyKad number, business registration number, or passport number as a proxy for your "
                    "bank account number. InstantTransfer is available through MYBank GO and MYBank Online Banking.\n\n"
                    "Q: What is InstantTransfer QR?\n"
                    "A: InstantTransfer QR is a unified QR code standard that enables you to make payments at "
                    "merchants by scanning a QR code through MYBank GO. InstantTransfer QR is interoperable "
                    "across all Malaysian banks and e-wallets. You can also receive money by displaying "
                    "your personal InstantTransfer QR code.\n\n"
                    "Q: What is InstantTransfer Transfer and what are the limits?\n"
                    "A: InstantTransfer Transfer allows instant fund transfers to any InstantTransfer-registered proxy. "
                    "Transfer limits through MYBank GO: RM30,000 per transaction, RM50,000 per day. "
                    "Transfers are processed in real-time, 24/7, including weekends and public holidays. "
                    "There is no fee for InstantTransfer transfers to other Malaysian banks.\n\n"
                    "Q: Can I make cross-border payments through MYBank GO?\n"
                    "A: Yes, MYBank GO supports cross-border QR payments to Thailand (via the "
                    "Malaysia-Thailand QR payment linkage) and Singapore (via the Malaysia-Singapore "
                    "real-time payment linkage). International telegraphic transfers (TT) to over 200 "
                    "countries are also available through the app."
                ),
            },
            {
                "heading": "Online Banking and Security",
                "content": (
                    "Q: How is MYBank Online Banking different from MYBank GO?\n"
                    "A: MYBank Online Banking is the web-based banking platform accessible through any "
                    "browser at www.mybank.com.my. It offers similar features to MYBank GO, with additional "
                    "capabilities for business banking users including bulk payments, payroll, and trade "
                    "finance. MYBank GO is optimised for mobile use with features like QR payments and "
                    "biometric login.\n\n"
                    "Q: What should I do if I suspect fraudulent activity on my account?\n"
                    "A: Immediately call our 24-hour fraud hotline at 1-300-88-6911 or use the 'Kill "
                    "Switch' feature in MYBank GO to instantly freeze all your cards and digital access. "
                    "You can also visit any MYBank branch with your MyKad. Report the incident to the "
                    "Royal Malaysia Police (PDRM) and obtain a police report. MYBank will investigate "
                    "within the timelines prescribed by BNM.\n\n"
                    "Q: What is Secure2u?\n"
                    "A: Secure2u is MYBank's push notification authentication system. Instead of SMS "
                    "one-time passwords (OTP), Secure2u sends a push notification to your registered "
                    "device for transaction verification. It is more secure than SMS OTP and is mandatory "
                    "for transactions above RM500. Secure2u is activated during MYBank GO registration."
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank Digital Banking Frequently Asked Questions (Updated February 2024)",
                "document_type": "faq",
                "entity": "MYBank Group",
                "published_date": datetime(2024, 2, 10),
                "version": "2024.02",
                "status": "current",
                "superseded_by": None,
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": None,
                "related_documents": [],
                "amendment_history": [],
            },
            "approvals": [
                {"approver": "Encik Tan Kah Wei", "role": "Head of Digital Banking", "date": datetime(2024, 2, 5)},
            ],
            "regulatory": {
                "bnm_circulars": ["BNM/RH/PD 028-18"],
                "compliance_categories": ["consumer_education", "digital_banking"],
                "data_classification": "public",
            },
            "people_mentioned": [],
            "distribution": {
                "target_audience": ["retail_customers", "digital_banking_users"],
                "regions": ["Malaysia"],
            },
        },
    })

    # ── General Banking FAQ (March 2024) ────────────────────────────────
    faqs.append({
        "title": "MYBank General Banking Frequently Asked Questions (Updated March 2024)",
        "sections": [
            {
                "heading": "Account Opening and Management",
                "content": (
                    "Q: What types of accounts does MYBank offer?\n"
                    "A: MYBank offers the following deposit accounts: (1) MYBank Savings Account — basic "
                    "savings with no minimum balance, competitive interest, and debit card; (2) MYBank "
                    "Savings Plus — premium savings with tiered interest rates for balances above RM10,000; "
                    "(3) MYBank Current Account — for individuals and businesses, with cheque book facility; "
                    "(4) MYBank Fixed Deposit — tenures from 1 month to 60 months, minimum placement RM5,000 "
                    "(RM1,000 for online placements via MYBank GO).\n\n"
                    "Q: How do I open a savings account at MYBank?\n"
                    "A: You can open a savings account in two ways: (1) Visit any MYBank branch with your "
                    "original MyKad and minimum initial deposit of RM250; (2) Open online through MYBank GO "
                    "app using eKYC — just download the app, scan your MyKad, complete the facial "
                    "verification, and make an initial deposit of RM20 or more. Digital account opening "
                    "takes approximately 10 minutes.\n\n"
                    "Q: Are my deposits protected?\n"
                    "A: Yes, all eligible deposits with MYBank Berhad are protected by Perbadanan Insurans "
                    "Deposit Malaysia (PIDM) up to RM250,000 per depositor per member institution. This "
                    "includes savings accounts, current accounts, fixed deposits, and other eligible "
                    "deposit products. Islamic deposits are protected under a separate protection limit. "
                    "For more information, visit www.pidm.gov.my."
                ),
            },
            {
                "heading": "Branch Services and Contact Information",
                "content": (
                    "Q: What are MYBank's branch operating hours?\n"
                    "A: Standard branch hours are Monday to Friday, 9:30 AM to 4:00 PM. Selected branches "
                    "in major shopping malls operate extended hours including weekends: Monday to Sunday, "
                    "10:00 AM to 7:00 PM. Self-service terminals (ATM, CDM, cheque deposit) are available "
                    "24/7 at most branches.\n\n"
                    "Q: How many branches does MYBank have?\n"
                    "A: MYBank operates 450 branches and over 2,800 ATMs across Malaysia, including all "
                    "states in Peninsular Malaysia, Sabah, and Sarawak. We also have a presence in Labuan "
                    "and operate branches in Singapore, Indonesia (through MYBank Niaga), Thailand (through "
                    "MYBank Thai), Cambodia, and Vietnam.\n\n"
                    "Q: How do I contact MYBank?\n"
                    "A: You can reach us through: MYBank Contact Centre 1-300-88-6922 (24 hours, 7 days); "
                    "MYBank GO app live chat (24/7); email general@mybank.com.my; social media @MYBankMY "
                    "on Facebook, Twitter/X, and Instagram; or visit any MYBank branch. For Platinum "
                    "cardholders: Platinum Priority Line 1-300-88-6900.\n\n"
                    "Q: How do I make a complaint?\n"
                    "A: You can lodge a complaint through any of the above channels. MYBank will acknowledge "
                    "receipt within 2 working days and provide a resolution within 14 working days. If you "
                    "are not satisfied with the resolution, you may escalate to Bank Negara Malaysia's "
                    "BNMLINK (1-300-88-5465) or the Ombudsman for Financial Services (OFS) at 03-2272 2811."
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank General Banking Frequently Asked Questions (Updated March 2024)",
                "document_type": "faq",
                "entity": "MYBank Group",
                "published_date": datetime(2024, 3, 1),
                "version": "2024.03",
                "status": "current",
                "superseded_by": None,
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": None,
                "related_documents": [],
                "amendment_history": [],
            },
            "approvals": [
                {"approver": "Puan Nurasyikin binti Mohd Ali", "role": "Head of Customer Experience", "date": datetime(2024, 2, 25)},
            ],
            "regulatory": {
                "bnm_circulars": [],
                "compliance_categories": ["consumer_education"],
                "data_classification": "public",
            },
            "people_mentioned": [],
            "distribution": {
                "target_audience": ["retail_customers", "prospective_customers"],
                "regions": ["Malaysia"],
            },
        },
    })

    return faqs
