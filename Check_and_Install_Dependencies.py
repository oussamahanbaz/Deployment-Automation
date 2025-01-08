import shutil
import subprocess
import time
from rich import print
from tqdm import tqdm
import sys
import main

def check (input) :
        if shutil.which(input) is None:
            print (f" [red] {input} not found [/red]")
            return 1
        else:
            print (f"[green] {input} is already installed [/green] ")
            return 0


def instjava ():
     if check("java")==1:
        injava = input("do you want install java (yes/no)  ?")
        if (injava =="yes"):
            with tqdm(total=100) as pbar:
             subprocess.run(["sudo", "apt", "install", "openjdk-17-jdk", "-y"], check=True)
             for _ in range(100):
                  pbar.update(1)
            print("Java 17 installed")

            
def instphp ():
         if check("php")==1:
             inphp = input("do you want install php (yes/no) ?")
             if (inphp =="yes"):
               with tqdm(total=100) as pbar:
                  subprocess.run(["sudo","apt-get", "install" ,"ca-certificates", "apt-transport-https", "software-properties-common"])
                  subprocess.run(["sudo", "add-apt-repository", "ppa:ondrej/php", "-y"])
                  subprocess.run(["sudo", "apt-get","update"])
                  subprocess.run(["sudo", "apt", "install", "php8.3", "-y"], check=True)
                  for _ in range(100):
                    pbar.update(1)
                  print("PHP 8.3 installed")

def instnode ():
         if check("node")==1:
             innode = input("do you want install node (yes/no)  ?")
             if (innode =="yes"):                
                with tqdm(total=100) as pbar:

                 subprocess.run( "curl -sL https://deb.nodesource.com/setup_22.x | sudo bash -", check=True ,shell=True)
                 subprocess.run(["sudo", "apt", "install", "nodejs", "-y"], check=True)
                 for _ in range(100):
                    pbar.update(1)
                 print("Node.js 22 installed")
                 

def insflask  ():

         if check("flask")==1:
             inflask = input("do you want install flask (yes/no) ?")
             if (inflask =="yes"):
                print("Installing Flask...")
                with tqdm(total=100) as pbar:
                 subprocess.run([sys.executable, "-m", "pip", "install", "flask"],check=True )
                 for _ in range(100):
                    pbar.update(1)
             print("flask installed")

def install ():
     print("[yellow]1. check java [/yellow]")
     print ("[yellow]2. check php[/yellow]")
     print ("[yellow]3. check node[/yellow]")
     print ("[yellow]4. check flask[/yellow]")
     print ("[red]0. Exit[/red]")
     print ()

     entre = input("Enter your choice : ")
     if entre== "1":
        instjava()     
        install ()
     if entre == "2":
        instphp()        
        install ()
     if entre == "3":
        instnode()        
        install ()
     if entre == "4":
        insflask()   
        install ()   
     if entre =="0":
        main.main()