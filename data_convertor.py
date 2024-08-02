import pandas as pd
import os

class format_data:
    def __init__(self,save_data,path_csv) -> None:
        self.save_data = save_data
        self.path_csv = path_csv
    
    def text_csv(self):
        if not os.path.exists(self.path_csv):
            with open(self.path_csv, 'w') as file:
                pass
        
        with open(self.save_data, 'r') as file:
            data = file.read()
        conversations = data.split('##')
        formatted_data = []

        
        for conversation in conversations:
        
            lines = conversation.strip().split('\n')
            if len(lines) < 2:
                continue
            conversation_id = lines[0].split(':')[0].split()[-1]
            
        
            turn_id = 1
            for line in lines[1:]:
                line = line.strip()
                if line.startswith("Caller:"):
                    role = "caller"
                    parts = line.split(':', 1)
                    if len(parts) > 1:
                        audio_file = parts[1].strip()
                        text = ""
                elif line.startswith("Customer:"):
                    role = "customer"
                    audio_file = ""
                    parts = line.split(':', 1)
                    if len(parts) > 1:
                        text = parts[1].strip()
                    else:
                        text = ""
                else:
                    continue
                
 
                formatted_data.append([conversation_id, turn_id, role, audio_file, text])
                turn_id += 1

 
        df = pd.DataFrame(formatted_data, columns=["conversation_id", "turn_id", "role", "audio_file", "text"])
        
        df.to_csv(self.path_csv, index=False)
        print("files📁 saved sucessfully:😋")



if __name__ =="__main__":
    pass