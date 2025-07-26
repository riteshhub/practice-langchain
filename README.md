# practice-langchain

A playground for experimenting with [LangChain](https://python.langchain.com/) and various LLM integrations, including Google Gemini, HuggingFace, and open-source models.

## Features

- **Model Integrations:**  
  - Google Gemini ([`1.models/3.google_model.py`](1.models/3.google_model.py))
  - HuggingFace ([`1.models/2.hugging_face_model.py`](1.models/2.hugging_face_model.py))
  - Open Source (Ollama) ([`1.models/1.open_source_model.py`](1.models/1.open_source_model.py))

- **Output Parsing:**  
  - String output ([`2.parsers/2.string_parser.py`](2.parsers/2.string_parser.py))
  - Pydantic output ([`2.parsers/3.pydantic_parser.py`](2.parsers/3.pydantic_parser.py))
  - Structured output ([`2.parsers/1.structured_output.py`](2.parsers/1.structured_output.py))

- **Prompt Templates:**  
  - Examples in [`3.prompts/`](3.prompts/info.md)

- **Runnables:**  
  - Chains and workflows in [`5.runnables/`](5.runnables/info.md)

- **RAG:**  
  - Retrieval-Augmented Generation examples in [`4.rag/`](4.rag/info.md)

- **Tools & Agents:**  
  - Custom tools and agent examples in [`6.tools/`](6.tools/info.md) and [`7.agents/`](7.agents/info.md)

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
    cd practice-langchain
    ```
2. Install UV from PyPI
    ```sh
    pip install uv
    ```
3. Install dependencies:
    ```sh
    uv sync
    ```

4. Set up environment variables in [.env](.env) as needed.

### Running Examples

Each script in the numbered directories can be run directly, for example:

```sh
python 1.models/3.google_model.py
python 2.parsers/2.string_parser.py
```

## Project Structure

```
practice_langchain/
│
├── main.py
├── 1.models/
├── 2.parsers/
├── 3.prompts/
├── 4.rag/
├── 5.runnables/
├── 6.tools/
├── 7.agents/
├── .env
├── pyproject.toml
└── README.md
```

- **1.models/**: LLM integrations
- **2.parsers/**: Output parsing examples
- **3.prompts/**: Prompt templates
- **4.rag/**: Retrieval-Augmented Generation examples
- **5.runnables/**: Chains/workflows
- **6.tools/**: Custom and built-in tools
- **7.agents/**: Agent systems and examples

## References

- [LangChain Documentation](https://python.langchain.com/)
- [LangChain Google GenAI](https://python.langchain.com/docs/integrations/chat/google_genai)
- [LangChain HuggingFace](https://python.langchain.com/docs/integrations/chat/huggingface)
- [LangChain Ollama](https://python.langchain.com/docs/integrations/chat/ollama)