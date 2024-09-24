#!/bin/bash

sudo activate-global-python-argcomplete
sudo apt install python-argparse
eval "$(register-python-argcomplete main.py)"
chmod +x main.py
zshrc_file="$HOME/.zshrc"

if ! grep -q "autoload -U compinit; compinit" "$zshrc_file"; then
  echo "La commande 'compinit' n'est pas présente dans le fichier .zshrc. Ajout de la commande..."
  echo "autoload -U compinit; compinit" >> "$zshrc_file"
  else 
  echo "nope"
fi
