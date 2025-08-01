#!/usr/bin/env python3
"""
DARKARMY v2 - Refactored version of darkarmy.py for Python 3
Coded by Amn3sia - be honored
"""


import sys
import os
import time
import re
import socket
import logging
import subprocess
import requests
from urllib.parse import urlparse
from threading import Thread
from queue import Queue

# Color utility for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def color_text(text, color):
    return f"{color}{text}{Colors.ENDC}"

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Directories and shells lists (same as original)
DIRECTORIES = [
    '/uploads/', '/upload/', '/files/', '/resume/', '/resumes/', '/documents/', '/docs/', '/pictures/',
    '/file/', '/Upload/', '/Uploads/', '/Resume/', '/UsersFiles/', '/Usersiles/', '/usersFiles/',
    '/Users_Files/', '/UploadedFiles/', '/Uploaded_Files/', '/uploadedfiles/', '/uploadedFiles/',
    '/hpage/', '/admin/upload/', '/admin/uploads/', '/admin/resume/', '/admin/resumes/', '/admin/pictures/',
    '/pics/', '/photos/', '/Alumni_Photos/', '/alumni_photos/', '/AlumniPhotos/', '/users/'
]

SHELLS = [
    'wso.php', 'shell.php', 'an.php', 'hacker.php', 'lol.php', 'up.php', 'cp.php', 'upload.php',
    'sh.php', 'pk.php', 'mad.php', 'x00x.php', 'worm.php', '1337worm.php', 'config.php', 'x.php', 'haha.php'
]

YES = {'yes', 'y', 'ye', 'Y'}
NO = {'no', 'n'}


def clear_screen():
    """Clear the terminal screen."""
    if os.name == 'posix':
        subprocess.run(['clear'])
    elif os.name == 'nt':
        subprocess.run(['cls'])


def unique(seq):
    """Return a list of unique items, preserving order."""
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]


def get_input(prompt, validation_type=None):
    """Get user input safely with optional validation."""
    while True:
        try:
            user_input = input(prompt).strip()
            if validation_type == "integer":
                if not user_input.isdigit():
                    print("Invalid input. Please enter a number.")
                    continue
                return int(user_input)
            elif validation_type == "yes_no":
                if user_input.lower() not in YES and user_input.lower() not in NO:
                    print("Invalid input. Please enter 'y' or 'n'.")
                    continue
                return user_input
            elif validation_type == "ip_address":
                try:
                    socket.inet_aton(user_input)
                    return user_input
                except socket.error:
                    print("Invalid IP address format.")
                    continue
            elif validation_type == "port_range":
                if re.match(r"^\d+-\d+$", user_input):
                    start, end = map(int, user_input.split('-'))
                    if 0 <= start <= 65535 and 0 <= end <= 65535 and start <= end:
                        return user_input
                    else:
                        print("Invalid port range. Ports must be between 1-65535 and start must be less than or equal to end.")
                else:
                    print("Invalid port range format. Use start-end (e.g., 1-1000).")
                continue
            return user_input
        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            sys.exit(0)


def updatedarkarmy():
    import os
    print("This Tool is Only Available for Linux and Similar Systems.")
    choiceupdate = input("Continue Y / N: ")
    if choiceupdate.lower() in ['yes', 'y']:
        try:
            if os.path.exists("DARKARMY"):
                subprocess.run(["darkarmy"], check=True)
            else:
                subprocess.run(["git", "clone", "https://github.com/graham-creator/D4RKARMY.git"], check=True)
                subprocess.run(["sudo", "bash", "./update.sh"], cwd="DARKARMY", check=True)
                subprocess.run(["darkarmy"], check=True)
        except subprocess.CalledProcessError as e:
            logging.error(f"Command failed: {e}")
        except FileNotFoundError:
            logging.error("Required command not found. Make sure git and darkarmy are installed and in your PATH.")

def sitechecker():
    print("[*] Running Shell Checker (Placeholder)")
    # Add actual implementation here, e.g., subprocess.run(["python", "shell_checker.py"])

def poet():
    print("[*] Running POET (Placeholder)")
    # Add actual implementation here

def weeman():
    print("[*] Running Phishing Framework (Weeman) (Placeholder)")
    # Add actual implementation here, e.g., subprocess.run(["weeman"])

def postexp():
    clear_screen()
    print(color_text("   {1}--Shell Checker", Colors.OKGREEN))
    print(color_text("   {2}--POET", Colors.OKGREEN))
    print(color_text("   {3}--Phishing Framework \n", Colors.OKGREEN))
    print(color_text("   {99}-Return to main menu \n\n ", Colors.FAIL))
    choice11 = get_input(color_text("DARKARMY~# ", Colors.BOLD), validation_type="integer")
    clear_screen()
    if choice11 == 1:
        sitechecker()
    elif choice11 == 2:
        poet()
    elif choice11 == 3:
        weeman()
    elif choice11 == 99:
        menu()

def passwd() -> None:
    """Password attack menu with input validation."""
    print(color_text("   {1}--Cupp ", Colors.OKGREEN))
    print(color_text("   {2}--Ncrack \n ", Colors.OKGREEN))
    print(color_text("   {99}-Back To Main Menu \n", Colors.FAIL))
    choice3 = get_input(color_text("DARKARMY~# ", Colors.BOLD), validation_type="integer")
    if choice3 == 1:
        clear_screen()
        cupp()
    elif choice3 == 2:
        clear_screen()
        ncrack()
    elif choice3 == 99:
        clear_screen()
        menu()
    elif choice3 == 3:
        fb()
    else:
        menu()

def fb():
    print("[*] Running fb (Placeholder)")

def cupp():
    print("[*] Running cupp (Placeholder)")

def ncrack():
    print("[*] Running ncrack (Placeholder)")

def setoolkit():
    import os
    print("The Social-Engineer Toolkit is an open-source penetration testing framework")
    choice = input("y / n :")
    if choice.lower() in ['yes', 'y']:
        try:
            if os.path.exists("social-engineer-toolkit"):
                subprocess.run(["python", "social-engineer-toolkit/setup.py"], check=True)
            else:
                subprocess.run(["git", "clone", "https://github.com/trustedsec/social-engineer-toolkit.git"], check=True)
                subprocess.run(["python", "social-engineer-toolkit/setup.py"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error during setoolkit installation: {e}")
    elif choice.lower() in ['no', 'n']:
        clear_screen()
        info()
    elif choice == "":
        menu()
    else:
        menu()

def ssls():
    import os
    print("sslstrip is a MITM tool that implements Moxie Marlinspike's SSL stripping attacks.")
    choice = input("y / n :")
    if choice.lower() in ['yes', 'y']:
        try:
            if os.path.exists("sslstrip"):
                subprocess.run(["python", "sslstrip/setup.py"], check=True)
            else:
                subprocess.run(["git", "clone", "https://github.com/moxie0/sslstrip.git"], check=True)
                subprocess.run(["sudo", "apt-get", "install", "-y", "python-twisted-web"], check=True)
                subprocess.run(["python", "sslstrip/setup.py"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error during sslstrip installation: {e}")
    elif choice.lower() in ['no', 'n']:
        snif()
    elif choice == "":
        menu()
    else:
        menu()

def pisher():
    import os
    print("HTTP server for phishing in python. (and framework) Usually you will want to run Weeman with DNS spoof attack. (see dsniff, ettercap).")
    choice = input("Install Weeman ? Y / N : ")
    if choice.lower() in ['yes', 'y']:
        try:
            if os.path.exists("weeman"):
                subprocess.run(["python", "weeman/weeman.py"], check=True)
            else:
                subprocess.run(["git", "clone", "https://github.com/samyoyo/weeman.git"], check=True)
                subprocess.run(["python", "weeman/weeman.py"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error during weeman installation: {e}")
    elif choice.lower() in ['no', 'n']:
        menu()
    else:
        menu()

def smtpsend():
    import subprocess
    try:
        subprocess.run(["wget", "http://pastebin.com/raw/Nz1GzWDS", "--output-document=smtp.py"], check=True)
        subprocess.run(["python", "smtp.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running SMTP Mailer: {e}")

def Fscan(ip):
    print(f"[*] Running Fscan on {ip} (Placeholder)")
    # Placeholder for actual Fscan implementation

def nmap():
    import os
    choice7 = input("continue ? Y / N : ")
    if choice7.lower() in ['yes', 'y']:
        try:
            if os.path.exists("nmap"):
                subprocess.run(["./configure"], cwd="nmap", check=True)
                subprocess.run(["make"], cwd="nmap", check=True)
                subprocess.run(["make", "install"], cwd="nmap", check=True)
            else:
                subprocess.run(["git", "clone", "https://github.com/nmap/nmap.git"], check=True)
                subprocess.run(["./configure"], cwd="nmap", check=True)
                subprocess.run(["make"], cwd="nmap", check=True)
                subprocess.run(["make", "install"], cwd="nmap", check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error during nmap installation: {e}")
    elif choice7.lower() in ['no', 'n']:
        info()
    elif choice7 == "":
        menu()
    else:
        menu()

def ports():
    clear_screen()
    target = input('Select a Target IP : ')
    import subprocess
    try:
        subprocess.run(["nmap", "-O", "-Pn", target], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running nmap ports scan: {e}")
    sys.exit()

def h2ip():
    host = input("Select A Host : ")
    import socket
    try:
        ips = socket.gethostbyname(host)
        print(ips)
    except socket.gaierror:
        print("Invalid host or unable to resolve.")

def wpue():
    import os
    import subprocess
    try:
        if os.path.exists("wpscan"):
            target = input("Select a Wordpress target : ")
            subprocess.run(["ruby", "wpscan/wpscan.rb", "--url", target, "--enumerate", "u"], check=True)
        else:
            subprocess.run(["git", "clone", "https://github.com/wpscanteam/wpscan.git"], check=True)
            target = input("Select a Wordpress target : ")
            subprocess.run(["ruby", "wpscan/wpscan.rb", "--url", target, "--enumerate", "u"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running wpue: {e}")

def cmsscan():
    import os
    import subprocess
    try:
        if os.path.exists("CMSmap"):
            target = input("select target : ")
            subprocess.run(["sudo", "cmsmap.py", target], cwd="CMSmap", check=True)
        else:
            subprocess.run(["git", "clone", "https://github.com/Dionach/CMSmap.git"], check=True)
            target = input("select target : ")
            subprocess.run(["sudo", "cmsmap.py", target], cwd="CMSmap", check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running cmsscan: {e}")

def XSStrike():
    import os
    import subprocess
    try:
        if os.path.exists("XSStrike"):
            subprocess.run(["pip", "install", "-r", "XSStrike/requirements.txt"], check=True)
            subprocess.run(["python", "XSStrike/xsstrike.py"], check=True)
        else:
            subprocess.run(["sudo", "rm", "-rf", "XSStrike"], check=True)
            subprocess.run(["git", "clone", "https://github.com/UltimateHackers/XSStrike.git"], check=True)
            subprocess.run(["pip", "install", "-r", "XSStrike/requirements.txt"], check=True)
            subprocess.run(["python", "XSStrike/xsstrike.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running XSStrike: {e}")

def doork():
    import os
    import subprocess
    choice = input("Continue Y / N: ")
    if choice.lower() in ['yes', 'y']:
        try:
            subprocess.run(["pip", "install", "beautifulsoup4", "requests"], check=True)
            if os.path.exists("doork"):
                target = input("Target : ")
                subprocess.run(["python", "doork/doork.py", "-t", target, "-o", "log.log"], check=True)
            else:
                subprocess.run(["git", "clone", "https://github.com/AeonDave/doork"], check=True)
                target = input("Target : ")
                subprocess.run(["python", "doork/doork.py", "-t", target, "-o", "log.log"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running doork: {e}")

def scanusers():
    site = input('Enter a website : ')
    try:
        users = site
        if 'http://www.' in users:
            users = users.replace('http://www.', '')
        if 'http://' in users:
            users = users.replace('http://', '')
        if '.' in users:
            users = users.replace('.', '')
        if '-' in users:
            users = users.replace('-', '')
        if '/' in users:
            users = users.replace('/', '')
        while len(users) > 2:
            print(users)
            import urllib.request
            resp = urllib.request.urlopen(site + '/cgi-sys/guestbook.cgi?user=%s' % users).read().decode()
            if 'invalid username' not in resp.lower():
                print("\tFound -> %s" % users)
            users = users[:-1]
    except Exception as e:
        print(f"Error scanning users: {e}")

def crips():
    print("[*] Running crips (Placeholder)")

def webhack():
    print("[*] Running webhack (Placeholder)")

def wire():
    print(color_text("   {1}--reaver ", Colors.OKGREEN))
    print(color_text("   {2}--pixiewps", Colors.OKGREEN))
    print(color_text("   {3}--Bluetooth Honeypot GUI Framework", Colors.OKGREEN))
    print(color_text("   {4}--Fluxion\n", Colors.OKGREEN))
    print(color_text("   {99}-Back To The Main Menu \n\n", Colors.FAIL))
    choice4 = get_input(color_text("DARKARMY~# ", Colors.BOLD), validation_type="integer")
    if choice4 == 1:
        clear_screen()
        reaver()
    elif choice4 == 2:
        clear_screen()
        pixiewps()
    elif choice4 == 3:
        bluepot()
    elif choice4 == 4:
        fluxion()
    elif choice4 == 99:
        menu()

def reaver():
    print("[*] Running Reaver (Placeholder)")

def pixiewps():
    print("[*] Running Pixiewps (Placeholder)")

def bluepot():
    print("[*] Running Bluetooth Honeypot GUI Framework (Bluepot) (Placeholder)")

def fluxion():
    print("[*] Running Fluxion (Placeholder)")

def exp():
    print(color_text("   {1}--ATSCAN", Colors.OKGREEN))
    print(color_text("   {2}--sqlmap", Colors.OKGREEN))
    print(color_text("   {3}--Shellnoob", Colors.OKGREEN))
    print(color_text("   {4}--commix", Colors.OKGREEN))
    print(color_text("   {5}--FTP Auto Bypass", Colors.OKGREEN))
    print(color_text("   {6}--jboss-autopwn", Colors.OKGREEN))
    print(color_text("   {7}--Blind SQL Automatic Injection And Exploit", Colors.OKGREEN))
    print(color_text("   {8}--Bruteforce the Android Passcode given the hash and salt", Colors.OKGREEN))
    print(color_text("   {9}--Joomla SQL injection Scanner \n ", Colors.OKGREEN))
    print(color_text("   {99}-Go Back To Main Menu \n\n", Colors.FAIL))
    choice5 = get_input(color_text("DARKARMY~# ", Colors.BOLD), validation_type="integer")
    if choice5 == 2:
        clear_screen()
        sqlmap()
    elif choice5 == 1:
        clear_screen()
        atscan()
    elif choice5 == 3:
        clear_screen()
        shellnoob()
    elif choice5 == 4:
        clear_screen()
        commix()
    elif choice5 == 5:
        clear_screen()
        gabriel()
    elif choice5 == 6:
        clear_screen()
        jboss()
    elif choice5 == 7:
        clear_screen()
        bsqlbf()
    elif choice5 == 8:
        androidhash()
    elif choice5 == 9:
        cmsfew()
    elif choice5 == 99:
        menu()

def sqlmap():
    print("[*] Running SQLMap (Placeholder)")

def atscan():
    print("[*] Running ATSCAN (Placeholder)")

def shellnoob():
    print("[*] Running Shellnoob (Placeholder)")

def commix():
    print("[*] Running Commix (Placeholder)")

def gabriel():
    print("[*] Running FTP Auto Bypass (Gabriel) (Placeholder)")

def jboss():
    print("[*] Running JBoss Autopwn (Placeholder)")

def bsqlbf():
    print("[*] Running Blind SQL Automatic Injection And Exploit (Placeholder)")

def androidhash():
    print("[*] Running Android Hash Bruteforce (Placeholder)")

def cmsfew():
    print("[*] Running Joomla SQL Injection Scanner (Placeholder)")

def snif():
    print(color_text("   {1}--Setoolkit ", Colors.OKGREEN))
    print(color_text("   {2}--SSLtrip", Colors.OKGREEN))
    print(color_text("   {3}--pyPISHER", Colors.OKGREEN))
    print(color_text("   {4}--SMTP Mailer \n ", Colors.OKGREEN))
    print(color_text("   {99}-Back To Main Menu \n\n", Colors.FAIL))
    choice6 = get_input(color_text("DARKARMY~# ", Colors.BOLD), validation_type="integer")
    if choice6 == 1:
        clear_screen()
        setoolkit()
    elif choice6 == 2:
        clear_screen()
        ssls()
    elif choice6 == 3:
        clear_screen()
        pisher()
    elif choice6 == 4:
        clear_screen()
        smtpsend()
    elif choice6 == 99:
        clear_screen()
        menu()

def dzz():
    clear_screen()
    aaa = input("Target IP : ")
    Fscan(aaa)

def info() -> None:
    """Information gathering menu with input validation."""
    print(darkarmy_logo)
    print(color_text("  {1}--Nmap ", Colors.OKGREEN))
    print(color_text("  {2}--Setoolkit", Colors.OKGREEN))
    print(color_text("  {3}--Port Scanning", Colors.OKGREEN))
    print(color_text("  {4}--Host To IP", Colors.OKGREEN))
    print(color_text("  {5}--wordpress user", Colors.OKGREEN))
    print(color_text("  {6}--CMS scanner", Colors.OKGREEN))
    print(color_text("  {7}--XSStrike", Colors.OKGREEN))
    print(color_text("  {8}--Dork - Google Dorks Passive Vulnerability Auditor ", Colors.OKGREEN))
    print(color_text("  {9}--Scan A server's Users  ", Colors.OKGREEN))
    print(color_text("  {10}-Crips\n  ", Colors.OKGREEN))
    print(color_text("  {99}-Back To Main Menu \n\n", Colors.FAIL))
    choice2 = get_input(color_text("DARKARMY~# ", Colors.BOLD), validation_type="integer")
    if choice2 == 1:
        clear_screen()
        nmap()
    elif choice2 == 2:
        clear_screen()
        setoolkit()
    elif choice2 == 3:
        clear_screen()
        ports()
    elif choice2 == 4:
        clear_screen()
        h2ip()
    elif choice2 == 5:
        clear_screen()
        wpue()
    elif choice2 == 6:
        clear_screen()
        cmsscan()
    elif choice2 == 7:
        clear_screen()
        XSStrike()
    elif choice2 == 8:
        clear_screen()
        doork()
    elif choice2 == 9:
        clear_screen()
        scanusers()
    elif choice2 == 10:
        clear_screen()
        crips()
    elif choice2 == 99:
        clear_screen()
        menu()
    else:
        menu()

def menu():
    while True:
        clear_screen()
        print(darkarmy_logo)
        print(color_text("   [!] Coded By Amn3sia[!]", Colors.WARNING))
        print(color_text("   {1}--Information Gathering", Colors.OKGREEN))
        print(color_text("   {2}--Password Attacks", Colors.OKGREEN))
        print(color_text("   {3}--Wireless Testing", Colors.OKGREEN))
        print(color_text("   {4}--Exploitation Tools", Colors.OKGREEN))
        print(color_text("   {5}--Sniffing & Spoofing", Colors.OKGREEN))
        print(color_text("   {6}--Android Hacking", Colors.OKGREEN))
        print(color_text("   {7}--Web Hacking", Colors.OKGREEN))
        print(color_text("   {8}--Private Web Hacking", Colors.OKGREEN))
        print(color_text("   {9}--Post Exploitation", Colors.OKGREEN))
        print(color_text("   {0}--Update The DARKARMY", Colors.OKGREEN))
        print(color_text("   {99}-Exit", Colors.FAIL))
        choice = get_input(color_text("DARKARMY~# ", Colors.BOLD), validation_type="integer")
        clear_screen()

        if choice == 1:
            info()
        elif choice == 2:
            passwd()
        elif choice == 3:
            wire()
        elif choice == 4:
            exp()
        elif choice == 5:
            snif()
        elif choice == 6:
            webhack()
        elif choice == 7:
            dzz()
        elif choice == 8:
            postexp()
        elif choice == 9:
            postexp()
        elif choice == 0:
            updatedarkarmy()
        elif choice == 99:
            clear_screen()
            sys.exit(0)
        else:
            continue


darkarmy_logo = (
    f"{Colors.WARNING}  \n"
    f"   _(`-')               (`-') <-.(`-') (`-')  _    (`-') <-. (`-')             \n"
    f"   (OO ).->         <-.(OO )  __( OO) (OO ).-/ <-.(OO )    \\(`-')_      .->   \n"
    f"{Colors.FAIL}"
    f"  \\    .'_    .---. ,------,)'-'. ,--./ ,---.  ,------,),--./  ,-.) ,--.'  ,-.\n"
    f" '`'-..__)  / .  | |   /`. '|  .'   /| \\ /`.\ |   /`. '|   `.'   |(`-')'.'  / \n"
    f" |  |  ' | / /|  | |  |_.' ||      /)'-'|_.' ||  |_.' ||  |'.'|  |(OO \\    /  \n"
    f" |  |  / :/ '-'  |||  .   .'|  .   '(|  .-.  ||  .   .'|  |   |  | |  /   /) \n"
    f" |  '-'  /`---|  |'|  |\\  \\ |  |\\   \\|  | |  ||  |\\  \\ |  |   |  | `-/   /`  \n"
    f" `------'     `--' `--' '--'`--' '--'`--' `--'`--' '--'`--'   `--'   `--'     \n"
    f"                                                     {Colors.ENDC}"
)

if __name__ == "__main__":
    menu()
