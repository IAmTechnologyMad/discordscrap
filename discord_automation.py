import json
import tkinter as tk
from tkinter import filedialog
from rich import print
from rich.prompt import Prompt


def extract_user_info(data, option):
    user_info = []
    keys_to_check = ['username', 'user_name', 'userID', 'displayName', 'nickname', 'user']
    
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                for key in keys_to_check:
                    if key in item:
                        if option == 1:
                            user_info.append({'username': item[key]})
                        elif option == 2:
                            user_info.append({'username': item[key], 'content': item.get('content', 'No content')})
                        break
            else:
                print(f"Error: Item is not a dictionary: {item}")
    else:
        print("Error: Data is neither a list nor a dictionary")
    
    return user_info

def upload_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    
    if file_path:
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                print(data)
                
                option = int(Prompt.ask("[bold yellow] Choose an option [/bold yellow] ( [bold blue] 1: Extract username [/bold blue], [bold red] 2: Extract username and message) [/bold red]"))
                
                user_info = extract_user_info(data, option)
                
                base_name = file_path.rsplit('.', 1)[0]
                output_file_name = f"{base_name}.txt"
                
                with open(output_file_name, "w") as output_file:
                    for info in user_info:
                        if option == 1:
                            output_file.write(f"{info['username']}\n")
                        elif option == 2:
                            output_file.write(f"{info['username']}: {info['content']}\n")
                        
                print(f"[bold yellow] File saved to {output_file_name} [/bold yellow]")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

upload_file()

if __name__ == "__main__":
    upload_file()

