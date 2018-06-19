

sms = {'ban':'bannir',
       'xD':'::rofl:',
       'x)':':smile:',
       ':D:':':smile:',
       'kick':'expulser',
       'bi1':'bien',
       'tro':'trop',
       ':/':':confused:',
       'wait':'attends',
       'sava':'ça va',
       'ca':'ça',
       'troll':'trompe',
       'cpas':"c'est pas",
       'stv':'si tu veux',
       'fo':'faux',
       'u':'toi'
       }


def anti_sms(text):
    for k,v in sms.items():
        text = text.replace(" "+k+" "," "+v+" ")
    return text
