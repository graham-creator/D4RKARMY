#!/bin/bash

set -e

# Colors for output
BLACK='\e[30m'
RED='\e[31m'
GREEN='\e[92m'
YELLOW='\e[33m'
ORANGE='\e[93m'
BLUE='\e[34m'
PURPLE='\e[35m'
CYAN='\e[96m'
WHITE='\e[37m'
NC='\e[0m'
purpal='\033[35m'

# Function to check if running as root
check_root() {
    if [ "$EUID" -ne 0 ]; then
        echo -e "${RED}[✘] Please run as root or use sudo.${NC}"
        exit 1
    fi
}



# Additional git clone command to ensure repo is cloned in current directory
if [ ! -d "D4RKARMY" ]; then
    echo -e "${CYAN}[>] Cloning DARKARMY repository in current directory...${NC}"
    git clone https://github.com/graham-creator/D4RKARMY.git || { echo -e "${RED}[✘] Failed to clone repository.${NC}"; exit 1; }
    echo -e "${GREEN}[✔] Repository cloned successfully in current directory.${NC}"
fi

# Function to show loading gauge
show_loading() {
    clear
    counter=1
    (
    while :
    do
        cat <<EOF
XXX
$counter
Loading DARKARMY INSTALLER ....
XXX
EOF
        (( counter+=20 ))
        [ $counter -eq 100 ] && break
        sleep 1
    done
    ) | whiptail --title " DARKARMY " --gauge "Please wait" 7 70 0
}

# Main installation function
install_darkarmy() {
    clear
    echo -e "${RED} "
    echo ""
    echo "  ██████   █████  ██████  ██   ██  █████  ██████  ███    ███ ██    ██        "
    echo "  ██   ██ ██   ██ ██   ██ ██  ██  ██   ██ ██   ██ ████  ████  ██  ██         "
    echo "  ██   ██ ███████ ██████  █████   ███████ ██████  ██ ████ ██   ████          "
    echo "  ██   ██ ██   ██ ██   ██ ██  ██  ██   ██ ██   ██ ██  ██  ██    ██           "
    echo "  ██████  ██   ██ ██   ██ ██   ██ ██   ██ ██   ██ ██      ██    ██  V2.1     "
    echo "                                                                             "
    echo "                                     Welcome To DARKARMY Installer           "
    echo -e "${GREEN}===================================================================${NC}"
    echo -e "${BLUE}   www.dark4rmy.in || https://github.com/graham-creator ${NC}"
    echo -e "${GREEN}===================================================================${NC}"
    echo -e "${RED}                                   [!] This Tool Must Run As ROOT [!]${NC}\n"
    echo ""
    echo -e "${CYAN}[>] Press ENTER to Install DARKARMYv2, CTRL+C to Abort.${NC}"
    read -r INPUT
    echo ""

    # Determine install directory
    if [ -n "$DARKARMY_INSTALL_DIR" ]; then
        INSTALL_DIR="$DARKARMY_INSTALL_DIR"
        BIN_DIR="$INSTALL_DIR/bin"
    else
        if [ "$PREFIX" = "/data/data/com.termux/files/usr" ]; then
            INSTALL_DIR="$PREFIX/usr/share/doc/DARKARMY"
            BIN_DIR="$PREFIX/usr/bin"
        else
            # Check if default directory is writable, else fallback to user home directory
            if [ -w "/usr/share/doc" ]; then
                INSTALL_DIR="/usr/share/doc/DARKARMY"
                BIN_DIR="/usr/bin"
            else
                echo -e "${YELLOW}[!] Default install directory /usr/share/doc is not writable. Falling back to user home directory.${NC}"
                INSTALL_DIR="$HOME/.darkarmy"
                BIN_DIR="$HOME/.local/bin"
                mkdir -p "$BIN_DIR"
                echo -e "${GREEN}[✔] Using install directory: $INSTALL_DIR${NC}"
                echo -e "${GREEN}[✔] Using bin directory: $BIN_DIR${NC}"
            fi
        fi
    fi

    echo "[✔] Checking directories..."
    if [ -d "$INSTALL_DIR" ]; then
        echo -e "[!] A Directory DARKARMY Was Found.. Do You Want To Replace It ? [y/n]:"
        read -r mama
        while [[ ! "$mama" =~ ^[YyNn]$ ]]; do
            echo "Please enter y or n:"
            read -r mama
        done
        if [[ "$mama" =~ ^[Yy]$ ]]; then
            rm -rf "$INSTALL_DIR" || { echo -e "${RED}[✘] Failed to remove existing directory.${NC}"; exit 1; }
        else
            echo "Installation aborted."
            exit 0
        fi
    fi

    echo "[✔] Installing ..."
    mkdir -p "$INSTALL_DIR" || { echo -e "${RED}[✘] Failed to create install directory.${NC}"; exit 1; }
    cp darkarmy_v2.py "$INSTALL_DIR/" || { echo -e "${RED}[✘] Failed to copy darkarmy_v2.py.${NC}"; exit 1; }

    # Create wrapper script
    echo "#!/bin/bash
python3 $INSTALL_DIR/darkarmy_v2.py" '${1+"$@"}' > DARKARMY
    chmod +x DARKARMY
    sudo cp DARKARMY "$BIN_DIR/" || { echo -e "${RED}[✘] Failed to copy wrapper script to $BIN_DIR.${NC}"; exit 1; }
    rm DARKARMY

    if [ -d "$INSTALL_DIR" ]; then
        echo ""
        echo -e "[✔] Successfully Installed DARKARMYv2 !!! \n\n"
        echo -e "${GREEN}       [+]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[+]"
        echo      "       [+]                                                             [+]"
        echo -e "${GREEN}       [+]     ✔✔✔ Now Just Type In Terminal (DARKARMY) ✔✔✔         [+]"
        echo      "       [+]                                                             [+]"
        echo -e "${GREEN}       [+]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[+]"
    else
        echo -e "${RED}[✘] Installation Failed. Please try again. [✘]"
        exit 1
    fi
}

# Run script
check_root



show_loading
install_darkarmy
