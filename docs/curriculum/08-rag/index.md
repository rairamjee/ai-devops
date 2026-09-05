# Phase 08 — RAG

> Retrieval-augmented generation: give a model your own documents, measure whether it actually uses them, and learn every way retrieval fails.

**Status:** 📋 planned · **Estimated effort:** 2 weeks · **Prerequisites:** Phases 00–07.

## Overview

```text
Documents → Chunking → Embeddings → Vector Database → Retrieval → Context → LLM → Answer
```

You will build that pipeline on PostgreSQL + pgvector. You will learn embeddings and similarity, chunking strategies and metadata, top-k retrieval, reranking and hybrid search, and, above all, evaluation: how to know when retrieval missed, when the model ignored the context, and when it hallucinated. Other vector databases are covered conceptually so you can evaluate them.

## Why a DevOps engineer needs this

RAG is the most common enterprise LLM architecture and it has a database at its heart. Ingestion pipelines, index freshness, query latency, embedding-model versioning and retrieval quality are operational concerns, and the assistant you build here is the knowledge base your agent (Phase 09) and capstone (Phase 17) search.

## Learning objectives

- Explain embeddings and vector similarity and compute one by hand for a tiny case.
- Chunk documents sensibly and attach metadata that supports filtering.
- Store and query vectors in pgvector, including index choice.
- Implement top-k retrieval, reranking and hybrid (keyword + vector) search.
- Evaluate retrieval quality and answer grounding; detect hallucination.
- Operate the pipeline: re-ingestion, embedding-model upgrades, index rebuilds.

## Lessons

| # | Lesson | Status |
|---|---|---|
| 01 | Why RAG: the problem it solves and what it does not solve | 📋 |
| 02 | Embeddings and similarity | 📋 |
| 03 | Chunking and metadata | 📋 |
| 04 | PostgreSQL + pgvector: storing, indexing and querying vectors | 📋 |
| 05 | Retrieval: top-k, reranking, hybrid search | 📋 |
| 06 | Evaluation: retrieval quality, grounding, hallucination | 📋 |

## Labs

| Lab | Difficulty | Environment | Status |
|---|---|---|---|
| 8.1 — Embed and compare sentences; visualise nearest neighbours | 🟢 | Local | 📋 |
| 8.2 — Ingest a runbook collection into pgvector; query it; break retrieval with bad chunking and fix it | 🟡 | Local, Docker | 📋 |
| 8.3 — Build an evaluation set and measure retrieval and grounding before and after reranking | 🟡 | Local, Docker | 📋 |

## Phase project — Project 4: DevOps Knowledge Assistant

A RAG assistant over your own runbooks and documentation, on pgvector, with an ingestion pipeline, hybrid search, reranking, an evaluation harness and full documentation. Deployed alongside Project 3.

## Assessment

- **Knowledge check:** 15 questions.
- **Practical:** add metadata filtering by environment (prod/staging) to the retriever.
- **Troubleshooting:** the answer is in the documents but the assistant says it does not know; diagnose.
- **Architecture:** design the re-ingestion strategy when the embedding model changes.
- **Interview:** why can retrieval fail, and how do you evaluate a RAG system?

## Checkpoint

Move on to [Phase 09 — AI Agents](../09-ai-agents/) when Project 4 answers questions from your runbooks, you can show its evaluation numbers, and you can explain three distinct ways retrieval fails.
