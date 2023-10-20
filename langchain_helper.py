import os
from api_key import openai_api_key
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

os.environ['OPENAI_API_KEY'] = openai_api_key

llm = OpenAI(temperature=0.8)

def generate_restaurant_name_and_item(cuisine):
    prompt_temp_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a resturant for {cuisine} food . Suggest a fancy name for this "
    )


    name_chain = LLMChain(
        llm=llm,
        prompt=prompt_temp_name,
        output_key='resturant_name')

    prompt_temp_item = PromptTemplate(
        input_variables=['resturant_name'],
        template="Suggest food menu for {resturant_name} , Give output in comma seprated from"
    )

    item_chain = LLMChain(
        llm=llm, 
        prompt=prompt_temp_item,
        output_key='menu_items'
        )
    chain = SequentialChain(
        chains=[name_chain,item_chain],
        input_variables = ['cuisine'],
        output_variables = ['resturant_name','menu_items'])

    return chain({'cuisine':cuisine})
