from colorama import Fore, init
import time
import os

# Initialise Colorama
init(autoreset=True)

print(Fore.CYAN + "[==============================]")
print(Fore.YELLOW + "     ANOS VIP PANEL V1.0")
print(Fore.CYAN + "[==============================]")

print(Fore.WHITE + "1: Télécharger le panel")
print(Fore.WHITE + "2: Contacter l'admin")

choix = input(Fore.GREEN + "\nChoix: ")

match choix:
    case "1":
        mdp = input(Fore.BLUE + "Mot de passe: ")

        if mdp == "Anos123":
            print(Fore.GREEN + "Mot de passe correct !")
            print(Fore.CYAN + "Ouverture du téléchargement...")
            time.sleep(1)

            os.system(
                "termux-open-url "
                "'https://www.mediafire.com/file/eoybijq71kooxlk/Anosxyz.apk/file'"
            )

        else:
            print(Fore.RED + "Mot de passe incorrect !!")
            print(Fore.YELLOW + "Redirection vers l'admin...")
            time.sleep(3)

            os.system(
                "termux-open-url "
                "'https://wa.me/23407071776576'"
            )

    case "2":
        print(Fore.CYAN + "Ouverture de WhatsApp...")
        time.sleep(1)

        os.system(
            "termux-open-url "
            "'https://wa.me/23407071776576'"
        )

    case _:
        print(Fore.RED + "Choix invalide !")

