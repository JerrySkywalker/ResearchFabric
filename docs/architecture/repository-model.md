# Repository Model

A Lab can keep accepted Lean modules and draft proofs within its own repository. The Vault stores reviewed explanations and links to the exact source, declaration and revision. Reusable standalone libraries can be referenced as ordinary pinned dependencies.

Each repository has one durable role.

| Repository class | Owns | Does not own |
| --- | --- | --- |
| ResearchFabric | public architecture, philosophy, manifests, navigation | template source or runtime state |
| Research Vault Template | generic cross-project knowledge structure and workflows | project experiments or adopted project design |
| Research Design Lab Template | generic executable project-research structure and workflows | cross-project canonical knowledge |
| Specialized instances | their own knowledge or project state | template roadmap completion |
| Private pair coordination | roadmap, pair state, decisions, compact receipts | component source, smoke, assets |

There are no submodules, subtrees, source mirrors, or automatic synchronization. Template evolution is applied deliberately to instances. Repository commits establish traceability, while scientific validity depends on methods, evidence, review, and authority beyond Git.

