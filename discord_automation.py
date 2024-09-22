import json
import os
import subprocess
from tqdm import tqdm
from rich import print

print("\n \n[bold white]  ----------------------------------------- [/bold white]")
print("[bold green]  WELCOME TO RAPID FREELANCIN SCRAP SERVICE [/bold green]")
print("[bold white]  ----------------------------------------- [/bold white]\n")

TOKEN = input("Enter your Discord Token: ")
num_channels = int(input("\n Enter the number of channels to scrape: "))
channel_ids = []

for i in range(num_channels):
    channel_id = input(f"\n Enter the Discord Channel ID for channel {i+1}: ")
    channel_ids.append(channel_id)

EXPORTDIRECTORY = "C:\\Users\\kents\\Downloads\\scrap\\"
EXEPATH = "C:\\Users\\kents\\Downloads\\DiscordChatExporter.Cli.win-x64\\"
EXPORTFORMAT = "Json"

for i, CHANNEL in enumerate(channel_ids):
    OUTPUT_JSON = f"{EXPORTDIRECTORY}discord_chat_channel_{i+1}.json"
    
    print(f"\n[bold green]Scraping Discord channel {i+1}...[/bold green]")
    subprocess.run([
        f"{EXEPATH}DiscordChatExporter.Cli", "export", 
        "-t", TOKEN, 
        "-c", CHANNEL, 
        "-f", EXPORTFORMAT, 
        "-o", OUTPUT_JSON
    ])
    
    print(f"[bold yellow]JSON file saved at: {OUTPUT_JSON}[/bold yellow]\n")

    with open(OUTPUT_JSON, 'r', encoding='utf-8') as file:
        data = json.load(file)

    n = [
        (message['author']['name'], message['timestamp'], message['content'])
        for message in data['messages'] if 'name' in message['author']
    ]

    output_file = f"{EXPORTDIRECTORY}discord_chat_channel_{i+1}.txt"
    with open(output_file, 'w', encoding='utf-8') as file:
        for name, timestamp, content in tqdm(n, colour="red"):
            file.write(f"Name: {name}\nTimestamp: {timestamp}\nMessage: {content}\n\n")

    print(f"\n[bold yellow]File saved as {output_file} [/bold yellow]\n")

print("[bold green]CODE EXIT HERE, THANKYOU![/bold green]")
