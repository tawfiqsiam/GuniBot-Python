#!/usr/bin/env python
#coding=utf8

import feedparser,csv,asyncio,time,datetime
import sys,traceback
from fcts import utilities,common

yt_link={'neil3000':'UC7SdIxpBCuP-KXSqaexTdAw',
         'grand_corbeau':'UCAt_W0Rgr33OePJ8jylkx0A',
         'mojang':'UC1sELGmy5jp5fQUugmuYlXQ',
         'frm':'frminecraft',
         'fr-minecraft':'frminecraft',
         'freebuild':'UCFl41Y9Hf-BtZBn7LGPHNAQ',
         'fb':'UCFl41Y9Hf-BtZBn7LGPHNAQ',
         'aurelien_sama':'AurelienSama',
         'asilis':'UC-SJq_WeVTWc4sy76JOHhTA',
         'oxisius':'UC-SJq_WeVTWc4sy76JOHhTA',
         'leirof':'UCimA2SBz78Mj-TQ2n4TmEVw',
         'gunivers':'UCtQb5O95cCGp9iquLjY9O1g',
         'platon_neutron':'UC2xPiOqjQ-nZeCka_ZNCtCQ',
         'aragorn1202':'UCjDG6KLKOm6_8ax--zgeB6Q'
         }

rss_check_list={'web-frm':('391970380878708740','http://fr-minecraft.net/rss.php','web'),
                'web-mc.net':('393289077212053504','https://minecraft.net/fr-fr/feeds/community-content/rss','web'),
                'tw_mee6':('447066303736578058','mee6bot','tw'),
                'yt-fb':('393118419656114177','UCFl41Y9Hf-BtZBn7LGPHNAQ','yt'),
                'yt-slicedlime':('421004758380314625','slicedlime','yt'),
                'tw-dinnerbone':('421004758380314625','Dinnerbone','tw'),
                'tw-mojang-support':('421004758380314625','MojangSupport','tw'),
                'tw-minecraft':('421004758380314625','Minecraft','tw'),
                'tw_adrian':('421004758380314625','adrian_ivl','tw'),
                'web-discord':('447066303736578058','https://discord.statuspage.io/history.rss','web'),
                'tw-discord':('447066303736578058','discordapp','tw'),
                'yt-discord':('447066303736578058','UCZ5XnGb-3t7jCkXdawN2tkA','yt'),
                'tw-optifine':('421004758380314625','sp614x','tw')
                }

rss_web_annonce=""":newspaper:  | {0}  ({1})

{2}
 """

rss_tweet_annonce="""<:twitter:437220693726330881>  | Nouveau tweet de **{0}**  ({1})

{2}

{3}
 """

rss_yt_annonce="""<:youtube:447459436982960143>  | Nouvelle vidéo de **{0}** ({1})

{2}
"""

web_link={'fr-minecraft':'http://fr-minecraft.net/rss.php',
          'frm':'http://fr-minecraft.net/rss.php',
          'minecraft.net':'https://minecraft.net/fr-fr/feeds/community-content/rss',
          'arobazzz':'http://le-minecraftien.e-monsite.com/blog/do/rss.xml',
          'minecraftien':'http://le-minecraftien.e-monsite.com/blog/do/rss.xml',
          'gunivers':'https://gunivers.net/feed/'
          }

reddit_link={'minecraft':'https://www.reddit.com/r/Minecraft',
             'reddit':'https://www.reddit.com/r/news',
             'discord':'https://www.reddit.com/r/discordapp'
             }

def rss_yt(identifiant):
    texte="erreur yt"
    if identifiant=='help':
        texte="Pour rechercher une chaîne youtube, vous devez entrer l'identifiant de cette chaîne.\n\
Vous la trouverez à la fin de l'url de la chaine, elle peut être soit le nom, soit une suite de caractères aléatoires.\n\
*Astuce : certaines chaînes sont déjà renseignées dans mon code. Vous pouvez parfois vous contenter de mettre `neil3000` ou `Oxisius` :wink:*"
        return texte,[]
    else:
        url = 'https://www.youtube.com/feeds/videos.xml?channel_id='+identifiant
        feeds = feedparser.parse(url)
        if feeds.entries==[]:
            url = 'https://www.youtube.com/feeds/videos.xml?user='+identifiant
            feeds = feedparser.parse(url)
            if feeds.entries==[]:
                texte = "Oops, rien à afficher :confused:"
                return texte,[]
        try:
            texte = "<:youtube:447459436982960143>  Voici la dernière vidéo de "+feeds.entries[0]['author']+" :\n**"+feeds.entries[0]['title']+"**\n Publié le "+utilities.date(feeds.entries[0]['published_parsed'])+"\n Lien : "+feeds.entries[0]['link']
        except IOError:
            utilities.print2('RSS : aucun accès à Internet')
            texte = "Oups, je n'arrive pas à me connecter :thinking:"
    return texte,feeds.entries[0]

def rss_tw(nom):
    if nom=='help':
        texte="Pour rechercher une chaîne twitter, vous devez entrer l'identifiant de cette chaîne.\n\
Vous la trouverez à la fin de l'url de la chaîne, elle correspond généralement au nom de l'utilisateur.\n\
Par exemple, pour *https://twitter.com/Mc_AsiliS*, il faut rentrer `Mc_AsiliS`"
        return texte,[]
    else:
        url = 'http://twitrss.me/twitter_user_to_rss/?user='+nom
        feeds = feedparser.parse(url)
        if feeds.entries==[]:
            url = 'http://twitrss.me/twitter_user_to_rss/?user='+nom.capitalize()
            feeds = feedparser.parse(url)
            if feeds.entries==[]:
                texte = "Oops, rien à afficher :confused:"
                return texte,[]
        if feeds.entries[0]['published_parsed'] > feeds.entries[1]['published_parsed']:
            f = feeds.entries[0]
        else:
            f = feeds.entries[1]
        try:
            texte = "<:twitter:437220693726330881>  Voici le dernier tweet de **"+f['author'].replace('(','').replace(')','')+"** :\n\n"+f['title']+"\n\nPublié le "+utilities.date(f['published_parsed'])+"\n Lien : "+f['link']
        except IOError:
            utilities.print2('RSS : aucun accès à Internet')
            texte = "Oups, je n'arrive pas à me connecter :thinking:"
        return texte,f

def rss_web(lien):
    if lien=='help':
        texte="Pour rechercher un flux rss web, vous devez entrer l'url de ce flux.\n\
Et mauvaise nouvelle : là, c'est à vous de chercher <:hey:401062040241700864>.\n\
Mais pour vous aider, j'ai déjà trouvé 2-3 pages web. Pour choisir celle de minecraft.net par exemple, il vous suffit d'entrer `minecraft.net`\n\
Sympa, non ?"
        return texte,[]
    else:
        if lien=='http://fr-minecraft.net/rss.php':
            texte = '<:frm:447460560573825025> '
        elif lien == 'https://minecraft.net/fr-fr/feeds/community-content/rss':
            texte = '<:mojang:447460822772613151> '
        else:
            texte = ':newspaper: '
        feeds = feedparser.parse(lien)
        if feeds.entries==[]:
            texte = "Oops, rien à afficher :confused:"
            return texte,[]
        else:
            try:
                texte += "Voici le dernier post sur *"+feeds['feed']['title']+"* :\n\n"+feeds.entries[0]['title']+"\n\nPublié le "+utilities.translater(feeds.entries[0]['published'])+"\n Lien : "+feeds.entries[0]['link']
            except IOError:
                utilities.print2('RSS : aucun accès à Internet')
                texte = "Oups, je n'arrive pas à me connecter :thinking:"
    return texte,feeds.entries[0]

def rss_reddit(lien,param):
    texte=''
    if lien=='help' or param.lower()=='help':
        texte="Voici la syntaxe de la commande : `!rss reddit <new|best> <lien|nom>`\n\
*new* permet d'avoir le dernier message posté, *best* celui qui est le plus mieux :rofl:"
    else:
        if param.lower()=='best':
            feeds = feedparser.parse(lien+"/.rss")
            if feeds.entries==[]:
                feeds = feedparser.parse('https://www.reddit.com/r/{0}/.rss'.format(lien))
        elif param.lower()=='new':
            feeds=feedparser.parse('http://www.reddit.com/r/{0}/new/.rss'.format(lien))
            if feeds.entries==[]:
                l = lien.split("/")
                l.insert(5,'new')
                l.append('.rss')
                utilities.print2("/".join(l))
                if feeds.entries==[]:
                    feeds = feedparser.parse("/".join(l))
        else:
            texte="Paramètre invalide\nSyntaxe : `!rss reddit <new|best> <lien|nom>`"
            feeds = feedparser.parse("http://lol.fr")
        if feeds.entries==[] and texte=='':
            texte = "Oops, rien à afficher :confused:"
        elif feeds.entries!=[]:
            try:
                date = utilities.date(feeds.entries[0]['updated_parsed'])
                texte = "<:reddit:447462065204887573>  Voici le dernier post sur *"+feeds['feed']['title']+"* :\n\n"+feeds.entries[0]['title']+"\n\nPublié le "+date+"\n Lien : "+feeds.entries[0]['link']
            except IOError:
                utilities.print2('RSS : aucun accès à Internet')
                texte = "Oups, je n'arrive pas à me connecter :thinking:"
    return texte

def rss_check(salon,date,ident):
    #utilities.print2("check appelé pour "+ident)
    logr=[]
    a=0
    try:
        with open('../bot-stats/rss.csv', newline='',encoding='utf-8') as csvfile:
            f = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in f:
                logr.append(row)
                if row[0]==salon and row[1]==ident:
                    a=row
    except:
        utilities.print2("Erreur lors de la lecture du fichier - rss_check("+salon+','+date+','+ident+")")
        utilities.erreur(True)
    b = a!=0 and a[0]==salon and a[2]==date
    return b,logr

def rss_write(salon,date,titre,logr,ident):
    utilities.print2("(rss) write appelé pour "+ident)
    with open('../bot-stats/rss.csv','w',newline='',encoding='utf-8') as csvfile:
        logw = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        count = 0
        for i in logr:
            if i[0]==salon and i[1]==ident:
                utilities.print2("(rss) MàJ du log pour "+salon)
                c=[salon,ident,date,titre.replace('\n',"   ")]
                count = 1
            elif i[1] not in rss_check_list.keys():
                continue
            else:
                c=i
            try:
                logw.writerow(c)
            except UnicodeEncodeError:
                logw.writerow(utilities.anti_code(c))
    if count == 0:
        with open('../bot-stats/rss.csv','a',newline='',encoding='utf-8') as csvfile:
            logw = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            utilities.print2("(rss) Création du log pour "+salon)
            logw.writerow([salon,ident,date,titre.replace('\n',"   ")])
            count=1

def rss_loop_1():
    global rss_check_list
    count=0
    for k,v in rss_check_list.items():
        count+=1
        if v[2]=='tw':
            t,f = rss_tw(v[1])
        elif v[2]=='yt':
            t,f = rss_yt(v[1])
        elif v[2]=='web':
            t,f = rss_web(v[1])
        if f == []:
            utilities.print2("(rss) Erreur sur la boucle : salon "+v[0]+"\t\t"+v[1])
            return -1,-1,-1
        date=f['published']
        titre=f['title'].replace("é","e")
        titre=titre.replace("à","a").replace("î","i").replace(" ","\n").replace("…","...")
        b,l = rss_check(v[0],date,k)
        if b==False:
            rss_write(v[0],date,titre,l,k)
            if v[2]=='web':
                try:
                    texte = rss_web_annonce.format(f['title'],utilities.date(f['published_parsed']),f['link'])
                except KeyError:
                    texte=rss_web_annonce.format(f['title'],f['published'],f['link'])
            elif v[2]=='tw':
                texte=rss_tweet_annonce.format(f['author'].replace(')','').replace('(',''),utilities.date(f['published_parsed']),f['title'],f['link'])
            elif v[2]=='yt':
                texte = rss_yt_annonce.format(f['author'],utilities.date(f['published_parsed']),f['link'])
            else:
                texte=rss_web_annonce.format(f['title'],f['published'],f['link'])
            if k=='web-frm':
                texte=texte+"\n<@&391986402461745153>"
            elif k=='yt-fb':
                texte+="\n<@!375598088850505728>"
            return texte,v[0],count
    return None,None,count
            
async def rss_loop_2(client):
    global rss_check_list
    c=0
    utilities.print2("("+utilities.date(datetime.datetime.now())+") boucle rss")
    while c<len(rss_check_list.keys())+1:
        t,s,c=rss_loop_1()
        if t != None:
            salon = utilities.canal_finder_name(client,'391968999098810388',s)
            if salon==None:
                salon = utilities.canal_finder_all(client,s)
            if salon==None:
                return
            await salon.send(t)
        c+=1

async def rss(client,wait=True):
    if wait:
        await asyncio.sleep(10)
    await rss_loop_2(client)
    while not client.is_closed():
        await asyncio.sleep(10)
        if int(datetime.datetime.now().minute)%10==0:
            await rss_loop_2(client)
            await asyncio.sleep(50)

async def rss_msg(message):
    rep = await message.channel.send("Recherche en cours...") 
    liste = message.content.split(" ")
    c=0
    try:
        arg = liste[1].lower()
        m = liste[2]
        c=1
    except:
        if arg != 'help':
            texte="<:excusemewhat:418154673523130398> Pardon ? Je crois qu'il manque un paramètre là..."
            c=-1
    if c==1:
        if arg=='yt' or arg=='youtube':
            for k,v in yt_link.items():
                if k==m.lower():
                    m=v
            texte,f = rss_yt(m)
        elif arg=='twitter':
            texte,f = rss_tw(m)
        elif arg=='web' or arg=='site':
            for k,v in web_link.items():
                if k==m.lower():
                    m=v
            texte,f = rss_web(m)
        elif arg=='reddit':
            arg1=liste[2]
            try:
                m=liste[3]
            except IndexError:
                m='Minecraft'
            for k,v in reddit_link.items():
                if k==m.lower():
                    m=v
            texte = rss_reddit(m,arg1)
        else:
            c=0
    if c==0:
        texte="`!rss <youtube|twitter|reddit|web> <id>`\n\
En premier argument, vous devez mettre le type de média, suivi de l'identifiant du flux.\n\
Vous aurez plus d'aide sur cette commande en tapant `help` à la place de l'identifiant :wink:"
    await rep.edit(content=texte)
