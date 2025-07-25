## Agents
An AI Agent is an intelligent system that receives a high level goal from a user and AUTONOMOUSLY plans, decides and execute a sequence of actions by using external tools, APIs or knowledge sources, all while maintaining context, reasoning over multiple steps adapting to new information and optimizing for the intended outcome.

**Agent** = **LLM** *(Language Understanding and Reasoning)* + **Tools** *(APIs, External tools, Knowledge Base)*

### Characteristics of Agent System
* Goal Driven -> just mention what you want not how to do it.
* Autonomous Planning -> it breaks down problem and arrange tasks on its own.
* Tool Usage -> knows when to use which tools from the list of provided tools.
* Context Aware -> maintains conversation history across steps
* Adaptive -> Rethinks or adjust plans when things change (eg:- API not responding)

### Design Patterns
**React** -> It is a design pattern used in AI agents that stands for *Reasoning + Action*. It allows LLM to combine internal reasoning *(Thought)* with external actions *(Tools)* in a structured, multi step process.
It loops through below until reached final answer
- THOUGHT       : what is the goal
- ACTION        : how to fullfill it
- OBSERVATION   : response from llm

🔔 There are other patterns as well but ReAct is the most used one

## References
https://python.langchain.com/api_reference/core/agents.html
