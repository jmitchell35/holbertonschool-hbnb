# Correction de la partie 4

## Pre-requis

Les instructions d'installation sont pensées pour un utilisateur WSL2 ou Ubuntu via l'interface en lignes de commandes.

## Set up

Il suffit de cloner le repo. J'ai laissé la BDD avec des users et des places.

```bash
git clone https://github.com/jmitchell35/holbertonschool-hbnb.git
```

Le back est dans le répertoire part3.
Creer un environnement virtuel avec venv et/ou pyenv.

```bash
python3 -m venv venv
```
OU
```bash
# Install dependencies
sudo apt-get update
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

# Install pyenv
curl https://pyenv.run | bash
```

Installer une version de l'interpreteur python dans pyenv
```bash
# List available Python versions
pyenv install --list

# Install a specific version
pyenv install 3.9.22

# Select version for local directory
pyenv local 3.9.22

# Then only create venv
python -m venv venv

# venv directory can also be hidden as one sees fit
python -m venv .venv
```

Activer l'environnement virtuel
```bash
source venv/bin/activate
```

Installer les requirements
```bash
pip install -r requirements.txt
```

Run le serveur :
```bash
python run.py
```

Le client peut être testé via Live Server sur VS Code ou toute autre forme d'hébergement en local.

admin : admin@gmail.com / 12345
Axel : axel.gore@holbertonschool.com / password

## Faire des requêtes en back au besoin

J'ai inclus la Collection Postman avec les requêtes de la partie 3 au besoin.

https://github.com/jmitchell35/holbertonschool-hbnb/blob/main/part4/HBNB%20part3.postman_collection.json
