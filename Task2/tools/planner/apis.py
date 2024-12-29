import os
from langchain.prompts import PromptTemplate # type: ignore
from Prompts.ReACT.prompts import planner_agent_prompt
from langchain.chat_models import ChatOpenAI # type: ignore
from langchain.schema import ( # type: ignore
    AIMessage,
    HumanMessage,
    SystemMessage
)
class Planner:
    def __init__(self,
                agent_prompt: PromptTemplate = planner_agent_prompt,
                model_name: str = 'gpt-4o-mini'
                ):
        OPENAI_API_KEY = os.getenv('OPEN_AI_API')
        self.llm = ChatOpenAI(model_name=model_name, temperature=0, max_tokens=15000, openai_api_key=OPENAI_API_KEY)
        
        self.agent_prompt = agent_prompt

        pass

    def run(self,text, query):
        return self.llm([HumanMessage(content=self._build_agent_prompt(text, query))]).content
    
    def _build_agent_prompt(self, text, query) -> str:
        return self.agent_prompt.format(
            text=text,
            query=query)