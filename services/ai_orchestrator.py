import os
from langchain.chains import APIChain, SimpleSequentialChain, LLMChain
from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from core.config import settings
from services.api_specs import apiSpec_weather, apiSpec_attractions

def ask(input_query):
    """
    Processes the input query using various LangChain components.

    This function sets up a series of LangChain components including LLMChain and APIChain,
    which are then used in a SimpleSequentialChain to process the given query.

    Args:
        input_query (str): The user's input query.

    Returns:
        str: The processed response.
    """

    # Set OpenAI API Key from settings
    os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY

    # Initialize LLM (Language Model) with ChatOpenAI
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", max_tokens=1024, verbose=True)

    # Define a prompt template for finding the biggest city in a country
    city_template = PromptTemplate(template="Find the biggest city in {country}", input_variables=["country"])
    chain_city = LLMChain(llm=llm, prompt=city_template, verbose=True)

    # Set up APIChain for weather and attractions APIs
    chain_weather = APIChain.from_llm_and_api_docs(llm, apiSpec_weather, verbose=False,
                                                   limit_to_domains=["http://127.0.0.1:5000"],
                                                   output_keys=["temperature"])

    chain_attractions = APIChain.from_llm_and_api_docs(llm, apiSpec_attractions, verbose=False,
                                                       limit_to_domains=["http://127.0.0.1:5000"])

    # Define a prompt template for summarizing context about a city
    sum_template = PromptTemplate(template="Summarise all nicely with a few sentences of context about {city}", input_variables=["city"])
    chain_sum = LLMChain(llm=llm, prompt=sum_template)

    # Create a sequential chain combining city, weather, and attractions chains
    chain_seq = SimpleSequentialChain(chains=[chain_city, chain_weather, chain_attractions, chain_sum], verbose=True)

    # Execute the chain with the input query and print the response
    response = chain_seq.run({"input": input_query})
    print(response)
    return response

# Example usage: response = ask("your query here")
