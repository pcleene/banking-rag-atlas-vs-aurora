"""
Template-based generator for MYBank product disclosure sheets.
Produces 10 PDS documents with realistic Malaysian banking product details.
"""

from datetime import datetime


def generate_product_disclosures() -> list[dict]:
    """Generate 10 product disclosure sheet documents with full metadata."""
    sheets = []

    # ── Gold Credit Card PDS v2.1 (Jan 2024) - CURRENT ─────────────────
    sheets.append({
        "title": "MYBank Gold Credit Card Product Disclosure Sheet v2.1",
        "sections": [
            {
                "heading": "Product Overview",
                "content": (
                    "The MYBank Gold Credit Card is a rewards-based credit card designed for Malaysian "
                    "professionals and salaried individuals seeking a premium credit card experience with "
                    "competitive rewards, comprehensive insurance coverage, and access to exclusive lifestyle "
                    "privileges. This Product Disclosure Sheet is issued in accordance with Bank Negara "
                    "Malaysia's Guidelines on Product Transparency and Disclosure (BNM/RH/GL 016-4) and "
                    "supersedes all previous versions of the MYBank Gold Credit Card PDS.\n\n"
                    "Card Network: Visa / Mastercard (customer's choice at application)\n"
                    "Card Currency: Malaysian Ringgit (MYR)\n"
                    "Minimum Credit Limit: RM5,000\n"
                    "Maximum Credit Limit: RM100,000\n"
                    "Validity Period: 5 years from date of issuance\n"
                    "Contactless Payment: Enabled (Visa payWave / Mastercard Contactless)\n"
                    "Digital Wallet: Compatible with Apple Pay, Google Pay, Samsung Pay, and Huawei Pay"
                ),
            },
            {
                "heading": "Eligibility Criteria",
                "content": (
                    "To apply for the MYBank Gold Credit Card, applicants must meet the following criteria:\n\n"
                    "Age Requirement: Minimum 21 years old at the time of application. Supplementary "
                    "cardholders must be at least 18 years old.\n\n"
                    "Income Requirement:\n"
                    "- Salaried applicants: Minimum annual income of RM36,000 (equivalent to RM3,000 per month)\n"
                    "- Self-employed applicants: Minimum annual income of RM48,000 (equivalent to RM4,000 per month)\n\n"
                    "Residency: Malaysian citizens and permanent residents. Non-residents with valid employment "
                    "pass may apply with a minimum annual income of RM60,000.\n\n"
                    "Credit History: Applicants must have a satisfactory credit record as assessed by the "
                    "Central Credit Reference Information System (CCRIS) maintained by Bank Negara Malaysia "
                    "and CTOS Data Systems Sdn Bhd. Applicants with any outstanding bankruptcy status or "
                    "legal proceedings related to debt recovery are not eligible.\n\n"
                    "Documentation Required: MyKad (or passport for non-residents), latest 3 months' salary "
                    "slips or EA form, latest 6 months' bank statements (for self-employed applicants), and "
                    "completed application form."
                ),
            },
            {
                "heading": "Fees and Charges",
                "content": (
                    "Annual Fee:\n"
                    "- Principal card: RM200 per annum\n"
                    "- Supplementary card: RM100 per annum\n"
                    "- Annual fee waiver: First year annual fee is waived for new cardholders. Annual fee "
                    "is waived in subsequent years if total annual retail spend exceeds RM30,000.\n\n"
                    "Late Payment Charges:\n"
                    "- RM50 or 1% of total outstanding balance, whichever is higher\n"
                    "- Late payment charges are applied if the minimum payment is not received by the "
                    "payment due date stated on the monthly statement\n\n"
                    "Cash Advance Fee:\n"
                    "- 5% of the cash advance amount, subject to a minimum of RM20 per transaction\n"
                    "- Cash advance limit: Up to 50% of the approved credit limit\n\n"
                    "Foreign Transaction Fee:\n"
                    "- 1.5% of the converted transaction amount in Malaysian Ringgit\n"
                    "- Foreign currency conversion is based on the prevailing exchange rate determined "
                    "by the card network (Visa/Mastercard) on the date of conversion\n\n"
                    "Other Fees:\n"
                    "- Card replacement fee: RM25\n"
                    "- Returned cheque fee: RM20\n"
                    "- Statement copy request: RM5 per statement (free via MYBank GO app)\n"
                    "- Overlimit fee: RM50 per occurrence\n"
                    "- Sales draft retrieval: RM15 per request"
                ),
            },
            {
                "heading": "Interest Rates",
                "content": (
                    "Retail Purchase Interest Rate:\n"
                    "- 15% per annum, calculated on a daily basis on the outstanding balance from the "
                    "transaction date if the total outstanding balance is not paid in full by the payment "
                    "due date. Interest-free period of up to 20 days is granted if the previous month's "
                    "statement balance is paid in full.\n\n"
                    "Cash Advance Interest Rate:\n"
                    "- 18% per annum, calculated on a daily basis from the date of the cash advance "
                    "transaction. No interest-free period is available for cash advance transactions.\n\n"
                    "Balance Transfer Promotional Rate:\n"
                    "- 6.99% per annum for a tenure of 12 months (subject to approval and campaign "
                    "availability). One-time processing fee of 3% of the transfer amount applies. "
                    "Balance transfer is available for balances from other banks' credit cards only.\n\n"
                    "Minimum Monthly Payment:\n"
                    "- 5% of the total outstanding balance or RM50, whichever is higher\n\n"
                    "Important Note: In accordance with Bank Negara Malaysia's responsible lending "
                    "guidelines, MYBank encourages cardholders to pay their outstanding balance in full "
                    "each month to avoid interest charges. Cardholders who consistently pay only the "
                    "minimum amount may take significantly longer to settle their debts."
                ),
            },
            {
                "heading": "Rewards Programme",
                "content": (
                    "MYBank Rewards Points Programme:\n\n"
                    "Earning Structure:\n"
                    "- Dining transactions (local and overseas): 5x MYBank Rewards Points per RM1 spent\n"
                    "- Online transactions (e-commerce, digital subscriptions): 3x MYBank Rewards Points per RM1 spent\n"
                    "- All other retail transactions: 1x MYBank Rewards Point per RM1 spent\n\n"
                    "Point Value: 1 MYBank Rewards Point = approximately RM0.005 in redemption value\n\n"
                    "Redemption Options:\n"
                    "- Statement credit: 2,000 points = RM10 rebate\n"
                    "- Air miles conversion: 2,500 points = 1,000 Airline A frequent-flyer miles or "
                    "1,000 Airline B frequent-flyer miles\n"
                    "- Gift catalogue: Over 500 items available via MYBank GO app\n"
                    "- Cashback: 5,000 points = RM25 cash back to card account\n\n"
                    "Points Validity: Points expire 36 months from the date of earning.\n\n"
                    "Exclusions: The following transactions are not eligible for rewards points: cash "
                    "advances, balance transfers, annual fees, interest charges, late payment charges, "
                    "government-related transactions, insurance premium payments, and transactions at "
                    "educational institutions."
                ),
            },
            {
                "heading": "Insurance and Protection",
                "content": (
                    "Complimentary Insurance Benefits:\n\n"
                    "- Travel accident insurance: Up to RM500,000 coverage when full fare is charged "
                    "to the MYBank Gold Credit Card\n"
                    "- Purchase protection: Up to RM5,000 per item for purchases made with the card, "
                    "covering theft and accidental damage within 90 days of purchase\n"
                    "- Extended warranty: Additional 12 months beyond the manufacturer's warranty for "
                    "purchases made with the card\n\n"
                    "These insurance benefits are underwritten by MYBank General Insurance Berhad and "
                    "are subject to the terms and conditions of the respective insurance policies. Full "
                    "details of coverage, exclusions, and claims procedures are available at "
                    "www.mybank.com.my/gold-card-insurance."
                ),
            },
            {
                "heading": "Important Disclosures",
                "content": (
                    "This Product Disclosure Sheet is not a contract and does not create any binding "
                    "obligations on MYBank Berhad. The terms and conditions governing the MYBank Gold "
                    "Credit Card are set out in the MYBank Credit Card Agreement, which the cardholder "
                    "must read and agree to before accepting the card.\n\n"
                    "MYBank Berhad reserves the right to vary the terms and conditions, including fees, "
                    "charges, and interest rates, by providing 21 calendar days' prior written notice to "
                    "cardholders, in accordance with the Financial Services Act 2013 and Bank Negara "
                    "Malaysia's Guidelines on Product Transparency and Disclosure.\n\n"
                    "For complaints and feedback, cardholders may contact:\n"
                    "- MYBank Contact Centre: 1-300-88-6922 (24 hours)\n"
                    "- Email: cardservices@mybank.com.my\n"
                    "- Visit any MYBank branch nationwide\n\n"
                    "If the complaint is not resolved to the cardholder's satisfaction, it may be "
                    "referred to Bank Negara Malaysia's BNMLINK or the Financial Ombudsman Scheme "
                    "(OFS) operated by the Ombudsman for Financial Services (OFS Malaysia).\n\n"
                    "Effective Date: 15 January 2024\n"
                    "Version: 2.1\n"
                    "Document Reference: PDS/CC/GOLD/2024/v2.1"
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank Gold Credit Card Product Disclosure Sheet v2.1",
                "document_type": "product_disclosure",
                "entity": "MYBank Group",
                "published_date": datetime(2024, 1, 15),
                "version": "2.1",
                "status": "current",
                "superseded_by": None,
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": "MYBank Gold Credit Card Product Disclosure Sheet v1.8",
                "related_documents": [
                    "MYBank Credit Card Agreement",
                    "MYBank Gold Credit Card Insurance Policy",
                ],
                "amendment_history": [
                    {"version": "2.0", "date": datetime(2023, 7, 1), "changes": "Updated rewards structure, revised income criteria"},
                    {"version": "2.1", "date": datetime(2024, 1, 15), "changes": "Updated fee schedule, added balance transfer promo rate"},
                ],
            },
            "approvals": [
                {"approver": "Puan Norashikin binti Ahmad", "role": "Head of Consumer Banking Products", "date": datetime(2024, 1, 10)},
                {"approver": "Encik Razif bin Mohd Salleh", "role": "Chief Compliance Officer", "date": datetime(2024, 1, 12)},
            ],
            "regulatory": {
                "bnm_circulars": ["BNM/RH/GL 016-4"],
                "compliance_categories": ["product_disclosure", "consumer_protection"],
                "data_classification": "public",
            },
            "people_mentioned": [],
            "product": {
                "product_name": "MYBank Gold Credit Card",
                "product_category": "credit_card",
                "effective_date": datetime(2024, 1, 15),
                "fee_schedule": [
                    {"fee_type": "annual_fee_principal", "amount": "RM200", "conditions": "Waived first year; waived if annual spend > RM30,000"},
                    {"fee_type": "annual_fee_supplementary", "amount": "RM100", "conditions": None},
                    {"fee_type": "late_payment", "amount": "RM50 or 1% of outstanding (whichever higher)", "conditions": None},
                    {"fee_type": "cash_advance", "amount": "5% (min RM20)", "conditions": None},
                    {"fee_type": "foreign_transaction", "amount": "1.5%", "conditions": None},
                    {"fee_type": "card_replacement", "amount": "RM25", "conditions": None},
                    {"fee_type": "overlimit", "amount": "RM50", "conditions": None},
                ],
                "eligibility_criteria": [
                    {"criterion": "min_age", "value": "21 years"},
                    {"criterion": "min_income_salaried", "value": "RM36,000 per annum"},
                    {"criterion": "min_income_self_employed", "value": "RM48,000 per annum"},
                    {"criterion": "residency", "value": "Malaysian citizen or permanent resident"},
                ],
                "interest_rates": [
                    {"rate_type": "retail_purchase", "rate": "15% p.a."},
                    {"rate_type": "cash_advance", "rate": "18% p.a."},
                    {"rate_type": "balance_transfer_promo", "rate": "6.99% p.a. for 12 months"},
                ],
                "rewards": [
                    {"category": "dining", "multiplier": "5x points per RM1"},
                    {"category": "online", "multiplier": "3x points per RM1"},
                    {"category": "other", "multiplier": "1x point per RM1"},
                ],
            },
            "distribution": {
                "target_audience": ["retail_customers", "salaried_professionals"],
                "regions": ["Malaysia"],
            },
        },
    })

    # ── Gold Credit Card PDS v1.8 (June 2022) - SUPERSEDED ─────────────
    sheets.append({
        "title": "MYBank Gold Credit Card Product Disclosure Sheet v1.8",
        "sections": [
            {
                "heading": "Product Overview",
                "content": (
                    "The MYBank Gold Credit Card is a rewards credit card designed for Malaysian "
                    "professionals seeking value and convenience. This Product Disclosure Sheet is "
                    "issued pursuant to Bank Negara Malaysia's Guidelines on Product Transparency and "
                    "Disclosure (BNM/RH/GL 016-4).\n\n"
                    "Card Network: Visa / Mastercard\n"
                    "Card Currency: Malaysian Ringgit (MYR)\n"
                    "Minimum Credit Limit: RM3,000\n"
                    "Maximum Credit Limit: RM80,000\n"
                    "Validity Period: 5 years from date of issuance\n"
                    "Contactless Payment: Enabled (Visa payWave / Mastercard Contactless)"
                ),
            },
            {
                "heading": "Eligibility Criteria",
                "content": (
                    "To apply for the MYBank Gold Credit Card, applicants must meet the following criteria:\n\n"
                    "Age Requirement: Minimum 21 years old at the time of application. Supplementary "
                    "cardholders must be at least 18 years old.\n\n"
                    "Income Requirement:\n"
                    "- Salaried applicants: Minimum annual income of RM30,000 (equivalent to RM2,500 per month)\n"
                    "- Self-employed applicants: Minimum annual income of RM42,000 (equivalent to RM3,500 per month)\n\n"
                    "Residency: Malaysian citizens and permanent residents.\n\n"
                    "Credit History: Applicants must have a satisfactory credit record as assessed by CCRIS "
                    "and CTOS. Applicants with any outstanding bankruptcy status are not eligible.\n\n"
                    "Documentation Required: MyKad, latest 3 months' salary slips or latest EA form, "
                    "latest 3 months' bank statements (for self-employed applicants)."
                ),
            },
            {
                "heading": "Fees and Charges",
                "content": (
                    "Annual Fee:\n"
                    "- Principal card: RM180 per annum\n"
                    "- Supplementary card: RM90 per annum\n"
                    "- Annual fee waiver: First year annual fee is waived for new cardholders.\n\n"
                    "Late Payment Charges:\n"
                    "- RM40 or 1% of total outstanding balance, whichever is higher\n\n"
                    "Cash Advance Fee:\n"
                    "- 5% of the cash advance amount, subject to a minimum of RM15 per transaction\n\n"
                    "Foreign Transaction Fee:\n"
                    "- 1.75% of the converted transaction amount in Malaysian Ringgit\n\n"
                    "Other Fees:\n"
                    "- Card replacement fee: RM25\n"
                    "- Returned cheque fee: RM20\n"
                    "- Statement copy request: RM10 per statement\n"
                    "- Overlimit fee: RM50 per occurrence"
                ),
            },
            {
                "heading": "Interest Rates",
                "content": (
                    "Retail Purchase Interest Rate:\n"
                    "- 17.5% per annum, calculated on a daily basis on the outstanding balance from the "
                    "transaction date if the total outstanding balance is not paid in full by the payment "
                    "due date. Interest-free period of up to 20 days is granted if the previous month's "
                    "statement balance is paid in full.\n\n"
                    "Cash Advance Interest Rate:\n"
                    "- 18% per annum, calculated on a daily basis from the date of the cash advance "
                    "transaction. No interest-free period is available for cash advance transactions.\n\n"
                    "Minimum Monthly Payment:\n"
                    "- 5% of the total outstanding balance or RM50, whichever is higher\n\n"
                    "Note: In line with Bank Negara Malaysia's guidelines on responsible lending, MYBank "
                    "encourages cardholders to pay the full outstanding balance each month."
                ),
            },
            {
                "heading": "Rewards Programme",
                "content": (
                    "MYBank Rewards Points Programme:\n\n"
                    "Earning Structure:\n"
                    "- Dining transactions: 3x MYBank Rewards Points per RM1 spent\n"
                    "- All other retail transactions: 1x MYBank Rewards Point per RM1 spent\n\n"
                    "Point Value: 1 MYBank Rewards Point = approximately RM0.005 in redemption value\n\n"
                    "Redemption Options:\n"
                    "- Statement credit: 2,500 points = RM10 rebate\n"
                    "- Air miles conversion: 3,000 points = 1,000 Airline A frequent-flyer miles\n"
                    "- Gift catalogue: Available via MYBank online banking\n\n"
                    "Points Validity: Points expire 24 months from the date of earning.\n\n"
                    "Exclusions: Cash advances, balance transfers, annual fees, interest charges, late "
                    "payment charges, and government-related transactions are not eligible for rewards points."
                ),
            },
            {
                "heading": "Important Disclosures",
                "content": (
                    "This Product Disclosure Sheet is not a contract. The terms and conditions governing "
                    "the MYBank Gold Credit Card are set out in the MYBank Credit Card Agreement.\n\n"
                    "MYBank Berhad reserves the right to vary the terms and conditions by providing 21 "
                    "calendar days' prior written notice, in accordance with the Financial Services Act 2013.\n\n"
                    "For complaints: MYBank Contact Centre 1-300-88-6922 (24 hours) or email "
                    "cardservices@mybank.com.my.\n\n"
                    "Effective Date: 1 June 2022\n"
                    "Version: 1.8\n"
                    "Document Reference: PDS/CC/GOLD/2022/v1.8"
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank Gold Credit Card Product Disclosure Sheet v1.8",
                "document_type": "product_disclosure",
                "entity": "MYBank Group",
                "published_date": datetime(2022, 6, 1),
                "version": "1.8",
                "status": "superseded",
                "superseded_by": "MYBank Gold Credit Card Product Disclosure Sheet v2.1",
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": "MYBank Gold Credit Card Product Disclosure Sheet v1.5",
                "related_documents": ["MYBank Credit Card Agreement"],
                "amendment_history": [
                    {"version": "1.8", "date": datetime(2022, 6, 1), "changes": "Updated fee schedule and rewards earning rate"},
                ],
            },
            "approvals": [
                {"approver": "Puan Norashikin binti Ahmad", "role": "Head of Consumer Banking Products", "date": datetime(2022, 5, 25)},
            ],
            "regulatory": {
                "bnm_circulars": ["BNM/RH/GL 016-4"],
                "compliance_categories": ["product_disclosure", "consumer_protection"],
                "data_classification": "public",
            },
            "people_mentioned": [],
            "product": {
                "product_name": "MYBank Gold Credit Card",
                "product_category": "credit_card",
                "effective_date": datetime(2022, 6, 1),
                "fee_schedule": [
                    {"fee_type": "annual_fee_principal", "amount": "RM180", "conditions": "Waived first year only"},
                    {"fee_type": "annual_fee_supplementary", "amount": "RM90", "conditions": None},
                    {"fee_type": "late_payment", "amount": "RM40 or 1% of outstanding (whichever higher)", "conditions": None},
                    {"fee_type": "cash_advance", "amount": "5% (min RM15)", "conditions": None},
                    {"fee_type": "foreign_transaction", "amount": "1.75%", "conditions": None},
                ],
                "eligibility_criteria": [
                    {"criterion": "min_age", "value": "21 years"},
                    {"criterion": "min_income_salaried", "value": "RM30,000 per annum"},
                    {"criterion": "min_income_self_employed", "value": "RM42,000 per annum"},
                ],
                "interest_rates": [
                    {"rate_type": "retail_purchase", "rate": "17.5% p.a."},
                    {"rate_type": "cash_advance", "rate": "18% p.a."},
                ],
                "rewards": [
                    {"category": "dining", "multiplier": "3x points per RM1"},
                    {"category": "other", "multiplier": "1x point per RM1"},
                ],
            },
            "distribution": {
                "target_audience": ["retail_customers", "salaried_professionals"],
                "regions": ["Malaysia"],
            },
        },
    })

    # ── Platinum Credit Card PDS v3.0 (March 2024) - CURRENT ───────────
    sheets.append({
        "title": "MYBank Platinum Credit Card Product Disclosure Sheet v3.0",
        "sections": [
            {
                "heading": "Product Overview",
                "content": (
                    "The MYBank Platinum Credit Card is a premium credit card offering superior rewards, "
                    "airport lounge access, and enhanced lifestyle benefits for affluent professionals and "
                    "high-net-worth individuals. This Product Disclosure Sheet is issued pursuant to Bank "
                    "Negara Malaysia's Guidelines on Product Transparency and Disclosure (BNM/RH/GL 016-4).\n\n"
                    "Card Network: Visa Signature / Mastercard World\n"
                    "Card Currency: Malaysian Ringgit (MYR)\n"
                    "Minimum Credit Limit: RM20,000\n"
                    "Maximum Credit Limit: RM500,000\n"
                    "Validity Period: 5 years from date of issuance\n"
                    "Contactless Payment: Enabled with Apple Pay, Google Pay, Samsung Pay, and Huawei Pay\n"
                    "Airport Lounge Access: Complimentary access to Plaza Premium Lounges (8 visits per year)"
                ),
            },
            {
                "heading": "Eligibility Criteria",
                "content": (
                    "Age Requirement: Minimum 21 years old. Supplementary cardholders: minimum 18 years old.\n\n"
                    "Income Requirement:\n"
                    "- Salaried applicants: Minimum annual income of RM80,000\n"
                    "- Self-employed applicants: Minimum annual income of RM100,000\n\n"
                    "Existing MYBank Gold cardholders with a consistent payment track record of at least 12 "
                    "months and annual card spend exceeding RM50,000 may be invited to upgrade to Platinum.\n\n"
                    "Credit History: Applicants must have an excellent credit record with no adverse CCRIS "
                    "or CTOS history. A maximum of two credit card facilities from other issuers is preferred."
                ),
            },
            {
                "heading": "Fees and Charges",
                "content": (
                    "Annual Fee:\n"
                    "- Principal card: RM500 per annum (waived for first 2 years; waived thereafter if annual "
                    "spend exceeds RM80,000)\n"
                    "- Supplementary card: RM250 per annum (waived for life)\n\n"
                    "Late Payment Charges: RM75 or 1% of total outstanding balance, whichever is higher\n\n"
                    "Cash Advance Fee: 5% of the cash advance amount, minimum RM25\n\n"
                    "Foreign Transaction Fee: 1.25% of converted amount in MYR\n\n"
                    "Other Fees:\n"
                    "- Card replacement: RM50 (expedited delivery to any address worldwide)\n"
                    "- Overlimit fee: Waived for Platinum cardholders\n"
                    "- Statement copy: Free via MYBank GO app"
                ),
            },
            {
                "heading": "Interest Rates and Balance Transfer",
                "content": (
                    "Retail Purchase Interest Rate: 13.5% per annum (tiered: 13.5% for balances below "
                    "RM50,000; 12.5% for balances above RM50,000). Interest-free period of up to 25 days.\n\n"
                    "Cash Advance Interest Rate: 17% per annum\n\n"
                    "Balance Transfer: 5.99% per annum for 12 months or 4.99% per annum for 6 months. "
                    "Processing fee of 2.5% of transfer amount.\n\n"
                    "Minimum Monthly Payment: 5% of outstanding balance or RM100, whichever is higher"
                ),
            },
            {
                "heading": "Rewards and Privileges",
                "content": (
                    "MYBank Platinum Rewards Programme:\n\n"
                    "- Dining (local and overseas): 8x MYBank Rewards Points per RM1\n"
                    "- Travel (airlines, hotels, travel agencies): 5x MYBank Rewards Points per RM1\n"
                    "- Online shopping: 4x MYBank Rewards Points per RM1\n"
                    "- All other retail: 1.5x MYBank Rewards Points per RM1\n\n"
                    "Airport Lounge: 8 complimentary visits per year to Plaza Premium Lounges at KLIA, "
                    "KLIA2, Penang, Kota Kinabalu, and 30+ international airports.\n\n"
                    "Concierge Service: 24/7 lifestyle concierge for restaurant reservations, event "
                    "tickets, travel bookings, and gift procurement.\n\n"
                    "Golf Privileges: Complimentary green fees at 15 golf courses across Malaysia (4 "
                    "rounds per year, subject to availability).\n\n"
                    "Points Validity: 48 months from date of earning."
                ),
            },
            {
                "heading": "Important Disclosures",
                "content": (
                    "Effective Date: 1 March 2024\nVersion: 3.0\n"
                    "Document Reference: PDS/CC/PLAT/2024/v3.0\n\n"
                    "This PDS is not a contract. Cardholders should refer to the MYBank Credit Card "
                    "Agreement for full terms. MYBank Berhad reserves the right to vary terms with 21 "
                    "days' notice in accordance with the Financial Services Act 2013.\n\n"
                    "MYBank Contact Centre: 1-300-88-6922 | Platinum Priority Line: 1-300-88-6900"
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank Platinum Credit Card Product Disclosure Sheet v3.0",
                "document_type": "product_disclosure",
                "entity": "MYBank Group",
                "published_date": datetime(2024, 3, 1),
                "version": "3.0",
                "status": "current",
                "superseded_by": None,
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": "MYBank Platinum Credit Card Product Disclosure Sheet v2.5",
                "related_documents": ["MYBank Credit Card Agreement", "MYBank Gold Credit Card Product Disclosure Sheet v2.1"],
                "amendment_history": [
                    {"version": "3.0", "date": datetime(2024, 3, 1), "changes": "Enhanced rewards, added airport lounge, reduced interest rates"},
                ],
            },
            "approvals": [
                {"approver": "Puan Norashikin binti Ahmad", "role": "Head of Consumer Banking Products", "date": datetime(2024, 2, 25)},
            ],
            "regulatory": {
                "bnm_circulars": ["BNM/RH/GL 016-4"],
                "compliance_categories": ["product_disclosure", "consumer_protection"],
                "data_classification": "public",
            },
            "people_mentioned": [],
            "product": {
                "product_name": "MYBank Platinum Credit Card",
                "product_category": "credit_card",
                "effective_date": datetime(2024, 3, 1),
                "fee_schedule": [
                    {"fee_type": "annual_fee_principal", "amount": "RM500", "conditions": "Waived first 2 years; waived if annual spend > RM80,000"},
                    {"fee_type": "late_payment", "amount": "RM75 or 1% (whichever higher)", "conditions": None},
                    {"fee_type": "cash_advance", "amount": "5% (min RM25)", "conditions": None},
                    {"fee_type": "foreign_transaction", "amount": "1.25%", "conditions": None},
                ],
                "eligibility_criteria": [
                    {"criterion": "min_age", "value": "21 years"},
                    {"criterion": "min_income_salaried", "value": "RM80,000 per annum"},
                    {"criterion": "min_income_self_employed", "value": "RM100,000 per annum"},
                ],
                "interest_rates": [
                    {"rate_type": "retail_purchase", "rate": "13.5% p.a."},
                    {"rate_type": "cash_advance", "rate": "17% p.a."},
                    {"rate_type": "balance_transfer_promo", "rate": "5.99% p.a. for 12 months"},
                ],
                "rewards": [
                    {"category": "dining", "multiplier": "8x points per RM1"},
                    {"category": "travel", "multiplier": "5x points per RM1"},
                    {"category": "online", "multiplier": "4x points per RM1"},
                    {"category": "other", "multiplier": "1.5x points per RM1"},
                ],
            },
            "distribution": {
                "target_audience": ["affluent_customers", "high_net_worth"],
                "regions": ["Malaysia"],
            },
        },
    })

    # ── Platinum Credit Card PDS v2.5 (Nov 2022) - SUPERSEDED ──────────
    sheets.append({
        "title": "MYBank Platinum Credit Card Product Disclosure Sheet v2.5",
        "sections": [
            {
                "heading": "Product Overview",
                "content": (
                    "The MYBank Platinum Credit Card is a premium credit card for affluent professionals. "
                    "This PDS is issued pursuant to BNM/RH/GL 016-4.\n\n"
                    "Card Network: Visa Signature / Mastercard World\n"
                    "Card Currency: MYR\nMinimum Credit Limit: RM15,000\n"
                    "Maximum Credit Limit: RM300,000\nValidity Period: 5 years"
                ),
            },
            {
                "heading": "Fees and Charges",
                "content": (
                    "Annual Fee: Principal card RM450 per annum (waived first year). "
                    "Supplementary card RM200 per annum.\n\n"
                    "Late Payment: RM60 or 1% of outstanding (whichever higher)\n"
                    "Cash Advance Fee: 5% (min RM20)\n"
                    "Foreign Transaction Fee: 1.5%\n"
                    "Card Replacement: RM40\nOverlimit Fee: RM50"
                ),
            },
            {
                "heading": "Interest Rates",
                "content": (
                    "Retail Purchase: 15% per annum. Cash Advance: 18% per annum.\n"
                    "Balance Transfer: 6.99% p.a. for 12 months (3% processing fee).\n"
                    "Minimum Monthly Payment: 5% or RM100, whichever higher."
                ),
            },
            {
                "heading": "Rewards",
                "content": (
                    "Dining: 5x points per RM1. Travel: 3x points per RM1. "
                    "All other: 1x point per RM1.\n"
                    "Airport lounge: 4 visits per year (Plaza Premium Lounges, KLIA/KLIA2 only).\n"
                    "Points validity: 36 months.\n\n"
                    "Effective Date: 15 November 2022\nVersion: 2.5\n"
                    "Document Reference: PDS/CC/PLAT/2022/v2.5"
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank Platinum Credit Card Product Disclosure Sheet v2.5",
                "document_type": "product_disclosure",
                "entity": "MYBank Group",
                "published_date": datetime(2022, 11, 15),
                "version": "2.5",
                "status": "superseded",
                "superseded_by": "MYBank Platinum Credit Card Product Disclosure Sheet v3.0",
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": None,
                "related_documents": ["MYBank Credit Card Agreement"],
                "amendment_history": [],
            },
            "approvals": [
                {"approver": "Puan Norashikin binti Ahmad", "role": "Head of Consumer Banking Products", "date": datetime(2022, 11, 10)},
            ],
            "regulatory": {
                "bnm_circulars": ["BNM/RH/GL 016-4"],
                "compliance_categories": ["product_disclosure"],
                "data_classification": "public",
            },
            "people_mentioned": [],
            "product": {
                "product_name": "MYBank Platinum Credit Card",
                "product_category": "credit_card",
                "effective_date": datetime(2022, 11, 15),
                "fee_schedule": [
                    {"fee_type": "annual_fee_principal", "amount": "RM450", "conditions": "Waived first year only"},
                    {"fee_type": "late_payment", "amount": "RM60 or 1% (whichever higher)", "conditions": None},
                    {"fee_type": "foreign_transaction", "amount": "1.5%", "conditions": None},
                ],
                "eligibility_criteria": [
                    {"criterion": "min_income_salaried", "value": "RM72,000 per annum"},
                ],
                "interest_rates": [
                    {"rate_type": "retail_purchase", "rate": "15% p.a."},
                    {"rate_type": "cash_advance", "rate": "18% p.a."},
                ],
                "rewards": [
                    {"category": "dining", "multiplier": "5x points per RM1"},
                    {"category": "travel", "multiplier": "3x points per RM1"},
                    {"category": "other", "multiplier": "1x point per RM1"},
                ],
            },
            "distribution": {
                "target_audience": ["affluent_customers"],
                "regions": ["Malaysia"],
            },
        },
    })

    # ── SME Overdraft Facility PDS (2024) - CURRENT ─────────────────────
    sheets.append({
        "title": "MYBank SME Overdraft Facility Product Disclosure Sheet 2024",
        "sections": [
            {
                "heading": "Product Overview",
                "content": (
                    "The MYBank SME Overdraft Facility is a revolving credit facility designed to provide "
                    "working capital flexibility for small and medium enterprises (SMEs) registered in "
                    "Malaysia. This facility allows eligible SME borrowers to withdraw funds up to their "
                    "approved overdraft limit as and when needed, providing a cost-effective solution for "
                    "managing cash flow fluctuations.\n\n"
                    "This Product Disclosure Sheet is prepared in compliance with Bank Negara Malaysia's "
                    "Guidelines on Product Transparency and Disclosure (BNM/RH/GL 016-4) and the Financial "
                    "Services Act 2013. The facility is offered under MYBank's SME Banking division and "
                    "is aligned with BNM's SME Financing initiatives."
                ),
            },
            {
                "heading": "Facility Details and Eligibility",
                "content": (
                    "Facility Type: Revolving Overdraft (Clean or Secured)\n"
                    "Facility Amount: RM50,000 to RM2,000,000\n"
                    "Tenure: 12 months, subject to annual review and renewal\n"
                    "Security: Clean (for facilities up to RM250,000 under CGC Portfolio Guarantee) or "
                    "secured by property, fixed deposits, or other acceptable collateral\n\n"
                    "Eligibility:\n"
                    "- SMEs registered in Malaysia under the Companies Act 2016 or Registration of "
                    "Business Act 1956\n"
                    "- Annual turnover not exceeding RM50 million (in line with SME Corp Malaysia definition)\n"
                    "- Minimum 2 years in business operations\n"
                    "- Satisfactory credit record with no adverse CCRIS or CTOS entries\n"
                    "- Must maintain a current/savings account with MYBank Berhad\n\n"
                    "Interest Rate: Base Rate (BR) + 2.50% per annum (currently 6.50% p.a. as of January "
                    "2024, based on MYBank's prevailing BR of 4.00%). Interest is calculated on a daily "
                    "rest basis on the amount utilised.\n\n"
                    "Facility Fee: 0.50% per annum on the approved facility limit, payable upfront upon "
                    "drawdown. Renewal fee of 0.25% per annum on subsequent renewals."
                ),
            },
            {
                "heading": "Fees, Charges and Repayment",
                "content": (
                    "Processing Fee: RM500 (non-refundable)\n"
                    "Facility Fee: 0.50% of approved limit (first year); 0.25% on renewal\n"
                    "Legal and Documentation Fee: At cost (estimated RM1,500 - RM3,000 for secured facilities)\n"
                    "Stamp Duty: As prescribed under the Stamp Act 1949\n"
                    "Early Termination: No penalty for early termination\n\n"
                    "Repayment: Interest is debited monthly to the overdraft account. The principal is "
                    "repayable on demand or upon expiry of the facility tenure, whichever is earlier. "
                    "MYBank reserves the right to recall the facility at any time with written notice.\n\n"
                    "Excess Utilisation: Utilisation beyond the approved limit is subject to MYBank's "
                    "discretion. An excess interest rate of BR + 5.00% (currently 9.00% p.a.) applies "
                    "to any amount exceeding the approved limit.\n\n"
                    "Effective Date: 2 January 2024\nVersion: 2024.1\n"
                    "Document Reference: PDS/SME/OD/2024/v1"
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank SME Overdraft Facility Product Disclosure Sheet 2024",
                "document_type": "product_disclosure",
                "entity": "MYBank Group",
                "published_date": datetime(2024, 1, 2),
                "version": "2024.1",
                "status": "current",
                "superseded_by": None,
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": "MYBank SME Overdraft Facility Product Disclosure Sheet 2021",
                "related_documents": ["MYBank SME Banking General Terms and Conditions"],
                "amendment_history": [],
            },
            "approvals": [
                {"approver": "Encik Shahril bin Mohd Zain", "role": "Head of SME Banking", "date": datetime(2023, 12, 20)},
            ],
            "regulatory": {
                "bnm_circulars": ["BNM/RH/GL 016-4"],
                "compliance_categories": ["product_disclosure", "sme_financing"],
                "data_classification": "public",
            },
            "people_mentioned": [],
            "product": {
                "product_name": "MYBank SME Overdraft Facility",
                "product_category": "sme_lending",
                "effective_date": datetime(2024, 1, 2),
                "fee_schedule": [
                    {"fee_type": "processing_fee", "amount": "RM500", "conditions": None},
                    {"fee_type": "facility_fee", "amount": "0.50% first year; 0.25% renewal", "conditions": None},
                ],
                "eligibility_criteria": [
                    {"criterion": "business_tenure", "value": "Minimum 2 years"},
                    {"criterion": "annual_turnover", "value": "Up to RM50 million"},
                ],
                "interest_rates": [
                    {"rate_type": "standard", "rate": "BR + 2.50% p.a. (currently 6.50%)"},
                    {"rate_type": "excess_utilisation", "rate": "BR + 5.00% p.a. (currently 9.00%)"},
                ],
                "rewards": [],
            },
            "distribution": {
                "target_audience": ["sme_customers"],
                "regions": ["Malaysia"],
            },
        },
    })

    # ── SME Overdraft Facility PDS (2021) - SUPERSEDED ──────────────────
    sheets.append({
        "title": "MYBank SME Overdraft Facility Product Disclosure Sheet 2021",
        "sections": [
            {
                "heading": "Product Overview",
                "content": (
                    "The MYBank SME Overdraft Facility provides working capital flexibility for eligible "
                    "SMEs. This PDS is prepared in compliance with BNM/RH/GL 016-4.\n\n"
                    "Facility Type: Revolving Overdraft (Clean or Secured)\n"
                    "Facility Amount: RM30,000 to RM1,000,000\n"
                    "Tenure: 12 months, subject to annual review\n"
                    "Security: Clean (up to RM150,000) or secured by property/fixed deposits"
                ),
            },
            {
                "heading": "Rates and Fees",
                "content": (
                    "Interest Rate: Base Rate (BR) + 3.00% per annum (7.00% p.a. as of March 2021, "
                    "based on BR of 4.00%). Calculated on daily rest basis.\n\n"
                    "Processing Fee: RM500\n"
                    "Facility Fee: 0.75% of approved limit (first year); 0.50% on renewal\n"
                    "Excess Utilisation Rate: BR + 6.00% (currently 10.00% p.a.)\n\n"
                    "Eligibility: SMEs registered in Malaysia, minimum 3 years in business, annual "
                    "turnover up to RM25 million, satisfactory CCRIS/CTOS record.\n\n"
                    "Effective Date: 15 March 2021\nVersion: 2021.1\n"
                    "Document Reference: PDS/SME/OD/2021/v1"
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank SME Overdraft Facility Product Disclosure Sheet 2021",
                "document_type": "product_disclosure",
                "entity": "MYBank Group",
                "published_date": datetime(2021, 3, 15),
                "version": "2021.1",
                "status": "superseded",
                "superseded_by": "MYBank SME Overdraft Facility Product Disclosure Sheet 2024",
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
                {"approver": "Encik Shahril bin Mohd Zain", "role": "Head of SME Banking", "date": datetime(2021, 3, 10)},
            ],
            "regulatory": {
                "bnm_circulars": ["BNM/RH/GL 016-4"],
                "compliance_categories": ["product_disclosure", "sme_financing"],
                "data_classification": "public",
            },
            "people_mentioned": [],
            "product": {
                "product_name": "MYBank SME Overdraft Facility",
                "product_category": "sme_lending",
                "effective_date": datetime(2021, 3, 15),
                "fee_schedule": [
                    {"fee_type": "processing_fee", "amount": "RM500", "conditions": None},
                    {"fee_type": "facility_fee", "amount": "0.75% first year; 0.50% renewal", "conditions": None},
                ],
                "eligibility_criteria": [
                    {"criterion": "business_tenure", "value": "Minimum 3 years"},
                    {"criterion": "annual_turnover", "value": "Up to RM25 million"},
                ],
                "interest_rates": [
                    {"rate_type": "standard", "rate": "BR + 3.00% p.a. (7.00%)"},
                    {"rate_type": "excess_utilisation", "rate": "BR + 6.00% p.a. (10.00%)"},
                ],
                "rewards": [],
            },
            "distribution": {
                "target_audience": ["sme_customers"],
                "regions": ["Malaysia"],
            },
        },
    })

    # ── Home Loan Package PDS (2024) - CURRENT ──────────────────────────
    sheets.append({
        "title": "MYBank Home Loan Package Product Disclosure Sheet 2024",
        "sections": [
            {
                "heading": "Product Overview",
                "content": (
                    "The MYBank Home Loan Package is a conventional housing loan facility designed for "
                    "individuals purchasing residential property in Malaysia. The package offers competitive "
                    "interest rates, flexible tenure options, and optional mortgage protection coverage. "
                    "This PDS is prepared in compliance with Bank Negara Malaysia's Guidelines on Product "
                    "Transparency and Disclosure (BNM/RH/GL 016-4) and the Financial Services Act 2013.\n\n"
                    "Facility Type: Term Loan (Conventional)\n"
                    "Loan Amount: RM100,000 to RM5,000,000\n"
                    "Maximum Margin of Finance: Up to 90% of property value (subject to BNM LTV limits)\n"
                    "Tenure: 5 to 35 years (maximum age at maturity: 70 years)\n"
                    "Security: First legal charge over the financed property"
                ),
            },
            {
                "heading": "Interest Rates and Repayment",
                "content": (
                    "Standard Variable Rate: Base Rate (BR) + 1.75% per annum (currently 5.75% p.a. based "
                    "on MYBank's BR of 4.00%). The effective lending rate is subject to changes in the Base "
                    "Rate as determined by MYBank.\n\n"
                    "Promotional Rate (for new applications): BR + 1.50% (5.50% p.a.) for the first 3 years, "
                    "reverting to BR + 1.75% thereafter. Applicable for loan amounts of RM300,000 and above.\n\n"
                    "Lock-in Period: 3 years from the date of first disbursement. Early settlement or "
                    "refinancing within the lock-in period incurs a penalty of 2% on the outstanding balance.\n\n"
                    "Repayment: Monthly instalment basis. For a RM500,000 loan over 30 years at 5.75% p.a., "
                    "the estimated monthly instalment is approximately RM2,918.\n\n"
                    "Stamp Duty: 0.5% on the loan facility agreement as prescribed under the Stamp Act 1949. "
                    "Legal fees are borne by the borrower and are calculated based on the Solicitors' "
                    "Remuneration Order 2005."
                ),
            },
            {
                "heading": "Eligibility and Documentation",
                "content": (
                    "Eligibility:\n"
                    "- Malaysian citizens and permanent residents aged 18 to 65 years\n"
                    "- Minimum monthly income of RM3,000 (salaried) or RM4,000 (self-employed)\n"
                    "- Satisfactory credit record with CCRIS and CTOS\n"
                    "- Debt Service Ratio (DSR) not exceeding 70% of net income\n\n"
                    "Property Eligibility: Completed residential properties, properties under construction "
                    "(progressive loan), sub-sale properties. Commercial properties and vacant land are not "
                    "eligible under this package.\n\n"
                    "Required Documents: MyKad, latest 3 months' salary slips, latest EA form or tax "
                    "return (Form BE/B), Sale and Purchase Agreement, property valuation report (for "
                    "sub-sale), bank statements for last 6 months (self-employed).\n\n"
                    "Effective Date: 15 January 2024\nVersion: 2024.1\n"
                    "Document Reference: PDS/HL/2024/v1"
                ),
            },
            {
                "heading": "Fees and Charges",
                "content": (
                    "Processing Fee: Waived\n"
                    "Legal Fee: At cost (based on Solicitors' Remuneration Order 2005)\n"
                    "Valuation Fee: At cost (typically RM500 - RM2,000 depending on property value)\n"
                    "Stamp Duty on Loan Agreement: 0.5% of loan amount\n"
                    "Stamp Duty on Transfer (MOT): Tiered rates per Stamp Act 1949\n"
                    "Early Settlement Penalty: 2% of outstanding balance during lock-in period; nil thereafter\n"
                    "Late Payment Charge: 1% per annum on overdue instalment amount\n"
                    "Switching Fee (variable to fixed): 0.5% of outstanding balance\n\n"
                    "Mortgage Reducing Term Assurance (MRTA): Optional. Premium based on loan amount, tenure, "
                    "and borrower's age. MYBank recommends MRTA or equivalent mortgage protection coverage "
                    "for all housing loan borrowers."
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank Home Loan Package Product Disclosure Sheet 2024",
                "document_type": "product_disclosure",
                "entity": "MYBank Group",
                "published_date": datetime(2024, 1, 15),
                "version": "2024.1",
                "status": "current",
                "superseded_by": None,
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": "MYBank Home Loan Package Product Disclosure Sheet 2022",
                "related_documents": ["MYBank Home Loan General Terms and Conditions"],
                "amendment_history": [],
            },
            "approvals": [
                {"approver": "Encik Rizal bin Ibrahim", "role": "Head of Mortgage Lending", "date": datetime(2024, 1, 10)},
            ],
            "regulatory": {
                "bnm_circulars": ["BNM/RH/GL 016-4"],
                "compliance_categories": ["product_disclosure", "consumer_protection", "mortgage_lending"],
                "data_classification": "public",
            },
            "people_mentioned": [],
            "product": {
                "product_name": "MYBank Home Loan Package",
                "product_category": "mortgage",
                "effective_date": datetime(2024, 1, 15),
                "fee_schedule": [
                    {"fee_type": "processing_fee", "amount": "Waived", "conditions": None},
                    {"fee_type": "early_settlement_penalty", "amount": "2% during lock-in; nil after", "conditions": None},
                    {"fee_type": "late_payment", "amount": "1% p.a. on overdue amount", "conditions": None},
                ],
                "eligibility_criteria": [
                    {"criterion": "min_age", "value": "18 years"},
                    {"criterion": "max_age_at_maturity", "value": "70 years"},
                    {"criterion": "min_income_salaried", "value": "RM3,000 per month"},
                    {"criterion": "max_dsr", "value": "70%"},
                ],
                "interest_rates": [
                    {"rate_type": "standard_variable", "rate": "BR + 1.75% (5.75% p.a.)"},
                    {"rate_type": "promotional", "rate": "BR + 1.50% (5.50% p.a.) for first 3 years"},
                ],
                "rewards": [],
            },
            "distribution": {
                "target_audience": ["retail_customers", "home_buyers"],
                "regions": ["Malaysia"],
            },
        },
    })

    # ── Home Loan Package PDS (2022) - SUPERSEDED ───────────────────────
    sheets.append({
        "title": "MYBank Home Loan Package Product Disclosure Sheet 2022",
        "sections": [
            {
                "heading": "Product Overview",
                "content": (
                    "The MYBank Home Loan Package is a conventional housing loan facility for individuals "
                    "purchasing residential property in Malaysia. This PDS is issued pursuant to "
                    "BNM/RH/GL 016-4.\n\n"
                    "Facility Type: Term Loan (Conventional)\n"
                    "Loan Amount: RM100,000 to RM3,000,000\n"
                    "Maximum Margin of Finance: Up to 90%\n"
                    "Tenure: 5 to 35 years (max age at maturity: 65 years)\n"
                    "Security: First legal charge over financed property"
                ),
            },
            {
                "heading": "Rates, Fees and Eligibility",
                "content": (
                    "Interest Rate: Base Rate (BR) + 2.00% per annum (5.75% p.a. based on BR of 3.75%). "
                    "Promotional rate: BR + 1.75% (5.50% p.a.) for first 2 years.\n\n"
                    "Lock-in Period: 5 years. Early settlement penalty: 3% of outstanding balance during "
                    "lock-in period.\n\n"
                    "Late Payment: 1% p.a. on overdue instalment\nProcessing Fee: RM200\n\n"
                    "Eligibility: Malaysian citizens 21-60 years, minimum income RM3,500/month (salaried), "
                    "DSR not exceeding 65%.\n\n"
                    "Effective Date: 1 April 2022\nVersion: 2022.1\n"
                    "Document Reference: PDS/HL/2022/v1"
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank Home Loan Package Product Disclosure Sheet 2022",
                "document_type": "product_disclosure",
                "entity": "MYBank Group",
                "published_date": datetime(2022, 4, 1),
                "version": "2022.1",
                "status": "superseded",
                "superseded_by": "MYBank Home Loan Package Product Disclosure Sheet 2024",
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
                {"approver": "Encik Rizal bin Ibrahim", "role": "Head of Mortgage Lending", "date": datetime(2022, 3, 25)},
            ],
            "regulatory": {
                "bnm_circulars": ["BNM/RH/GL 016-4"],
                "compliance_categories": ["product_disclosure", "mortgage_lending"],
                "data_classification": "public",
            },
            "people_mentioned": [],
            "product": {
                "product_name": "MYBank Home Loan Package",
                "product_category": "mortgage",
                "effective_date": datetime(2022, 4, 1),
                "fee_schedule": [
                    {"fee_type": "processing_fee", "amount": "RM200", "conditions": None},
                    {"fee_type": "early_settlement_penalty", "amount": "3% during 5-year lock-in", "conditions": None},
                ],
                "eligibility_criteria": [
                    {"criterion": "min_age", "value": "21 years"},
                    {"criterion": "min_income_salaried", "value": "RM3,500 per month"},
                    {"criterion": "max_dsr", "value": "65%"},
                ],
                "interest_rates": [
                    {"rate_type": "standard_variable", "rate": "BR + 2.00% (5.75% p.a.)"},
                    {"rate_type": "promotional", "rate": "BR + 1.75% (5.50% p.a.) for first 2 years"},
                ],
                "rewards": [],
            },
            "distribution": {
                "target_audience": ["retail_customers", "home_buyers"],
                "regions": ["Malaysia"],
            },
        },
    })

    # ── Fixed Deposit Rates Sheet (Q1 2024) - CURRENT ───────────────────
    sheets.append({
        "title": "MYBank Fixed Deposit Rates Sheet Q1 2024",
        "sections": [
            {
                "heading": "Fixed Deposit Interest Rates",
                "content": (
                    "The following fixed deposit interest rates are effective from 2 January 2024 and apply "
                    "to new and renewed placements with MYBank Berhad. Rates are subject to change and "
                    "are displayed in accordance with Bank Negara Malaysia's Guidelines on Product "
                    "Transparency and Disclosure (BNM/RH/GL 016-4).\n\n"
                    "Conventional Fixed Deposit Rates (per annum):\n\n"
                    "1 month: 2.80%\n"
                    "3 months: 3.00%\n"
                    "6 months: 3.15%\n"
                    "9 months: 3.20%\n"
                    "12 months: 3.30%\n"
                    "18 months: 3.35%\n"
                    "24 months: 3.40%\n"
                    "36 months: 3.45%\n"
                    "48 months: 3.50%\n"
                    "60 months: 3.55%\n\n"
                    "Minimum Placement: RM5,000\n"
                    "Minimum Placement for Online FD (via MYBank GO app): RM1,000\n\n"
                    "Premium Fixed Deposit Rates (placements of RM100,000 and above):\n"
                    "3 months: 3.15% | 6 months: 3.30% | 12 months: 3.50% | 24 months: 3.60%\n\n"
                    "Senior Citizen Premium: Additional 0.10% per annum for customers aged 60 and above.\n\n"
                    "Early Withdrawal: Penalty of 50% of the accrued interest. For placements held less "
                    "than 3 months, no interest is payable."
                ),
            },
            {
                "heading": "Terms and Conditions",
                "content": (
                    "Fixed deposit accounts are covered under Perbadanan Insurans Deposit Malaysia (PIDM) "
                    "up to RM250,000 per depositor per member institution. Customers are advised to refer "
                    "to PIDM's website at www.pidm.gov.my for further details.\n\n"
                    "Interest Computation: Based on actual number of days divided by 365 days per year.\n"
                    "Interest Payment: At maturity for tenures of 12 months and below; semi-annually for "
                    "tenures exceeding 12 months.\n"
                    "Auto-Renewal: Fixed deposits are automatically renewed at the prevailing rate on "
                    "the maturity date unless the customer instructs otherwise.\n"
                    "Joint Account: Available for up to 4 account holders with 'either or survivor' mandate.\n\n"
                    "Effective Date: 2 January 2024\n"
                    "Document Reference: RATES/FD/Q1-2024"
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank Fixed Deposit Rates Sheet Q1 2024",
                "document_type": "product_disclosure",
                "entity": "MYBank Group",
                "published_date": datetime(2024, 1, 2),
                "version": "Q1-2024",
                "status": "current",
                "superseded_by": None,
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": "MYBank Fixed Deposit Rates Sheet Q3 2022",
                "related_documents": [],
                "amendment_history": [],
            },
            "approvals": [
                {"approver": "Puan Siti Mariam binti Abdullah", "role": "Head of Deposits", "date": datetime(2023, 12, 28)},
            ],
            "regulatory": {
                "bnm_circulars": ["BNM/RH/GL 016-4"],
                "compliance_categories": ["product_disclosure", "deposit_taking"],
                "data_classification": "public",
            },
            "people_mentioned": [],
            "product": {
                "product_name": "MYBank Conventional Fixed Deposit",
                "product_category": "fixed_deposit",
                "effective_date": datetime(2024, 1, 2),
                "fee_schedule": [
                    {"fee_type": "early_withdrawal_penalty", "amount": "50% of accrued interest", "conditions": None},
                ],
                "eligibility_criteria": [
                    {"criterion": "min_placement", "value": "RM5,000 (RM1,000 online)"},
                ],
                "interest_rates": [
                    {"rate_type": "1_month", "rate": "2.80% p.a."},
                    {"rate_type": "3_months", "rate": "3.00% p.a."},
                    {"rate_type": "6_months", "rate": "3.15% p.a."},
                    {"rate_type": "12_months", "rate": "3.30% p.a."},
                    {"rate_type": "24_months", "rate": "3.40% p.a."},
                ],
                "rewards": [],
            },
            "distribution": {
                "target_audience": ["retail_customers", "corporate_customers"],
                "regions": ["Malaysia"],
            },
        },
    })

    # ── Fixed Deposit Rates Sheet (Q3 2022) - SUPERSEDED ────────────────
    sheets.append({
        "title": "MYBank Fixed Deposit Rates Sheet Q3 2022",
        "sections": [
            {
                "heading": "Fixed Deposit Interest Rates",
                "content": (
                    "Effective from 1 July 2022. Rates are subject to change.\n\n"
                    "Conventional Fixed Deposit Rates (per annum):\n\n"
                    "1 month: 2.00%\n3 months: 2.25%\n6 months: 2.50%\n"
                    "12 months: 2.75%\n24 months: 2.85%\n36 months: 2.90%\n\n"
                    "Minimum Placement: RM5,000\n\n"
                    "Premium Rates (RM100,000+): 3 months: 2.40% | 6 months: 2.65% | 12 months: 2.95%\n\n"
                    "Senior Citizen Premium: Additional 0.10% p.a. for customers aged 60 and above.\n"
                    "Early Withdrawal Penalty: 50% of accrued interest.\n\n"
                    "PIDM coverage: Up to RM250,000 per depositor per member institution.\n\n"
                    "Effective Date: 1 July 2022\nDocument Reference: RATES/FD/Q3-2022"
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank Fixed Deposit Rates Sheet Q3 2022",
                "document_type": "product_disclosure",
                "entity": "MYBank Group",
                "published_date": datetime(2022, 7, 1),
                "version": "Q3-2022",
                "status": "superseded",
                "superseded_by": "MYBank Fixed Deposit Rates Sheet Q1 2024",
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
                {"approver": "Puan Siti Mariam binti Abdullah", "role": "Head of Deposits", "date": datetime(2022, 6, 28)},
            ],
            "regulatory": {
                "bnm_circulars": ["BNM/RH/GL 016-4"],
                "compliance_categories": ["product_disclosure", "deposit_taking"],
                "data_classification": "public",
            },
            "people_mentioned": [],
            "product": {
                "product_name": "MYBank Conventional Fixed Deposit",
                "product_category": "fixed_deposit",
                "effective_date": datetime(2022, 7, 1),
                "fee_schedule": [
                    {"fee_type": "early_withdrawal_penalty", "amount": "50% of accrued interest", "conditions": None},
                ],
                "eligibility_criteria": [
                    {"criterion": "min_placement", "value": "RM5,000"},
                ],
                "interest_rates": [
                    {"rate_type": "1_month", "rate": "2.00% p.a."},
                    {"rate_type": "3_months", "rate": "2.25% p.a."},
                    {"rate_type": "6_months", "rate": "2.50% p.a."},
                    {"rate_type": "12_months", "rate": "2.75% p.a."},
                ],
                "rewards": [],
            },
            "distribution": {
                "target_audience": ["retail_customers"],
                "regions": ["Malaysia"],
            },
        },
    })

    return sheets
