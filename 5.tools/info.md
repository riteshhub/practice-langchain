## Tools
Tools are a Python function with a schema that defines the function's name, description and expected arguments.
Tools can be passed to LLM models that support tool calling allowing the model to request the execution of a specific function with specific inputs.

There are 2 ways to interact with tools in langchain.
1. Create Custom tool
2. Use Built-in tools

### Ways to create custom tools
* Using @tool decorator
* Using StructuredTool class
* Using BaseTool class

There are other ways but not recommended anymore.

### Built-in tools
LangChain provides a range of built-in tools that are ready-to-use functions or integrations designed to be called by large language models (LLMs). These tools enable common functionalities—such as web search, calculations, or API interactions—without requiring custom development for every task.

## References
https://python.langchain.com/docs/integrations/tools/