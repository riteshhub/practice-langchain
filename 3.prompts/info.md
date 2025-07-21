## Prompt Template
A prompt template in LangChain is a reusable structure designed to generate prompts for language models. It works by defining a string template containing placeholders for dynamic values. When specific inputs are provided, these placeholders are filled in to produce a final prompt tailored for the model. This approach allows for consistent, reproducible, and flexible prompt generation across various use cases

`simple_template.py` Here we will learn how to make use of simple prompt templates.
`chat_template.py` In this you will learn how can we give a charater to LLM by assigning a role via **system** property in prompt template.
`chatbot_without_memory.py` We will learn how to build a very simple chatbot. Here you can observe that chatbot will not be able to memorize your conversation. For example:
```
You: which number is greater between 14 and 28.
AI: 28 is greater than 14
You: Multiply greater number by 2
AI: Please provide greater number so that I can multiply it by 2.
```
`chatbot_with_memory.py` Here we will learn on how can we overcome the limitation with memory by storing all the conversation in a list and everytime pass this list to LLM, so it can have a context and provide answers based on this. However, this is still not a complete solution in sense that by looking at the converstation history, one will not be able to understand, that which message is user message and which one is AI message.

`message_placeholeder.py`


## References
https://python.langchain.com/docs/concepts/prompt_templates/