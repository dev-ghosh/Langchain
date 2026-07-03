from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal,color):
    # create prompt
    prompt=PromptTemplate(
        input_variables=["animal","color"],
        template="Give 3 short cool names for a {color} {animal}.Only names"
    )
    # initialise LLM
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.7,
        max_tokens=30
    )
    # create chain
    chain= prompt | llm
    # invoke chain
    response=chain.invoke({"animal":animal,"color":color}) # .invoke means run this once given input
    return response.content



if __name__ == "__main__": #Run this block of code only if this file is executed directly, not when it is imported.
    print(generate_pet_name("dog" , "black"))
