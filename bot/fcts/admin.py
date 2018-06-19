#!/usr/bin/env python
#coding=utf-8

import sys,discord,asyncio,shutil,random,datetime,importlib,os,time,string,inspect,traceback
from fcts import admin,aide,bot,bvn,citations,clear,common,emoji,fun,hunter,lang_tr,mc,modo,rss,test,timer,utilities,vote,server,say,stats,xp
from fcts.lang import *

async def change_game(client,message):
    try:
        Type=message.content.split()[1]
        act = " ".join(message.content.split()[2:])
    except IndexError:
        act = ""
    if act=="":
        await message.channel.send(lang_tr.tr(message.guild,"admin","change_game-0"))
        return
    if Type in ['game','play']:
        await client.change_presence(activity=discord.Game(name=act))
    elif Type in ['watch','see']:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=act,timestamps={'start':time.time()}))
    elif Type in ['listen']:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name=act,timestamps={'start':time.time()}))
    elif Type in ['stream']:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming,name=act,timestamps={'start':time.time()}))
    await utilities.suppr(message)

async def execute(client,message):
##    try:
##        a = eval(message.content.replace('!exec ',''))
##    except:
##        try:
##            for l in message.content.replace('!exec ','').split("\n"):
##                print(l)
##                exec(l)
##        except:
##            await message.channel.send(utilities.erreur(send=True))
##            return
##        await message.add_reaction('\U00002705')
##        return
##    await message.channel.send(str(a))
        code= message.content.replace('!exec','').strip()
        env = {
        'bot': client,
        'message':message,
        'channel': message.channel,
        'author': message.author,
        'server': message.guild
        }
        python = '```py\n{}\n```'

        env.update(globals())

        try:
            result = eval(code, env)
            if inspect.isawaitable(result):
                result = await result
        except Exception as e:
            await message.channel.send(python.format(type(e).__name__ + ': ' + str(e)))
            return

        await message.channel.send(python.format(result))

async def repl(client,message):
    variables = {"author" : message.author, "message" : message, "last" : None,"client":client,"guild":message.guild}
    await message.channel.send("Enter code to execute or evaluate\n`exit` or `quit` to exit")
    def check(m):
        return 279568324260528128 == m.author.id and m.content.startswith('`')
    p = "```py\n{}\n```"
    while True:
        print('boucle')
        message = await client.wait_for("message",check=check)
        print("detect")
        if message.content.startswith("```python") and message.content.endswith("```"):
            code = message.content.replace("python","")[4:-3].strip(" \n")
        else:
            code = message.content.replace("await ","").strip("` \n")
        if code in ("quit", "exit", "quit()", "exit()"):
            await message.channel.send('Exiting repl')
            return
        function = exec
        if '\n' not in code:
            try:
                code = compile(code, "<repl>", "eval")
            except SyntaxError:
                pass
            else:
                function = eval
        if function is exec:
                try:
                    code = compile(code, "<repl>", "exec")
                except SyntaxError as e:
                    try:
                        code = compile("await "+code, "<repl>", "exec")
                    except:
                        await message.channel.send("{0.text}{1:>{0.offset}}\n{2}: {0}".format(e, '^', type(e).__name__))
                        continue
        try:
                result = function(code, variables)
                if inspect.isawaitable(result):
                        result = await result
        except:
                await message.channel.send(p.format("\n".join(traceback.format_exc().splitlines()[-2:]).strip()))
        else:
                if function is eval:
                        try:
                                await message.channel.send(p.format(result))
                        except Exception as e:
                                await message.channel.send(p.format("{}: {}".format(type(e).__name__, e)))
                variables["last"] = result
    print("fin de la boucle")

async def hear_init(client,hear,message):
    liste = message.content.replace('!hear ','').split(' ')
    try:
        hear = [int(liste[0]),int(liste[1])]
    except ValueError:
        await message.channel.send(lang_tr.tr(message.guild,"admin","heard_init-0"))
        return [000,000]
    except:
        utilities.erreur(True)
        await message.channel.send(lang_tr.tr(message.guild,"admin","heard_init-1"))
        return [000,000]
    server = utilities.server_finder(client,hear[0])
    salon = utilities.canal_finder_name(client,hear[0],hear[1])
    if server == None or salon == None:
        await message.channel.send(lang_tr.tr(message.guild,"admin","heard_init-2"))
        return [000,000]
    else:
        await message.channel.send(lang_tr.tr(message.guild,"admin","heard_init-3").format(salon.name,server.name))
        return hear

async def heard(client,message,hear):
    salon = utilities.canal_finder_all(client,438735948650512394,True)
    if message.guild==None:
        return
    if hear[0]=='user' and hear[1]==message.channel.id:
        await salon.send("**"+message.author.name+"** *("+str(message.created_at)+")*\n"+message.content)
        return
    try:
        hear[0]=int(hear[0])
        hear[1]=int(hear[1])
    except:
        utilities.erreur(True)
        return
    if message.guild.id==hear[0] and message.channel.id==hear[1]:
        await salon.send("**"+message.author.name+"** *("+str(message.created_at)+")*\n"+message.content)

async def mp(client,message):
    """Transfère les mp recus dans le salon"""
    if message.channel.recipient.id == 279568324260528128:
        return
    salon = utilities.canal_finder_all(client,438749996024856576,True)
    await salon.send("**"+message.author.name+"** *("+str(message.created_at)+" / "+message.channel.recipient.name+")*\n"+message.content)
    await new_sentence(client,message)
    for i in message.attachments:
        await salon.send(i.url)

def reload(message):
    """Recharger un module"""
    liste=message.content.split(" ")
    liste.append('all')
    count=0
    reponse=[]
    if liste[2]=='all':
        for c in common.modules:
            reponse.append('importlib.reload('+c+')')
    else:
        m = message.content.replace("!admin reload ","").split(" ")
        for i in m:
                reponse.append('importlib.reload('+i+')')
    return reponse

async def msg_2(client,message,liste):
    """Deuxième check de la commande d'admin"""
    cmds=['shutdown','reload','xp_reload','server_reload','hunter_reload','backup','serv_test <owner_reload>','sconfig_reset <serverid>','sconfig <see/change> <serverid> [...]']
    if len(liste)>1:
        if liste[1]=='shutdown':
            m = await message.channel.send(lang_tr.tr(message.guild,"admin","msg_2-0"))
            await backup_auto(client)
            await m.edit(content=lang_tr.tr(message.guild,"admin","msg_2-1"))
            utilities.print2("Bot en voie d'extinction")
            await client.close()
            await asyncio.sleep(5)
            sys.exit()
        elif liste[1]=='reload': 
            if liste[2]=='help' or liste[2].startswith('list'):
                await message.channel.send("\n".join(common.modules))
            else:
                reloads = reload(message)
                return reloads
        elif liste[1]=='xp_reload':
            await xp.reload(message.channel)
        elif liste[1]=='server_reload':
            await server.check_len(message.channel)
        elif liste[1]=='hunter_reload':
            await hunter.reload(msg=None)
            await message.delete()
        elif liste[1]=='sconfig_reset':
            await server.delete_server(client,message.channel,liste[2])
        elif liste[1]=='serv_test' and len(liste)>2:
            if liste[2]=='owner_reload':
                mes = await message.channel.send(lang_tr.tr(message.guild,"admin","msg_2-2"))
                role = utilities.role_finder(message.guild,"Owners",False)
                count=0
                owners = utilities.owners_finder(client.guilds,"id")
                for m in message.guild.members:
                    if m.id in owners and role not in m.roles:
                        await m.add_roles(role)
                        count+=1
                    elif m.id not in owners and role in m.roles:
                        await m.remove_roles(role)
                        count+=1
                if count==0:
                    text = lang_tr.tr(message.guild,"admin","msg_2-3")
                elif count==1:
                    text = lang_tr.tr(message.guild,"admin","msg_2-4")
                else:
                    text = str(count)+" "+lang_tr.tr(message.guild,"admin","msg_2-5")
                await mes.edit(content=text)
        elif liste[1]=='backup':
            try:
                await message.author.send(file=discord.File('../bot-stats/'+liste[2]))
            except IndexError:
##                for i in ['ranks.txt','rss.csv','server-options.csv','slowmode.csv','hunter.txt','stats1.csv','stats2.csv']:
##                    await message.author.send(file=discord.File('../bot-stats/'+i))
                archive = shutil.make_archive('archives','zip','../bot-stats')
                await message.author.send(file=discord.File(archive))
            try:
                await message.delete()
            except discord.errors.Forbidden:
                pass
        elif liste[1]=='sconfig':
            if (liste[2]=="change" and len(liste)<6) or (liste[2]=="see" and len(liste)<4):
                await message.channel.send("Il manque un paramètre...")
                return
            if liste[3].isnumeric():
                content = " ".join(liste[1:3]+liste[4:])
                guild = client.get_guild(int(liste[3]))
                if guild == None:
                    await message.channel.send("Serveur "+liste[3]+" introuvable")
                    return
                await server.msg_admin(client,message.channel,content,guild)
            else:
                await message.channel.send("Mauvaise syntaxe : sconfig <see/change> <serverid> [...]")
    else:
        await message.channel.send("- "+"\n- ".join(cmds))

async def msg(client,message):
    """Premier check de la commande d'admin"""
    liste=message.content.split(" ")
    mod = await msg_2(client,message,liste)
    if len(liste)>1 and mod!=None:
        if liste[1]=='reload' and mod != []:
            mods=[]
            c=0
            for i in mod:
                try:
                    exec(i)
                    c+=1
                    mods.append(i.replace("importlib.reload(","").replace(")",""))
                except:
                    utilities.erreur()
            if mods != []:
                await message.channel.send(lang_tr.tr(message.guild,"admin","msg-0").format(", ".join(mods)))
                utilities.print2("Module(s) "+", ".join(mods)+" correctement importé(s) !")

async def tell(client,message):
    liste=message.content.replace("!tell ","").split(" ")
    user = utilities.user_finder_all(client,liste[0],True)
    del liste[0]
    if user==None or len(liste)==0:
        return
    try:
        await user.send(" ".join(liste))
    except:
        await message.channel.send(utilities.erreur())
    await message.delete()

##def random_number():
##    """Sort un numéro random pour les bugs"""
##    n = random.choice([range(2,13)])
##    number = ""
##    for i in n:
##        r = random.random()
##        if r<0.6:
##            number += str(int(random.random()*10))
##        elif r<0.9:
##            if random.random()<0.6:
##                number += random.choice(common.letters)
##            else:
##                number += random.choice(common.letters).upper()
##        else:
##            number += random.choice(['-','_','.',',','/','_','-'])
##    return number

def random_number():
    date = datetime.datetime.now()
    number = "M7-"+str(date.day+date.month)[:2]+str(random.choice(string.ascii_uppercase)).replace("I","L")+str(date.hour+date.minute)[:2]+""+str(random.choice(string.ascii_lowercase)).replace("l","i")
    return number

async def bug(client,message):
    """Gestion des bugs"""
    liste=message.content.replace("!bug ","").split(" ")
    salon_bug = utilities.canal_finder_name(client,356067272730607628,444623204108075008)
    salon_news = utilities.canal_finder_name(client,356067272730607628,444623108658298890)
    if liste[0]=='add':
        number = random_number()
        await salon_bug.send("N°"+number+" : "+" ".join(liste[1:]))
        await utilities.suppr(message)
    elif liste[0] in ['del','delete','rm','remove','fix']:
        msg = await utilities.message_finder(salon_bug,"N°"+liste[1])
        if msg == None:
            await message.channel.send(lang_tr.tr(message.guild,"admin","bug-0").format(liste[1]))
        else:
            a = datetime.datetime.now()
            t = "("+str(a.day)+"/"+str(a.month)+") "
            text = "~~"+msg.content+"~~"
            await msg.edit(content=text,delete_after=604800.0)
            await salon_news.send(t+"Bug n°{} corrigé".format(liste[1]))
            await message.delete()

async def new_sentence(client,message):
    """Transfère toutes les phrases/mp dans un salon"""
    salon = utilities.canal_finder_name(client,356067272730607628,447811623114244096)
    if message.guild == None:
        await salon.send("(MP | "+message.channel.recipient.name+")\n"+message.content.replace('<@!436835675304755200>','MEE7').replace('<@411134209822949378>','frm-BOT'))
    else:
        await salon.send("("+message.guild.name+" | "+message.channel.name+")\n"+message.content.replace('<@!436835675304755200>','MEE7').replace('<@411134209822949378>','frm-BOT'))

async def backup_auto(client):
    """Envoie une backup du bot dans le salon"""
    try:
        archive = shutil.make_archive('backup','tar','..')
    except FileNotFoundError:
        utilities.print2("Impossible de trouver le fichier de sauvegarde")
        return
    try:
        shutil.move(archive,'..')
    except shutil.Error:
        os.remove('../backup.tar')
        shutil.move(archive,'..')
    utilities.print2("("+utilities.date(datetime.datetime.now())+") Backup auto !")

async def backup_loop(client):
    await asyncio.sleep(10)
    await backup_auto(client)
    count = 2
    while not client.is_closed():
        if int(datetime.datetime.now().hour)%6==0 and count != int(datetime.datetime.now().hour):
            await backup_auto(client)
            count = int(datetime.datetime.now().hour)
        a = datetime.datetime.now()
        await asyncio.sleep((60-a.minute)*60)
