import os
from langchain.prompts import PromptTemplate # type: ignore
from Utils.Prompt import planner_route_OP_agent
from langchain.chat_models import ChatOpenAI # type: ignore
from langchain.schema import ( # type: ignore
    AIMessage,
    HumanMessage,
    SystemMessage
)
class Planner:
    def __init__(self,
                agent_prompt: PromptTemplate = planner_route_OP_agent,
                model_name: str = ''
                ):
        OPENAI_API_KEY = os.getenv('OPEN_AI_API')
        if model_name == 'gpt-4o-2024-11-20':
            self.llm = ChatOpenAI(model_name=model_name, temperature=0, max_tokens=15000, openai_api_key=OPENAI_API_KEY)
        
        self.agent_prompt = agent_prompt

        pass

    def run(self, text, query):
        return self.llm([HumanMessage(content=self._build_agent_prompt(text, query)) ]).content
    
    def _build_agent_prompt(self, text, query) -> str:
        return self.agent_prompt.format(
            given_information=text,
            query=query)