import subprocess
import os
from rich import print
import main
import shutil
import Check_and_Install_Dependencies




def addphpsite (domain_name):
    try:
        port = input ("enter the port number")

        #add laravel ..........................................        
        Check_and_Install_Dependencies.instphp()
        subprocess.run(["sudo", "apt","install" ,"php8.3-fpm"])

        git_url = input("Enter the GitHub repository URL: ")
        subprocess.run(["git", "clone", git_url, f"/services/{domain_name}"])

        
           
        config_content = f"""
            server {{
            listen {port};
            server_name {domain_name} www.{domain_name};
            root /services/{domain_name}/public;

            index index.php index.html index.htm;

            location / {{
                try_files $uri $uri/ /index.php?$query_string;
            }}

            location ~ \\.php$ {{
                include snippets/fastcgi-php.conf;
                fastcgi_pass unix:/var/run/php/php8.3-fpm.sock;
                fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
                include fastcgi_params;
            }}

            location ~ /\\.ht {{
                deny all;
            }}
        }}
        """
        
        config_path = f"/etc/nginx/sites-available/{domain_name}"
        with open(config_path, "w") as f:
            f.write(config_content)
        subprocess.run(["sudo", "ln", "-s", config_path, f"/etc/nginx/sites-enabled/{domain_name}"])

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running a command: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

            

def addhtmlsite(domain_name ):
    try:
        port = input ("enter the port number")
        git_url = input("Enter the GitHub repository URL: ")
        subprocess.run(["sudo","git", "clone", git_url, f"/services/{domain_name}"], check=True)
        config_content = f"""
        server {{
            listen {port};
            server_name {domain_name} www.{domain_name};
            
            root /services/{domain_name};

            index index.html index.htm;

            location / {{
                try_files $uri $uri/ =404;
            }}

            access_log /var/log/nginx/{domain_name}.access.log;
            error_log /var/log/nginx/{domain_name}.error.log;
        }}
        """

        config_path = f"/etc/nginx/sites-available/{domain_name}"
        with open(config_path, "w") as config_file:
            config_file.write(config_content)
            
      #  subprocess.run(["sudo", "ln", "-s", config_path, f"/etc/nginx/sites-enabled/{domain_name}"])

        subprocess.run(["sudo", "nginx", "-t"], check=True)
        subprocess.run(["sudo", "systemctl", "reload", "nginx"], check=True)


    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running a command: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def addjavasite(domain_name):
    try:
        port = input ("enter the port number")

        git_url = input("Enter the GitHub repository URL: ")
       
        workdir = f"/services/{domain_name}"
        subprocess.run(["sudo", "mkdir", "-p", workdir])
        subprocess.run(["sudo", "chown", "-R", f"{os.getenv('USER')}:{os.getenv('USER')}", workdir])
        os.chmod(workdir, 0o755)

        subprocess.run(["git", "clone", git_url, workdir], check=True)

        if shutil.which("mvn") is None:
            print("Maven not found. Installing Maven...")
            subprocess.run(["sudo", "apt", "install", "maven", "-y"])
        os.chdir(workdir)
        subprocess.run(["mvn", "clean", "package"])
        subprocess.run(["sudo", "nano", f"/etc/nginx/sites-available/{domain_name}"])

        config_content = f"""
        server {{
            listen {port};
            server_name {domain_name} www.{domain_name};

            location / {{
                proxy_pass http://localhost:8080;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
            }}

            access_log /var/log/nginx/{domain_name}.access.log;
            error_log /var/log/nginx/{domain_name}.error.log;
        }}
        """

        config_path = f"/etc/nginx/sites-available/{domain_name}"
        with open(config_path, "w") as config_file:
            config_file.write(config_content)

        subprocess.run(["sudo", "ln", "-s", config_path, f"/etc/nginx/sites-enabled/{domain_name}"], check=True)
        subprocess.run(["sudo", "nginx", "-t"], check=True)
        subprocess.run(["sudo", "systemctl", "reload", "nginx"], check=True)

        # Étape 7 : Créer et configurer le service systemd
        version = input("Enter the version of your application (e.g., 1.0): ")
        path = f"{workdir}/target/{domain_name}-{version}.jar"

        service_content = f"""
        [Unit]
        Description=Java Application - {domain_name}
        After=network.target

        [Service]
        User={os.getenv('USER')}
        ExecStart=/usr/bin/java -jar {path}
        Restart=always
        RestartSec=10
        WorkingDirectory={workdir}
        StandardOutput=journal
        StandardError=journal

        [Install]
        WantedBy=multi-user.target
        """

        service_path = f"/etc/systemd/system/{domain_name}.service"
        with open(service_path, "w") as service_file:
            service_file.write(service_content)

        subprocess.run(["sudo", "systemctl", "enable", domain_name], check=True)
        subprocess.run(["sudo", "systemctl", "start", domain_name], check=True)


    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running a command: {e}")
    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Unexpected error: {e}")

    
    
    
def addnodesite (domain_name):
    try:
        port = input ("enter the port number")
        workdir = f"/services/{domain_name}"
        subprocess.run(["sudo", "mkdir", "-p", workdir], check=True)
        subprocess.run(["sudo", "chown", "-R", f"{os.getenv('USER')}:{os.getenv('USER')}", workdir], check=True)
        os.chmod(workdir, 0o755)

        git_url = input("Enter the GitHub repository URL: ")
        subprocess.run(["git", "clone", git_url, workdir], check=True)

        if shutil.which("node") is None or shutil.which("npm") is None:
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "nodejs", "-y"], check=True)
            subprocess.run(["sudo", "apt", "install", "npm", "-y"], check=True)

        os.chdir(workdir)
        subprocess.run(["npm", "install"], check=True)
        subprocess.run(["sudo", "npm", "install", "-g", "pm2"], check=True)
        
        subprocess.run(["sudo", "nano", f"/etc/nginx/sites-available/{domain_name}"])
        config_content = f"""
                server {{
                    listen {port};
                    server_name {domain_name} www.{domain_name};
                    

                    index index.html index.htm;

                    location / {{
                        proxy_pass http://localhost:3000;
                        proxy_set_header Host $host;
                        proxy_set_header X-Real-IP $remote_addr;
                        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                        proxy_set_header X-Forwarded-Proto $scheme;
                    }}

                    access_log /var/log/nginx/{domain_name}.access.log;
                    error_log /var/log/nginx/{domain_name}.error.log;
                }}
                """
                
        config_path = f"/etc/nginx/sites-available/{domain_name}"
        with open(config_path, "w") as config_file:
            config_file.write(config_content)
        subprocess.run(["sudo", "ln", "-s", f"/etc/nginx/sites-available/{domain_name}", "/etc/nginx/sites-enabled/"])
        subprocess.run(["sudo", "systemctl", "reload", "nginx"])
    
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running a command: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


import subprocess
import os
import shutil

def addflasksite(domain_name):
    try:
        port = input("Enter the port number: ")
        
        workdir = f"/services/{domain_name}"
        
        subprocess.run(["sudo", "mkdir", "-p", workdir], check=True)
        subprocess.run(["sudo", "chown", "-R", f"{os.getenv('USER')}:{os.getenv('USER')}", workdir], check=True)
        os.chmod(workdir, 0o755)
        
        git_url = input("Enter the GitHub repository URL: ")
        subprocess.run(["git", "clone", git_url, workdir], check=True)

        # Vérifier si Python et venv sont installés
        if shutil.which("python3") is None:
            subprocess.run(["sudo", "apt", "install", "python3-pip", "python3-dev"], check=True)
            subprocess.run(["sudo", "apt", "install", "python3-venv"], check=True)
        
         
        os.chdir(workdir)
        subprocess.run(["python3", "-m", "venv", "env"], check=True)
        print("Virtual environment 'env' created successfully.")

        os.chdir(workdir)
        venv_pip = os.path.join(workdir, "env", "bin", "pip")

        if os.path.exists("requirements.txt"):
            print("Installing requirements...")
            subprocess.run([venv_pip, "install", "-r", "requirements.txt"], check=True)

        print("Installing gunicorn and flask in the virtual environment...")
        subprocess.run([venv_pip, "install", "gunicorn", "flask"], check=True)
      
        
        # Créer le fichier de service pour Gunicorn
        service_content = f"""
        [Unit]
        Description=Gunicorn instance to serve flask.server.io
        After=network.target

        [Service]
        User={os.getenv('USER')}
        Group=www-data
        WorkingDirectory={workdir}
        Environment="PATH={workdir}/env/bin"
        ExecStart={workdir}/env/bin/gunicorn --bind 0.0.0.0:5000 app:app

        [Install]
        WantedBy=multi-user.target
        """
        service_path = f"/etc/systemd/system/{domain_name}.service"
        with open(service_path, "w") as service_file:
            service_file.write(service_content)
        
        subprocess.run(["sudo", "systemctl", "start", f"{domain_name}"], check=True)

        # Créer la configuration Nginx
        config_content = f"""
        server {{
            listen {port};
            server_name {domain_name} www.{domain_name};

            index index.html index.htm;

            location / {{
                proxy_pass http://localhost:5000;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
            }}

            access_log /var/log/nginx/{domain_name}.access.log;
            error_log /var/log/nginx/{domain_name}.error.log;
        }}
        """
        config_path = f"/etc/nginx/sites-available/{domain_name}"
        with open(config_path, "w") as config_file:
            config_file.write(config_content)

        subprocess.run(["sudo", "ln", "-s", config_path, "/etc/nginx/sites-enabled/"], check=True)
        subprocess.run(["sudo", "systemctl", "reload", "nginx"], check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running a command: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
