"""
Template-based generator for MYBank Group annual report documents.
Produces 8 annual reports with realistic Malaysian banking content.
"""

from datetime import datetime


def generate_annual_reports() -> list[dict]:
    """Generate 8 annual report documents with full metadata."""
    reports = []

    # ── MYBank Group Annual Report 2019 ─────────────────────────────────
    reports.append({
        "title": "MYBank Group Annual Report 2019",
        "sections": [
            {
                "heading": "Board of Directors",
                "content": (
                    "The Board of Directors of MYBank Group Berhad comprises twelve members, "
                    "including four independent non-executive directors, in compliance with Bank Negara Malaysia's "
                    "Corporate Governance Policy Document (BNM/RH/PD 029-9). The Chairman, Dato' Sri Haji Mohamad "
                    "Razlan bin Abdullah, brings over thirty years of experience in the Malaysian financial services "
                    "sector, having previously served as Deputy Governor of Bank Negara Malaysia.\n\n"
                    "Group Chief Executive Officer Tan Wei Ming was appointed on 1 January 2016 and continues to "
                    "lead the Group's transformation agenda. The Board also welcomed Puan Sri Datin Rosmawati binti "
                    "Ismail as an independent non-executive director, strengthening the Board's expertise in risk "
                    "governance. Dr. Rajendra Nair a/l Subramaniam serves as Chairman of the Board Risk Management "
                    "Committee, overseeing the Group's enterprise risk management framework.\n\n"
                    "In line with BNM's Policy Document on Corporate Governance (BNM/RH/GL 001-31), the Board "
                    "conducted its annual effectiveness assessment facilitated by an external consultant. The "
                    "assessment confirmed that the Board's composition, competencies, and dynamics are well-aligned "
                    "with the Group's strategic direction and risk appetite."
                ),
            },
            {
                "heading": "Financial Highlights",
                "content": (
                    "MYBank Group recorded a net profit of RM4.12 billion for the financial year ended "
                    "31 December 2019, representing a 6.3% increase from RM3.88 billion in 2018. Total assets "
                    "grew 8.1% to RM498.7 billion, supported by strong loan growth across all segments. The "
                    "Group's return on equity stood at 11.4%, while its cost-to-income ratio improved to 45.2% "
                    "from 46.8% in the prior year.\n\n"
                    "Gross loans and financing expanded 7.9% to RM352.1 billion, with community banking "
                    "contributing RM128.4 billion and corporate banking RM145.3 billion. Customer deposits grew "
                    "6.5% to RM389.2 billion, with the current account and savings account (CASA) ratio "
                    "improving to 36.8%. The Group maintained a healthy Common Equity Tier 1 (CET1) capital "
                    "ratio of 13.2%, well above the minimum requirement of 7.0% under the Basel III framework "
                    "as prescribed by Bank Negara Malaysia.\n\n"
                    "Net interest margin remained stable at 2.18%, while non-interest income grew 12.4% "
                    "to RM3.56 billion, driven by strong wealth management and treasury trading activities. "
                    "The Group's gross impaired loan ratio stood at 1.82%, with loan loss coverage at 98.7%. "
                    "Dividends declared for the year totalled RM2.31 billion, translating to a payout ratio "
                    "of 56.1%."
                ),
            },
            {
                "heading": "CEO Message",
                "content": (
                    "Dear Valued Shareholders,\n\n"
                    "I am pleased to present the MYBank Group Annual Report for the financial year 2019. "
                    "Despite a challenging macroeconomic environment marked by US-China trade tensions and "
                    "moderating domestic GDP growth of 4.3%, the Group delivered commendable results across "
                    "all key financial metrics.\n\n"
                    "Our digital transformation programme, MYBank Digital 2022, continues to gain traction. "
                    "We processed over 1.2 billion digital transactions during the year, a 34% increase from "
                    "2018. Our mobile banking application, MYBank GO, surpassed 8 million active users, "
                    "cementing our position as a leading digital bank in Malaysia. We invested RM680 million "
                    "in technology infrastructure, with a particular focus on cloud migration, data analytics, "
                    "and cybersecurity capabilities.\n\n"
                    "In the SME segment, we disbursed RM42.3 billion in financing, supporting over 180,000 "
                    "small and medium enterprises nationwide. This is aligned with Bank Negara Malaysia's "
                    "Financial Inclusion agenda and the Government's SME Masterplan 2012-2020. We also "
                    "launched the MYBank SME Digital Financing platform, enabling end-to-end digital loan "
                    "applications for working capital facilities up to RM500,000.\n\n"
                    "Looking ahead to 2020, the Group will continue to invest in our people, technology, "
                    "and regional expansion. I wish to express my sincere gratitude to our Board of Directors, "
                    "management team, and 42,000 employees across nine countries for their dedication and "
                    "commitment.\n\n"
                    "Tan Wei Ming\nGroup Chief Executive Officer\nMYBank Group Berhad"
                ),
            },
            {
                "heading": "Strategy Summary",
                "content": (
                    "The Group's five-year strategic plan, Vision 2024, is anchored on four pillars: "
                    "Customer Centricity, Digital Leadership, Regional Connectivity, and Sustainability. "
                    "In 2019, the Group made significant progress across all pillars.\n\n"
                    "Under Customer Centricity, the Group enhanced its wealth management proposition through "
                    "the launch of MYBank Premier, a premium banking service targeting high-net-worth "
                    "individuals with investable assets exceeding RM3 million. Under Digital Leadership, "
                    "the Group invested in artificial intelligence capabilities, deploying chatbot assistants "
                    "across retail and corporate banking channels. Under Regional Connectivity, the Group's "
                    "ASEAN operations contributed 28% of Group profit before tax, with MYBank Niaga in "
                    "Indonesia and MYBank Thai in Thailand as key growth engines.\n\n"
                    "Sustainability remains central to the Group's long-term value creation strategy. The "
                    "Group committed RM30 billion in sustainable financing by 2025, covering green bonds, "
                    "social impact lending, and ESG-linked loans. In 2019, the Group was included in the "
                    "FTSE4Good Bursa Malaysia Index for the fourth consecutive year."
                ),
            },
            {
                "heading": "Risk Management",
                "content": (
                    "The Group's enterprise risk management framework is governed by the Board Risk "
                    "Management Committee (BRMC) and underpinned by the Three Lines of Defence model, "
                    "in compliance with BNM's Policy Document on Risk Governance (BNM/RH/PD 028-18). "
                    "The Group's risk appetite statement defines quantitative thresholds for credit, "
                    "market, liquidity, and operational risks.\n\n"
                    "Credit risk remains the Group's largest risk exposure, with gross credit exposures "
                    "totalling RM456.2 billion. The Group employs internal ratings-based (IRB) models "
                    "approved by Bank Negara Malaysia for computing credit risk-weighted assets under "
                    "Basel III. Stress testing is conducted semi-annually, simulating severe but "
                    "plausible macroeconomic scenarios including GDP contraction of 3%, ringgit "
                    "depreciation of 15%, and property price declines of 20%.\n\n"
                    "Operational risk management was strengthened through the implementation of a new "
                    "integrated risk and control self-assessment (RCSA) platform. The Group recorded "
                    "total operational risk losses of RM28.4 million in 2019, a 12% reduction from the "
                    "prior year. Cybersecurity investments increased by 40% to address the evolving "
                    "threat landscape, with the Group achieving ISO 27001 certification across all "
                    "domestic operations."
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank Group Annual Report 2019",
                "document_type": "annual_report",
                "entity": "MYBank Group",
                "published_date": datetime(2020, 3, 15),
                "fiscal_year": 2019,
                "version": "1.0",
                "status": "superseded",
                "superseded_by": "MYBank Group Annual Report 2020",
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": None,
                "related_documents": ["MYBank Group Annual Report 2018"],
                "amendment_history": [],
            },
            "approvals": [
                {"approver": "Dato' Sri Haji Mohamad Razlan bin Abdullah", "role": "Chairman", "date": datetime(2020, 2, 28)},
                {"approver": "Tan Wei Ming", "role": "Group CEO", "date": datetime(2020, 2, 28)},
            ],
            "regulatory": {
                "bnm_circulars": ["BNM/RH/PD 029-9", "BNM/RH/GL 001-31"],
                "compliance_categories": ["corporate_governance", "financial_reporting"],
                "data_classification": "public",
            },
            "people_mentioned": [
                {"name": "Tan Wei Ming", "role": "Group CEO", "entity": "MYBank Group",
                 "tenure_start": datetime(2016, 1, 1), "tenure_end": datetime(2021, 6, 30)},
                {"name": "Dato' Sri Haji Mohamad Razlan bin Abdullah", "role": "Chairman", "entity": "MYBank Group",
                 "tenure_start": datetime(2014, 5, 1), "tenure_end": None},
                {"name": "Dr. Rajendra Nair a/l Subramaniam", "role": "BRMC Chairman", "entity": "MYBank Group",
                 "tenure_start": datetime(2017, 3, 1), "tenure_end": None},
            ],
            "distribution": {
                "target_audience": ["shareholders", "analysts", "regulators"],
                "regions": ["Malaysia", "ASEAN"],
            },
        },
    })

    # ── MYBank Group Annual Report 2020 ─────────────────────────────────
    reports.append({
        "title": "MYBank Group Annual Report 2020",
        "sections": [
            {
                "heading": "Board of Directors",
                "content": (
                    "The Board of Directors of MYBank Group Berhad maintained its composition of twelve "
                    "members throughout the financial year 2020. Dato' Sri Haji Mohamad Razlan bin Abdullah "
                    "continued to serve as Chairman, providing steady leadership during the unprecedented "
                    "challenges posed by the COVID-19 pandemic. Group CEO Tan Wei Ming led the management "
                    "team through the crisis with decisive action, including the swift implementation of "
                    "Bank Negara Malaysia's loan moratorium programme.\n\n"
                    "The Board convened eighteen meetings during the year, compared to the usual twelve, "
                    "reflecting the heightened governance requirements during the pandemic. The Board Risk "
                    "Management Committee, chaired by Dr. Rajendra Nair a/l Subramaniam, met fortnightly "
                    "during the Movement Control Order (MCO) period to monitor credit quality and liquidity "
                    "positions. Encik Azman bin Mohd Yusof was appointed as Group Chief Risk Officer, "
                    "replacing Puan Faridah binti Hassan who retired after 28 years of distinguished service."
                ),
            },
            {
                "heading": "Financial Highlights",
                "content": (
                    "MYBank Group recorded a net profit of RM3.41 billion for the financial year ended "
                    "31 December 2020, a decrease of 17.2% from RM4.12 billion in 2019, primarily due to "
                    "significantly higher expected credit loss (ECL) provisions under MFRS 9 in response "
                    "to the COVID-19 pandemic. Total assets grew 5.3% to RM525.1 billion. The Group's "
                    "return on equity declined to 9.2% from 11.4% in the prior year.\n\n"
                    "The Group proactively set aside RM2.18 billion in ECL provisions, including RM1.34 "
                    "billion in management overlay provisions to address potential credit deterioration "
                    "from the economic downturn. Gross impaired loan ratio increased to 2.14% from 1.82%, "
                    "but loan loss coverage strengthened to 112.3%. The Group's CET1 capital ratio remained "
                    "robust at 13.8%, providing a comfortable buffer above BNM's minimum requirement.\n\n"
                    "Under the BNM blanket moratorium programme, the Group granted automatic six-month "
                    "loan repayment deferrals to 2.1 million individual borrowers and 98,000 SME customers, "
                    "covering RM189 billion in outstanding financing. The Group also provided targeted "
                    "repayment assistance to an additional 124,000 borrowers who required extended support "
                    "beyond the moratorium period."
                ),
            },
            {
                "heading": "CEO Message",
                "content": (
                    "Dear Valued Shareholders,\n\n"
                    "The year 2020 will be remembered as one of the most challenging periods in our Group's "
                    "history. The COVID-19 pandemic tested our operational resilience, financial strength, "
                    "and commitment to our stakeholders in ways we could not have anticipated.\n\n"
                    "I am proud to report that MYBank Group rose to the occasion. Within 72 hours of the "
                    "Movement Control Order announcement on 16 March 2020, we activated our business "
                    "continuity plans across all nine countries of operation. Over 85% of our headquarters "
                    "staff transitioned to work-from-home arrangements, and we maintained uninterrupted "
                    "service across our 450 branches nationwide, with enhanced health and safety protocols.\n\n"
                    "Our digital channels proved critical during the crisis. MYBank GO mobile app "
                    "registrations surged 67% to 13.4 million users, while digital transaction volumes "
                    "increased 52% to 1.82 billion transactions. We accelerated the deployment of our "
                    "digital account opening service, enabling customers to open savings accounts entirely "
                    "online, with eKYC verification powered by our proprietary AI engine.\n\n"
                    "Despite the financial headwinds, we continued to invest RM720 million in technology, "
                    "recognising that our digital capabilities will be a key competitive differentiator in "
                    "the post-pandemic era. I am grateful to our 42,500 employees for their extraordinary "
                    "resilience and dedication during this difficult year.\n\n"
                    "Tan Wei Ming\nGroup Chief Executive Officer\nMYBank Group Berhad"
                ),
            },
            {
                "heading": "Risk Management",
                "content": (
                    "The COVID-19 pandemic fundamentally reshaped the Group's risk landscape in 2020. "
                    "The Board Risk Management Committee activated the Group's crisis management protocol, "
                    "establishing a dedicated COVID-19 Risk Task Force chaired by Group Chief Risk Officer "
                    "Encik Azman bin Mohd Yusof.\n\n"
                    "Credit risk management was the primary focus, with the Group conducting enhanced "
                    "portfolio reviews across all lending segments. Industry-specific stress tests were "
                    "performed for sectors most affected by the pandemic, including tourism, hospitality, "
                    "retail, and aviation. The Group identified RM18.7 billion in exposures requiring "
                    "heightened monitoring, representing approximately 5.3% of the total loan portfolio.\n\n"
                    "Liquidity risk management was strengthened through proactive balance sheet management. "
                    "The Group maintained a Liquidity Coverage Ratio (LCR) of 148%, well above the "
                    "regulatory minimum of 100%. Net Stable Funding Ratio (NSFR) stood at 112%. The Group "
                    "also participated in BNM's RM10 billion Special Relief Facility and RM5 billion "
                    "Automation and Digitalisation Facility to channel concessionary financing to affected "
                    "businesses, in compliance with BNM's Policy Document on Liquidity Risk Management "
                    "(BNM/RH/PD 032-15)."
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank Group Annual Report 2020",
                "document_type": "annual_report",
                "entity": "MYBank Group",
                "published_date": datetime(2021, 3, 18),
                "fiscal_year": 2020,
                "version": "1.0",
                "status": "superseded",
                "superseded_by": "MYBank Group Annual Report 2021",
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": "MYBank Group Annual Report 2019",
                "related_documents": ["MYBank Group Annual Report 2019"],
                "amendment_history": [],
            },
            "approvals": [
                {"approver": "Dato' Sri Haji Mohamad Razlan bin Abdullah", "role": "Chairman", "date": datetime(2021, 2, 26)},
                {"approver": "Tan Wei Ming", "role": "Group CEO", "date": datetime(2021, 2, 26)},
            ],
            "regulatory": {
                "bnm_circulars": ["BNM/RH/PD 029-9", "BNM/RH/PD 032-15"],
                "compliance_categories": ["corporate_governance", "financial_reporting", "crisis_management"],
                "data_classification": "public",
            },
            "people_mentioned": [
                {"name": "Tan Wei Ming", "role": "Group CEO", "entity": "MYBank Group",
                 "tenure_start": datetime(2016, 1, 1), "tenure_end": datetime(2021, 6, 30)},
                {"name": "Dato' Sri Haji Mohamad Razlan bin Abdullah", "role": "Chairman", "entity": "MYBank Group",
                 "tenure_start": datetime(2014, 5, 1), "tenure_end": None},
                {"name": "Encik Azman bin Mohd Yusof", "role": "Group CRO", "entity": "MYBank Group",
                 "tenure_start": datetime(2020, 4, 1), "tenure_end": None},
            ],
            "distribution": {
                "target_audience": ["shareholders", "analysts", "regulators"],
                "regions": ["Malaysia", "ASEAN"],
            },
        },
    })

    # ── MYBank Group Annual Report 2021 (CEO Transition) ────────────────
    reports.append({
        "title": "MYBank Group Annual Report 2021",
        "sections": [
            {
                "heading": "Board of Directors",
                "content": (
                    "The year 2021 marked a significant leadership transition for MYBank Group Berhad. "
                    "After six years of distinguished service, Group Chief Executive Officer Tan Wei Ming "
                    "retired effective 30 June 2021, having successfully steered the Group through the "
                    "COVID-19 crisis and laid the foundation for the Group's digital transformation.\n\n"
                    "The Board of Directors appointed Lim Siew Hua as the incoming Group Chief Executive "
                    "Officer, effective 1 July 2021. Incoming CEO Lim Siew Hua succeeds Tan Wei Ming, "
                    "bringing twenty-two years of experience within the Group, most recently as Deputy "
                    "Group CEO and Head of Group Wholesale Banking. Lim Siew Hua became the first female "
                    "Group CEO in the history of MYBank Group, reflecting the Board's commitment to "
                    "diversity and inclusion.\n\n"
                    "Dato' Sri Haji Mohamad Razlan bin Abdullah continued as Chairman. The Board appointed "
                    "two new independent directors: Encik Kamal Ariffin bin Hashim, former Secretary-General "
                    "of the Ministry of Finance, and Ms. Chen Li Ping, a distinguished fintech entrepreneur "
                    "and former partner at McKinsey & Company's Southeast Asia practice."
                ),
            },
            {
                "heading": "Financial Highlights",
                "content": (
                    "MYBank Group delivered a strong recovery in 2021, recording a net profit of RM4.58 "
                    "billion, a 34.3% increase from RM3.41 billion in 2020. The improvement was driven by "
                    "lower net expected credit loss provisions and robust fee-based income growth. Total "
                    "assets reached RM548.9 billion, while return on equity recovered to 12.1%.\n\n"
                    "Gross loans and financing grew 6.2% to RM388.7 billion, supported by resilient "
                    "mortgage demand and a recovery in corporate lending activity. Customer deposits "
                    "expanded 4.8% to RM428.6 billion, with CASA ratio reaching a record high of 41.2%, "
                    "benefiting from the low interest rate environment. The Group's net interest margin "
                    "compressed modestly to 2.05% due to multiple OPR cuts by Bank Negara Malaysia.\n\n"
                    "The Group released RM420 million in management overlay provisions as credit quality "
                    "stabilised, while maintaining RM920 million in overlay provisions as a prudent buffer. "
                    "CET1 capital ratio improved to 14.3%, reflecting strong internal capital generation. "
                    "The Group declared total dividends of RM2.74 billion, representing a payout ratio "
                    "of 59.8%."
                ),
            },
            {
                "heading": "CEO Message",
                "content": (
                    "Dear Valued Shareholders,\n\n"
                    "It is my privilege to address you for the first time as Group Chief Executive Officer "
                    "of MYBank Group Berhad. I assumed this role on 1 July 2021, succeeding Tan Wei Ming, "
                    "whose visionary leadership over the past six years has positioned the Group for "
                    "continued success. I am deeply honoured by the trust placed in me by the Board and "
                    "our shareholders.\n\n"
                    "The Group delivered a strong financial performance in 2021, demonstrating the resilience "
                    "of our diversified business model and the strength of our franchise across ASEAN. As "
                    "Malaysia's economy recovered from the pandemic with GDP growth of 3.1%, our Group "
                    "capitalised on the improving conditions while maintaining disciplined risk management.\n\n"
                    "I have outlined my strategic vision for the Group under the refreshed plan, MYBank "
                    "Forward 2026. This plan builds on the strong foundations laid by my predecessor and "
                    "focuses on three transformative priorities: accelerating digital and data capabilities, "
                    "deepening our ASEAN connectivity, and embedding sustainability at the core of our "
                    "business model. We will invest RM4.5 billion over the next five years in technology "
                    "and talent to execute this vision.\n\n"
                    "I also wish to recognise Tan Wei Ming's outstanding contributions to the Group. Under "
                    "his leadership, MYBank Group's market capitalisation grew from RM62 billion to RM89 "
                    "billion, and our digital transformation programme positioned us as a regional leader "
                    "in digital banking.\n\n"
                    "Lim Siew Hua\nGroup Chief Executive Officer\nMYBank Group Berhad"
                ),
            },
            {
                "heading": "Strategy Summary",
                "content": (
                    "MYBank Forward 2026, the Group's refreshed five-year strategic plan unveiled by "
                    "incoming CEO Lim Siew Hua, is built on three transformative priorities that will "
                    "drive the Group's next phase of growth and value creation.\n\n"
                    "The first priority, Digital & Data, targets a 60% increase in digital revenue "
                    "contribution by 2026. Key initiatives include the development of a unified data "
                    "platform leveraging cloud-native architecture, the deployment of AI and machine "
                    "learning across credit decisioning, fraud detection, and customer personalisation, "
                    "and the launch of a Banking-as-a-Service (BaaS) platform for ecosystem partners.\n\n"
                    "The second priority, ASEAN Connectivity, aims to increase the ASEAN contribution "
                    "to Group profit before tax from 28% to 35%. The Group will deepen its presence in "
                    "Indonesia through MYBank Niaga and in Thailand through MYBank Thai, while exploring "
                    "targeted opportunities in Vietnam and the Philippines. Cross-border transaction "
                    "banking and supply chain financing will be key growth areas.\n\n"
                    "The third priority, Sustainability, commits the Group to achieving net-zero financed "
                    "emissions by 2050, with interim targets for 2030. The Group will mobilise RM65 billion "
                    "in sustainable financing by 2026, develop a comprehensive climate risk assessment "
                    "framework aligned with TCFD recommendations, and embed ESG considerations into all "
                    "lending and investment decisions."
                ),
            },
            {
                "heading": "Risk Management",
                "content": (
                    "The Group's risk management framework continued to evolve in 2021 to address the "
                    "post-pandemic environment. The Board Risk Management Committee, chaired by Dr. Rajendra "
                    "Nair a/l Subramaniam, oversaw the implementation of enhanced credit risk monitoring "
                    "tools and the development of climate risk assessment capabilities.\n\n"
                    "Credit quality showed encouraging improvement, with the gross impaired loan ratio "
                    "declining to 1.94% from 2.14% in 2020. The Group wound down its targeted repayment "
                    "assistance programmes, with 87% of assisted borrowers resuming regular repayments. "
                    "The remaining borrowers were assessed individually and reclassified under the Group's "
                    "standard credit review processes, in accordance with BNM's revised guidelines on "
                    "credit risk management (BNM/RH/PD 030-12).\n\n"
                    "Operational risk management focused on strengthening resilience against cyber threats "
                    "and technology disruptions. The Group invested RM185 million in cybersecurity, including "
                    "the establishment of a 24/7 Security Operations Centre (SOC) and the deployment of "
                    "advanced threat detection capabilities using artificial intelligence. The Group "
                    "conducted two full-scale business continuity exercises, simulating a simultaneous "
                    "cyber attack and pandemic scenario across its domestic and regional operations."
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank Group Annual Report 2021",
                "document_type": "annual_report",
                "entity": "MYBank Group",
                "published_date": datetime(2022, 3, 20),
                "fiscal_year": 2021,
                "version": "1.0",
                "status": "superseded",
                "superseded_by": "MYBank Group Annual Report 2022",
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": "MYBank Group Annual Report 2020",
                "related_documents": ["MYBank Group Annual Report 2020"],
                "amendment_history": [],
            },
            "approvals": [
                {"approver": "Dato' Sri Haji Mohamad Razlan bin Abdullah", "role": "Chairman", "date": datetime(2022, 2, 25)},
                {"approver": "Lim Siew Hua", "role": "Group CEO", "date": datetime(2022, 2, 25)},
            ],
            "regulatory": {
                "bnm_circulars": ["BNM/RH/PD 029-9", "BNM/RH/PD 030-12"],
                "compliance_categories": ["corporate_governance", "financial_reporting"],
                "data_classification": "public",
            },
            "people_mentioned": [
                {"name": "Tan Wei Ming", "role": "Former Group CEO", "entity": "MYBank Group",
                 "tenure_start": datetime(2016, 1, 1), "tenure_end": datetime(2021, 6, 30)},
                {"name": "Lim Siew Hua", "role": "Group CEO", "entity": "MYBank Group",
                 "tenure_start": datetime(2021, 7, 1), "tenure_end": None},
                {"name": "Dato' Sri Haji Mohamad Razlan bin Abdullah", "role": "Chairman", "entity": "MYBank Group",
                 "tenure_start": datetime(2014, 5, 1), "tenure_end": None},
            ],
            "distribution": {
                "target_audience": ["shareholders", "analysts", "regulators"],
                "regions": ["Malaysia", "ASEAN"],
            },
        },
    })

    # ── MYBank Group Annual Report 2022 ─────────────────────────────────
    reports.append({
        "title": "MYBank Group Annual Report 2022",
        "sections": [
            {
                "heading": "Board of Directors",
                "content": (
                    "The Board of Directors of MYBank Group Berhad comprises thirteen members as at "
                    "31 December 2022, following the appointment of Puan Nurul Izzah binti Anwar as an "
                    "additional independent non-executive director. Dato' Sri Haji Mohamad Razlan bin "
                    "Abdullah serves as Chairman, with Lim Siew Hua as Group Chief Executive Officer "
                    "completing her first full year in the role.\n\n"
                    "The Board continued to strengthen its oversight of emerging risks, including climate "
                    "risk and technology disruption. A new Board Technology and Innovation Committee was "
                    "established, chaired by Ms. Chen Li Ping, to provide dedicated oversight of the "
                    "Group's digital transformation agenda and technology risk management. The Board also "
                    "approved the Group's Climate Risk Management Framework, aligning with BNM's Climate "
                    "Change and Principle-based Taxonomy (BNM/RH/PD 029-24)."
                ),
            },
            {
                "heading": "Financial Highlights",
                "content": (
                    "MYBank Group achieved record financial performance in 2022, with net profit reaching "
                    "RM5.23 billion, a 14.2% increase from RM4.58 billion in 2021. This was driven by "
                    "net interest margin expansion following OPR hikes by Bank Negara Malaysia, as well as "
                    "strong growth in fee-based income. Total assets grew to RM578.4 billion.\n\n"
                    "Net interest margin expanded to 2.28% from 2.05%, benefiting from the 100 basis "
                    "points cumulative OPR increase during the year. Gross loans and financing grew 8.4% "
                    "to RM421.3 billion, with strong momentum in mortgage lending and SME financing. "
                    "Customer deposits grew 5.9% to RM453.9 billion, though CASA ratio moderated to 38.5% "
                    "as customers shifted towards fixed deposits in the rising rate environment.\n\n"
                    "Return on equity improved to 13.4%, while cost-to-income ratio was maintained at "
                    "44.1%. CET1 capital ratio stood at 14.1%. The Group declared dividends of RM3.14 "
                    "billion, with a payout ratio of 60.1%. Earnings per share grew to 58.2 sen from "
                    "51.0 sen in the prior year."
                ),
            },
            {
                "heading": "CEO Message",
                "content": (
                    "Dear Valued Shareholders,\n\n"
                    "MYBank Group delivered an exceptional year in 2022, achieving record profitability "
                    "while making significant strides in our MYBank Forward 2026 strategic plan. The "
                    "Malaysian economy grew 8.7%, driven by the post-pandemic recovery and strong domestic "
                    "demand, creating a favourable operating environment for the banking sector.\n\n"
                    "Our digital transformation is yielding tangible results. Digital channel transactions "
                    "now account for 78% of total transaction volume, up from 62% in 2020. Our MYBank GO "
                    "app has been rated the number one banking app in Malaysia on both App Store and Google "
                    "Play, with 18.2 million registered users. We processed over RM120 billion in digital "
                    "payments, representing a 45% year-on-year increase.\n\n"
                    "In sustainability, we mobilised RM28.4 billion in sustainable financing during the year, "
                    "bringing cumulative sustainable financing to RM52.1 billion against our target of "
                    "RM65 billion by 2026. We also published our inaugural Climate Risk Report aligned with "
                    "TCFD recommendations and completed climate stress testing across our domestic loan "
                    "portfolio.\n\n"
                    "Our ASEAN operations contributed 31% of Group profit before tax, up from 28% in 2021. "
                    "MYBank Niaga in Indonesia delivered a 22% profit growth, while MYBank Thai achieved a "
                    "return on equity of 11.8%, its highest in five years.\n\n"
                    "Lim Siew Hua\nGroup Chief Executive Officer\nMYBank Group Berhad"
                ),
            },
            {
                "heading": "Risk Management",
                "content": (
                    "The Group's risk management capabilities were further enhanced in 2022 through "
                    "investments in data analytics, climate risk modelling, and regulatory technology. "
                    "The Board Risk Management Committee approved the Group's enhanced Risk Appetite "
                    "Framework, which now incorporates ESG risk metrics and climate-related financial "
                    "risk indicators.\n\n"
                    "Credit quality improved significantly, with the gross impaired loan ratio declining "
                    "to 1.62% from 1.94% in 2021. Management overlay provisions of RM500 million were "
                    "released during the year as the credit environment normalised. The Group's total ECL "
                    "provisions amounted to RM6.8 billion, representing loan loss coverage of 106.2%.\n\n"
                    "Market risk management addressed the challenges of rising interest rates and currency "
                    "volatility. The Group's Value-at-Risk (VaR) for trading activities averaged RM12.4 "
                    "million, within the Board-approved limit of RM35 million. Interest rate risk in the "
                    "banking book (IRRBB) was managed within a net interest income sensitivity of +/- 2.8% "
                    "for a 100 basis point parallel rate shock, in compliance with BNM's IRRBB standards "
                    "(BNM/RH/STD 033-6)."
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank Group Annual Report 2022",
                "document_type": "annual_report",
                "entity": "MYBank Group",
                "published_date": datetime(2023, 3, 22),
                "fiscal_year": 2022,
                "version": "1.0",
                "status": "superseded",
                "superseded_by": "MYBank Group Annual Report 2023",
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": "MYBank Group Annual Report 2021",
                "related_documents": ["MYBank Group Annual Report 2021"],
                "amendment_history": [],
            },
            "approvals": [
                {"approver": "Dato' Sri Haji Mohamad Razlan bin Abdullah", "role": "Chairman", "date": datetime(2023, 2, 24)},
                {"approver": "Lim Siew Hua", "role": "Group CEO", "date": datetime(2023, 2, 24)},
            ],
            "regulatory": {
                "bnm_circulars": ["BNM/RH/PD 029-9", "BNM/RH/PD 029-24", "BNM/RH/STD 033-6"],
                "compliance_categories": ["corporate_governance", "financial_reporting", "climate_risk"],
                "data_classification": "public",
            },
            "people_mentioned": [
                {"name": "Lim Siew Hua", "role": "Group CEO", "entity": "MYBank Group",
                 "tenure_start": datetime(2021, 7, 1), "tenure_end": None},
                {"name": "Dato' Sri Haji Mohamad Razlan bin Abdullah", "role": "Chairman", "entity": "MYBank Group",
                 "tenure_start": datetime(2014, 5, 1), "tenure_end": None},
            ],
            "distribution": {
                "target_audience": ["shareholders", "analysts", "regulators"],
                "regions": ["Malaysia", "ASEAN"],
            },
        },
    })

    # ── MYBank Group Annual Report 2023 ─────────────────────────────────
    reports.append({
        "title": "MYBank Group Annual Report 2023",
        "sections": [
            {
                "heading": "Board of Directors",
                "content": (
                    "The Board of Directors of MYBank Group Berhad maintained thirteen members as at "
                    "31 December 2023. Dato' Sri Haji Mohamad Razlan bin Abdullah continued his distinguished "
                    "tenure as Chairman. Group CEO Lim Siew Hua completed her second full year in the role, "
                    "driving the execution of MYBank Forward 2026. The Board Gender Diversity policy has "
                    "achieved its target with women comprising 38% of Board membership, exceeding the 30% "
                    "target set by the Securities Commission Malaysia.\n\n"
                    "The Board Nomination and Remuneration Committee, chaired by Tan Sri Dato' Seri Amirah "
                    "binti Kamaruddin, completed its succession planning review for all Group Management "
                    "Committee positions. The Board approved the Group's refreshed Fit and Proper Policy, "
                    "aligned with BNM's updated Fit and Proper Criteria policy document (BNM/RH/PD 026-12). "
                    "Dr. Rajendra Nair a/l Subramaniam continues as BRMC Chairman."
                ),
            },
            {
                "heading": "Financial Highlights",
                "content": (
                    "MYBank Group continued its strong financial trajectory in 2023, recording a net profit "
                    "of RM5.67 billion, a 8.4% increase from the prior year. Total assets grew 6.1% to "
                    "RM613.7 billion, consolidating the Group's position as one of the largest banking groups "
                    "in Southeast Asia. Return on equity was maintained at 13.6%.\n\n"
                    "Gross loans and financing expanded 7.1% to RM451.2 billion, with mortgage lending "
                    "contributing RM142.8 billion and SME financing reaching RM98.4 billion. The Group's "
                    "net interest margin stabilised at 2.22% as BNM held the OPR steady at 3.00% throughout "
                    "the year. Non-interest income grew 11.2% to RM5.13 billion, led by wealth management "
                    "fees, transaction banking income, and insurance commissions.\n\n"
                    "Asset quality remained robust with a gross impaired loan ratio of 1.48%, the lowest "
                    "in five years. The Group's cost-to-income ratio improved to 43.2%, reflecting ongoing "
                    "productivity gains from digital investments. CET1 ratio stood at 14.5%, with total "
                    "capital ratio at 18.2%. Dividends declared totalled RM3.52 billion, representing a "
                    "payout ratio of 62.1%."
                ),
            },
            {
                "heading": "CEO Message",
                "content": (
                    "Dear Valued Shareholders,\n\n"
                    "I am delighted to present MYBank Group's Annual Report for 2023, a year in which we "
                    "delivered record profitability while advancing our strategic transformation at pace. "
                    "The Malaysian economy grew 3.7%, moderated from the high base of 2022, but the banking "
                    "sector remained well-supported by resilient domestic demand and a healthy labour market.\n\n"
                    "Our MYBank Forward 2026 strategy is on track across all three pillars. In Digital & Data, "
                    "we launched our unified data platform and deployed over 120 AI and machine learning "
                    "models across credit decisioning, fraud detection, and customer personalisation. Our "
                    "digital revenue contribution reached 42%, up from 31% at the start of the plan.\n\n"
                    "In ASEAN Connectivity, our regional operations contributed 33% of Group profit before "
                    "tax, approaching our 35% target. We expanded our cross-border payment capabilities to "
                    "cover seven ASEAN countries through real-time payment linkages. In Sustainability, "
                    "cumulative sustainable financing reached RM61.8 billion, and we established a dedicated "
                    "Energy Transition Finance team to support our clients' decarbonisation journeys.\n\n"
                    "We also made significant investments in our people, launching the MYBank Academy to "
                    "upskill 15,000 employees in data literacy, design thinking, and agile methodologies. "
                    "Our employee engagement score reached 82%, the highest in the Group's history.\n\n"
                    "Lim Siew Hua\nGroup Chief Executive Officer\nMYBank Group Berhad"
                ),
            },
            {
                "heading": "Strategy Summary",
                "content": (
                    "Halfway through the MYBank Forward 2026 plan, the Group conducted a mid-term review "
                    "to assess progress and recalibrate priorities. The review confirmed that the Group is "
                    "on track to achieve most of its 2026 financial targets, including return on equity "
                    "of 13-15%, cost-to-income ratio below 43%, and sustainable financing of RM65 billion.\n\n"
                    "Key strategic initiatives launched or accelerated in 2023 include: (1) MYBank Ventures, "
                    "a corporate venture arm with RM500 million in committed capital to invest in fintech "
                    "startups across ASEAN; (2) Project Horizon, a core banking system modernisation programme "
                    "that will migrate the Group's legacy systems to a cloud-native, microservices architecture "
                    "over the next three years; and (3) MYBank Wealth, an integrated wealth management "
                    "platform targeting the growing affluent segment in Malaysia and Singapore.\n\n"
                    "The Group also deepened its collaboration with Bank Negara Malaysia on regulatory "
                    "innovation, participating in BNM's sandbox for open banking API standards and contributing "
                    "to the development of Malaysia's real-time payment infrastructure enhancement programme."
                ),
            },
            {
                "heading": "Risk Management",
                "content": (
                    "The Group's enterprise risk management framework was further strengthened in 2023 "
                    "with the integration of climate risk into the overall risk appetite framework. The "
                    "Board Risk Management Committee approved sector-specific carbon intensity targets for "
                    "the Group's lending portfolio, covering power generation, oil and gas, palm oil, and "
                    "transportation sectors.\n\n"
                    "Climate stress testing was expanded to cover the Group's ASEAN operations, with "
                    "scenario analysis conducted under both orderly and disorderly transition pathways "
                    "aligned with NGFS scenarios. The Group estimated potential credit losses of RM2.1 "
                    "billion under a disorderly transition scenario over a 10-year horizon, primarily "
                    "concentrated in carbon-intensive sectors.\n\n"
                    "Cyber risk management remains a top priority, with the Group investing RM210 million "
                    "in cybersecurity capabilities. The Group's Security Operations Centre now operates "
                    "across three time zones, providing 24/7 threat monitoring and response capabilities. "
                    "The Group conducted a red team exercise simulating a sophisticated nation-state attack, "
                    "with all critical systems maintaining operational integrity. The Group continues to "
                    "comply with BNM's Risk Management in Technology policy (BNM/RH/PD 028-18) and the "
                    "Technology Risk Management Framework."
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank Group Annual Report 2023",
                "document_type": "annual_report",
                "entity": "MYBank Group",
                "published_date": datetime(2024, 3, 25),
                "fiscal_year": 2023,
                "version": "1.0",
                "status": "superseded",
                "superseded_by": "MYBank Group Annual Report 2024",
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": "MYBank Group Annual Report 2022",
                "related_documents": ["MYBank Group Annual Report 2022", "MYBank Niaga Annual Report 2023", "MYBank Thai Annual Report 2023"],
                "amendment_history": [],
            },
            "approvals": [
                {"approver": "Dato' Sri Haji Mohamad Razlan bin Abdullah", "role": "Chairman", "date": datetime(2024, 2, 28)},
                {"approver": "Lim Siew Hua", "role": "Group CEO", "date": datetime(2024, 2, 28)},
            ],
            "regulatory": {
                "bnm_circulars": ["BNM/RH/PD 029-9", "BNM/RH/PD 026-12", "BNM/RH/PD 028-18"],
                "compliance_categories": ["corporate_governance", "financial_reporting", "climate_risk", "technology_risk"],
                "data_classification": "public",
            },
            "people_mentioned": [
                {"name": "Lim Siew Hua", "role": "Group CEO", "entity": "MYBank Group",
                 "tenure_start": datetime(2021, 7, 1), "tenure_end": None},
                {"name": "Dato' Sri Haji Mohamad Razlan bin Abdullah", "role": "Chairman", "entity": "MYBank Group",
                 "tenure_start": datetime(2014, 5, 1), "tenure_end": None},
                {"name": "Dr. Rajendra Nair a/l Subramaniam", "role": "BRMC Chairman", "entity": "MYBank Group",
                 "tenure_start": datetime(2017, 3, 1), "tenure_end": None},
            ],
            "distribution": {
                "target_audience": ["shareholders", "analysts", "regulators"],
                "regions": ["Malaysia", "ASEAN"],
            },
        },
    })

    # ── MYBank Group Annual Report 2024 (Current) ──────────────────────
    reports.append({
        "title": "MYBank Group Annual Report 2024",
        "sections": [
            {
                "heading": "Board of Directors",
                "content": (
                    "The Board of Directors of MYBank Group Berhad comprises fourteen members as at "
                    "31 December 2024, with the appointment of Encik Hafiz bin Mohd Noor, former CEO of "
                    "Bursa Malaysia, as a non-independent non-executive director. Dato' Sri Haji Mohamad "
                    "Razlan bin Abdullah continues as Chairman, marking his tenth year in the role.\n\n"
                    "Group CEO Lim Siew Hua completed her third full year of leadership, driving the Group "
                    "to new milestones in digital banking, regional expansion, and sustainable finance. "
                    "Under her leadership, the Group's market capitalisation surpassed RM110 billion, "
                    "making it the most valuable bank listed on Bursa Malaysia.\n\n"
                    "The Board's governance framework was enhanced with the publication of a refreshed "
                    "Board Charter incorporating BNM's latest corporate governance expectations. The Board "
                    "also approved an updated Related Party Transaction Policy and a new Group Conduct and "
                    "Culture Framework, reflecting the growing importance of conduct risk management in "
                    "the banking industry."
                ),
            },
            {
                "heading": "Financial Highlights",
                "content": (
                    "MYBank Group achieved another year of record performance in 2024, with net profit "
                    "reaching RM6.14 billion, an 8.3% increase from RM5.67 billion in 2023. Total assets "
                    "grew 7.2% to RM657.8 billion. The Group's return on equity stood at 14.1%, exceeding "
                    "the upper end of our MYBank Forward 2026 target range.\n\n"
                    "Gross loans and financing expanded 8.8% to RM490.8 billion, with strong growth across "
                    "all segments. Mortgage lending grew 9.2% to RM155.9 billion, SME financing expanded "
                    "11.4% to RM109.6 billion, and corporate lending increased 7.1% to RM158.3 billion. "
                    "Customer deposits grew 6.8% to RM505.2 billion, with CASA ratio at 37.8%.\n\n"
                    "Net interest margin remained stable at 2.20% as BNM held the OPR at 3.00%. "
                    "Non-interest income grew 13.8% to RM5.84 billion, with wealth management and "
                    "transaction banking as key contributors. The cost-to-income ratio improved further "
                    "to 42.1%, achieving the sub-43% target one year ahead of plan. CET1 ratio was "
                    "maintained at 14.3%, while total capital ratio stood at 18.5%. Dividends declared "
                    "totalled RM3.87 billion."
                ),
            },
            {
                "heading": "CEO Message",
                "content": (
                    "Dear Valued Shareholders,\n\n"
                    "It is my pleasure to present MYBank Group's Annual Report for 2024, a year of "
                    "significant milestones and continued strategic progress. The Group achieved record "
                    "net profit of RM6.14 billion, a testament to the strength of our franchise and the "
                    "dedication of our 44,000 employees across ten countries.\n\n"
                    "Malaysia's economy grew 4.8% in 2024, supported by robust domestic demand, a recovery "
                    "in global trade, and the positive impact of structural reforms under the MADANI Economy "
                    "framework. The banking sector benefited from this favourable environment, with system "
                    "loan growth of 6.4%.\n\n"
                    "Our MYBank Forward 2026 strategic plan has delivered transformative results. Digital "
                    "revenue contribution reached 48%, approaching our 60% target. We launched MYBank AI "
                    "Assistant, a generative AI-powered customer service platform that handles 2.3 million "
                    "interactions monthly. Our ASEAN operations now contribute 34% of Group profit before "
                    "tax, nearly achieving our 35% target.\n\n"
                    "In sustainability, we surpassed our RM65 billion sustainable financing target one year "
                    "ahead of plan, reaching RM71.2 billion in cumulative sustainable financing. We also "
                    "published our first Transition Plan, detailing our pathway to net-zero financed "
                    "emissions by 2050 with science-based interim targets for 2030.\n\n"
                    "Looking ahead to 2025, I am confident in the Group's ability to navigate the evolving "
                    "macroeconomic landscape and deliver sustained value creation for all stakeholders.\n\n"
                    "Lim Siew Hua\nGroup Chief Executive Officer\nMYBank Group Berhad"
                ),
            },
            {
                "heading": "Strategy Summary",
                "content": (
                    "With the MYBank Forward 2026 plan entering its penultimate year, the Group is "
                    "well-positioned to achieve or exceed most of its strategic targets. Key highlights "
                    "from the 2024 strategy execution include:\n\n"
                    "Project Horizon, the core banking modernisation programme, completed its first phase, "
                    "migrating retail banking operations in Malaysia to the new cloud-native platform. "
                    "The migration delivered a 40% improvement in transaction processing speed and a 30% "
                    "reduction in technology operating costs. Phase two, covering corporate and wholesale "
                    "banking, is scheduled for completion by mid-2025.\n\n"
                    "MYBank Ventures made four investments totalling RM120 million in fintech companies "
                    "across payments, insurtech, and green finance. The venture portfolio has generated "
                    "strategic value through technology partnerships and talent pipeline development.\n\n"
                    "The Group also launched MYBank SME Marketplace, a digital platform connecting SME "
                    "customers with ecosystem partners for accounting, logistics, and e-commerce services. "
                    "The platform onboarded 28,000 SME customers in its first six months of operation. "
                    "These initiatives reinforce the Group's vision of becoming a technology-led financial "
                    "services group with deep ASEAN roots."
                ),
            },
            {
                "heading": "Risk Management",
                "content": (
                    "Risk management in 2024 focused on emerging risks including generative AI, "
                    "geopolitical uncertainty, and the evolving regulatory landscape. The Board Risk "
                    "Management Committee approved a new AI Risk Management Framework governing the "
                    "Group's deployment of artificial intelligence across customer-facing and internal "
                    "applications, aligned with BNM's guidance on responsible AI adoption.\n\n"
                    "Credit quality remained excellent, with the gross impaired loan ratio at a record "
                    "low of 1.38%. The Group's ECL provisions totalled RM7.2 billion, with loan loss "
                    "coverage at 108.4%. The Group conducted comprehensive climate stress testing across "
                    "all operating entities, incorporating physical risk scenarios including flood modelling "
                    "for Malaysian operations and heat stress projections for regional portfolios.\n\n"
                    "Cybersecurity investments increased to RM245 million, with the Group deploying "
                    "AI-powered threat detection and response capabilities. The Group achieved zero "
                    "material cybersecurity incidents during the year, reflecting the effectiveness of "
                    "its multi-layered defence strategy. Operational resilience was further strengthened "
                    "through the establishment of a third data centre in Cyberjaya, providing enhanced "
                    "disaster recovery capabilities. The Group complies with BNM's Policy Document on "
                    "Risk Management in Technology (BNM/RH/PD 028-18) and Outsourcing guidelines."
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank Group Annual Report 2024",
                "document_type": "annual_report",
                "entity": "MYBank Group",
                "published_date": datetime(2025, 3, 20),
                "fiscal_year": 2024,
                "version": "1.0",
                "status": "current",
                "superseded_by": None,
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": "MYBank Group Annual Report 2023",
                "related_documents": ["MYBank Group Annual Report 2023"],
                "amendment_history": [],
            },
            "approvals": [
                {"approver": "Dato' Sri Haji Mohamad Razlan bin Abdullah", "role": "Chairman", "date": datetime(2025, 2, 27)},
                {"approver": "Lim Siew Hua", "role": "Group CEO", "date": datetime(2025, 2, 27)},
            ],
            "regulatory": {
                "bnm_circulars": ["BNM/RH/PD 029-9", "BNM/RH/PD 028-18"],
                "compliance_categories": ["corporate_governance", "financial_reporting", "climate_risk", "ai_governance"],
                "data_classification": "public",
            },
            "people_mentioned": [
                {"name": "Lim Siew Hua", "role": "Group CEO", "entity": "MYBank Group",
                 "tenure_start": datetime(2021, 7, 1), "tenure_end": None},
                {"name": "Dato' Sri Haji Mohamad Razlan bin Abdullah", "role": "Chairman", "entity": "MYBank Group",
                 "tenure_start": datetime(2014, 5, 1), "tenure_end": None},
                {"name": "Encik Hafiz bin Mohd Noor", "role": "Non-Executive Director", "entity": "MYBank Group",
                 "tenure_start": datetime(2024, 3, 1), "tenure_end": None},
            ],
            "distribution": {
                "target_audience": ["shareholders", "analysts", "regulators"],
                "regions": ["Malaysia", "ASEAN"],
            },
        },
    })

    # ── MYBank Niaga Annual Report 2023 ─────────────────────────────────
    reports.append({
        "title": "MYBank Niaga Annual Report 2023",
        "sections": [
            {
                "heading": "Board of Commissioners",
                "content": (
                    "The Board of Commissioners of PT MYBank Niaga Tbk comprises seven members, "
                    "including four independent commissioners, in compliance with Otoritas Jasa Keuangan "
                    "(OJK) Regulation No. 33/POJK.04/2014 on the Board of Directors and Board of "
                    "Commissioners of Public Companies. President Commissioner Dato' Ir. Ahmad Zulkifli "
                    "bin Zainal Abidin represents MYBank Group as the majority shareholder with a 96.1% "
                    "ownership stake.\n\n"
                    "President Director Ahmad Faisal has led MYBank Niaga since January 2020, driving "
                    "the bank's digital transformation and market share expansion. Under his leadership, "
                    "MYBank Niaga has strengthened its position as the fifth-largest private bank in "
                    "Indonesia by assets. The Board of Commissioners commends Ahmad Faisal's strategic "
                    "vision in positioning the bank for the opportunities presented by Indonesia's "
                    "rapidly growing digital economy."
                ),
            },
            {
                "heading": "Financial Highlights",
                "content": (
                    "PT MYBank Niaga Tbk recorded a net profit of IDR 7.82 trillion (approximately "
                    "RM2.34 billion) for the financial year ended 31 December 2023, a 15.8% increase "
                    "from IDR 6.75 trillion in 2022. Total assets grew 11.2% to IDR 342.1 trillion. "
                    "The bank's return on equity improved to 14.8% from 13.5% in the prior year.\n\n"
                    "Total loans and financing expanded 12.4% to IDR 231.6 trillion, driven by strong "
                    "growth in consumer and commercial banking. The bank's market share of system loans "
                    "increased to 4.2% from 3.9%. Customer deposits grew 9.8% to IDR 278.4 trillion, "
                    "with CASA ratio at 56.2%, among the highest in the Indonesian banking industry.\n\n"
                    "Net interest margin expanded to 5.12% from 4.89%, benefiting from a favourable "
                    "rate environment and improving asset yields. The cost-to-income ratio improved to "
                    "41.8%. The bank's capital adequacy ratio (CAR) stood at 22.4%, well above the "
                    "OJK minimum requirement of 8%. Non-performing loan (NPL) ratio improved to 1.8% "
                    "from 2.1% in the prior year."
                ),
            },
            {
                "heading": "President Director Message",
                "content": (
                    "Dear Shareholders,\n\n"
                    "MYBank Niaga delivered a strong performance in 2023, capitalising on Indonesia's "
                    "robust economic growth of 5.05% and the continued expansion of the country's "
                    "financial services sector. Our results demonstrate the success of our strategy "
                    "to build a leading digital bank in Indonesia while maintaining our strength in "
                    "traditional banking channels.\n\n"
                    "Our digital transformation programme, Niaga Digital Forward, achieved significant "
                    "milestones. Our mobile banking application, MYBank Niaga Mobile, surpassed 12 "
                    "million active users, processing over 850 million transactions during the year. "
                    "We launched our QRIS-based merchant payment solution, onboarding 180,000 merchants "
                    "across Java, Sumatra, and Kalimantan.\n\n"
                    "As a subsidiary of MYBank Group, we benefit from the Group's technology investments "
                    "and regional connectivity. During the year, we deepened our collaboration with "
                    "MYBank Group on cross-border trade finance and supply chain solutions, supporting "
                    "the growing trade corridor between Malaysia and Indonesia.\n\n"
                    "Ahmad Faisal\nPresident Director\nPT MYBank Niaga Tbk"
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank Niaga Annual Report 2023",
                "document_type": "annual_report",
                "entity": "MYBank Niaga",
                "published_date": datetime(2024, 4, 10),
                "fiscal_year": 2023,
                "version": "1.0",
                "status": "current",
                "superseded_by": None,
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": "MYBank Niaga Annual Report 2022",
                "related_documents": ["MYBank Group Annual Report 2023"],
                "amendment_history": [],
            },
            "approvals": [
                {"approver": "Dato' Ir. Ahmad Zulkifli bin Zainal Abidin", "role": "President Commissioner", "date": datetime(2024, 3, 28)},
                {"approver": "Ahmad Faisal", "role": "President Director", "date": datetime(2024, 3, 28)},
            ],
            "regulatory": {
                "bnm_circulars": [],
                "compliance_categories": ["corporate_governance", "financial_reporting"],
                "data_classification": "public",
            },
            "people_mentioned": [
                {"name": "Ahmad Faisal", "role": "President Director", "entity": "MYBank Niaga",
                 "tenure_start": datetime(2020, 1, 1), "tenure_end": None},
                {"name": "Dato' Ir. Ahmad Zulkifli bin Zainal Abidin", "role": "President Commissioner", "entity": "MYBank Niaga",
                 "tenure_start": datetime(2019, 6, 1), "tenure_end": None},
            ],
            "distribution": {
                "target_audience": ["shareholders", "analysts", "regulators"],
                "regions": ["Indonesia"],
            },
        },
    })

    # ── MYBank Thai Annual Report 2023 ──────────────────────────────────
    reports.append({
        "title": "MYBank Thai Annual Report 2023",
        "sections": [
            {
                "heading": "Board of Directors",
                "content": (
                    "The Board of Directors of MYBank Thai Public Company Limited comprises eleven "
                    "members, including five independent directors, in compliance with the Securities "
                    "and Exchange Commission (SEC) of Thailand's corporate governance code. Chairman "
                    "Khun Prasert Sitthisakulchai brings extensive experience in the Thai financial "
                    "services industry. MYBank Group holds a 94.8% ownership stake in MYBank Thai.\n\n"
                    "CEO Somchai Prasertsak was appointed in April 2019 and has led the bank through "
                    "a period of significant transformation. Under his leadership, MYBank Thai has "
                    "improved its return on equity from 7.2% to 11.8% over five years, reflecting the "
                    "success of cost optimisation initiatives and portfolio rebalancing towards higher-"
                    "yielding segments. The Board acknowledges CEO Somchai Prasertsak's leadership in "
                    "driving operational excellence across the organisation."
                ),
            },
            {
                "heading": "Financial Highlights",
                "content": (
                    "MYBank Thai recorded a net profit of THB 12.4 billion (approximately RM1.58 "
                    "billion) for the financial year ended 31 December 2023, a 9.6% increase from "
                    "THB 11.3 billion in 2022. Total assets grew 7.8% to THB 1,042 billion. The bank's "
                    "return on equity stood at 11.8%, the highest in five years.\n\n"
                    "Loans and financing expanded 8.1% to THB 724 billion, with retail and consumer "
                    "lending contributing 42% of the loan portfolio. Customer deposits grew 6.4% to "
                    "THB 832 billion. Net interest margin improved to 3.28% from 3.12%, reflecting "
                    "the Bank of Thailand's tightening cycle. The cost-to-income ratio improved to "
                    "43.6% from 45.2%.\n\n"
                    "Non-performing loan ratio improved to 2.4% from 2.8%, supported by proactive "
                    "portfolio management and strengthened credit underwriting. The bank's capital "
                    "adequacy ratio stood at 18.9%, well above the Bank of Thailand's minimum "
                    "requirement. The bank declared dividends of THB 6.2 billion."
                ),
            },
            {
                "heading": "CEO Message",
                "content": (
                    "Dear Shareholders,\n\n"
                    "MYBank Thai delivered a commendable performance in 2023, building on the "
                    "strategic initiatives we have implemented over the past four years. Thailand's "
                    "economy grew 1.9%, moderated by the slowdown in global trade and tourism "
                    "recovery, but the banking sector remained resilient.\n\n"
                    "Our digital banking strategy continues to drive customer acquisition and "
                    "engagement. Our mobile application, MYBank Thai GO, reached 4.8 million active "
                    "users, with digital transactions accounting for 72% of total transaction volume. "
                    "We launched a partnership with Grab Financial Thailand for digital lending to "
                    "gig economy workers, disbursing THB 2.1 billion in micro-loans during the year.\n\n"
                    "As part of the MYBank Group network, we leverage the Group's technology "
                    "platforms and cross-border capabilities. The Malaysia-Thailand QR payment "
                    "linkage, developed in collaboration with MYBank Group and Bank Negara Malaysia, "
                    "has facilitated over 500,000 cross-border retail transactions since its launch.\n\n"
                    "Somchai Prasertsak\nChief Executive Officer\nMYBank Thai Public Company Limited"
                ),
            },
        ],
        "metadata": {
            "source": {
                "document_title": "MYBank Thai Annual Report 2023",
                "document_type": "annual_report",
                "entity": "MYBank Thai",
                "published_date": datetime(2024, 4, 15),
                "fiscal_year": 2023,
                "version": "1.0",
                "status": "current",
                "superseded_by": None,
                "section": None,
                "page_range": None,
                "language": "en",
            },
            "lineage": {
                "supersedes_document": "MYBank Thai Annual Report 2022",
                "related_documents": ["MYBank Group Annual Report 2023"],
                "amendment_history": [],
            },
            "approvals": [
                {"approver": "Khun Prasert Sitthisakulchai", "role": "Chairman", "date": datetime(2024, 3, 30)},
                {"approver": "Somchai Prasertsak", "role": "CEO", "date": datetime(2024, 3, 30)},
            ],
            "regulatory": {
                "bnm_circulars": [],
                "compliance_categories": ["corporate_governance", "financial_reporting"],
                "data_classification": "public",
            },
            "people_mentioned": [
                {"name": "Somchai Prasertsak", "role": "CEO", "entity": "MYBank Thai",
                 "tenure_start": datetime(2019, 4, 1), "tenure_end": None},
                {"name": "Khun Prasert Sitthisakulchai", "role": "Chairman", "entity": "MYBank Thai",
                 "tenure_start": datetime(2018, 1, 1), "tenure_end": None},
            ],
            "distribution": {
                "target_audience": ["shareholders", "analysts", "regulators"],
                "regions": ["Thailand"],
            },
        },
    })

    return reports
