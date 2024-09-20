from discum.utils.slash import SlashCommander
import discum
import time
import threading
import random

TOKEN = "" # Account token
GUILD_ID = "" # Server ID
CHANNEL_ID = "" # Channel ID

bot = discum.Client(token=TOKEN, log=False)

def send_bump_command(): # This just makes sure the bot does the command as soon as you turn it on.
    try:
        slashCmds = bot.getSlashCommands("302050872383242240").json()
        s = SlashCommander(slashCmds)
        data = s.get(['bump'])
        bot.triggerSlashCommand("302050872383242240", CHANNEL_ID, guildID=GUILD_ID, data=data)
        print('Sent initial bump')
    except Exception as e:
        print(f"Error occurred sending initial bump: {e}")
    
    while True:
        random_sleep_time = random.uniform(300, 400) # Does the command every 5-6 minutes, you can edit it. (300 seconds = 5mins)
        print(f"Waiting {random_sleep_time:.2f} seconds.")
        time.sleep(random_sleep_time)
        
        try:
            slashCmds = bot.getSlashCommands("302050872383242240").json()
            s = SlashCommander(slashCmds)
            data = s.get(['bump'])
            
            bot.triggerSlashCommand("302050872383242240", CHANNEL_ID, guildID=GUILD_ID, data=data)
            print('Sent bump')
        
        except Exception as e:
            print(f"An error occurred: {e}")

thread = threading.Thread(target=send_bump_command)
thread.start()

bot.gateway.run(auto_reconnect=True)
