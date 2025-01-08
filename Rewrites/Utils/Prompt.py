from langchain.prompts import PromptTemplate # type: ignore

QUERY_GENERATION_PROMPT = """
Craft a prompt that asks llm to generate a travel plan given the following information. The input includes details such as trip duration, budget type, attractions types that the traveler wants to visit, dining preferences that they want to try, and accommodation requirements. Also, mention that detailed business information is provided, too.

----- Example Starts -----
Input: 
{'general': '2 days, moderate budget', 'attraction': 'history oriented', 'restaurants': 'French, good environment', 'hotel': 'good quality, good location'}

Output:
I want to go for a 2-day trip with a moderate budget. I want to visit some history-oriented attractions. Please find some good environment restaurants that provide French cuisine, I want to stay in a good quality hotel in a good location.
----- Example Ends -----

Input: {input}

Human query: """

query_generation_agent = PromptTemplate(
                        input_variables=["input"],
                        template=QUERY_GENERATION_PROMPT,
                        )