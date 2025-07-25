## Runnables
A runnable in LangChain is a simple way to bundle tasks—like functions or language model calls—so you can connect them together into a sequence (called a chain) and run the whole set easily.

### In simple terms:

* Think of runnables as building blocks for your workflow.
* Each runnable represents one step, like calling a model or formatting text.
* You can link these steps together so that the result of one becomes the input for the next—just like connecting toy blocks.

### Why use runnables?

* They make it easy to connect different tasks in order, so you don’t have to manage each step manually.
* You can run one input at a time (invoke), process many at once (batch), or even handle streaming data (stream).
* Runnables support both normal and fast (async) execution, helping your workflow run efficiently.
* If you have an error or want to trace what happens, runnables provide built-in tools to help.

## Add Ons
use ```chain.get_graph().print_ascii()``` to see the flowchat for chains

## References
https://python.langchain.com/api_reference/core/runnables.html