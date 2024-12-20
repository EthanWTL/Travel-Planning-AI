from langchain.prompts import PromptTemplate # type: ignore

ZEROSHOT_REACT_INSTRUCTION = """Collect information for a query plan using interleaving 'Thought', 'Action', and 'Observation' steps. Ensure you gather valid information related to transportation, dining, attractions, and accommodation. All information should be written in Notebook, which will then be input into the Planner tool. Note that the nested use of tools is prohibited. 'Thought' can reason about the current situation, and 'Action' can have 3 different types:

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

(4) NotebookWrite[Short Description]
Description: Writes a new data entry into the Notebook tool with a short description. This tool should be used immediately after AccommodationSearch, AttractionSearch, or RestaurantSearch. Only the data stored in Notebook can be seen by Planner. So you should write all the information you need into Notebook.
Parameters: Short Description - A brief description or label for the stored data. You don't need to write all the information in the description. The data you've searched for will be automatically stored in the Notebook.
Example: NotebookWrite[Accomodation for day 1] would store the informatrion of the hotel for day 1 that you have choosed.

(5) Planner[Query]
Description: A smart planning tool that crafts detailed plans based on user input and the information stroed in Notebook.
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