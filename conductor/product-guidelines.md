# Product Guidelines: PyCaretAgent

## 1. Coding Standards
- **Python Version:** 3.12+ for modern feature support.
- **Import Style:** Use `google.adk` for SDK imports.
- **Type Hinting:** Mandatory for all tool and agent function signatures.
- **Docstrings:** Required for all public methods and agent tool definitions.

## 2. Agent Design
- **Single Responsibility:** Each sub-agent should handle one domain (e.g., Classification).
- **Tool Granularity:** Tools should be atomic wrappers around PyCaret functions.
- **Instruction Centralization:** Prompts must be stored in `pycaretagent/utils/instructions/`.

## 3. Data & State
- **DuckDB:** Primary engine for local analytical processing.
- **MLflow:** Used for all experiment logging and model tracking.
- **Configuration:** Managed via `.env` and `pycaretagent/utils/config.py`.

## 4. Quality Assurance
- **Automated Testing:** Pytest for unit and integration tests.
- **Validation:** Every agent change must be validated through reproduction scripts.
- **Linting:** Use `ruff` for fast linting and formatting.
