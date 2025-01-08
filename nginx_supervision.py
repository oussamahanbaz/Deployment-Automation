
import subprocess
import shutil
from rich import print
import main

#manipule les fichiers et les dossiers et inside it

def nginx_existence():
    
    if shutil.which("nginx") is None:
        print("[red] \nNginx is not installed  \n \n[/red]")
        subprocess.run(["sudo", "apt", "install", "nginx", "-y"])
    else:
        print("[green]\nNginx is installed\n \n[/green]")
        
        
def nginx_option():       
    print("[yellow]\nEnter Nginx action[/yellow] ([green]start[/green]/[red]stop[/red]/[blue]restart[/blue]/[cyan]reload[/cyan]/[magenta]enable[/magenta]/[white]disable[/white]): ")

    action = input()
    if action =="start" or action =="stop" or action=="restart" or action=="reload" or action=="enable" or action =="disable" :
        if action == "start":
            subprocess.run(["sudo", "systemctl", "start", "nginx"])
        elif action == "stop":
            subprocess.run(["sudo", "systemctl", "stop", "nginx"])
        elif action == "restart":
            subprocess.run(["sudo", "systemctl", "restart", "nginx"])
        elif action == "reload":
            subprocess.run(["sudo", "systemctl", "reload", "nginx"])
        elif action == "enable":
            subprocess.run(["sudo", "systemctl", "enable", "nginx"])
        elif action == "disable":
            subprocess.run(["sudo", "systemctl", "disable", "nginx"])
       
            return
    else :  print ("[red]your input is false [/red]") ;        nginx_option()

def nginx_conf():    
    subprocess.run(["sudo", "nginx", "-t"])
    
def nginx_supervisions():
    print ("[yellow]1. check nginx existence [/yellow]" )
    print ("[yellow]2. options [/yellow]" )
    print ("[yellow]3. check configuration [/yellow]" )

    print ("[red]0. Exit[/red]")

    inp = input ("  Enter your choice : ")
    if inp =="1":
       nginx_existence()
       nginx_supervisions()
    elif inp =="2":
       nginx_option()
       nginx_supervisions()
    elif inp =="3":
        nginx_conf()
        nginx_supervisions()
    elif inp =="0":
          main.main()
