
import os 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


# load env  vars
load_dotenv()

# init cht ChatOpenAI instance

llm = ChatOpenAI(model="gpt-4o-mini")


resp = llm.invoke("hello, Are you working?") 

print (resp.content)



