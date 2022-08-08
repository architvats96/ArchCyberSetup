import pyfiglet
from termcolor import colored
import subprocess

# FUNCTIONS
def system_update():                # This function updates the system
    print("Updating system")
    subprocess.call("sudo pacman -Syu --noconfirm".split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(colored("System updated","green"))

def install_dependencies():         # This function installs dependencies
    ## Installing blackarch to enable further package download
    print("Installing blackarch")
    subprocess.call("curl -O https://blackarch.org/strap.sh".split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.call("chmod +x strap.sh".split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.call("sudo ./strap.sh".split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(colored("Blackarch Installed\n","green"))

    ## Installing yay to enable further package download via AUR
    print("Installing yay")
    subprocess.call("sudo pacman -Sy base-devel git yay --noconfirm".split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(colored("Yay Installed\n","green"))
    

def check_tool_status(tool):            # This function checks if the tool is installed or not
    if (tool == "metasploit"):
        status = subprocess.call(["which", "msfdb"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    elif (tool == "dnsutils"):
        status = subprocess.call(["which", "dig"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    elif (tool == "rpctools"):
        status = subprocess.call(["which", "rpcclient"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    elif (tool == "set"):
        status = subprocess.call(["which", "setoolkit"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        status = subprocess.call(["which", tool], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # 0 means that the tool is installed
    # 1 means that the tool is not installed
    return status

def install_tools():                    # This is the main function which is used to install tools
    tool_list = ["aircrack-ng", 
    "autorecon", 
    "beef", 
    "burpsuite",  
    "dirbuster", 
    "dnsrecon", 
    "dnsenum", 
    "dnsutils", 
    "enum4linux", 
    "filezilla", 
    "ffuf", 
    "gobuster", 
    "hashcat", 
    "host", 
    "hping", 
    "hydra", 
    "john", 
    "kerbrute", 
    "lbd", 
    "ldapsearch", 
    "metasploit", 
    "nbtscan", 
    "nikto", 
    "nmap", 
    "recon-ng", 
    "reconnoitre", 
    "rpctools", 
    "set", 
    "smbclient", 
    "smbmap", 
    "sqlmap", 
    "sublist3r", 
    "uniscan", 
    "wafw00f", 
    "whatweb", 
    "wpscan"]

    unable_to_install = []                  # This list is of all the tools that were not installed.
    installed = []                          # This list is of all the tools that have been successfully installed
    # Tool installation begins here
    for tool in tool_list:

        ## Checking if the tool is installed already.
        print(f"\nChecking installation status of {tool}")
        tool_check = check_tool_status(tool)
        

        if (tool_check == 1):                   # Tool needs to be installed                                                                  
            print(f"Installing {tool}")
            subprocess.call(["sudo", "pacman", "-S", tool, "--noconfirm"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            tool_check = check_tool_status(tool)
            if (tool_check == 0):               # Tool has been successfully installed with default reporitories
                installed.append(tool)
                print(colored(f"{tool} has been successfully installed","green"))

            elif(tool_check == 1):              # Tool wasn't installed with default repositories
                subprocess.call(["yay", "-S", tool, "--noconfirm"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                tool_check = check_tool_status(tool)
                if (tool_check == 0):               # Tool has been successfully installed with AUR
                    installed.append(tool)
                    print(colored(f"{tool} has been successfully installed","green"))
                else:
                    unable_to_install.append(tool)
                    print(colored(f"{tool} wasn't installed", "red"))
            else:
                unable_to_install.append(tool)
                print(colored("Unknown error occured","red"))
        else:                                   # Tool is already installed
            print(colored(f"{tool} is already installed", "green"))
    
    print(colored(f"\nFollowing tools have been installed in the system: \n {installed}"))

    if unable_to_install:
        print(colored(f"\nUnable to install the following tools: \n {unable_to_install}"))
    else:
        print(colored("\nAll tools have been successfully installed", "green"))




# CREATING BANNER
subprocess.call("pip install pyfiglet".split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.call("pip install termcolor".split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("---------------------------------------------------------------------------------")
banner = pyfiglet.figlet_format("ArchCyberSetup")
print(colored(banner, "green"))
print(colored("By techno","green"))
print("---------------------------------------------------------------------------------")


# PROGRAM BEGINS
try:
    choice = "random"
    while (choice != ""):
        choice = input("\n\nPress ENTER to install tools or else press CTRL + C to exit: ")
        if (choice == ""):
            system_update()
            install_dependencies()
            install_tools()
        else:
            print("Invalid input. Please try again.")
except KeyboardInterrupt:
    print("\nExiting the program..................")
    exit(0)
