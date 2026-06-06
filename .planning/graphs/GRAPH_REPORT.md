# Graph Report - .  (2026-06-04)

## Corpus Check
- 279 files · ~375.543 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 8 nodes · 13 edges · 1 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output
- Edge kinds: contains: 7 · calls: 6


## Input Scope
- Requested: auto
- Resolved: committed (source: default-auto)
- Included files: 279 · Candidates: 351
- Excluded: 30 untracked · 3450 ignored · 0 sensitive · 2 missing committed
- Recommendation: Use --scope all or graphify.yaml inputs.corpus for a knowledge-base folder.

## Graph Freshness
- Built from Git commit: `efac086`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `gql()` - 7 edges
2. `get_organization_id()` - 2 edges
3. `create_teams()` - 2 edges
4. `create_labels()` - 2 edges
5. `create_projects()` - 2 edges
6. `get_existing_teams()` - 2 edges
7. `create_issues()` - 2 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities

### Community 0 - "Community 0"
Cohesion: 0.46
Nodes (7): create_issues(), create_labels(), create_projects(), create_teams(), get_existing_teams(), get_organization_id(), gql()

## Suggested Questions
_Not enough signal to generate questions. This usually means the corpus has no AMBIGUOUS edges, no bridge nodes, no INFERRED relationships, and all communities are tightly cohesive. Add more files or run with --mode deep to extract richer edges._