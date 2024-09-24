sudo activate-global-python-argcomplete
git clone https://github.com/Folteto/TGVMAXiSchlag.git
cd TGVMAXiSchlag
pipx install -r requirement.txt
eval "$(register-python-argcomplete main.py)"
chmod +x main.py
