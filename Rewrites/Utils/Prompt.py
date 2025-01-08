from langchain.prompts import PromptTemplate # type: ignore

HUMAN_QUERY_GENERATION_PROMPT = """
Craft a a human like query for a travel plan given the following information. The input includes details such as trip duration, budget type, attractions types that the traveler wants to visit, dining preferences that they want to try, and accommodation requirements. Make sure each pairs of key words, like good environment, good location, are mentioned specifically.

----- Example Starts -----
Input: 
- general: 2 days, moderate budget, 
- attraction: history oriented, 
- restaurants: French, good environment, 
- hotel: good quality, good location

Output:
I want to go for a 2-day trip with a moderate budget. I want to visit some history-oriented attractions. Please find some good environment restaurants that provide French cuisine, I want to stay in a good quality hotel in a good location.
----- Example Ends -----

PromptInput: {input}

Output:"""

human_query_generation_agent = PromptTemplate(
                        input_variables=["input"],
                        template=HUMAN_QUERY_GENERATION_PROMPT,
                        )