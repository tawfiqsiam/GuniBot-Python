#!/usr/bin/env python
#coding=utf-8

import random

traducteur={"Monday":"Lundi",
            "Tuesday":"Mardi",
            "Wednesday":"Mercredi",
            "Thursday":"Jeudi",
            "Friday":"Vendredi",
            "Satudray":"Samedi",
            "Sunday":"Dimanche",
            "January":"Janvier",
            "Jan ":"Janvier ",
            "February":"Février ",
            "Feb ":"Février ",
            "March":"Mars",
            "April":"Avril",
            "Apr":"Avril",
            "May":"Mai",
            "June":"Juin",
            "July":"Juillet",
            "August":"Aout",
            "September":"Septembre",
            "October":"Octobre",
            "November":"Novembre",
            "December":"Décembre",
            "Direct Message with":"MP avec",
            "idle":"inactif",
            "online":"connecté",
            "None":"Rien",
            "dnd":"ne pas déranger",
            "offline":"déconnecté",
            "Mon,":"Lundi",
            "Tue,":"Mardi",
            "Wed,":"Mercredi",
            "Fri,":"Vendredi",
            "Sat,":"Samedi",
            "Sun,":"Samedi"
            }

month={'1':'Janvier',
       '2':'Février',
       '3':'Mars',
       '4':'Avril',
       '5':'Mai',
       '6':'Juin',
       '7':'Juillet',
       '8':'Aout',
       '9':'Septembre',
       '10':'Octobre',
       '11':'Novembre',
       '12':'Décembre'}

day={'1':'Lundi',
     '2':'Mardi',
     '3':'Mercredi',
     '4':'Jeudi',
     '5':'Vendredi',
     '6':'Samedi',
     '7':'Dimanche'}

pan_msg={"AÏE ! Non mais ça va pas de tirer sur les bots comme ça {1} ?!":98,
         "Bien joué ! Tu as abattu un {0} sauvage !":50,
         "Oouuuuhhhh !!!! Le caribooouuuuu !!!!":25,
         ":duck: < QUAAK":10,
         "_X< COUAC":10,
         "Bravo {1} !!!!! Tu as explosé un cookie !":45,
         "{1} viens d'abattre un de ces multiples et envahissants pigeons, GG":10,
         "BZZZZZZ Sprotch (R.I.P. Mouche)":10,
         "{1} a tué un chasseur. Merci à lui, ces tueurs abattent trop d'animaux.":30,
         ":dog2:< OUAF":10,
         "-1 prof de philo":50,
         "{1} a fait tomber la statue de la Liberté :statue_of_liberty:":70,
         "Ton tir a ouvert le coffre de la Banque de France :euro:":60,
         "{1} a détruit un chocolat liégeois :chocolate_bar:":10,
         "{1} a tué le respect.":40,
         "*The translator has been destroyed*":25,
         "{1} vient de tirer sur {0} en nettoyant son fusil":60,
         "Un utilisateur Skype a été abattu par {1}.":40,
         "Le tir touche la carrosserie d'une voiture, ce qui, bien évidemment, la fait exploser.":25,
         "Une centrale nucléaire est touchée, provoquant une terrible explosion qui rase plusieurs kilomètres de la carte":75,
         "**HEADSHOT** sur {0} !":75,
         ":gun: {1}":50,
         "{1} s'est tiré dessus":-20,
         "{1} a détruit l'Anneau, mettant fin au règne de Sauron.":80,
         "Bravo !!!!! Tu as explosé un cookie légendaire !":95,
         "Vous venez d'offrir un cookie à Pikachu. Trop mignon !":85,
         "La balle a détruit la musique *Despacito*":50,
         ":chicken:< COT COT COT":10,
         ":turkey:< GLOUGLOU":10,
         ":dragon_face:< ROOAAAR":20,
         "{1} a décroché la Lune :full_moon:":40,
         "Le Soleil est tombé :sunny:":40,
         "Un vaisseau alien est détruit, arrêtant net l'invasion en cours :space_invader:":40,
         "Régicide :prince:":30,
         "{1} tire sur un bidon d'essence, atomisant une troupe de zombies touristes":25,
         "**M-M-M-MONSTERKILL** :fire:":70,
         ":cow:< MEEEUUUH":10,
         "La balle a abattu un arbre, pense donc aux écologistes {1} <:divineanger:414882760159789056>":-10,
         "Shérif touché, prison occupée par {1}":-10,
         "Oh mon dieu {1} vient d'abattre son propre ami ! :scream:":-20,
         "Oh le joli bamb.....**PANN**":10,
         "Tudududut Tudududut **BAM** en plein dans le réveil {1} :alarm_clock:":25,
         "Bravo, {1} vient d'éradiquer une colonie de frelons :thumbsup:":20,
         "{1} vient de tuer le roi canard :skull_crossbones: SPROTCH":-15,
         "Vous avez loupé votre cible":-20,
         "{1} a touché un *blurp*":-15,
         "La blurpelisation continue grâce à {1} !":+30,
         "<:blurple:443024761547653140> < *BLURP*":-5,
         "La balle de {1} heurte un champ de force et revient en arrière :leftwards_arrow_with_hook: ":-10,
         "{1} s'est tiré dans le pied :no_mouth:":-5
         }

special_pan={"{2} a été grièvement touché par {1}. Dommage pour lui...":-40,
             "{1} a tiré sur {2}, qui l'a très mal pris <:divineanger:414882760159789056>":-30,
             "Un Grand Corbeau touché, ça risque de te faire mal {1}...":-70
             }

kill_msg=["Oh toi, tu vas mourir !",
          "***BOUM !*** {1} est tombé dans un piège posé par {0} !",
          "Heureusement que le sol a amorti la chute de {1} !",
          "{0} a crié \"Fus Roh Dah\" alors que {1} était à coté d'une falaise...",
          "Eh non, tu ne peux pas arreter les balles avec tes mains {1} :shrug:",
          "Il faut être __dans__ l’ascenseur {1}, pas __au-dessus__...",
          "{1} est resté trop près des enceintes lors d'un concert de heavy metal",
          "Rester à moins de 10m d'une explosion atomique, ce n'était pas une bonne idée {1}...",
          "Non ! Les doubles sauts ne sont pas possibles {1} !",
          "{1} a imité Icare... splash.",
          "C'est bien d'avoir un pistolet à portails {1}, encore faut il ne pas en ouvrir un au dessus des piques....",
          "{1} est mort. Paix à son âme... :sneezing_face:",
          "{0} a tué {1}",
          "{1} a été shot par {0}",
          "Bye {1} ! :ghost:",
          "{1} a vu tomber une enclume volante... sur sa tête :head_bandage:",
          "{1} part se suicider après que {0} ai coupé sa connexion",
          "Attention {1} ! Le feu, ça brûle :fire:",
          "{1} est parti sans pelle lors d'une attaque zombie",
          "{1} a tenté de faire un calin à un creeper",
          "{1}, les bains de lave sont chauds, mais la lave, ça brûle...",
          "{1} a tenté un rocket jump",
          "Il ne fallait pas écouter la jolie mélodie de la Lullaby, {1} :musical_note:",
          "{2}.exe *a cessé de fonctionner*"]

bvn_msg = ["Un {user} sauvage apparaît !",
           "/summon {user} ~ ~ ~",
           "{user} est là pour tous nous sauver :tada:",
           "{user} join the game",
           "Fuyez pauvres fous ! {user} est sur vous !",
           "Hey, {user} joined us! It's a trap!",
           "{user} a rejoint. Vous devez construire des pylônes supplémentaires.",
           "Bienvenue, {user}. On espère que vous avez apporté de la pizza.",
           "{user} est ici, comme la prophétie l'avait annoncé.",
           "Bienvenue {user} :wave:",
           "On dirait que {user} vient d'arriver !",
           "Bienvenue {user} ! J'espère que tu vas passer un agréable moment ici !",
           "Joueur {user} prêt",
           "new_Member(name={user}) - Bienvenue !"
           ]

modules=["admin","aide","bot","bvn","citations","clear","common","emoji","fr","fun","hunter","lang_tr","mc","modo","rss","server","stats","test","timer","utilities","vote","xp"]

levelup_msg=["Je suis Charlie, mais {0} monte niveau {1}","Je s'appelle Groot. Et {0} passe niveau {1}.","Hey, {0} n'est que niveau {1} <:shook:400355814394560532> ? Faut monter plus vite, allez !\n*Hurry up guys !*","{0} vient d'atteindre le niveau {1} !","Niveau {1} réussi pour {0} ! Congratulations !","Level up {0} ! Level {1} !","Vos compétences sont améliorées au niveau {1} {0}.","Attention à ne pas trop écrire {0}, tu passe déjà au niveau {1} :no_mouth:","Le niveau {1} fait passer vos dégâts et et vos PV à +{1}% {0}.","Vous êtes au niveau {1} {0}. Plus que ***fatal error system: number not found*** niveaux à obtenir pour être au level maximum.","Level {1} {0} !","On m'informe à l'instant que {0} vient de passer niveau {1} <:excusemewhat:418154673523130398>"]

osekour_msg=["Attends, je finis de regarder mon film","On arrive ! Mais pourquoi ne répondez-vous plus ? Ne simulez pas la mort !","Oui on sait qu'il y a du feu, on n'a pas besoin de venir : on fait un barbecue à la caserne","*Les secours sont actuellement indisponibles, veuillez attendre la fin de la pause*","*Ce numéro n'existe pas. Veuillez réessayer avec un autre numéro.*","*Maintenance de la ligne en cours. Veuillez réessayer d'ici 430 heures.*","*Votre forfait mobile est arrivé à son terme. Vous pouvez en racheter un pour 86,25€*","Encore 2 tomes du Seigneur des Anneaux à finir de lire, et je suis à vous !","Merci de ne pas nous déranger pendant les fêtes","Désolé, il y a plus de 3 flocons de neige: nous sommes coincés au garage","Il va falloir attendre la fin de notre grève... Comment ça, vous n'êtes pas au courant ?! Ça fait pourtant bien deux mois que nous avons commencé !"]

months=["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Décembre"]

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

commands_server=["(everyone) !infos","(everyone) !membercount","(everyone) !channelinfo [#channel]","(staff) !freeze <on|off>","(everyone) !roleinfo <role>","(staff) !purge","(everyone) !search <text>","(everyone) !stats [all|server|channel]","(owner) !bvn","(everyone) !serverinfo","(everyone) !mc <item|entity|help> <data>","(owner) !sconfig <see|change|help> ...","(everyone) !invite [#salon]","(staff) !kick <user> [raison]","(staff) !ban <user> [raison]","(staff) !unban <userID>","(everyone) !find <user|channel|server|staff|help> <id|help>","(staff) !mute/unmute <user>","(everyone) !mutelist","(staff) !slowmode <secondes>","(staff) !slowoff","(everyone) !calc <calcul>","(staff) !clear <nombre|joueur> [true|false]","(everyone) !rss <youtube|twitter|web|help> <id|help>","(everyone) !vote <texte>","(everyone) !sondage <nombre> <texte>","(everyone) !top [nombre]","(everyone) !userinfo [nom|identifiant]","(everyone) !rank <someone>"]

commands_mp=["!infos","!mc <item|entity|help> <data>","!say <texte>","!calc <calcul>","!rss <youtube|twitter|web> <id>","!count","!vote <texte>","!sondage <nombre> <texte>","!fun","!rank [someone]","!top [nombre]"]


emojis={"thumbsup":"\U0001F44D",
        "thumbsdown":"\U0001F44E",
        "1":"1⃣",
        "2":"2⃣",
        "3":"3⃣",
        "4":"4⃣",
        "5":"5⃣",
        "6":"6⃣",
        "7":"7⃣",
        "8":"8⃣",
        "9":"9⃣",
        "10":"\U0001f51f"
        }

numbers_emojis = {"0":':zero:',
                  "1":':one:',
                  "2":':two:',
                  "3":':three:',
                  "4":':four:',
                  "5":':five:',
                  "6":':six:',
                  "7":':seven:',
                  "8":':eight:',
                  "9":':nine:',
                  "10":':keycap_ten: '
                  }

user_desc={'279568324260528128':"Un grand génie. Et accessoirement mon créateur",
           '411134209822949378':"Coucou ! C'est moi !",
           '375598088850505728':"Créateur de messages random, et un assez bon builder",
           '278611007952257034':"Un dev Linux/Android, créateur de plugin et plein d'autres choses",
           '348415857728159745':"Un dev de bots python, qui m'a beaucoup aidé :kissing_heart:",
           '286827468445319168':"Buildeur & Redstoneur Médiéval",
           "199615256882970624":"Staff de MEE6 très sympa, et fr !"
           }

user_img={'279568324260528128':'Zrunner.png',
          '375598088850505728':'Aragorn.png',
          '286827468445319168':'platon-neutron.png'
          }
