import os
from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


## MEMORY ###
# 
# Importing necessary types from the typing module
from typing import TypedDict, List  

# Define a TypedDict named 'State' to represent a structured dictionary
class State(TypedDict):

    text: str  # Stores the original input text
    classification: str  # Represents the classification result (e.g., category label)
    entities: List[str]  # Holds a list of extracted entities (e.g., named entities)
    summary: str  # Stores a summarized version of the text



## LLM ##
##
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)




## CAPABILILITY ##
##
def classification_node(state: State):
   """
   Classify the text into one of predefined categories.
   
   Parameters:
       state (State): The current state dictionary containing the text to classify
       
   Returns:
       dict: A dictionary with the "classification" key containing the category result
       
   Categories:
       - News: Factual reporting of current events
       - Blog: Personal or informal web writing
       - Research: Academic or scientific content
       - Other: Content that doesn't fit the above categories
   """
    
   # Define a prompt template that asks the model to classify the given text
   prompt = PromptTemplate(
       input_variables=["text"],
       template="Classify the following text into one of the categories: News, Blog, Research, or Other.\n\nText: {text}\n\nCategory:"
   )

   # Format the prompt with the input text from the state
   message = HumanMessage(content=prompt.format(text=state["text"]))

   # Invoke the language model to classify the text based on the prompt
   classification = llm.invoke([message]).content.strip()

   # Return the classification result in a dictionary
   return {"classification": classification}