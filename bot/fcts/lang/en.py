#!/usr/bin/env python
#coding=utf-8

fun = {
    "count-0":"Counting messages...",
    "count-1":"You have posted {count} messages in this channel",
    "msg-0":"{0} just offered <@375598088850505728> a bow of cookies! <:cookies_eat:421791321410240514>",
    "msg-1":"Hello :wave: I'm here {0}",
    "msg-2":":wave: Hi ! I'm here !\nMaybe you meant `!help`?",
    "msg-3":"Yippee! Time to party!",
    "msg-4":"You wish to report a member or a server to the Discord staff? It's this way",
    "msg-5":"Unable to find the corresponding message. You need to enter the message ID as the first argument, and the emoji as the second point :upside_down:",
    "msg-6":"Failed, it fell on the side!",
    "msg-7":["{0} was spared by Thanos","Thanos decided to reduce {0} to ashes. For the good of humanity..."],
    "invitation-0":"Oops, I don't have permission to create an invitation (\"Manage server\")",
    "invitation-1":"__**Server invitation link :**__\n\n:incoming_envelope: Here is a link to the channel {} (He still has {} uses - {} seconds left) : ",
    "calc-0":"Oops, calculating error",
    "calc-1":"<:maths:451067921121148937> | You can use this command to calculate such things as sums, products...\n\
You also have access to other kinds of more elaborate calculations such as random numbers. All you have to do is enter `random()`, or `randint(0,10)` for example.\n\
Sine calculations are also accepted, just enter `sin(pi)` or `sin(90)`. By default the calculations are done in radians.",
    "liste-0":"Here is the list of *useless and thus essential* commands that I have:"
    }

admin={
    "change_game-0":"Select *play*, *watch*, *listen* or *stream* followed by the name",
    "hear_init-0":"Invalid ID",
    "heard_init-1":"Error",
    "heard_init-2":"Can't find this server/channel",
    "heard_init-3":"Listening of the channel {} (server {})",
    "msg_2-0":"Creating backup...",
    "msg_2-1":"Bot shutdown",
    "msg_2-2":"Operation in progress...",
    "msg_2-3":"No affected members",
    "msg_2-4":"1 affected memberé",
    "msg_2-5":"affected members",
    "msg-0":"Module(s) *{}* correctly imported !",
    "bug-0":"Bug #{} not found"
    }

aide={"staff":"Staff Commands Only",
    "everyone":"Commands for Everyone"}

bvn={"aide":"""__**Welcome to the join & leave message module**__

This module is used to configure an automatic message each time a member enters or exits your server.

__** Configuration**__

`1-` To configure the room where these messages are written, enter `!sconfig change welcome_channel` followed by the room ID (right click -> "Copy ID" for computer, or keep pressing on the channel -> "Copy ID" for phone, but you will need to have enabled the developer mode to get this option).
`2-` To configure a message, enter `!sconfig change <welcome|leave> <message>`. For this message you can use variables, which are {user} to mention the member, {server} for the server name, and {owner} for the server owner name.
"""}

clear={"help":"The syntax is `!clear <number | player>[true | false]`. Enter *true* if you wish\
keep the pinned messages, *false* if you don't want it. By default, *true* is enabled.\n\
Warning: this command is reserved for certain staff members only!**",
       "arg":"Oops, invalid 2nd argument",
       "msg-1":" messages deleted!",
       "msg-2":"Sorry {0}, but due to Discord restrictions this command is not available in mp :confused:",
       "msg-3":"Sorry {0}, but you don't have the required role to access this command",
       "purge-0":"Do you really want to do a complete purge of this channel? (answer \"yes\" if so)",
       "purge-1":"Time expired, you didn't answer fast enough :hourglass:",
       "purge-2":"Oops, fail ¯\(ツ)_/¯ \nComplain to @Z_runner#7515"}

hunter={"pan-0":"Congratulations! {0} has reached level {1} in this game!",
        "":"That's too bad. {} just lost in levels and goes down to level {} in this game :confused:",
        "check-0":"Oops, you're out of munitions :confused:\nWait still {0}h {1}mn :hourglass:",
        "check-1":"New player detected! Welcome to {0} !",
        "shop-0":"You never seem to have participated in this game {0}. Why the hell would you buy ammo??",
        "shop-1":"{0} bought {1} new ammo cartridge for {2} xp !",
        "shop-2":"You seriously thought you could buy a negative number of bullets? :rofl:",
        "shop-3":"You only have {0} experience points, it's not enough :upside_down:",
        "shop-4":"This command allows you to purchase munitions without waiting for the next automatic reload. Just type `!shop` followed by the number of cartridges to buy !",
        "shop-5":"Oops, number entered is invalid :upside_down:",
        "reload-0":"You can't reload your weapon manually :thinking:\
\nHowever, you automatically win {0} every 4 hours, and you can buy cartridges with the command `!shop` ! ({1}xp per cartridge)",
        "rank-0":"**Rank :** {0}\n\n**Level :** {1}\n\n**Points :** {2}\n\n**Remaining munitions :** {3}",
        "rank-1":"Unable to find member {}",
        "top-0":"Oops, there seems to be an error in the command.\nRemember, the syntax is `!top[number]` :innocent:",
        "top-1":"xp levels on *Hunter* - TOP ",
        "top-2":"Ranks",
        "top-3":"Name",
        "top-4":"Experience points",
        "top-5":"Well done, you're first!",
        "top-6":"Oops, you're not ranked yet.",
        "top-7":"You are ranked {0}th !",
        "aide":"""Hunter commands:
- `!phelp` Opens this menu.
- `!pan` Allows to shoot. More information in the `!pinfo`.
- `!rank` Your current level and other statistics.
- `!top` The overall ranking on the number of points.
- `!pinfo` Information about the game.
`!shop [number]` Buy cartridges ({0}xp per cartridge)""",
        "infos":"""**Hello and welcome to the game *Hunter*** !
It's a game of ~~shoot~~ chance inspired by a very famous game of duck hunting, still in development.
The goal of the game is simple: shoot, and if you are lucky you will come across an object that gives a lot of xp. Obviously the more an object brings back xp, the rarer it is !
You start with {0} ammunition, and your loader is filled every four hours, but you can also buy it at {1}xp per cartouche.
We will think to thank **Aragorn1202** and **Platon_Neutron** for inventing the different sentences, as well as *Z_runner#7515* for coding the bot :wink:

*Amuse yourselves well, and... may the luck be with you !*"""}

mc={"msg-0":"Oops, there' s a missing parameter",
    "msg-1":"Name: {}\nNumeric ID: {}\nID: {}",
    "msg-2":"Name: {}\nNumeric ID: {}:{}\nID: {}",
    "msg-3":"Unable to find this item",
    "msg-4":"Items correctly imported!",
    "msg-5":"Entities correctly imported!",
    "msg-6":"Items and entities correctly imported!",
    "msg-7":"Invalid setting. Select `item`, `entity` or `all`",
    "msg-8":"This command allows you to find a Mineraft® block or entity from its name or ID. All you have to do is enter `!mc <item/entity> <data>` to get the corresponding information !\n*PS  the database is currently in 1.12*",
    "msg-9":"Invalid settings. Select `help`, `item` or `entity`",
    "msg-10":"Unable to find this entity"
    }

modo={"slowon-0":"The channel {0} is now in slowmode! ({1} seconds)",
      "slowon-1":"Um... sorry, but we only accept seconds as parameter: rolling_eyes: ",
      "slowon-2":"Um... there seems to be an error :thinking:\nRemember, the syntax is `!slowmode <seconds>`",
      "slowon-3":"You don't seem to have enough permissions to do that....",
      "slowoff-0":"The channel {0} is no longer in slowmode",
      "slowoff-1":"Wow, calm down here, channel is not in slowmode!",
      "slow_check-0":"Not so fast {0}, channem {1} is in slowmode!",
      "mute-help":"This command is used to prevent a member from speaking, throughout the server. The syntax is `!mute <user>`, or `!unmute <user>` to give him the voice again.\n\
- The system works by applying the *muted* role to the member, so it must be placed below the role of <@!411134209822949378>\n\
- <@!411134209822949378> must also have permission to add a role to a member (\"manage roles\")\n\
- It's recommended to remove the \"Send messages\" permission manually at the *muted* role in each of the channels where the bot is not present, to improve its efficiency\n\
**Attention: this command is reserved for certain members of the staff!**",
      "mute-0":"No members were found",
      "mute-1":"Ah, it seems {} is already muted...",
      "mute-2":"You can't silence another staff member!",
      "mute-3":"**{0}** has been silenced by {1}",
      "mute-4":"I don't have the required permissions :confused:",
      "mute-5":"Oops, the role 'muted' does not exist :confused:",
      "mute-6":"Sorry, you don't have permission to do this.",
      "unmute-0":"Ah, it seems {} is not muted...",
      "unmute-1":"**{0}** can talk again!",
      "unmute-2":"{0} was unmuted by {1}",
      "unmute-3":"Um... it seems I don't have the necessary permissions <:excusemewhat:418154673523130398>",
      "mutelist-0":"No member is mute here :thinking:",
      "mutelist-1":"List of mute members: ",
      "ban-0":"Member {} was not found :confused:",
      "ban-1":"You can't ban another staff member!",
      "ban-2":"Someone's banning you from the server **{}** :confused:\nReason : ",
      "ban-3":"Someone's banning you from the server **{}** :confused:",
      "ban-4":" has just been banned from this server. Reason : ",
      "ban-5":" has just been banned from this server.",
      "ban-6":"Good news, the ban didn't work!",
      "ban-7":"Sorry, you don't have permission to banish :confused:",
      "unban-0":" seems to be in this server. Are you sure about your command? :upside_down:",
      "unban-1":" doesn't seem to be on the banned list :confused:",
      "unban-2":" can join us again! Enter `!invite` to receive a new invitation link to send!",
      "unban-3":"You do not have permission to do this <:red_cross:447509074771312652>",
      "kick-0":"Somebody's kicking you off the server **{}** :confused:\nReason : {}",
      "kick-1":"Somebody's kicking you off the server **{}** :confused:",
      "kick-2":"**{}** just got kicked off the server.. Reason : {}",
      "kick-3":"**{}** just got kicked off the server..",
      "kick-4":"Good news, it seems the kick didn't work! :champagne:"
      }

xp={"rank-0":"{0} is a **bot**, can't win an xp!",
    "rank-1":"Unable to find member {0}"
    }

infos={"text-0":"""Hello! I'm {0} !

I'm a bot that allows you to do a lot of things: moderation, mini-games, an xp system, statistics and many other super useful commands (and totally pointless ones)! 
You can start by typing `!help` in this chat to see the list of available commands, then `!sconfig see` will let you see the configuration options (a website is in preparation). 

:globe_with_meridians: Two links may be useful: 
:arrow_forward: My Discord server : http://discord.gg/ECRv8he
:arrow_forward: A link to invite me to another server : <https://bot.discord.io/zbot>

Have a nice day!"""}

#
