import time 
import os
import random
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY ")

class datagenerator:
    def __init__(self,prompt,save_data,number_of_data_entries,st) -> None:
        self.prompt = prompt
        self.save_data = save_data
        self.number = number_of_data_entries
        self.st = st
    
    def llm_caller(self):
        api_key = os.environ.get("GOOGLE_API_KEY", "AIzaSyDAWlilbkYBE5lxQ7nPLN3FNhc-11-Gph0")
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", verbose=True, temperature=0.1, google_api_key=api_key)
        if not os.path.exists(self.save_data):
            with open(self.save_data, 'w') as file:
                pass
        i = 0
        with open(self.save_data, 'w') as file:
            while True:
                response = llm.invoke(self.prompt)  
                file.write(str(response.content)+"\n\n\n")
                i = i+1
                print(i)
                self.st.write("entry"+ "  "+ str(i) +" " +"created Sucessfully  😋")
                time.sleep(4)
                if i == self.number:
                    break
            
         

if __name__ == "__main__":
    pass


