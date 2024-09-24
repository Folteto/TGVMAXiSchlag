sudo activate-global-python-argcomplete
pipx install -r requirement.txt
eval "$(register-python-argcomplete main.py)"
chmod +x main.py
