#!/bin/bash

if [ $UID -eq 0 ]; then
    echo "Execution du script Docker !"
    apt install docker.io
    docker build -t autosint .
    echo "Installation terminée ! Tapez : 'docker run autosint' pour que lancer AutOsint !"
else
  echo "Le script doit être lancé en tant que root"
fi