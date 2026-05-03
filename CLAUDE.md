# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
**LINE ChatGuard** is an AI-powered cybersecurity firewall for LINE users. It detects and prevents personal security threats through three primary engines:
- **File Scanner**: Dual-layer scanning using ClamAV (local) and VirusTotal (cloud).
- **Scam Detector**: NLP-based classification of scam messages using fine-tuned Transformer models (e.g., WangchanBERTa).
- **URL Analyzer**: ML-based phishing detection using lexical and domain features.

## Development Commands
- **Run Project**: `uv run python main.py` (Entry point for FastAPI)
- **Add Dependency**: `uv add <<<package>>>`
- **Run Python Shell**: `uv run python`
- **Update Dependencies**: `uv lock --upgrade`

## Architecture & Structure
The project is built with a modern Python 3.13+ stack managed by `uv`.

### Core Flow
1. **Webhook Gateway (FastAPI)**: Receives events from LINE, validates signatures, and routes events.
2. **Analysis Engines**: 
   - `app/line_api.py` currently handles the basic webhook response.
   - Future engines will reside in `scanners/` (File, Scam, URL).
3. **Response Engine**: Aggregates verdicts and sends alerts back to the user via LINE Messaging API.

### Directory Layout
- `app/`: Core application logic (webhook handling, API clients).
- `scanners/`: Security analysis implementations.
- `models/`: ML model training and inference scripts.
- `data/`: Datasets for training and evaluation.
- `storage/`: Runtime artifacts (quarantine, model weights, DB).
- `tests/`: Test suite for security engines.

## Tech Stack
- **Backend**: FastAPI, `line-bot-sdk` (v3), `python-dotenv`.
- **ML/NLP**: PyTorch, Hugging Face Transformers, PyThaiNLP, scikit-learn.
- **Security**: ClamAV (`pyclamd`), VirusTotal API (`vt-py`).
- **Environment**: Python 3.13, `uv` package manager.

## Key Constraints & Requirements
- **Signature Validation**: Every webhook request MUST be validated using the LINE Channel Secret.
- **Async First**: Use `asyncio` and FastAPI's async capabilities for non-blocking security scans.
- **Thai Language Support**: Primary focus is on Thai language scam detection (SOTA: WangchanBERTa).
