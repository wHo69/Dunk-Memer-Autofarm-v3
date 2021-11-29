import requests
import random

data = requests.get(f'https://discordapp.com/api/v6/channels/793065688906465290/messages', headers={"Authorization": "mfa.Jmm7fpaEI0r-Zf3nXCvlubmLzmpaYXJuJsX-sp2ngmbUWEqvofysR2VUAeqcBTzSu-UnHuinWGKoV6f90jGs"}).json()        
options = data[0]['components'][0]['components']
msgId = data[0]["id"]

chosenCustomId = options[random.randint(1, 3)]["custom_id"]

r = requests.post("https://discord.com/api/v9/interactions", headers={"Authorization": "mfa.Jmm7fpaEI0r-Zf3nXCvlubmLzmpaYXJuJsX-sp2ngmbUWEqvofysR2VUAeqcBTzSu-UnHuinWGKoV6f90jGs"}, json={"type":3,"guild_id":"791588775456800798","channel_id":"793065688906465290","message_flags":0,"message_id":msgId,"application_id":"270904126974590976","data":{"component_type":2,"custom_id":chosenCustomId}})
print(r.status_code)