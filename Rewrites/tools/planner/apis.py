import os
from pandas import DataFrame
from langchain.prompts import PromptTemplate # type: ignore
from Utils.Prompt import planner_route_OP_agent
from langchain.chat_models import ChatOpenAI # type: ignore
from langchain_mistralai import ChatMistralAI
from langchain.schema import ( # type: ignore
    AIMessage,
    HumanMessage,
    SystemMessage
)
from transformers import pipeline
import torch

import ollama



class Planner:
    def __init__(self,
                agent_prompt: PromptTemplate = planner_route_OP_agent,
                model_name: str = ''
                ):
        OPENAI_API_KEY = os.getenv('OPEN_AI_API')
        MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')
        self.model_name = model_name
        if model_name == 'gpt-4o-2024-11-20':
            self.llm = ChatOpenAI(model_name=model_name, temperature=0, max_tokens=15000, openai_api_key=OPENAI_API_KEY)
        if model_name == 'mistral-large-2411':
            self.llm = ChatMistralAI(
                model="mistral-large-2411",
                temperature=0,
                max_tokens=15000,
                mistral_api_key = MISTRAL_API_KEY
            )
        if model_name == 'meta-llama/Llama-3.1-8B':
            self.llm = pipeline(
                    "text-generation", model="meta-llama/Llama-3.1-8B-Instruct", model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto"
               )
        if model_name == 'open-mixtral-8x7b':
            self.llm = ChatMistralAI(
                model="open-mixtral-8x7b",
                temperature=0,
                max_tokens=15000,
                mistral_api_key = MISTRAL_API_KEY
            )

        self.agent_prompt = agent_prompt

        pass

    def run(self, notebook, query):
        results = []
        for idx, unit in enumerate(notebook):
            if type(unit['Content']) == DataFrame:
                results.append({"index":idx, "Description":unit['Description'], "Content":unit['Content'].to_string(index=False)})
            else:
                results.append({"index":idx, "Description":unit['Description'], "Content":str(unit['Content'])})

        with open('test.txt', 'w') as f:
            f.write(str(results))

        if self.model_name == 'meta-llama/Llama-3.1-8B':
            messages = [{"role": "user", "content": self._build_agent_prompt(str(results), query)}]
            outputs = self.llm(messages,do_sample=False,max_new_tokens=5000)
            request = outputs[0]["generated_text"][-1]['content']
        else:
            request = self.llm.invoke([HumanMessage(content=self._build_agent_prompt(str(results), query))]).content
        return request
    
    def _build_agent_prompt(self, text, query) -> str:
        return self.agent_prompt.format(
            given_information=text,
            query=query)