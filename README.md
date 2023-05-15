# TGVMAXiSchlag
Oyé chers confrères schlags qui êtes prêts à tout pour ne pas donner un centime de plus que votre abonnement TGVMAX à la SNCF ! Vous galérez à trouver des **TGVMAX** directs et vous en avez marre d'essayer toutes les gares de France en croisant les doigts pour que l'une d'elles vous permette de ne pas payer votre voyage ? Cet outil peut vous aider ;) 

# Fonctionnement

Cet outil se base sur l'API de la SNCF ouverte au public. Cette API n'étant pas actualisée en temps réel, il est possible que **l'outil affiche des trains qui n'existent pas**. Si tel est le cas, gardez votre calme, et changez votre jour de recherche, quelle idée aussi d'espérer avoir un Paris-Bordeaux un jeudi de pont ?!?

# Prérequis
Vous devez avoir les éléments suivants installés sur votre machine : 

- Python 3 
- Les libraires Python argparse & requests

# Usage

    python .\main.py  -d "<gare de départ>" -a "<gare d'arrivée>" -t <date>

## Syntaxe 
**Les gares** ont une syntaxe à respecter imposée par l'API SNCF. Pour afficher la liste des gares, entrer la commande suivante :

    python .\main.py -a "a" -d "a" -t 0 -l

> Les majuscules doivent être respectées.
> Cette liste se situe dans /data/gares.txt

**La date de voyage** doit être de la forme `aaaa-mm-jj`

## Options
Quatre options sont disponibles :

- `-l`: affiche la liste des gares 
- `-s`: indiquer un nombre maximum d'étapes pour votre voyage (2 par défaut) 
- `-f`: forcer la recherche jusqu'au nombre d'étapes indiquées par `-s`. Par défaut, le programme ne cherchera pas de trajets avec des étapes supplémentaires si il en a trouvé avec moins d'étapes. 
- `-p`: affiche la liste de tous les trajets TGVMAX disponibles depuis la gare indiquée à la date donnée. 

## Exemples 

    python .\main.py -d "PARIS (intramuros)" -a "STRASBOURG" -t 2023-05-18 -s 3 
    python .\main.py -a "TOULOUSE MATABIAU" -d "BORDEAUX ST JEAN" -t 2023-12-05 -s 3 -f
    python .\main.py -d "PARIS (intramuros)" -a "a" -t 2023-04-26 -p


 

# Ajouts futurs

Idéalement, il faudra rendre de manière globale l'outil plus simple et agréable à utiliser. On pourra envisager une adaptation web. 