# Contributing

ResearchFabric welcomes focused improvements to its public architecture, philosophy, terminology, examples, and documentation tooling.

Before opening a change:

1. Keep English and Simplified-Chinese peers meaningfully aligned.
2. Preserve the Vault/Design Lab authority split and the portal's non-runtime role.
3. Do not import component source, private coordination records, research data, credentials, transcripts, or machine-specific paths.
4. Distinguish facts, proposals, evidence, and adopted decisions. Do not describe agent output as scientific evidence.
5. Avoid adding frameworks, middleware, submodules, or automation without a demonstrated public-portal need.
6. Run `python scripts/check_bilingual_docs.py`, `python -m py_compile scripts/check_bilingual_docs.py`, and `git diff --check`.

Prefer small pull requests with an explicit reason and updated bilingual peers. Component behavior changes belong in the relevant component repository.

