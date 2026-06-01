### Literature Review Agent

A **multi-agent system** for **automated scientific literature synthesis** and **critical evaluation**. This tool enables researchers to perform structured, reproducible, and domain-specific analysis of biomedical literature.

---

### 🧠 Key Features
- **PubMed Article Search**: Query PubMed with customizable research questions to retrieve relevant articles.
- **Multi-Role AI Review Process**:
  - **Evidence Extractor**: Pulls key findings, methods, datasets, and limitations from abstracts.
  - **Skeptical Reviewer**: Challenges methodology, sample size, reproducibility, and overstated conclusions.
  - **Bioinformatics Specialist**: Evaluates pipelines, normalization, batch correction, and statistical methods.
  - **Translational Scientist**: Assesses practical impact, clinical relevance, industrial relevance, and implementation limitations.
  - **Synthesizer**: Combines all reviews into a coherent analysis with consensus findings, disagreements, confidence assessments, and actionable conclusions.
- **Structured Output**:
  - Consensus findings
  - Methodological disagreements
  - Confidence assessments
  - Actionable conclusions
  - Identified limitations

---

### 📌 Workflow
1. **Query PubMed** for articles matching your research question.
2. **Extract key findings** from abstracts using the evidence extractor.
3. **Conduct specialized reviews** by domain experts (skeptical, bioinformatics, translational).
4. **Synthesize results** into a structured, actionable analysis.

---

### 🧪 Use Cases
- **Rapid literature review** for research proposals or grant applications.
- **Critical evaluation** of methodology in published work.
- **Identification of research gaps** and areas for further investigation.
- **Support for reproducibility assessments** and experimental design.

---

### 🔄 Technology Stack
- **PubMed API** for article retrieval.
- **OpenAI (Ollama)** for multi-agent reasoning and natural language processing.
- **BioPython** for interacting with PubMed and extracting abstracts.

---

### 📌 How to Use
1. Install dependencies: `pip install biopython openai`
2. Run the agent: `python reviewers.py -q "Your research question here"`
3. Review the final synthesis in the terminal.

---

This tool combines **natural language processing** with **domain-specific expertise** to provide **structured, actionable insights** from scientific literature, enabling researchers to focus on high-impact analysis rather than manual review.
