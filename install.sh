sudo activate-global-python-argcomplete
pipx install `cat requirements.txt"
eval "$(register-python-argcomplete main.py)"
chmod +x main.py
