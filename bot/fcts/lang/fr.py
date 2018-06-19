#!/usr/bin/env python
#coding=utf-8

fun = {
    "count-0":"Comptage des messages...",
    "count-1":"Vous avez posté {count} messages dans ce salon",
    "msg-0":"{0} vient d'offrir une boite de cookies à <@375598088850505728> ! <:cookies_eat:421791321410240514>",
    "msg-1":"Coucou :wave: Je suis là {0}",
    "msg-2":":wave: Coucou ! Je suis là !\nTu voulais peut-être dire `!help` ?",
    "msg-3":"Youpi ! C'est l'heure de faire la fête !",
    "msg-4":"Vous souhaitez reporter un membre ou un serveur à l'équipe de Discord ? C'est par ici",
    "msg-5":"Impossible de trouver le message correspondant. Il faut rentrer l'ID du message en 1er argument, et l'émoji en 2e :upside_down:",
    "msg-6":"Raté, c'est tombé sur la tranche !",
    "msg-7":["{0} a été épargné par Thanos","Thanos a décidé de réduire {0} en cendres. Pour le bien de l'humanité..."],
    "invitation-0":"Oops, je n'ai pas les permissions de créer une invitation (\"Gérer le serveur\")",
    "invitation-1":"__**Lien d'invitation du serveur :**__\n\n:incoming_envelope: Voici un lien d'invitation pour le salon {} (Il lui reste encore {} utilisations - {} secondes) : ",
    "calc-0":"Oups, erreur de calcul",
    "calc-1":"<:maths:451067921121148937> | Vous pouvez utiliser cette commande pour effectuer un calcul, tels que des sommes, produits...\n\
Vous avez aussi accès à d'autres sortes de calculs plus élaborés comme les nombres random. Il vous suffit pour cela de rentrer random()`, ou `randint(0,10)` par exemple.\n\
Les calculs de type sinus sont aussi acceptés, pour cela entrez simplement `sin(pi)` ou `sin(90)`. Par défaut les calculs sont faits en radians.\n",
    "liste-0":"Voici la liste des commandes *inutiles donc indispensables* que je possède :"
    }

admin={
    "change_game-0":"Sélectionnez *play*, *watch*, *listen* ou *stream* suivi du nom",
    "hear_init-0":"ID invalide",
    "heard_init-1":"Erreur",
    "heard_init-2":"Impossible de trouver ce serveur/salon",
    "heard_init-3":"Mise sous écoute du salon {} (serveur {})",
    "msg_2-0":"Création de la sauvegarde...",
    "msg_2-1":"Bot en voie d'extinction",
    "msg_2-2":"Opération en cours...",
    "msg_2-3":"Aucun membre affecté",
    "msg_2-4":"1 membre affecté",
    "msg_2-5":"membres affectés",
    "msg-0":"Module(s) *{}* correctement importé(s) !",
    "bug-0":"Le bug n°{} n'a pas été trouvé"
    }

aide={"staff":"Commandes réservées au staff",
    "everyone":"Commandes pour tout le monde"}

bvn={"aide":"""__**Bienvenue dans le module des message de join et de leave**__

Ce module vous sert à configurer un message automatique à chaque fois qu'un membre rentre ou sort de votre serveur.

__**La configuration**__

`1-` Pour configurer le salon où ces messages s'écrivent, entrez `!sconfig change welcome_channel` suivi de l'ID du salon (clic droit -> "Copier l'identifiant" pour ordinateur, ou rester appuyez sur le salon -> "Copier l'identifiant" pour téléphone, mais il vous faudras avoir activer le mode dévellopeur pour obtenir cette option).
`2-` Pour configurer un message, entrez `!sconfig change <welcome|leave> <message>`. Pour ce message vous pouvez utiliser des variables, qui sont {user} pour mentionner le membre, {server} pour le nom du serveur, et {owner} pour le nom du propriétaire du serveur.
"""}

clear={"help":"La syntaxe est `!clear <nombre  | joueur> [true | false]`. Entrez *true* si vous souhaitez \
conserver les messages épinglés, *false* si vous ne le souhaitez pas\nPar défaut, *true* est activé.\n\
**Attention : cette commande est réservée à certains membres du staff !**",
       "arg":"Oups, 2e argument invalide",
       "msg-1":" messages supprimés !",
       "msg-2":"Désolé {0}, mais en raison des restrictions de Discord cette commande n'est pas disponible en mp :confused:",
       "msg-3":"Désolé {0}, mais tu n'as pas le role requis pour accéder à cette commande",
       "purge-0":"Voulez-vous vraiment effectuer une purge complète de ce salon ? (répondez \"oui\" si oui)",
       "purge-1":"Temps écoulé, vous n'avez pas répondu à temps :hourglass:",
       "purge-2":"Oups, fail ¯\_(ツ)_/¯ \nPlaignez-vous à @Z_runner#7515"}

hunter={"pan-0":"Congratulations ! {} a atteint le niveau {} dans ce jeu !",
        "pan-1":"Dommage ! {} vient de perdre en niveaux et tombe au niveau {} dans ce jeu :confused:",
        "check-0":"Oups, il ne vous reste plus de munitions :confused:\nAttendez encore {}h {}mn :hourglass:",
        "check-1":"Nouveau joueur détecté ! Bienvenue à {} !",
        "shop-0":"Vous ne semblez avoir jamais participé à ce jeu {}. Pourquoi voulez-vous diable acheter des cartouches ??",
        "shop-1":"{0} a acheté {1} nouvelle cartouche pour {2} xp !",
        "shop-2":"Vous croyiez sérieusement pouvoir acheter un nombre négatif de balles ? :rofl:",
        "shop-3":"Vous n'avez que {0} points d'expérience, ce n'est pas suffisant :upside_down:",
        "shop-4":"Cette commande vous permet d'acheter des munitions sans devoir attendre le prochain rechargement automatique. Pour cela il suffit de taper `!shop` suivit du nombre de cartouches à acheter !",
        "shop-5":"Oups, le nombre entré est invalide :upside_down:",
        "reload-0":"Vous ne pouvez pas recharger votre arme manuellement :thinking:\
\nEn revanche vous gagnez automatiquement {} toutes les 4 heures, et vous pouvez acheter des cartouches avec la commande `!shop` ! ({}xp par cartouche)",
        "rank-0":"**Rang :** {}\n\n**Niveau :** {}\n\n**Points :** {}\n\n**Munitions restantes :** {}",
        "rank-1":"Impossible de trouver le membre {}",
        "top-0":"Oups, il semble y avoir une erreur dans la commande.\nPour rappel, la syntaxe est `!top [nombre]` :innocent:",
        "top-1":"Niveaux d'xp sur *Hunter* - TOP ",
        "top-2":"Places",
        "top-3":"Nom",
        "top-4":"Points d'expérience",
        "top-5":"Bravo, vous êtes le premier !",
        "top-6":"Oups, vous n'êtes pas encore classé",
        "top-7":"Vous êtes classés à la {}ème position !",
        "aide":"""Les commandes du Hunter:
- `!phelp` Fait apparaître ce menu.
- `!pan` Permet de tirer. Plus d'informations dans le `!pinfo`.
- `!rank` Votre niveau actuel et autres statistiques.
- `!top` Le classement global sur le nombre de points.
- `!pinfo` Les informations sur le jeu.
- `!shop [nombre]` Acheter des cartouches ({0}xp par cartouche)""",
        "infos":"""**Bonjour en bienvenue dans le jeu *Hunter*** !
Il s'agit d'un jeu de ~~tir~~ hasard inspiré d'un très célèbre jeu de chasse aux canards, encore en développement.
Le but du jeu est simple : tirez, et si vous avez de la chance vous tomberez sur un objet qui donne beaucoup d'xp. Évidemment plus un objet rapporte d'xp, plus il est rare !
Vous démarrez avec {0} munitions, et votre chargeur est rempli toutes les quatre heures, mais vous pouvez aussi en acheter à {1}xp par cartouche.
On pensera à remercier **Aragorn1202** et **Platon_Neutron** pour avoir inventé les différentes phrases, ainsi qu'à *Z_runner#7515* pour avoir codé le bot :wink:

*Amusez-vous bien, et... que la chance soit avec vous !*"""}

mc={"msg-0":"Oops, il manque un paramètre",
    "msg-1":"Nom : {}\nID numérique : {}\nID : {}",
    "msg-2":"Nom : {}\nID numérique : {}:{}\nID : {}",
    "msg-3":"Impossible de trouver cet item",
    "msg-4":"Items importés !",
    "msg-5":"Entités importées !",
    "msg-6":"Items et entités importés !",
    "msg-7":"Paramètre invalide. Sélectionnez `item`, `entity` ou `all`",
    "msg-8":"Cette commande permet de trouver un bloc ou une entité de Mineraft® à partir de son nom ou de son ID. Vous n'avez qu'à entrer `!mc <item/entity> <data>` pour obtenir les informations correspondantes !\n*PS : la base de donnée est actuellement en 1.12*",
    "msg-9":"Paramètres invalides. Sélectionnez `help`, `item` ou `entity`",
    "msg-10":"Impossible de trouver cette entité"
    
    }

modo={"slowon-0":"Le salon {} est maintenant en slowmode ! ({} secondes)",
      "slowon-1":"Hum... désolé, mais nous n'acceptons que les secondes en paramètre :rolling_eyes: ",
      "slowon-2":"Hum... il semble y avoir une erreur :thinking:\nPour rappel, la syntaxe est `!slowmode <secondes>`",
      "slowon-3":"Vous ne semblez pas posséder les permissions suffisantes pour faire cela...",
      "slowoff-0":"Le salon {} n'est plus en slowmode",
      "slowoff-1":"Wow on se calme ici, le salon n'est pas en slowmode !",
      "slow_check-0":"Pas trop vite {}, le salon {} est en slowmode !",
      "mute-help":"Cette commande sert à empêcher un membre de parler, dans tout le serveur. La syntaxe est `!mute <user>`, ou `!unmute <user>` pour lui redonner la parole. \n\
- Le système fonctionne en appliquant le rôle *muted* au membre, il faut donc que celui-ci soit placé en-dessous du rôle de <@!411134209822949378>\n\
- <@!411134209822949378> doit aussi posséder la permission d'ajouter un rôle à un membre (\"manage roles\" en anglais)\n\
- Il est recommandé d'enlever la permission \"Envoyer des messages\" (\"Send messages\") manuellement au rôle *muted* dans chacun des salons où le bot n'est pas présent, pour améliorer son efficacité\n\
**Attention : cette commande est réservée à certains membres du staff !**",
      "mute-0":"Aucun membre n'a été trouvé",
      "mute-1":"Ah, il semble que {} soit déjà mute...",
      "mute-2":"Vous ne pouvez pas réduire au silence un autre membre du staff !",
      "mute-3":"**{0}** a été réduit au silence par {1}",
      "mute-4":"Je n'ai pas les permissions requises :confused:",
      "mute-5":"Oops, le role 'muted' n'existe pas :confused:",
      "mute-6":"Désolé, vous n'avez pas la permission de faire ceci",
      "unmute-0":"Ah, il semble que {} ne soit pas mute...",
      "unmute-1":"**{0}** peut à nouveau parler !",
      "unmute-2":"{0} a été unmute par {1}",
      "unmute-3":"Hum... il semblerai que je ne dispose pas des permissions nécessaires <:excusemewhat:418154673523130398>",
      "mutelist-0":"Aucun membre n'est muet ici :thinking:",
      "mutelist-1":"Liste des membres muets : ",
      "ban-0":"Le membre {} n'a pas été trouvé :confused:",
      "ban-1":"Vous ne pouvez pas bannir un autre membre du staff  ! ",
      "ban-2":"Quelqu'un est en train de vous bannir du serveur **{}** :confused:\nRaison : ",
      "ban-3":"Quelqu'un est en train de vous bannir du serveur **{}** :confused:",
      "ban-4":" vient d'être banni de ce serveur. Raison : ",
      "ban-5":" vient d'être banni de ce serveur.",
      "ban-6":"Bonne nouvelle, le ban n'a pas fonctionné !",
      "ban-7":"Désolé, vous n'avez pas la permission de bannir :confused:",
      "unban-0":" semble être présent dans ce serveur. Vous êtes sûr de votre commande ? :upside_down:",
      "unban-1":" ne semble pas être dans la liste des bannis :confused:",
      "unban-2":" peut à nouveau nous rejoindre ! Entrez `!invite` pour recevoir un nouveau lien d'invitation à lui envoyer !",
      "unban-3":"Vous ne possédez pas la permission de faire ceci <:red_cross:447509074771312652>",
      "kick-0":"Quelqu'un est en train de vous expulser du serveur **{}** :confused:\nRaison : {}",
      "kick-1":"Quelqu'un est en train de vous expulser du serveur **{}** :confused:",
      "kick-2":"**{}** vient d'être kick du serveur. Raison : {}",
      "kick-3":"**{}** vient d'être kick du serveur.",
      "kick-4":"Bonne nouvelle, il semble que le kick n'ai pas fonctionné ! :champagne:"
      }

xp={"rank-0":"{0} est un **bot**, il ne peux pas gagner d'xp !",
    "rank-1":"Impossible de trouver le membre {0}"
    }

infos={"text-0":"""Bonjour ! Moi c'est {0} !

Je suis un bot qui permet de faire *beaucoup* de choses : de la modération, des mini-jeux, un système d'xp, des statistiques et plein d'autres commandes plus ou moins utiles ! 
Vous pouvez commencer par taper `!help` dans ce tchat pour voir la liste des commandes disponibles, puis `!sconfig see` vous permettra de voir les options de configuration (un site web est en préparation). 

:globe_with_meridians: Deux liens pourront vous être utiles : 
:arrow_forward: Mon serveur Discord : http://discord.gg/ECRv8he
:arrow_forward: Un lien pour m'inviter dans un autre serveur : <https://bot.discord.io/zbot>

Bonne journée !"""}
#
