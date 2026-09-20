# Architecture Overview

ResearchFabric separates durable research concerns so that each state has a clear authority.

```text
Bibliography authority (for example Zotero)     Durable large-asset authority
                    \                            /
                     references and identities
                              |
Research Vault Template <--- reviewed promotion ---> Research Design Lab Template
cross-project knowledge                              project execution and evidence
                              |
               humans authorize; agents assist
```

The public portal describes this relationship but does not sit in the execution path. Vault and Design Lab remain independent repositories with lockstep milestone versions. Exchange is explicit: a project can use reviewed knowledge and methods from the Vault; a reviewed project insight can be promoted back without copying its raw execution state.

The architecture uses Git for compact, reviewable state. Heavy outputs, bibliographic databases, managed attachments, and native tool stores remain external and are referenced through stable identities and provenance.

