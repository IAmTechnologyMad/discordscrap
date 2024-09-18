import json
import tkinter as tk
from tkinter import filedialog
from rich import print
from tqdm import tqdm
import os

root = tk.Tk()
root.withdraw()

print("[bold green] WELCOME TO RAPID FREELANCIN SCRAP SERVICE [/bold green]")
print("[bold white] ----------------------------------------- [/bold white]\n")

file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])

file_name = os.path.splitext(os.path.basename(file_path))[0]

with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
    
print(f"File chosen: [bold yellow]{file_name}.json[/bold yellow]\n")

n = [
    (message['author']['name'], message['timestamp'], message['content'])
    for message in data['messages'] if 'name' in message['author']
]

output_file = f"{file_name}.txt"
with open(output_file, 'w', encoding='utf-8') as file:
    for name, timestamp, content in tqdm(n, colour="red"):
        file.write(f"Nickname: {name}\nTimestamp: {timestamp}\nMessage: {content}\n\n")

print(f"[bold yellow] File saved as {output_file} [/bold yellow]")
