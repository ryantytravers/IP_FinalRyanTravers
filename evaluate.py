import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, f1_score

CATEGORIES = ["Confidentiality", "Termination", "Governing Law", "Non-Compete"]

train_data = [
    ("Tesla_SolarCity_2016", "Governing Law", "This Agreement and all claims arising out of it shall be governed by Delaware law without giving effect to conflict of laws principles."),
    ("Apple_Goldman_2019", "Governing Law", "This Credit Agreement shall be governed by, and construed and interpreted in accordance with, the law of the State of New York."),
    ("Amazon_WholeFoods_2017", "Governing Law", "This transaction shall be governed by and construed in accordance with the laws of the State of Washington applicable to contracts entered into therein."),
    ("Pfizer_BioNTech_2020", "Governing Law", "This Agreement shall be construed in accordance with the substantive laws of the State of New York, excluding its choice of law rules."),
    ("Netflix_Production_2021", "Governing Law", "This Agreement is executed under and shall be governed by California law, and any dispute shall be brought in Los Angeles County."),
    ("Alphabet_Looker_2019", "Governing Law", "Any claim arising out of or relating to this Agreement shall be governed by California law and litigated in Santa Clara County."),
    ("Boeing_Spirit_2021", "Governing Law", "All claims shall be governed by the laws of Illinois, without giving effect to any choice of law rules that would result in the application of another state's laws."),
    ("Starbucks_Nestle_2018", "Governing Law", "The construction, validity and performance of this Agreement shall be governed in all respects by English law."),

    ("Tesla_SolarCity_2016", "Confidentiality", "Each party agrees to maintain in strict confidence all proprietary technical drawings, formulations, and business plans disclosed by the other party."),
    ("Apple_Goldman_2019", "Confidentiality", "The recipient shall use Confidential Information solely to evaluate the business engagement and shall protect such information using reasonable care."),
    ("Amazon_WholeFoods_2017", "Confidentiality", "Confidential Information includes all non-public software code, customer volume forecasts, trade secrets, and operational benchmarks."),
    ("Pfizer_BioNTech_2020", "Confidentiality", "The Receiving Party agrees to prevent unauthorized publication or dissemination of clinical trial records and regulatory dossiers for five years."),
    ("Netflix_Production_2021", "Confidentiality", "Recipient shall strictly restrict access to proprietary subscriber records to employees who have a distinct need to know."),
    ("Alphabet_Looker_2019", "Confidentiality", "The Receiving Party shall not reveal or transfer proprietary intelligence reports or security vulnerability catalogs without written consent."),
    ("Boeing_Spirit_2021", "Confidentiality", "All industrial tooling designs, aerospace composite specifications, and stress testing simulations shall be treated as confidential technical data."),
    ("Starbucks_Nestle_2018", "Confidentiality", "Proprietary roasting recipes and trademark launch timelines must be retained as strictly confidential and shielded from competitors."),

    ("Tesla_SolarCity_2016", "Termination", "Either party may terminate this Agreement immediately upon written notice if the other party materially breaches any provision hereof and fails to cure."),
    ("Apple_Goldman_2019", "Termination", "The Administrative Agent may declare the commitments terminated and all outstanding notes immediately due upon an Event of Default."),
    ("Amazon_WholeFoods_2017", "Termination", "This Agreement may be terminated prior to the Effective Time by mutual agreement, or unilaterally if conditions are not satisfied by the Outside Date."),
    ("Pfizer_BioNTech_2020", "Termination", "BioNTech may terminate this Collaboration Agreement for convenience upon providing ninety days prior written notification to Pfizer."),
    ("Netflix_Production_2021", "Termination", "Netflix reserves the express right to terminate this contract immediately upon notice if contractor dissolves or ceases commercial operations."),
    ("Alphabet_Looker_2019", "Termination", "Either customer or provider may terminate the subscription upon sixty days notice if the other party enters into insolvency proceedings."),
    ("Boeing_Spirit_2021", "Termination", "Buyer may cancel this Purchase Order without penalty if Seller fails to deliver flight-certified airframe components according to schedule."),
    ("Starbucks_Nestle_2018", "Termination", "This Agreement will expire automatically upon the tenth anniversary of the Closing Date unless the parties execute a bilateral renewal."),

    ("Tesla_SolarCity_2016", "Non-Compete", "During the term and for twenty-four months after closing, Shareholder shall not directly engage in any enterprise developing residential solar power."),
    ("Apple_Goldman_2019", "Non-Compete", "The Executive agrees that for twelve months following separation, they shall not recruit or solicit any senior engineering employee."),
    ("Amazon_WholeFoods_2017", "Non-Compete", "The Seller covenants that it shall not solicit for hire any regional manager or grocery procurement specialist of Buyer for eighteen months."),
    ("Pfizer_BioNTech_2020", "Non-Compete", "During the Research Term, neither party shall independently commercialize an mRNA vaccine targeting the designated viral spike protein with any competitor."),
    ("Netflix_Production_2021", "Non-Compete", "Producer covenants that during production and for twelve months thereafter, Producer shall not develop a competing fantasy series for another network."),
    ("Alphabet_Looker_2019", "Non-Compete", "Founding stockholders covenant that for two years from closing, they will not establish any business offering competing cloud business intelligence."),
    ("Boeing_Spirit_2021", "Non-Compete", "Supplier covenants that it will not solicit or hire any active aeronautical engineers or quality assurance inspectors employed by Buyer."),
    ("Starbucks_Nestle_2018", "Non-Compete", "The Licensee shall not manufacture or distribute any packaged roast coffee products under a competing trade name in designated grocery channels.")
]

test_data = [
    ("Chevron_Hess_2023", "Governing Law", "All disputes arising hereunder shall be resolved pursuant to the laws of Texas without regard to choice of law rules."),
    ("JPMorgan_BearStearns_2008", "Governing Law", "This Agreement shall be construed in accordance with the internal laws of the State of New York, without regard to conflict principles."),
    ("Salesforce_Slack_2020", "Governing Law", "The substantive legal provisions of the State of Delaware apply exclusively to any controversy arising from this transaction."),
    ("Meta_Oculus_2014", "Governing Law", "Litigation concerning this agreement must be submitted to the jurisdiction of courts in San Mateo County under California jurisprudence."),

    ("Cisco_Splunk_2023", "Confidentiality", "Customer telemetry feeds, cybersecurity alerts, and uncompiled SIEM parser scripts disclosed hereunder shall remain proprietary trade secrets."),
    ("JPMorgan_BearStearns_2008", "Confidentiality", "The recipient party agrees not to disclose proprietary trading algorithms or client transactional logs under federal banking guidelines."),
    ("Salesforce_Slack_2020", "Confidentiality", "Neither party shall publish or disclose the analytical algorithms, product roadmaps, or database schemas of the other."),
    ("Meta_Oculus_2014", "Confidentiality", "All firmware specifications, tracking sensor algorithms, and optical designs disclosed under this agreement constitute Discloser trade secrets."),

    ("Adobe_Figma_2022", "Termination", "Either party may abandon this merger transaction if antitrust regulatory clearance is not secured before the termination long-stop date."),
    ("Exxon_Pioneer_2023", "Termination", "Failure to deliver certified title opinions prior to closing shall entitle the acquiring entity to terminate this acquisition agreement."),
    ("JPMorgan_BearStearns_2008", "Termination", "This Agreement shall terminate without further action upon any regulatory order explicitly prohibiting the consummation of the transactions."),
    ("Meta_Oculus_2014", "Termination", "In the event of an incurable breach of representations or warranties, the non-breaching entity may terminate this arrangement immediately."),

    ("Broadcom_VMware_2022", "Non-Compete", "Key virtualization architects covenant not to render software hypervisor consulting services to competing cloud vendors for eighteen months."),
    ("Qualcomm_NUVIA_2021", "Non-Compete", "Processor design personnel agree not to assist third-party entities in architectural development of custom ARM-compatible server cores."),
    ("JPMorgan_BearStearns_2008", "Non-Compete", "Senior partners agree that for two years after closing, they shall not solicit prime brokerage or high-net-worth wealth management clients."),
    ("Salesforce_Slack_2020", "Non-Compete", "Upon conclusion of the transaction, founder covenants to refrain from commercial activities that diminish enterprise market valuation."),
    ("GeneralElectric_Baker_2016", "Termination", "Upon expiration of the cure period without resolution, the aggrieved entity reserves the right to conclude all contractual engagements and enforce immediate settlement of outstanding proprietary obligations.")
]

train_records = []
for cid, cat, txt in train_data:
    for i in range(30):
        train_records.append((f"{cid}_train_{i}", cat, txt))

test_records = []
for cid, cat, txt in test_data:
    for i in range(14):
        test_records.append((f"{cid}_test_{i}", cat, txt))

train_df = pd.DataFrame(train_records, columns=["contract_name", "category", "text"])
test_df = pd.DataFrame(test_records, columns=["contract_name", "category", "text"])

X_train = train_df["text"].values
y_train = train_df["category"].values
X_test = test_df["text"].values
y_test = test_df["category"].values

def keyword_baseline_predict(text):
    t = text.lower()
    scores = {
        "Governing Law": 0,
        "Confidentiality": 0,
        "Termination": 0,
        "Non-Compete": 0
    }
    gov_words = ["governed by", "laws of", "jurisdiction", "conflicts of law", "courts of"]
    conf_words = ["confidential", "proprietary", "trade secret", "non-disclosure", "disclose"]
    term_words = ["terminate", "termination", "cure", "event of default", "cancel", "expiration"]
    comp_words = ["non-compete", "solicit", "competing", "restric", "recruit", "covenant"]

    for w in gov_words:
        if w in t:
            scores["Governing Law"] += 1
    for w in conf_words:
        if w in t:
            scores["Confidentiality"] += 1
    for w in term_words:
        if w in t:
            scores["Termination"] += 1
    for w in comp_words:
        if w in t:
            scores["Non-Compete"] += 1

    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return "Unclassified"
    return best_cat

y_pred_baseline = [keyword_baseline_predict(t) for t in X_test]
base_acc = accuracy_score(y_test, y_pred_baseline)
base_f1 = f1_score(y_test, y_pred_baseline, labels=CATEGORIES, average="macro")

vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english", max_features=2500)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
    "Multinomial Naive Bayes": MultinomialNB(),
    "Linear SVM": LinearSVC(random_state=42)
}

results = [
    {"Model": "Rule-Based Baseline", "Accuracy": f"{base_acc * 100:.2f}%", "Macro F1": f"{base_f1:.4f}"}
]

trained_clfs = {}
for name, clf in models.items():
    clf.fit(X_train_vec, y_train)
    y_pred = clf.predict(X_test_vec)
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, labels=CATEGORIES, average="macro")
    results.append({"Model": name, "Accuracy": f"{acc * 100:.2f}%", "Macro F1": f"{f1:.4f}"})
    trained_clfs[name] = (clf, y_pred)

results_df = pd.DataFrame(results)
print(results_df.to_string(index=False))
print("\n--- EMPIRICAL FAILURE CASES ---")
lr_preds = trained_clfs["Logistic Regression"][1]
seen_failures = set()
for i in range(len(y_test)):
    if y_test[i] != lr_preds[i] and X_test[i] not in seen_failures:
        seen_failures.add(X_test[i])
        print(f"True Label:      {y_test[i]}")
        print(f"Model Predicted: {lr_preds[i]}")
        print(f"Clause Text:     \"{X_test[i]}\"\n")