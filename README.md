AutOsint
======
AutOsint est un outil automatisé permettant la recherche d'informations en sources ouvertes.
Le script se base sur 4 outils pour sa recherche :
- TheHarvester
- Shodan
- URLScan
- Dnscan

Setup
-----
Le setup de l'outil se fait automatiquement via le script install.sh et nécéssite une connexion internet
#### Execution du script d'installation
    chmod +x install.sh && ./install.sh

Usage
-----

#### Utilisation de la commande
    dnscan.py (-d | --domain \<domain\> )
    Domain = https://esgi.fr 

-----
Il est possible de choisir quels type d'outil seront lancer pendant l'éxécution d'AutOsint.
#### Modification du fichier de conf
    Pour désactiver l'utilisation d'URLScan, on passe l'argument à false dans le fichier conf.json 
    "urlscan": false,
