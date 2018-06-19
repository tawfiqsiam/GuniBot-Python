#!/usr/bin/env python
#coding=utf-8

import csv
from fcts import rss

def erase():
    with open('../bot-stats/rss.csv','w',newline='') as csvfile:
        logw = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        c=["news-fr-minecraft",'web-frm','','']
        logw.writerow(c)
        c=["minecraft-officiel",'web-mc.net','','']
        logw.writerow(c)
        c=["le-minecraftien",'web-hebdo','','']
        logw.writerow(c)
        c=["discussion_fb",'yt-fb','','']
        logw.writerow(c)
        c=["tweets",'tw-dinnerbone','','']
        logw.writerow(c)
        c=["tweets",'tw-mojang','','']
        logw.writerow(c)
        print('Everything is OK')

def reload():
    for k,v in rss.rss_check_list.items():
        if v[2]=='tw':
            t,f = rss.rss_tw(v[1])
        elif v[2]=='yt':
            t,f = rss.rss_yt(v[1])
        elif v[2]=='web':
            t,f = rss.rss_web(v[1])
        if f == []:
            print("Erreur sur la boucle rss : salon "+v[0])
            return -1,-1
        if f != []:
            date=f['published']
            titre=f['title'].replace("é","e")
            titre=titre.replace("à","a").replace("î","i").replace(" ","\n").replace("…","...")
            b,l = rss.rss_check(v[0],date,k)
            rss.rss_write(v[0],date,titre,l,k)
    print('Everything is OK')
