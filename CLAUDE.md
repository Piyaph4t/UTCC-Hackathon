# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
AI model development for Cybersecurity, specifically focusing on **Personal Security**. The goal is to detect, prevent, and manage threats.

## Development Commands
- **Run Project**: `uv run python main.py`
- **Add Dependency**: `uv add <<package>>`
- **Run Python Shell**: `uv run python`
- **Update Dependencies**: `uv lock --upgrade`

## Architecture & Structure
The project uses a modern Python 3.13+ setup managed by `uv`.
- **Environment**: Managed via `pyproject.toml` and `uv.lock`.
- **NLP Stack**: Integrated with PyTorch, Hugging Face Transformers, spaCy, and NLTK for threat detection and analysis.
- **Current State**: Initial skeleton with `main.py` as the entry point.
