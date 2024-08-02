import streamlit as st



from data_generator import *
from prompt_data import prompt,prompt_data_in_gptdataset
from data_convertor import format_data
from gpt_convertor import *
import streamlit as st



class pipeline_builder:
    def __init__(self,save_data,save_csv,path_json,number_of_data_entries,prompt) -> None:
        self.save_data = save_data
        self.save_csv = save_csv
        self.save_json = save_json
        self.data_entry = number_of_data_entries
        self.prompt = prompt
        
        
    def call_data_generator(self):
        obj = datagenerator(self.prompt,save_data,number_of_data_entries)
        obj.llm_caller()
    
    def call_data_convertor(self):
        obj = format_data(self.save_data, self.save_csv)
        obj.text_csv()
        
    
    def call_gpt_formator(self):
        data_jsonl = gpt_data_convertor(self.save_csv,self.save_json)
        data_jsonl.convert_to_training_format()
    
    def call_opensource_llm_datasetcollector(self):
        pass




save_data = r"D:\Artificial-intelligance\Phone-calling-assistant\data\data-1.txt"
save_csv = r"D:\Artificial-intelligance\Programming\dataset\data.csv"
save_json = r"D:\Artificial-intelligance\Programming\dataset\gpt_data\training.jsonl"
number_of_data_entries = 4



st.set_page_config("Data Generator 🪪")
pipe = pipeline_builder(save_data,save_csv,save_json,number_of_data_entries,prompt)

# Define custom CSS for button styles
st.markdown("""
    <style>
    .gradient-button {
        background: linear-gradient(45deg, yellow, orange);
        border: none;
        color: white;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
        transition: background-color 0.3s ease;
    }

    .red-button {
        background-color: red;
        border: none;
        color: white;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
        transition: background-color 0.3s ease;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for button states
if 'data_generator' not in st.session_state:
    st.session_state['data_generator'] = False
if 'csv_convertor' not in st.session_state:
    st.session_state['csv_convertor'] = False
if 'gpt_formator' not in st.session_state:
    st.session_state['gpt_formator'] = False
if 'open_source_datagenerator' not in st.session_state:
    st.session_state['open_source_datagenerator'] = False

# Function to toggle button state
def toggle_button_state(button_key):
    st.session_state[button_key] = not st.session_state[button_key]

# Render buttons with conditional styles
with st.sidebar:
    if st.button("Data Generator📈", key="data_generator_btn"):
        toggle_button_state('data_generator')
    data_generator_class = 'red-button' if st.session_state['data_generator'] else 'gradient-button'
    st.markdown(f'<button class="{data_generator_class}">Data Generator📈</button>', unsafe_allow_html=True)

    if st.button("Csv Convertor 📃", key="csv_convertor_btn"):
        toggle_button_state('csv_convertor')
    csv_convertor_class = 'red-button' if st.session_state['csv_convertor'] else 'gradient-button'
    st.markdown(f'<button class="{csv_convertor_class}">Csv Convertor 📃</button>', unsafe_allow_html=True)

    if st.button("Gpt formator 🤖", key="gpt_formator_btn"):
        toggle_button_state('gpt_formator')
    gpt_formator_class = 'red-button' if st.session_state['gpt_formator'] else 'gradient-button'
    st.markdown(f'<button class="{gpt_formator_class}">Gpt formator 🤖</button>', unsafe_allow_html=True)

    if st.button("Open Source formator 🏭", key="open_source_datagenerator_btn"):
        toggle_button_state('open_source_datagenerator')
    open_source_datagenerator_class = 'red-button' if st.session_state['open_source_datagenerator'] else 'gradient-button'
    st.markdown(f'<button class="{open_source_datagenerator_class}">Open Source formator 🏭</button>', unsafe_allow_html=True)

# Conditional function calls based on button state
if st.session_state['data_generator']:
    st.write("Data Generator Called")

if st.session_state['csv_convertor']:
    st.write("Csv Convertor Called")

if st.session_state['gpt_formator']:
    st.write("Gpt formator Called")

if st.session_state['open_source_datagenerator']:
    st.write("Open Source datagenerator Called")