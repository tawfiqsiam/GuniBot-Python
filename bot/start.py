 #!/usr/bin/env python
#coding=utf-8

import time
t1=time.time()

import discord, asyncio, importlib,sys
from fcts import aide,admin,bot,bvn,citations,clear,common,emoji,fun,hunter,mc,modo,rss,test,timer,utilities,vote,say,server,stats,xp

fb_infos=442761240981536788
rank_sys={}
client = discord.Client()
hear = [0,0] #[serverid,channelid]

@client.event
async def on_error(event, *args, **kwargs):
    msg = utilities.erreur(True)
    message = args[0]
    salon = utilities.canal_finder_name(client,356067272730607628,445969411573153793)
    if message.guild == None:
        await salon.send("DM | "+message.channel.recipient.name+"\n"+msg)
    else:
        await salon.send(message.guild.name+" | "+message.channel.name+"\n"+msg)

@client.event
async def on_ready():
    global r
    utilities.print2('\nBot connecté')
    utilities.print2("Nom : "+client.user.name)
    utilities.print2("ID : "+str(client.user.id))
    serveurs = []
    for i in client.guilds:
        serveurs.append(i.name)
    ihvbsdi="Connecté sur ["+str(len(client.guilds))+"] "+", ".join(serveurs)
    utilities.print2(ihvbsdi)
    utilities.print2(utilities.translater(str(time.strftime("%d %B %H:%M:%S"))))
    utilities.print2("Prêt en "+str(t1+(time.time()-t2))+" sec")
    utilities.print2('------')
    await asyncio.sleep(3)
    if r=='1':
        await client.change_presence(activity=discord.Game(name="entrer !help"))
    elif r=='2':
        await client.change_presence(activity=discord.Game(name="SNAPSHOOT"))

@client.event
async def on_member_join(member):
    await bvn.new_member(client,member)

@client.event
async def on_member_remove(member):
    await bvn.ex_member(client,member)

@client.event
async def on_message(message):
    global rank_sys, hear
    await admin.heard(client,message,hear)
    if message.guild==None:
        await admin.mp(client,message)
#-----
    if message.content.startswith('!admin') and message.author==client.get_user(279568324260528128):
        await admin.msg(client,message)
#-----
    stats.change_stats(message)
#-----
    if message.guild!=None:
        if await modo.slow_check(message,client) or await modo.mute_check(message) or await modo.freeze_check(message):
            return        
        await say.sentence_check(client,message)
#-----
    if utilities.count_maj(utilities.anti_emoji(message.content))>75 and not message.author.bot and len(message.content)>5  and message.author.id != 279568324260528128 and message.guild!=None and message.channel.permissions_for(message.guild.me).send_messages:
        await message.channel.send("Hey, attention aux majuscules "+message.author.name+" !",delete_after=2.5)
        utilities.print2("majuscules "+message.author.name)
    elif utilities.mute_finder(message.author)==False and message.author.bot==False and len(message.content) in range(5,180) and str(message.content)[0] not in ['!','<','.','/'] and message.channel.id not in xp.ban_channels:
        rank_sys = await xp.message_xp(message,rank_sys)
#-----
    if message.content.startswith('!count'):
        await fun.count(message)
#-----
    elif message.content.startswith('!bug ') and message.author.id == 279568324260528128:
        await admin.bug(client,message)
#-----
    elif message.content.startswith('!hear ') and message.author.id == 279568324260528128:
        hear = await admin.hear_init(client,hear,message)
#-----
    elif message.content.startswith('!tell ') and message.author.id == 279568324260528128:
        await admin.tell(client,message)
#-----
    elif message.content.startswith('!rss '):
        liste=message.content.split(" ")
        if liste[1]=='check':
            await rss.rss(client,wait=False)
        else:
            await rss.rss_msg(message)
#-----
    elif message.content.startswith('!fb') and message.author.id == 279568324260528128:
        await mc.info_fb(client,fb_infos)
        await message.delete()
#-----
    elif message.content.startswith('!vote '):
        await vote.vote(message)
#-----
    elif message.content.startswith('!clear'):
        await clear.clear(client,message)
#-----
    elif message.content.startswith('!help'):
        await aide.msg(message.channel)
#-----
    elif message.content.startswith('!sondage '):
        await vote.sondage(message)       
#-----
    elif message.content.startswith('!calc '):
        await fun.calc(client,message)
#-----
    elif message.content.startswith('!userinfo'):
        await stats.userinfo(client,message)
#-----
    elif message.content.startswith('!fun'):
        await fun.liste(message.channel)
#-----
    elif message.content.lower() == '!rep':
        await utilities.rep(message)
#-----
    elif message.content.startswith('!activity') and message.author==client.get_user(279568324260528128):
        await admin.change_game(client,message)
#-----
    elif message.content.startswith('!rank'):
        if utilities.is_hunter(message) and message.guild != None:
            await hunter.rank(client,message)
        else:
            await xp.rank(client,message)
#-----
    elif message.content.startswith('!top'):
        if utilities.is_hunter(message) and message.guild != None:
            await hunter.top(client,message)
        else:
            await xp.top(client,message)
#-----
    elif message.content.startswith('!find '):
        await stats.find(message,client)
#-----
    elif message.content.startswith('!exec ') and message.author.id ==279568324260528128:
        await admin.execute(client,message)
#-----
    elif message.content.startswith('!test') and message.author.id ==279568324260528128:
        await test.test(client,message)
#-----
    elif message.content.startswith('!mc '):
        await mc.msg_init(message)
#-----
    elif message.content.startswith('!stats'):
        await stats.msg(client,message)
#-----
    elif message.guild != None:
        await bot.new_news(client,message)
        if message.content.startswith('!slowoff') or message.content.startswith('!slowmode off'):
            await modo.slowoff(message)
        #-----
        elif message.content.startswith('!slowmode '):
            await modo.slowon(message)
        #-----
        elif message.content.lower() == '!freeze on':
            await modo.freeze_on(message)
        #-----
        elif message.content.lower() == '!freeze off':
            await modo.freeze_off(message)
        #-----
        elif message.content.startswith('!mute '):
            await modo.mute(client,message)
        #-----
        elif message.content.startswith('!unmute '):
            await modo.unmute(client,message)
        #-----
        elif message.content.startswith('!mutelist'):
            await modo.mutelist(message)
        #-----
        elif (message.content.startswith('!bvn') or message.content.startswith('!bienvenue')) and message.author == message.guild.owner:
            await bvn.aide(message.channel)
        #-----
        elif message.content.startswith('!ban '):
            await modo.ban(client,message)
        #-----
        elif message.content.startswith('!unban '):
            await modo.unban(client,message)
        #-----
        elif message.content.startswith('!kick '):
            await modo.kick(client,message)
        #-----
        elif message.content.startswith('!sconfig '):
            await server.msg(client,message)
        #-----
        elif message.content.startswith('!pinfo'):
            await hunter.infos(message.channel)
        #-----
        elif message.content.startswith('!serverinfo'):
            await stats.serverinfo(message)
        #-----
        elif message.content.startswith("!roleinfo "):
            await stats.role_info(message)
        #-----
        elif message.content.startswith('!channelinfo'):
            await stats.channel_info(message)
        #-----
        elif message.content.startswith('!membercount'):
            await stats.membercount(message)
        #-----
        elif message.content.lower() == '!purge':
            await clear.big_purge(client,message)
        #-----
        elif utilities.is_hunter(message):
            await hunter.msg(client,message)
    await fun.msg(client,message)

t1=time.time()-t1
r=input("Quel bot activer ? (1 release, 2 snapshot) ")
if r=='1':
    token="NDExMTM0MjA5ODIyOTQ5Mzc4.DV3SKQ.A9qB1U7BUTBpt2JMIxmJGoobsq0"
    client.loop.create_task(mc.fb(client,fb_infos,True))
elif r=='2':
    token="NDM2ODM1Njc1MzA0NzU1MjAw.DbtSgQ.xOyqtO3l1BdYxl9zjtdDq7quQlE"
else:
    sys.exit()
r2=input("Lancement de la boucle rss ? (o/n) ")
if r2=='o':
    client.loop.create_task(rss.rss(client))
r3=input("Lancement de la boucle hunting ? (o/n) ")
if r3=='o':
    client.loop.create_task(hunter.loop(client))
r4=input("Lancement de la boucle backup ? (o/n) ")
if r4=='o':
    client.loop.create_task(admin.backup_loop(client))
t2=time.time()

     
client.run(token)
