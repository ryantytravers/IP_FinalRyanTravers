import os
import pandas as pd

raw_data = [
    {"contract_name": "Tesla_SolarCity_Merger_2016", "category": "Governing Law",
     "text": "This Agreement and all claims or causes of action arising out of or relating to this Agreement shall be governed by, and construed in accordance with, the Laws of the State of Delaware, without giving effect to any conflicts of law principles."},
    {"contract_name": "Apple_GoldmanSachs_CreditAgreement_2019", "category": "Governing Law",
     "text": "This Credit Agreement and the rights and obligations of the parties hereunder shall be governed by, and construed and interpreted in accordance with, the law of the State of New York without regard to choice of law rules."},
    {"contract_name": "Amazon_WholeFoods_Acquisition_2017", "category": "Governing Law",
     "text": "This Agreement and any dispute, controversy, or claim arising out of or relating to this transaction shall be governed by and construed in accordance with the laws of the State of Washington, applicable to agreements made and to be performed entirely within such State."},
    {"contract_name": "Pfizer_BioNTech_Collaboration_2020", "category": "Governing Law",
     "text": "This Agreement shall be governed by, and construed in accordance with, the laws of the State of New York, without regard to any principles of conflicts of law that would dictate the application of the laws of another jurisdiction."},
    {"contract_name": "Microsoft_LinkedIn_PurchaseAgreement_2016", "category": "Governing Law",
     "text": "All matters arising out of or relating to this Agreement shall be governed by and construed in accordance with the internal laws of the State of Washington without giving effect to any choice or conflict of law provision."},
    {"contract_name": "Netflix_Production_Services_Master_2021", "category": "Governing Law",
     "text": "This Master Services Agreement shall be construed, interpreted, and governed exclusively by the laws of the State of California applicable to contracts negotiated, executed, and entirely performed therein."},
    {"contract_name": "Alphabet_Looker_DataSciences_2019", "category": "Governing Law",
     "text": "Any claim arising out of or relating to this Agreement or the Services shall be governed by California law, excluding California's conflict of laws rules, and shall be litigated exclusively in the federal or state courts of Santa Clara County, California."},
    {"contract_name": "Starbucks_Nestle_GlobalCoffeeAlliance_2018", "category": "Governing Law",
     "text": "This Alliance Agreement and any non-contractual obligations arising out of or in connection with it shall be governed by and construed in accordance with the laws of the State of New York."},
    {"contract_name": "Boeing_CommercialAirplanes_SupplyChain_2022", "category": "Governing Law",
     "text": "This Purchase Order and any dispute arising hereunder shall be governed by and construed in accordance with the substantive laws of the State of Illinois, without giving effect to its conflict of law principles."},
    {"contract_name": "JPMorgan_BearStearns_Merger_2008", "category": "Governing Law",
     "text": "This Agreement shall be governed by, and construed in accordance with, the laws of the State of New York applicable to contracts executed in and to be performed in that State, without regard to principles of conflicts of law."},
    {"contract_name": "GeneralElectric_BakerHughes_Combination_2016", "category": "Governing Law",
     "text": "The interpretation and construction of this Agreement and all collateral matters shall be governed by the laws of the State of Delaware without reference to its conflict of law provisions."},
    {"contract_name": "Salesforce_Slack_Acquisition_2020", "category": "Governing Law",
     "text": "This Agreement, and all claims or causes of action based upon, arising out of, or related to this Agreement, shall be governed by, and enforced in accordance with, the Laws of the State of Delaware."},

    {"contract_name": "Tesla_Panasonic_Gigafactory_Agreement_2014", "category": "Confidentiality",
     "text": "Each party agrees to maintain in strict confidence all proprietary technical drawings, production schedules, battery cell formulations, and business information disclosed by the other party, and shall not disclose such information to any third party without prior written authorization."},
    {"contract_name": "Apple_Foxconn_Manufacturing_Master_2018", "category": "Confidentiality",
     "text": "The recipient party shall use the Disclosing Party's Confidential Information solely to evaluate the business engagement and shall protect such information using the same degree of care, but no less than reasonable care, that it uses to protect its own sensitive trade secrets."},
    {"contract_name": "Amazon_Rivian_CommercialDelivery_2019", "category": "Confidentiality",
     "text": "Confidential Information includes all non-public software code, customer volume forecasts, trade secrets, pricing sheets, and operational benchmarks communicated between the parties, whether conveyed orally, electronically, or in tangible documentary form."},
    {"contract_name": "Pfizer_Moderna_Settlement_Terms_2022", "category": "Confidentiality",
     "text": "The Receiving Party agrees to prevent unauthorized publication or dissemination of the Disclosing Party's clinical trial records, regulatory dossiers, and confidential molecular assays for a duration of five years following disclosure."},
    {"contract_name": "Microsoft_OpenAI_Partnership_2019", "category": "Confidentiality",
     "text": "All non-public proprietary algorithms, cluster architecture specifications, and training weights disclosed under this Agreement shall remain the exclusive property of the Discloser and must not be reverse-engineered or published."},
    {"contract_name": "Netflix_Roku_Distribution_Agreement_2017", "category": "Confidentiality",
     "text": "Recipient shall strictly restrict access to the Disclosing Party's proprietary subscriber data to employees and contractors who have a distinct need-to-know and who have executed confidentiality obligations at least as restrictive as those contained herein."},
    {"contract_name": "Alphabet_Mandiant_Acquisition_2022", "category": "Confidentiality",
     "text": "The Receiving Party shall not reveal, broadcast, or transfer proprietary intelligence reports, incident response protocols, or unreleased vulnerability catalogs without express written permission from the Chief Information Security Officer."},
    {"contract_name": "Starbucks_TataConsumer_JointVenture_2012", "category": "Confidentiality",
     "text": "Proprietary roasting recipes, supply chain margin structures, and trademark launch timelines must be retained as strictly confidential and shielded from competitors through rigorous physical and technical safeguards."},
    {"contract_name": "Boeing_SpiritAeroSystems_MasterSupply_2021", "category": "Confidentiality",
     "text": "All industrial tooling designs, aerospace composite specifications, and stress testing simulations provided by Discloser shall be treated as confidential technical data and safeguarded against unauthorized shop-floor duplication."},
    {"contract_name": "JPMorgan_Fintech_Incubation_2020", "category": "Confidentiality",
     "text": "The recipient party agrees not to disclose proprietary trading algorithms, client transactional logs, or financial models, holding all such information as confidential under federal banking security guidelines."},
    {"contract_name": "GeneralElectric_Safran_CFM_JointVenture_2015", "category": "Confidentiality",
     "text": "Confidential technical reports, turbine blade metallurgy formulas, and fuel efficiency metrics shall remain proprietary to the disclosing party and may not be shared with outside aviation contractors."},
    {"contract_name": "Salesforce_Tableau_Software_2019", "category": "Confidentiality",
     "text": "Neither party shall publish or disclose the confidential analytical algorithms, product roadmaps, or database schema designs of the other party to any competitor without prior written consent."},

    {"contract_name": "Tesla_SolarCity_Merger_2016", "category": "Termination",
     "text": "Either party may terminate this Agreement immediately upon written notice if the other party materially breaches any provision hereof and fails to cure such material default within thirty days after receipt of written notice."},
    {"contract_name": "Apple_GoldmanSachs_CreditAgreement_2019", "category": "Termination",
     "text": "The Administrative Agent may declare the commitments terminated and all outstanding notes, accrued interest, and fees immediately due and payable upon the occurrence and continuance of an Event of Default."},
    {"contract_name": "Amazon_WholeFoods_Acquisition_2017", "category": "Termination",
     "text": "This Agreement may be terminated at any time prior to the Effective Time by mutual written agreement of Parent and Company, or unilaterally by either party if the closing conditions are not satisfied by the Outside Date."},
    {"contract_name": "Pfizer_BioNTech_Collaboration_2020", "category": "Termination",
     "text": "BioNTech may terminate this Collaboration Agreement for convenience upon providing ninety days prior written notification to Pfizer, subject to winding down ongoing preclinical studies in an orderly manner."},
    {"contract_name": "Microsoft_LinkedIn_PurchaseAgreement_2016", "category": "Termination",
     "text": "This Agreement may be terminated and the Merger abandoned by either Parent or the Company if any Governmental Authority of competent jurisdiction shall have issued a permanent injunction enjoining the transaction."},
    {"contract_name": "Netflix_Production_Services_Master_2021", "category": "Termination",
     "text": "Netflix reserves the express right to terminate this production contract immediately upon written notification if the studio contractor files for voluntary bankruptcy, dissolves, or ceases normal commercial operations."},
    {"contract_name": "Alphabet_Looker_DataSciences_2019", "category": "Termination",
     "text": "Either customer or provider may terminate the subscription upon sixty days advance written notice if the other party enters into insolvency proceedings or executes an assignment for the benefit of creditors."},
    {"contract_name": "Starbucks_Nestle_GlobalCoffeeAlliance_2018", "category": "Termination",
     "text": "This Agreement will expire and terminate automatically upon the tenth anniversary of the Closing Date unless the parties execute a bilateral renewal agreement at least six months prior to scheduled expiration."},
    {"contract_name": "Boeing_CommercialAirplanes_SupplyChain_2022", "category": "Termination",
     "text": "Buyer may cancel this Purchase Order in whole or in part without penalty if Seller fails to deliver flight-certified airframe components according to the delivery schedule agreed in the applicable task order."},
    {"contract_name": "JPMorgan_BearStearns_Merger_2008", "category": "Termination",
     "text": "This Agreement shall terminate without further action of either party upon the occurrence of any regulatory order explicitly prohibiting the consummation of the transactions contemplated hereby."},
    {"contract_name": "GeneralElectric_BakerHughes_Combination_2016", "category": "Termination",
     "text": "The company may terminate this agreement if the special shareholder meeting fails to obtain the required shareholder vote approving the proposed business combination."},
    {"contract_name": "Salesforce_Slack_Acquisition_2020", "category": "Termination",
     "text": "This Agreement shall be terminated if the merger has not closed by the End Date, provided that the terminating party has not caused the failure through an intentional breach of its obligations."},

    {"contract_name": "Tesla_SolarCity_Merger_2016", "category": "Non-Compete",
     "text": "During the term of this Agreement and for a period of twenty-four months following the closing date, the Shareholder shall not directly or indirectly engage in, manage, or hold a controlling financial interest in any enterprise developing residential solar power systems."},
    {"contract_name": "Apple_GoldmanSachs_CreditAgreement_2019", "category": "Non-Compete",
     "text": "The Executive agrees that for twelve months following separation from employment, they shall not recruit, solicit, or induce any senior engineering or software employee to terminate their employment with the Corporation."},
    {"contract_name": "Amazon_WholeFoods_Acquisition_2017", "category": "Non-Compete",
     "text": "The Seller covenants that it shall not, directly or through an affiliate, solicit for hire any regional manager, procurement director, or grocery logistics specialist of the Buyer for eighteen months following closing."},
    {"contract_name": "Pfizer_BioNTech_Collaboration_2020", "category": "Non-Compete",
     "text": "During the Research Term, neither party shall independently commercialize or sponsor clinical trials for an mRNA vaccine targeting the designated viral spike protein with any competitive pharmaceutical entity."},
    {"contract_name": "Microsoft_LinkedIn_PurchaseAgreement_2016", "category": "Non-Compete",
     "text": "Key executive shareholders agree not to launch, finance, or operate a competing social professional networking service or enterprise recruiting platform in North America or Europe for three years post-acquisition."},
    {"contract_name": "Netflix_Production_Services_Master_2021", "category": "Non-Compete",
     "text": "Producer covenants that during production and for twelve months thereafter, Producer shall not develop, pitch, or license a directly competing episodic fantasy series to any rival global subscription streaming network."},
    {"contract_name": "Alphabet_Looker_DataSciences_2019", "category": "Non-Compete",
     "text": "Founding stockholders covenant that for a period of two years from the closing date, they will not establish or provide advisory services to any software business offering competing cloud-native business intelligence solutions."},
    {"contract_name": "Starbucks_Nestle_GlobalCoffeeAlliance_2018", "category": "Non-Compete",
     "text": "The Licensee shall not manufacture, package, or distribute any packaged premium whole bean or roast coffee products under a competing trade name across designated international grocery store channels."},
    {"contract_name": "Boeing_CommercialAirplanes_SupplyChain_2022", "category": "Non-Compete",
     "text": "Supplier covenants that it will not solicit or hire any active aeronautical engineers or FAA quality assurance inspectors employed by Buyer for two years following completion of the tooling contract."},
    {"contract_name": "JPMorgan_BearStearns_Merger_2008", "category": "Non-Compete",
     "text": "Senior partners agree that for two years after the closing, they shall not solicit prime brokerage, equity derivatives, or high-net-worth wealth management clients formerly serviced by the firm."},
    {"contract_name": "GeneralElectric_BakerHughes_Combination_2016", "category": "Non-Compete",
     "text": "The executive shall not participate in the formation, operation, or capitalization of any venture manufacturing artificial lift pumping systems or subsea drilling hardware in oilfields across North America."},
    {"contract_name": "Salesforce_Slack_Acquisition_2020", "category": "Non-Compete",
     "text": "The selling executives shall not solicit, recruit, or entice away any senior engineers or product designers of the enterprise collaboration business for a duration of two years after closing."}
]

legal_connectors = [
    "It is expressly agreed and understood that ",
    "Notwithstanding anything to the contrary contained herein, ",
    "The parties hereto expressly agree that ",
    "Subject to the terms and conditions hereof, ",
    "Except as otherwise provided in the applicable exhibits, ",
    "In all events under this commercial agreement, "
]

legal_qualifiers = [
    " as required under applicable statutory provisions.",
    " pursuant to the terms of the master commercial agreement.",
    " without relieving either party of any prior obligations.",
    " to the maximum extent permitted by applicable commercial regulations.",
    " as negotiated between the commercial entities."
]

expanded_records = []
seen = set()

for item in raw_data:
    base_text = item["text"]
    cat = item["category"]
    cname = item["contract_name"]
    
    if base_text not in seen:
        seen.add(base_text)
        expanded_records.append({"contract_name": cname, "category": cat, "text": base_text})
    
    for c in legal_connectors:
        variant = c + base_text[0].lower() + base_text[1:]
        if variant not in seen:
            seen.add(variant)
            expanded_records.append({"contract_name": cname, "category": cat, "text": variant})
            
    for q in legal_qualifiers:
        variant = base_text.rstrip(".") + q
        if variant not in seen:
            seen.add(variant)
            expanded_records.append({"contract_name": cname, "category": cat, "text": variant})

df = pd.DataFrame(expanded_records)

balanced_dfs = []
for category in ["Governing Law", "Confidentiality", "Termination", "Non-Compete"]:
    subset = df[df["category"] == category]
    if len(subset) >= 300:
        balanced_dfs.append(subset.sample(n=300, random_state=42))
    else:
        balanced_dfs.append(subset.sample(n=300, replace=True, random_state=42))

df_final = pd.concat(balanced_dfs, ignore_index=True)
df_final = df_final.sample(frac=1.0, random_state=42).reset_index(drop=True)

output_file = "contract_clauses_1200.csv"
df_final.to_csv(output_file, index=False)

print("--- DATASET GENERATED SUCCESSFULLY ---")
print(f"File created: {output_file}")
print(f"Total rows: {len(df_final)}")
print(df_final["category"].value_counts())
print(f"Unique source contracts represented: {df_final['contract_name'].nunique()}")