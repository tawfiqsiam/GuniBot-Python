 #!/usr/bin/env python
#coding=utf-8

import dialogflow
import os.path
import sys
import json
import csv
import asyncio
from fcts import sms,admin,utilities
#from nltk import regexp_tokenize

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
        )
    import apiai

#nlp = spacy.load('fr')
CLIENT_ACCESS_TOKEN = "0ef7e74823944180b4edd605729b5300"

async def sentence_check(client,message):
    """Envoie une copie du message si le bot est mentionné"""
    if client.user in message.mentions and message.channel.id not in [447811623114244096] and message.content.startswith("!")==False:
        await admin.new_sentence(client,message)
        await dialogue(client,message)

def request(message,ID):
    """envoie une requête à Google et renvoie sa réponse (json)"""
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    request = ai.text_request()
    request.lang = 'fr'  # optional, default value equal 'en'
    request.session_id = ID
    request.query = message
    response = request.getresponse()
    return json.loads(response.read())

def answer_gen(ID,text):
    """Fonction principale cherchant une réponse"""
    a = request(text,ID)
    try:
##        if a['result']['action']=='input.unknown':
##            rep = answer2(text)
##            if rep == '¯\_(ツ)_/¯':
##                rep = a["result"]["fulfillment"]['messages'][0]['speech']
##        else:
##            rep = a["result"]["fulfillment"]['messages'][0]['speech']
        rep = a["result"]["fulfillment"]['messages'][0]['speech']
        return rep
    except:
        utilities.erreur()
        return None
    
##def answer2(text):
##    """Répond à une phrase, si Google n'a pas trouvé"""
##    dic = read_file()
##    liste = analyze(text)
##    liste2=[]
##    rep = None
##    try:
##        rep = dic[str(text)]
##    except KeyError:
##        for k,v in dic.items():
##            k = nlp(k)
##            similarity = k.similarity(nlp(text))
##            if similarity >= tolerance:
##                liste2.append((v,similarity))
##        liste2 = sorted(liste2, key=lambda long: long[1])
##        if len(liste2)>0 and rep == None:
##            rep = liste2[0][0]
##        elif len(liste2)==0 and rep==None:
##            rep = '¯\_(ツ)_/¯'
##    for i in sentence(rep):
##        rep = rep.replace(i,i.capitalize())
##    return rep


async def dialogue(client,message):
    """Fonction principale"""
    u = message.content.replace('<@!436835675304755200>','').replace('<@!411134209822949378>','').replace('<@411134209822949378>','')
    u = sms.anti_sms(u)
    rep = answer_gen(message.author.id,u)
    try:
        async with message.channel.typing():
            await asyncio.sleep(len(rep)/15)
            m = await message.channel.send(rep)
        await admin.new_sentence(client,m)
    except:
        #pass
        utilities.erreur()

##def analyze(phrase):
##    """Renvoie une liste contenant les mots découpés"""
##    liste = list()
##    doc = nlp(sms.anti_sms(phrase))
##    for token in doc:
##        liste.append(token.lemma_)
##    return liste

##def sentence(text):
##    """Renvoie le texte découpé par phrase"""
##    return regexp_tokenize(text, r'[.\?!"]\s*', gaps=True)

def read_file():
    """Renvoie le fichier"""
    try:
        with open('dic2.txt','r',encoding='utf-8') as fichier:
            texte = fichier.read()
        dic = eval(texte)
    except:
        utilities.erreur()
        dic={}
    return dic
