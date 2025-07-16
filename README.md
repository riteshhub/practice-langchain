# practice-langchain

A playground for experimenting with [LangChain](https://python.langchain.com/) and various LLM integrations, including Google Gemini, HuggingFace, and open-source models.

## Features

- **Model Integrations:**  
  - Google Gemini ([`models/google_model.py`](models/google_model.py))
  - HuggingFace ([`models/hugging_face_model.py`](models/hugging_face_model.py))
  - Open Source (Ollama) ([`models/open_source_model.py`](models/open_source_model.py))

- **Output Parsing:**  
  - String output ([`parsers/string_parser.py`](parsers/string_parser.py))
  - Pydantic output ([`parsers/pydantic_parser.py`](parsers/pydantic_parser.py))
  - Structured output ([`parsers/structured_output.py`](parsers/structured_output.py))

- **Environment Management:**  
  Uses `.env` for API keys and configuration.

## Getting Started

### Prerequisites

- Python 3.12+
- API keys for Google Gemini, HuggingFace, etc. (set in `.env`)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/riteshhub/practice-langchain.git
    cd reusable-agents
    ```
2. Install UV from PyPI
    ```sh
    pip install uv
    ```
3. Install dependencies:
    ```sh
    uv sync
    ```

4. Set up environment variables in [.env](http://_vscodecontentref_/13) as needed.


### Running Examples

Each script in the `models/` and `parsers/` directories can be run directly:

```sh
python models/google_model.py
python parsers/string_parser.py
```

## Project Structure

```
practice_langchain/
│
├── main.py
├── models/
├── parsers/
├── prompts/
├── runnables/
├── .env
├── pyproject.toml
└── README.md
```

- **models/**: LLM integrations
- **parsers/**: Output parsing examples
- **prompts/**: Prompt templates (WIP)
- **runnables/**: (Reserved for chains/workflows)

## References

- [LangChain Documentation](https://python.langchain.com/)
- [LangChain Google GenAI](https://python.langchain.com/docs/integrations/chat/google_genai)
- [LangChain HuggingFace](https://python.langchain.com/docs/integrations/chat/huggingface)
- [LangChain Ollama](https://python.langchain.com/docs/integrations/chat/ollama)

---

> For more details, see the info files in [`models/info.md`](models/info.md)