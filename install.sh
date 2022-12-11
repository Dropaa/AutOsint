#!/bin/bash

if [ $UID -eq 0 ]; then
    echo "Execution du script d'installation"
    mkdir VenvProjet/logs
    git clone https://github.com/rbsec/dnscan.git
    cd dnscan && pip install -r requirements.txt
    cd ../ && pip install -r requirements.txt
    apt install theharvester
else
  echo "Le script doit être lancé en tant que root"
fi