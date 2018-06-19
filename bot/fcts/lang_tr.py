#!/usr/bin/env python
#coding=utf-8

from fcts import server, utilities
from importlib import reload as m_reload
from fcts.lang import fr, en
import discord

m_reload(fr)
m_reload(en)

def tr(serverID,moduleID,messageID):
    """Renvoie le texte en fonction de la langue"""
    if type(serverID)==discord.guild.Guild:
        lang_opt = server.find_staff(serverID.id,"langage")
    elif type(serverID)==None:
        lang_opt = ['fr']
    else:
        lang_opt = server.find_staff(serverID,"langage")
    if lang_opt not in [['fr'],['en']]:
        lang_opt=['fr']
    if lang_opt == ["fr"]:
        try:
            return eval("fr."+moduleID+"[\""+messageID+"\"]")
        except:
            utilities.erreur()
            return ""
    elif lang_opt==['en']:
        try:
            return eval("en."+moduleID+"[\""+messageID+"\"]")
        except:
            print("ERREUR - ERREUR - ERREUR")
            utilities.erreur()
            try:
                return eval("fr."+moduleID+"[\""+messageID+"\"]")
            except:
                return ""
