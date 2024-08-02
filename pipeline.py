from data_generator import *
from prompt_data import prompt,prompt_data_in_gptdataset
from data_convertor import format_data
from gpt_convertor import *
import streamlit as st




class pipeline_builder:
    def __init__(self,save_data,save_csv,save_json,number_of_data_entries,prompt) -> None:
        self.save_data = save_data
        self.save_csv = save_csv
        self.save_json = save_json
        self.data_entry = number_of_data_entries
        self.prompt = prompt
        
        
        
    def call_data_generator(self):
        st.subheader("Data Generator working ⚒️  :")
        obj = datagenerator(self.prompt,save_data,number_of_data_entries,st)
        obj.llm_caller()
        
            
    
    def call_data_convertor(self):
        st.subheader("Csv formator working 😋  :")
        obj = format_data(self.save_data, self.save_csv)
        obj.text_csv()
        
    
    def call_gpt_formator(self):
        st.subheader("Gpt formator working 🏭  :")
        data_jsonl = gpt_data_convertor(self.save_csv,self.save_json,st)
        data_jsonl.convert_to_training_format()
        st.header("hurry 😍 data created sucessfully ✅ ")
    def call_opensource_llm_datasetcollector(self):
        pass


st.set_page_config("Data Generator 🪪")

with st.sidebar:
    save_data = st.text_input("Enter the path for saving data:", r"D:\Artificial-intelligance\Phone-calling-assistant\data\data-1.txt")
    save_csv = st.text_input("Enter the path for saving CSV:", r"D:\Artificial-intelligance\Programming\dataset\data.csv")
    save_json = st.text_input("Enter the path for saving JSON:", r"D:\Artificial-intelligance\Programming\dataset\gpt_data\training.jsonl")
    prompt = st.text_area("Enter the prompt:", prompt)
    number_of_data_entries = st.number_input("Enter the number of data entries:", min_value=1, max_value=100, value=4)
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    data_generator = st.button("Data Generator📈")
    csv_convertor = st.button("Csv Convertor 📃")
    gpt_formator = st.button("Gpt formator 🤖")
    open_source_datagenerator = st.button("Open Source formator 🏭")
    st.markdown("<br><br>", unsafe_allow_html=True)
    process = st.button("Process")
pipe = pipeline_builder(save_data,save_csv,save_json,number_of_data_entries,prompt)



if process:    
    pipe.call_data_generator()
    pipe.call_data_convertor()
    pipe.call_gpt_formator()
    pipe.call_opensource_llm_datasetcollector()