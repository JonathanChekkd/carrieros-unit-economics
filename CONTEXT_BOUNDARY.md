# Context and confidentiality boundary

Maintainer: repository owner. Handling reviewed: 2026-10-22.

Implemented behavior is established by this repository's source and tests at an exact commit. Planning documents, reported results, generated indexes and graphs retain their own evidence status; none prove deployment or human acceptance. Organizational decisions belong in accepted, non-expired records in the [canonical company brain](https://github.com/carrieros-ai/carrieros-brain).

Cluster system-design information stays solely in the [private owning repository](https://github.com/carrieros-ai/carrier-os-cluster), including its same-repository branches and PRs. This repository may retain only that root locator and the handling rule. Do not ingest or export source excerpts, detailed design summaries, diagrams, embeddings, graphs or archives from it. Other private repositories are still outside that boundary. Use synthetic fixtures for checks.

Run `python3 scripts/check-context-boundary.py` before review. It rejects known restricted source/path locators and escaping tracked symlinks; it cannot detect every paraphrase or manual copy. Review content and archives separately. Historical copies, releases, caches and messages require separately scoped cleanup. Do not claim this check proves zero disclosure.

Git bundles are rejected here, including renamed bundles, because they can carry otherwise hidden repository history. Keep restricted recovery bundles in their private owning repository.
