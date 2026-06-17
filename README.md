# Gemini DevOps Guardrails 🚀🛡️

An automated, AI-powered DevSecOps security gate built using Google **Gemini 2.5** and **GitHub Actions** to scan Terraform Infrastructure as Code (IaC) for cloud security vulnerabilities before deployment.

## 🌟 Key Features
- **Structured Output Parsing:** Uses Gemini's strict JSON schema mode to enforce predictable PASS/FAIL responses.
- **Automated Gatekeeping:** Automatically blocks GitHub Actions CI/CD pipelines if critical security flaws are detected.
- **Zero Human Intervention:** Evaluates code risks and provides detailed remediation logic without manual peer review.

## 🛠️ Architecture
1. Developer pushes a `.tf` file change to the repository.
2. GitHub Actions runner executes a customized Python auditor script.
3. The script passes the raw IaC configurations to the Gemini API with strict system guardrails.
4. Gemini analyzes the risks, and responses are returned as structured JSON data.
5. Pipeline exits with `status 1` (Block) or `status 0` (Proceed) based on the AI evaluation.

## 📁 Repository Structure
- `.github/workflows/`: CI/CD automation pipeline.
- `src/guard.py`: Core AI integration script utilizing Google GenAI SDK.
- `terraform/`: Sandbox folder containing infrastructure code.

## 🚀 How to Set Up
1. Clone this repository.
2. Add your `GEMINI_API_KEY` as a GitHub Secret in your repository settings.
3. Push changes to `terraform/main.tf` to see the automated security gate in action!

---
Developed by **[Vikram Kanoujiya]** - Empowering DevOps with Agentic AI Systems.