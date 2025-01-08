
import subprocess
import shutil

import Check_and_Install_Dependencies
import manage_enabled_sites
import nginx_supervision
import system_health_monitoring
import site_management

def main() :
    
     print("web deployement tool")
     print("1. show System Health and Stats")
     print ("2. Nginx Supervision")
     print ("3. Manage Available Sites")
     print ("4. Manage Enabled Sites")
     print ("5. Check and Install Dependencies")
     print ("0. Exit")
     print ()

     entre = input("Enter your choice : ")
     if entre== "1":
        system_health_monitoring.system_health_monitoringg()
     
     
     if entre == "2":
        nginx_supervision.nginx_supervisions()
        
        
     if entre == "3":
        site_management.manage_available_sites()
        
       
     if entre == "4":
        manage_enabled_sites.manage_enabled_site()
        
     if entre =="5":
      Check_and_Install_Dependencies.install()
        
if __name__ == "__main__":
    main()