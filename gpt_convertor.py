import pandas as pd
import json
import os
from dotenv import load_dotenv
from prompt_data import prompt_data_in_gptdataset
load_dotenv()



class gpt_data_convertor:
    def __init__(self,df,path_gpt_formator,st) -> None:
        self.df = df
        self.path_csv_to_jsonl = path_gpt_formator
        self.st = st

    def convert_to_training_format(self):
            if not os.path.exists(self.df):
                with open(self.df,'w') as file:
                    pass
            df = pd.read_csv(self.df)
            grouped = df.groupby('conversation_id')
            training_data = []
            
            for _, conversation in grouped:
                messages = [
                    {
                        "role": "system",
                        "content" : prompt_data_in_gptdataset
                    }
                ]
                
                history = ""
                turn_number = 1
                last_audio_file = ""

                for _, row in conversation.iterrows():
                    if row['role'] == 'customer':
                        history += f"<TURN {turn_number}> {row['text']} ||| "
                        turn_number += 1
                        messages.append({
                            "role": "user",
                            "content": (history + f"<AUDIO> {last_audio_file}").strip(" ||| <AUDIO> ")
                        })
                    elif row['role'] == 'caller':
                        last_audio_file = row['audio_file']
                        messages.append({
                            "role": "assistant",
                            "content": row['audio_file']
                        })
                
            
                if messages[-1]['role'] != 'assistant':
                    messages.append({
                        "role": "assistant",
                        "content": "end_call.mp3"
                    })
                
                
                if len(messages) >= 3:  
                    training_data.append({"messages": messages})
                    
                    
            
            self.st.write(training_data[1])
            with open(self.path_csv_to_jsonl,"w") as file:
                 for training in training_data:
                    json.dump(training, file)
                    file.write('\n')
                    
            print("Conversion complete. Check 'training_data.json' for the result in dataset folder📁.")
            
            



if __name__ == "__main__":
    pass
   

            
   

    