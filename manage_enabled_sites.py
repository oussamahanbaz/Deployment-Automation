
import subprocess
import os
from rich import print
import main

def enabled_sites():

    enabled_sites = os.listdir("/etc/nginx/sites-enabled/")
    print(" [green]List all enabled sites: [/green]")
    for site in enabled_sites:
        print(f"+ {site}")
    print("\n \n")
    
def option ()  :
    print("[yellow]Enter action to perform[/yellow] ([green]enable[/green]/[red]disable[/red]/[blue]delete[/blue]) site: ")
    action = input()
    if action=="enable" or action=="disable" or action=="delete":

        site_name = input("Enter le nom du site: ")

        if action == "enable":
            subprocess.run(["sudo", "ln", "-s", f"/etc/nginx/sites-available/{site_name}", f"/etc/nginx/sites-enabled/"])
        elif action == "disable":
            subprocess.run(["sudo", "rm", f"/etc/nginx/sites-enabled/{site_name}"])
        elif action == "delete":
            subprocess.run(["sudo", "rm", f"/etc/nginx/sites-available/{site_name}"])
            subprocess.run(["sudo", "rm", f"/etc/nginx/sites-enabled/{site_name}"])
            subprocess.run(["sudo", "rm", f"/etc/nginx/sites-enabled/{site_name}"])
            
    
    else:             print("[red]Invalid action.[/red]") ;option()      

def manage_enabled_site():
    print ("[yellow]1. Enabled sites [/yellow]" )
    print ("[yellow]2. options [/yellow]" )
    print ("[red]0. Exit[/red]")
    
    inp = input ("Enter your choice :")
    if inp =="1":
       enabled_sites()
       manage_enabled_site()
    elif inp =="2":
       option()
       manage_enabled_site()
    elif inp =="0":
          main.main()