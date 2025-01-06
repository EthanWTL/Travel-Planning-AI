from langchain.prompts import PromptTemplate # type: ignore

ZEROSHOT_REACT_INSTRUCTION = """Collect information for a query plan using interleaving 'Thought', 'Action', and 'Observation' steps. Ensure you gather valid information related to transportation, dining, attractions, and accommodation. All information should be written in Notebook, which will then be input into the Planner tool. Note that the nested use of tools is prohibited. Dont include phrases like "Action: ", "Action 5", "Thought 1", or "Thought: " in your response. 'Thought' can reason about the current situation, and 'Action' can have 5 different types:

(1) AccommodationSearch[Budget,Preference]:
Description: Find the accommodation that matches the preference.
Parameters:
Preference: A list of preferences mentioned in the query.
Example: AccommodationSearch[Moderate Budget,[Good Location, Good Service]] would return the moderate price hotel that has a good or excellent location, as well as a good or excellent service.

(2) AttractionSearch[Budget, Preference]:
Description: Find the attractions that matches the preference.
Parameters:
Budget: The budget mentioned in the query.
Preference: A list of preferences mentioned in the query.
Example: AttractionSearch[Cheap budget,[Nature Oriented]] would return the cheap price and nature - oriented attractions.

(3) RestaurantSearch[Budget, Cuisine, Preference]:
Description: Find the restaurants that matches the preference.
Parameters:
Budget: The budget mentioned in the query.
Cuisine: The cuisine mentioned in the query.
Preference: A list of preferences mentioned in the query.
Example: RestaurantSearch[Expensive budget, Vietnamese, [Good Flavor, Good Value]] would return the expensive restaurants that offer Vietnamese cuisine, with good or excellent flavor and good or excellent value.

(4) BusinessClusterSearch[Number Of Clusters]:
Description: A tool that finds the number of business clusters given the information that you've collected. The tool will choose what business to be considered and return their spatial clustering information.
Parameters: 
Number Of Clusters: Determine how many spatial clusters that you want to find. 
Example: BusinessClusterSearch[3] would return you a list of 3 business clusters among some attractions and hotels that you've collected. The businesses in the same cluster indicates that they are closer to each other and prefered to be arranged for the same day of the travel.

(5) Planner[Query]
Description: A smart planning tool that crafts detailed plans based on user input and the information stored in Notebook.
Parameters: 
Query: The query from user.
Example: Planner[Give me a 3-day trip plan in Philadelphia] would return a detailed 3-day trip plan.

You should use as many as possible steps to collect engough information to input to the Planner tool. 

Each action only calls one function once. Do not add any description in the action.

Query: {query}{scratchpad}"""



zeroshot_react_agent_prompt = PromptTemplate(
                        input_variables=["query", "scratchpad"],
                        template=ZEROSHOT_REACT_INSTRUCTION,
                        )


PLANNER_INSTRUCTION = """You are a proficient planner. You will follow the instructions from the query and generated a travel plan with the given information like the following example.

----- Example Starts -----
Day X:
- Accommodation: 
  - Name: XXXX
    Address: XXXX, XXXX

- Breakfast: 
  - Name: XXXX 
    Address: XXXX, XXXX

- Morning Attraction: 
  - Name: XXXX 
    Address: XXXX, XXXX 

- Lunch: 
  - Name: XXXX 
    Address: XXXX, XXXX 

- Afternoon Attraction: 
  - Name: XXXX 
    Address: XXXX, XXXX 
  - Name: XXXX 
    Address: XXXX, XXXX 

- Dinner: 
  - Name: XXXX 
    Address: XXXX, XXXX 

- Night Attraction: 
  - Name: XXXX 
    Address: XXXX, XXXX 
----- Example Ends -----

Given information: {text}
Query: {query}
Travel Plan:"""


planner_agent_prompt = PromptTemplate(
                        input_variables=["text","query"],
                        template = PLANNER_INSTRUCTION,
                        )
