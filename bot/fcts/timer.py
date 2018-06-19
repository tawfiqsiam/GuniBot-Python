#!/usr/bin/env python
#coding=utf-8

import discord,asyncio,csv,re

# Syntaxe du timer dans le csv: [channelID,messageID,timer,type,message_final]
# La fonction appelée lorsque le membre entre un !timer est msg()

def count_time(text):
    """Renvoie le nombre de secondes et le message entré à partir du texte saisi"""
    try:
        jours = (re.search(r'\b(\d+)(j|d|(|\s)(jour|day)(|s))\b',text).group(0),re.search(r'\b(\d+)(j|d|(|\s)(jour|day)(|s))\b',text).group(1))
    except:
        jours = 0
    try:
        heures = (re.search(r'\b(\d+)(h|(|\s)(hour|heure)(|s))\b',text).group(0),re.search(r'\b(\d+)(h|(|\s)(hour|heure)(|s))\b',text).group(1))
    except:
        heures = 0
    try:
        minutes = (re.search(r'\b(\d+)(m|(|\s)(min|minute)(|s))\b',text).group(0),re.search(r'\b(\d+)(m|(|\s)(min|minute)(|s))\b',text).group(1))
    except:
        minutes = 0
    try:
        secondes = (re.search(r'\b(\d+)(s|(|\s)(sec(|onde(|s))))\b',text).group(0),re.search(r'\b(\d+)(s|(|\s)(sec(|onde(|s))))\b',text).group(1))
    except:
        secondes = 0
    timer = int(jours[1])*86400 + int(heures[1])*3600 + int(minutes[1])*60 + int(secondes[1])
    msg = ''
    for i in [('!timer',''),(jour[0],''),(heures[0],''),(minutes[0],''),(secondes[0],'')]:
        msg = msg.replace(i[0],i[1])
    return timer,msg
    
async def msg(message):
    """Fonction principale à appeler lors du !timer"""
    timer,msg = count_time(message.content)
    text,t = calc_format(timer)
    add_timer(message,timer,t,msg)
    await message.channel.send(msg.format())


def calc_format(timer):
    """Renvoie un texte formaté et le type de timer à partir du nombre en secondes"""
    if timer>3600:
        text="{} jours {} heures"
        t = 'h'
    elif timer>600:
        text="{} jours {} heures {} minutes"
        t = 'm'
    else:
        text = "{} jours {} heures {} minutes {} secondes"
        t = 's'
    d,q = divmod(timer,86400)
    h,q = divmod(q,3600)
    m,s = divmod(q,60)
    text = text.format(d,h,m,s)
    return text,t

def find_timer(messageid):
    """Renvoie les infos d'un timer à partir de l'ID du message"""
    liste=None
    with open('../bot-stats/timer.csv', newline='',encoding='utf-8') as csvfile:
        r = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in r:
            if row[2]==messageid:
                liste = row
    return liste

def add_timer(message,timer,content):
    """"Ajoute un timer au fichier csv"""
    with open('../bot-stats/server-options.csv','a',newline='') as csvfile:
        w = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        a,b = calc_format(timer)
        c = [message.channel.id,message.id,timer,b,content]
        w.writerow(c)

def update_timer(messageid,timer):
    """Modifie un timer dans le fichier csv"""
    with open('../bot-stats/timer.csv','w',newline='',encoding='utf-8') as csvfile:
        w = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        r = csv.reader(csvfile, delimiter=';', quotechar='|')
        for raw in r:
            if str(raw[1])==str(messageid):
                utilities.print2("MàJ du timer "+str(messageid)+" ("+timer+")")
                raw[2]=timer
            c=raw
            w.writerow(c)
