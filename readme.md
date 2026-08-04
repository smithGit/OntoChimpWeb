# OntoChimpWeb

AI-assisted ontology enhancement service.

## Purpose

This online version of OntoChimp, OntoChimpWeb, is an AI-assisted Ontology Enhancement Service that analyzes biomedical literature to identify candidate ontology classes that may be absent from, or inadequately represented in, a target ontology, while providing provenance and evidence for ontology curators.

## Technology

Development Backend:
- Python
- FastAPI
- SQLAlchemy (not sure where this is used...)
- MySQL
- Azure App Service (Linux)
- OpenRouter

Development Frontend:
(separate project not on this repository - development using Node and Typescript,
production planned for PHP implementation)
 
## Primary Operation
The user may specify three inputs:
A. Selection of up to three Large Language Models (LLM's), currently OpenAI GPT, Google Gemini, and Anthropic Claude. OpenRouter is used to access multiple models, and later additional models supported by OpenRouter will be validated with the system.
B. The prompt prefix desired, that specifies the domain of interest and any guidance the model should use. 
C. One or more reference documents uploaded as text files of up to 65kb.

The system will then build the full prompt, consisting of prefix, document text, and a fixed suffix specifying the JSON format required, and submit it to each of the LLM's selected, producing a list of key concept terms that the model deems significant.

**Primary Output**: A list of each term, for each model and each document.


## User Modes
Two modes of user operation are (will be) offered:
**Document Mode**: where the user works with a single document at a time, requiring no registration. The key concept terms identified are returned to the user as a .csv file, but no data is retained within the system other than the fact that the system was used. No user identification is needed.
**Project Mode**: for more serious ontology developments, where a project is registered and up to 12 documents may be processed at a time. Results will be retained on the system's MySQL database for ontology develop over a period of time.

## Status

August 4, 2026: Early proof-of-performance Prototype