import subprocess
import os
from rich import print
import main
import deployement_site

def available_sites():
    
    available_sites = os.listdir("/etc/nginx/sites-available/")
    print(" [green]sites Available :[/green]")
    for site in available_sites:
        print(f" {site}")
      
    
def add_site():
    
    
    site_type = input("Enter the site type (html / php / java / python / node): ")
    if site_type =="html" or site_type=="php" or site_type=="java" or site_type=="python" or site_type=="node":
        print("[yellow]Enter the domain name to add: [/yellow]")
        domain_name = input()


        if site_type == "html":
            deployement_site.addhtmlsite(domain_name)
        elif site_type == "php":
             deployement_site.addphpsite (domain_name)
        elif site_type == "java":
            deployement_site.addjavasite(domain_name)
        elif site_type == "python":
             deployement_site.addflasksite(domain_name)
        elif site_type == "node":
             deployement_site.addnodesite(domain_name)
    else:
            print("[red]Invalid action.[/red]")
            add_site()


    
    
    
def manage_available_sites():
     print("[yellow]1. check available site [/yellow]")
     print ("[yellow]2. add site[/yellow]")
   
     print ("[red]0. Exit[/red]")

     entre = input("Enter your choice : ")
     if entre== "1":
        available_sites()
        manage_available_sites()
     if entre == "2":
        add_site()
        manage_available_sites()
     if entre == "0":
        main.main()       
        
     