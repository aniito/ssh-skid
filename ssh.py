import os
import time
# from universal_skid import 2qi
# import skiddage
def gz():
        print("""
        
             ____________________________________________________
            /                                                    \
           |    _____________________________________________     |
           |   |                                             |    |
           |   |  ┌──(anito㉿43G)-[~]                        [ 43G ]
           |   |  └─# ssh start                              |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |    #43G                                     |    |
           |   |_____________________________________________|    |
           |                                                      |
            \_____________________________________________________/
                   \_______________________________________/
                _______________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-----------------------------. .-.---. .---.-.-.-.`-_
:-----------------------------------------------------------------------------:
`---._.-----------------------------------------------------------------._.---'        
        
        
        
        
        
        
        
        """)
        time.sleep(2)
        print("INSTALLING SSH")
        os.system("apt-get install ssh")
        x = input("mettre le root access au ssh ? [Y/N] : ")
        if x == "Y":
                print("IL FAUT TROUVER LA LIGNE AVEC #PermitRootLogin et enlever le #")
                import time
                cfd = input("prêt ? à y aller ? : ")
                print("sudo", end=" ", flush=True)
                time.sleep(0.5)
                print("nano", end=" ", flush=True)
                time.sleep(0.5)
                print("/etc/", end="", flush=True)
                time.sleep(0.5)
                print("ssh/", end="", flush=True)
                time.sleep(0.5)
                print("sshd_config", end="", flush=True)
                os.system("sudo nano /etc/ssh/sshd_config")
                
        else:
                print("passons !")
        
        print("Maintenant vous êtes prêts à ouvrir le SSH en root sur votre local !")
        op = input("voulez-vous avoir votre ip locale ? [Y/N] :")
        if op == "Y":
                os.system("ifconfig | grep 192")
                print("votre ip locale est contenue après inet ")
        else:
                print("pas d'affichage d'ip locale !")
                
        pm2 = input("voulez-vous installer nodejs et pm2 ? [Y/N] : ")
        if pm2 == "Y":
                print("installation de nodejs")
                os.system("sudo apt-get install nodejs")
                print("installation de npm")
                os.system("sudo apt-get install npm")
                print("installation de pm2")
                os.system("sudo npm i -g pm2")
                
        else:
                print("ok")
        print(" [+] Vous êtes maintenant prêts ! ")
        
                
                
         
