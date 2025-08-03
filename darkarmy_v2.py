#!/usr/bin/env python3
"""
DARKARMY v2 - Refactored version of darkarmy.py for Python 3
Coded by Amn3sia - be honored
"""

import sys
import os
import time
import subprocess

# Color utility for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RED = '\033[91m'  # Red color
    PURPLE = '\033[95m'  # Magenta/Purple color
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def color_text(text, color):
    return f"{color}{text}{Colors.ENDC}"

def clear_screen():
    if os.name == 'posix':
        subprocess.run(['clear'])
    else:
        subprocess.run(['cls'])

def logo():
    # Print the logo with the specific part in purple/magenta
    purple_text = color_text(""" _(`-')               (`-') <-.(`-') (`-')  _    (`-') <-. (`-')             
( (OO ).->         <-.(OO )  __( OO) (OO ).-/ <-.(OO )    \(OO )_   """, Colors.PURPLE)
    red_text = color_text("""   .->   
 \    .'_    .---. ,------,)'-'. ,--./ ,---.  ,------,),--./  ,-.) ,--.'  ,-.
 '`'-..__)  / .  | |   /`. '|  .'   /| \ /`.\ |   /`. '|   `.'   |(`-')'.'  /
 |  |  ' | / /|  | |  |_.' ||      /)'-'|_.' ||  |_.' ||  |'.'|  |(OO \    / 
 |  |  / :/ '-'  |||  .   .'|  .   '(|  .-.  ||  .   .'|  |   |  | |  /   /) 
 |  '-'  /`---|  |'|  |\  \ |  |\   \|  | |  ||  |\  \ |  |   |  | `-/   /`  
 `------'     `--' `--' '--'`--' '--'`--' `--'`--' '--'`--'   `--'   `--'    
                          """, Colors.RED)
    print(purple_text + red_text)

def clone_and_run(repo_url, run_cmd, cwd=None):
    try:
        # Extract repository name from URL
        repo_name = repo_url.rstrip('/').split('/')[-1].replace('.git', '')
        if not os.path.exists(repo_name):
            print(f"Cloning {repo_name}...")
            subprocess.run(['git', 'clone', repo_url], check=True)
        else:
            print(f"{repo_name} already exists.")
        print(f"Running {repo_name}...")
        subprocess.run(run_cmd, cwd=cwd or repo_name, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {repo_name}: {e}")
    except FileNotFoundError as e:
        print(f"Command not found error while running {repo_name}: {e}")
    except Exception as e:
        print(f"Unexpected error running {repo_name}: {e}")
    input("Press Enter to continue...")

# Tool functions with repo URLs and run commands
def lazyrecon():
    clone_and_run("https://github.com/nahamsec/lazyrecon.git", ["bash", "lazyrecon.sh"], cwd="lazyrecon")
    menu()

def redhawk():
    clone_and_run("https://github.com/Tuhinshubhra/RED_HAWK.git", ["php", "RED_HAWK.php"], cwd="RED_HAWK")
    menu()

def th3inspector():
    clone_and_run("https://github.com/Moham3dRiahi/Th3inspector.git", ["bash", "Th3inspector.sh"], cwd="Th3inspector")
    menu()

def wpgrabinfo():
    clone_and_run("https://github.com/Moham3dRiahi/WPGrabInfo.git", ["python3", "wpgrabinfo.py"], cwd="WPGrabInfo")
    menu()

def billcipher():
    clone_and_run("https://github.com/GitHackTools/BillCipher.git", ["python3", "BillCipher.py"], cwd="BillCipher")
    menu()

def gasmask():
    clone_and_run("https://github.com/twelvesec/gasmask.git", ["python3", "gasmask.py"], cwd="gasmask")
    menu()

def webkiller():
    clone_and_run("https://github.com/ultrasecurity/webkiller.git", ["python3", "webkiller.py"], cwd="webkiller")
    menu()

def fbi():
    clone_and_run("https://github.com/KnightSec-Official/FBI.git", ["python3", "fbi.py"], cwd="FBI")
    menu()

def dtect():
    clone_and_run("https://github.com/hudacbr/D-TECT.git", ["python3", "dtect.py"], cwd="D-TECT")
    menu()

def userrecon():
    clone_and_run("https://github.com/issamelferkh/userrecon.git", ["python3", "userrecon.py"], cwd="userrecon")
    menu()

def owscan():
    clone_and_run("https://github.com/Gameye98/OWScan.git", ["python", "owscan.py"], cwd="OWScan")
    menu()

def clickjacking_tester():
    clone_and_run("https://github.com/D4Vinci/Clickjacking-Tester.git", ["python", "clickjacking.py"], cwd="Clickjacking-Tester")
    menu()

def tm_scanner():
    clone_and_run("https://github.com/TechnicalMujeeb/TM-scanner.git", ["python", "tm_scanner.py"], cwd="TM-scanner")
    menu()

def androbugs():
    clone_and_run("https://github.com/AndroBugs/AndroBugs_Framework.git", ["python", "androbugs.py"], cwd="AndroBugs_Framework")
    menu()

def scanqli():
    clone_and_run("https://github.com/bambish/ScanQLi.git", ["python", "scanqli.py"], cwd="ScanQLi")
    menu()

def commix():
    clone_and_run("https://github.com/commixproject/commix.git", ["python", "commix.py"], cwd="commix")
    menu()

def wpseku():
    clone_and_run("https://github.com/m4ll0k/WPSeku.git", ["python", "wpseku.py"], cwd="WPSeku")
    menu()

def routersploit():
    clone_and_run("https://github.com/threat9/routersploit.git", ["python", "rsf.py"], cwd="routersploit")
    menu()

def nikto():
    clone_and_run("https://github.com/sullo/nikto.git", ["perl", "program/nikto.pl"], cwd="nikto")
    menu()

def reaver():
    clone_and_run("https://github.com/t6x/reaver-wps-fork-t6x.git", ["reaver"])
    menu()

def pixiewps():
    clone_and_run("https://github.com/wiire/pixiewps.git", ["pixiewps"])
    menu()

def bluepot():
    clone_and_run("https://github.com/andrewmichaelsmith/bluepot.git", [])
    menu()

def arat():
    clone_and_run("https://github.com/AhMyth/AhMyth-Android-RAT.git", ["python", "AhMyth.py"], cwd="AhMyth-Android-RAT")
    menu()

def goldeneye():
    clone_and_run("https://github.com/jseidl/GoldenEye.git", ["python", "goldeneye.py"], cwd="GoldenEye")
    menu()

def hulk():
    clone_and_run("https://github.com/grafov/hulk.git", ["python", "hulk.py"], cwd="hulk")
    menu()

def cmseek():
    clone_and_run("https://github.com/Tuhinshubhra/CMSeeK.git", ["python", "cmseek.py"], cwd="CMSeeK")
    menu()

def metasploit():
    print("Metasploit installation must be done manually.")
    input("Press Enter to continue...")
    menu()

def tmvenom():
    clone_and_run("https://github.com/TechnicalMujeeb/tmvenom.git", ["python", "tmvenom.py"], cwd="tmvenom")
    menu()

def zarp():
    clone_and_run("https://github.com/hatRiot/zarp.git", ["python", "zarp.py"], cwd="zarp")
    menu()

def autosploit():
    clone_and_run("https://github.com/NullArray/AutoSploit.git", ["python", "autosploit.py"], cwd="AutoSploit")
    menu()

def eggshell():
    clone_and_run("https://github.com/neoneggplant/EggShell.git", ["python", "eggshell.py"], cwd="EggShell")
    menu()

def brutal():
    clone_and_run("https://github.com/Screetsec/Brutal.git", ["bash", "Brutal.sh"], cwd="Brutal")
    menu()

def setoolkit():
    clone_and_run("https://github.com/trustedsec/social-engineer-toolkit.git", ["python", "setup.py"], cwd="social-engineer-toolkit")
    menu()

def ssls():
    clone_and_run("https://github.com/moxie0/sslstrip.git", ["python", "setup.py"], cwd="sslstrip")
    menu()

def pyphisher():
    clone_and_run("https://github.com/sneakerhax/PyPhisher.git", ["python", "pyphisher.py"], cwd="PyPhisher")
    menu()

def smtp_mailer():
    clone_and_run("https://github.com/halojoy/PHP-SMTP-Mailer.git", ["python", "smtp_mailer.py"], cwd="PHP-SMTP-Mailer")
    menu()

def python_packet_sniffer():
    clone_and_run("https://github.com/buckyroberts/Python-Packet-Sniffer.git", ["python", "sniffer.py"], cwd="Python-Packet-Sniffer")
    menu()

def androrat():
    clone_and_run("https://github.com/warecrer/AndroRAT.git", ["python", "androRAT.py"], cwd="AndroRAT")
    menu()

def csploit():
    clone_and_run("https://github.com/cSploit/android.git", ["python", "csploit.py"], cwd="cSploit")
    menu()

def thefatrat():
    clone_and_run("https://github.com/Exploit-install/TheFatRat.git", ["bash", "setup.sh"], cwd="TheFatRat")
    menu()

def socialbox():
    clone_and_run("https://github.com/Cyb0r9/SocialBox.git", ["bash", "SocialBox.sh"], cwd="SocialBox")
    menu()

def bluforce_fb():
    clone_and_run("https://github.com/AngelSecurityTeam/BluForce-FB.git", ["python", "bluforce.py"], cwd="BluForce-FB")
    menu()

def faceboom():
    clone_and_run("https://github.com/Oseid/FaceBoom.git", ["python", "faceboom.py"], cwd="FaceBoom")
    menu()

def instagram():
    clone_and_run("https://github.com/Pure-L0G1C/Instagram.git", ["python", "instagram.py"], cwd="Instagram")
    menu()

def instabrute():
    clone_and_run("https://github.com/xHak9x/instabrute.git", ["python", "instabrute.py"], cwd="instabrute")
    menu()

def brute_force_gmail():
    clone_and_run("https://github.com/0xfff0800/Brute-force-gmail.git", ["python", "gmail.py"], cwd="Brute-force-gmail")
    menu()

def gmailbruterv2():
    clone_and_run("https://github.com/DEMON1A/GmailBruterV2.git", ["python", "gmailbruter.py"], cwd="GmailBruterV2")
    menu()

def wpbrute():
    clone_and_run("https://github.com/BlackXploits/WPBrute.git", ["python", "wpbrute.py"], cwd="WPBrute")
    menu()

def cpanel_bruter():
    clone_and_run("https://github.com/imadoxhunter/Cpanel-Bruter.git", ["python", "cpanel.py"], cwd="Cpanel-Bruter")
    menu()

def rdp_brute():
    clone_and_run("https://github.com/TheDevFromKer/RDP-Brute.git", ["python", "rdp.py"], cwd="RDP-Brute")
    menu()

def shellphish():
    clone_and_run("https://github.com/rorizam323/shellphish.git", ["bash", "shellphish.sh"], cwd="shellphish")
    menu()

def hiddeneye():
    clone_and_run("https://github.com/DarkSecDevelopers/HiddenEye.git", ["python", "HiddenEye.py"], cwd="HiddenEye")
    menu()

def socialfish():
    clone_and_run("https://github.com/An0nUD4Y/SocialFish.git", ["python", "SocialFish.py"], cwd="SocialFish")
    menu()

def zphisher():
    clone_and_run("https://github.com/htr-tech/zphisher.git", ["bash", "zphisher.sh"], cwd="zphisher")
    menu()

def blackeye():
    clone_and_run("https://github.com/An0nUD4Y/blackeye.git", ["bash", "blackeye.sh"], cwd="blackeye")
    menu()
 
def menu():
    clear_screen()
    logo()
    print(color_text("<--------------------------Tools Categories--------------------------------->", Colors.OKGREEN))
    print(color_text("  {1}--Information Gathering", Colors.OKCYAN))
    print(color_text("  {2}--Vulnerability Analysis", Colors.OKCYAN))
    print(color_text("  {3}--Wireless Testing", Colors.OKCYAN))
    print(color_text("  {4}--Exploitation Tools", Colors.OKCYAN))
    print(color_text("  {5}--Sniffing & Spoofing", Colors.OKCYAN))
    print(color_text("  {6}--Android Hacking", Colors.OKCYAN))
    print(color_text("  {7}--Brute Force Tools", Colors.OKCYAN))
    print(color_text("  {8}--Phishing Tools", Colors.OKCYAN))
    print(color_text("  {9}--OS Installer", Colors.OKCYAN))
    print(color_text("  {0}--Credits", Colors.OKCYAN))
    print(color_text("  {99}--Exit", Colors.FAIL))
    print(color_text("<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>", Colors.OKGREEN))
    
    try:
        choice = int(input(color_text("DARKARMY~# ", Colors.BOLD)))
        if choice == 1:
            # Information Gathering Tools
            clear_screen()
            logo()
            print(color_text("Information Gathering Tools:", Colors.OKGREEN))
            print(color_text("  {1}--LazyRecon", Colors.OKCYAN))
            print(color_text("  {2}--RED HAWK", Colors.OKCYAN))
            print(color_text("  {3}--Th3inspector", Colors.OKCYAN))
            print(color_text("  {4}--WPGrabInfo", Colors.OKCYAN))
            print(color_text("  {5}--BillCipher", Colors.OKCYAN))
            print(color_text("  {6}--Gasmask", Colors.OKCYAN))
            print(color_text("  {7}--Webkiller", Colors.OKCYAN))
            print(color_text("  {8}--FBI", Colors.OKCYAN))
            print(color_text("  {9}--D-Tect", Colors.OKCYAN))
            print(color_text("  {10}--UserRecon", Colors.OKCYAN))
            print(color_text("  {11}--OWScan", Colors.OKCYAN))
            print(color_text("  {99}--Back to Main Menu", Colors.FAIL))
            sub_choice = int(input(color_text("DARKARMY~# ", Colors.BOLD)))
            if sub_choice == 1:
                lazyrecon()
            elif sub_choice == 2:
                redhawk()
            elif sub_choice == 3:
                th3inspector()
            elif sub_choice == 4:
                wpgrabinfo()
            elif sub_choice == 5:
                billcipher()
            elif sub_choice == 6:
                gasmask()
            elif sub_choice == 7:
                webkiller()
            elif sub_choice == 8:
                fbi()
            elif sub_choice == 9:
                dtect()
            elif sub_choice == 10:
                userrecon()
            elif sub_choice == 11:
                owscan()
            elif sub_choice == 99:
                menu()
            else:
                print(color_text("Invalid option! Please try again.", Colors.FAIL))
                time.sleep(1)
                menu()
        elif choice == 2:
            # Vulnerability Analysis Tools
            clear_screen()
            logo()
            print(color_text("Vulnerability Analysis Tools:", Colors.OKGREEN))
            print(color_text("  {1}--Clickjacking Tester", Colors.OKCYAN))
            print(color_text("  {2}--TM Scanner", Colors.OKCYAN))
            print(color_text("  {3}--AndroBugs", Colors.OKCYAN))
            print(color_text("  {4}--ScanQLi", Colors.OKCYAN))
            print(color_text("  {5}--Commix", Colors.OKCYAN))
            print(color_text("  {6}--WPSeku", Colors.OKCYAN))
            print(color_text("  {7}--RouterSploit", Colors.OKCYAN))
            print(color_text("  {8}--Nikto", Colors.OKCYAN))
            print(color_text("  {99}--Back to Main Menu", Colors.FAIL))
            sub_choice = int(input(color_text("DARKARMY~# ", Colors.BOLD)))
            if sub_choice == 1:
                clickjacking_tester()
            elif sub_choice == 2:
                tm_scanner()
            elif sub_choice == 3:
                androbugs()
            elif sub_choice == 4:
                scanqli()
            elif sub_choice == 5:
                commix()
            elif sub_choice == 6:
                wpseku()
            elif sub_choice == 7:
                routersploit()
            elif sub_choice == 8:
                nikto()
            elif sub_choice == 99:
                menu()
            else:
                print(color_text("Invalid option! Please try again.", Colors.FAIL))
                time.sleep(1)
                menu()
        elif choice == 3:
            # Wireless Testing Tools
            clear_screen()
            logo()
            print(color_text("Wireless Testing Tools:", Colors.OKGREEN))
            print(color_text("  {1}--Reaver", Colors.OKCYAN))
            print(color_text("  {2}--Pixiewps", Colors.OKCYAN))
            print(color_text("  {3}--BluePot", Colors.OKCYAN))
            print(color_text("  {99}--Back to Main Menu", Colors.FAIL))
            sub_choice = int(input(color_text("DARKARMY~# ", Colors.BOLD)))
            if sub_choice == 1:
                reaver()
            elif sub_choice == 2:
                pixiewps()
            elif sub_choice == 3:
                bluepot()
            elif sub_choice == 99:
                menu()
            else:
                print(color_text("Invalid option! Please try again.", Colors.FAIL))
                time.sleep(1)
                menu()
        elif choice == 4:
            # Exploitation Tools
            clear_screen()
            logo()
            print(color_text("Exploitation Tools:", Colors.OKGREEN))
            print(color_text("  {1}--A-RAT", Colors.OKCYAN))
            print(color_text("  {2}--GoldenEye", Colors.OKCYAN))
            print(color_text("  {3}--Hulk", Colors.OKCYAN))
            print(color_text("  {4}--CMSeeK", Colors.OKCYAN))
            print(color_text("  {5}--Metasploit", Colors.OKCYAN))
            print(color_text("  {6}--TM-Venom", Colors.OKCYAN))
            print(color_text("  {7}--Zarp", Colors.OKCYAN))
            print(color_text("  {8}--AutoSploit", Colors.OKCYAN))
            print(color_text("  {9}--EggShell", Colors.OKCYAN))
            print(color_text("  {10}--Brutal", Colors.OKCYAN))
            print(color_text("  {99}--Back to Main Menu", Colors.FAIL))
            sub_choice = int(input(color_text("DARKARMY~# ", Colors.BOLD)))
            if sub_choice == 1:
                arat()
            elif sub_choice == 2:
                goldeneye()
            elif sub_choice == 3:
                hulk()
            elif sub_choice == 4:
                cmseek()
            elif sub_choice == 5:
                metasploit()
            elif sub_choice == 6:
                tmvenom()
            elif sub_choice == 7:
                zarp()
            elif sub_choice == 8:
                autosploit()
            elif sub_choice == 9:
                eggshell()
            elif sub_choice == 10:
                brutal()
            elif sub_choice == 99:
                menu()
            else:
                print(color_text("Invalid option! Please try again.", Colors.FAIL))
                time.sleep(1)
                menu()
        elif choice == 5:
            # Sniffing & Spoofing Tools
            clear_screen()
            logo()
            print(color_text("Sniffing & Spoofing Tools:", Colors.OKGREEN))
            print(color_text("  {1}--SEToolkit", Colors.OKCYAN))
            print(color_text("  {2}--SSLStrip", Colors.OKCYAN))
            print(color_text("  {3}--PyPhisher", Colors.OKCYAN))
            print(color_text("  {4}--SMTP Mailer", Colors.OKCYAN))
            print(color_text("  {5}--Python Packet Sniffer", Colors.OKCYAN))
            print(color_text("  {99}--Back to Main Menu", Colors.FAIL))
            sub_choice = int(input(color_text("DARKARMY~# ", Colors.BOLD)))
            if sub_choice == 1:
                setoolkit()
            elif sub_choice == 2:
                ssls()
            elif sub_choice == 3:
                pyphisher()
            elif sub_choice == 4:
                smtp_mailer()
            elif sub_choice == 5:
                python_packet_sniffer()
            elif sub_choice == 99:
                menu()
            else:
                print(color_text("Invalid option! Please try again.", Colors.FAIL))
                time.sleep(1)
                menu()
        elif choice == 6:
            # Android Hacking Tools
            clear_screen()
            logo()
            print(color_text("Android Hacking Tools:", Colors.OKGREEN))
            print(color_text("  {1}--AndroRAT", Colors.OKCYAN))
            print(color_text("  {2}--CSploit", Colors.OKCYAN))
            print(color_text("  {3}--TheFatRat", Colors.OKCYAN))
            print(color_text("  {99}--Back to Main Menu", Colors.FAIL))
            sub_choice = int(input(color_text("DARKARMY~# ", Colors.BOLD)))
            if sub_choice == 1:
                androrat()
            elif sub_choice == 2:
                csploit()
            elif sub_choice == 3:
                thefatrat()
            elif sub_choice == 99:
                menu()
            else:
                print(color_text("Invalid option! Please try again.", Colors.FAIL))
                time.sleep(1)
                menu()
        elif choice == 7:
            # Brute Force Tools
            clear_screen()
            logo()
            print(color_text("Brute Force Tools:", Colors.OKGREEN))
            print(color_text("  {1}--SocialBox", Colors.OKCYAN))
            print(color_text("  {2}--BluForce-FB", Colors.OKCYAN))
            print(color_text("  {3}--FaceBoom", Colors.OKCYAN))
            print(color_text("  {4}--Instagram", Colors.OKCYAN))
            print(color_text("  {5}--Instabrute", Colors.OKCYAN))
            print(color_text("  {6}--Brute-force-gmail", Colors.OKCYAN))
            print(color_text("  {7}--GmailBruterV2", Colors.OKCYAN))
            print(color_text("  {8}--WPBrute", Colors.OKCYAN))
            print(color_text("  {9}--Cpanel-Bruter", Colors.OKCYAN))
            print(color_text("  {10}--RDP-Brute", Colors.OKCYAN))
            print(color_text("  {99}--Back to Main Menu", Colors.FAIL))
            sub_choice = int(input(color_text("DARKARMY~# ", Colors.BOLD)))
            if sub_choice == 1:
                socialbox()
            elif sub_choice == 2:
                bluforce_fb()
            elif sub_choice == 3:
                faceboom()
            elif sub_choice == 4:
                instagram()
            elif sub_choice == 5:
                instabrute()
            elif sub_choice == 6:
                brute_force_gmail()
            elif sub_choice == 7:
                gmailbruterv2()
            elif sub_choice == 8:
                wpbrute()
            elif sub_choice == 9:
                cpanel_bruter()
            elif sub_choice == 10:
                rdp_brute()
            elif sub_choice == 99:
                menu()
            else:
                print(color_text("Invalid option! Please try again.", Colors.FAIL))
                time.sleep(1)
                menu()
        elif choice == 8:
            # Phishing Tools
            clear_screen()
            logo()
            print(color_text("Phishing Tools:", Colors.OKGREEN))
            print(color_text("  {1}--Shellphish", Colors.OKCYAN))
            print(color_text("  {2}--HiddenEye", Colors.OKCYAN))
            print(color_text("  {3}--SocialFish", Colors.OKCYAN))
            print(color_text("  {4}--Zphisher", Colors.OKCYAN))
            print(color_text("  {5}--Blackeye", Colors.OKCYAN))
            print(color_text("  {99}--Back to Main Menu", Colors.FAIL))
            sub_choice = int(input(color_text("DARKARMY~# ", Colors.BOLD)))
            if sub_choice == 1:
                shellphish()
            elif sub_choice == 2:
                hiddeneye()
            elif sub_choice == 3:
                socialfish()
            elif sub_choice == 4:
                zphisher()
            elif sub_choice == 5:
                blackeye()
            elif sub_choice == 99:
                menu()
            else:
                print(color_text("Invalid option! Please try again.", Colors.FAIL))
                time.sleep(1)
                menu()
        elif choice == 9:
            # OS Installer
            print("OS Installer - Coming Soon!")
            time.sleep(2)
            menu()
        elif choice == 0:
            # Credits
            clear_screen()
            logo()
            print(color_text("Coded by Amn3sia - be honored", Colors.OKGREEN))
            print(color_text("Visit our website: https://darkarmy.live/", Colors.OKCYAN))
            print(color_text("GitHub: https://github.com/D4RK-4RMY/DARKARMY", Colors.OKCYAN))
            print(color_text("Happy Hacking!", Colors.OKGREEN))
            input("Press Enter to return to main menu...")
            menu()
        elif choice == 99:
            print(color_text("Exiting DARKARMY...", Colors.WARNING))
            clear_screen()
            sys.exit(0)
        else:
            print(color_text("Invalid option! Please try again.", Colors.FAIL))
            time.sleep(1)
            menu()
    except KeyboardInterrupt:
        print(color_text("\nExiting...", Colors.WARNING))
        clear_screen()
        sys.exit(0)
    except Exception as e:
        print(color_text(f"An error occurred: {str(e)}", Colors.FAIL))
        time.sleep(2)
        menu()

def main():
    menu()

if __name__ == "__main__":
    main()

