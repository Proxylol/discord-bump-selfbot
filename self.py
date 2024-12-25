from discum.utils.slash import SlashCommander
import discum
import time

TOKEN = "" # selfbot token
GUILD_ID = "" # server ID
CHANNEL_ID = "" # channel ID (to send bump)

bot = discum.Client(token=TOKEN, log=False)

try:
    slashCmds = bot.getSlashCommands("302050872383242240").json()
    s = SlashCommander(slashCmds)
    data = s.get(['bump'])
except Exception as e:
    print(f"couldnt find the slash command, make sure to send a message to the Disboard bot first")
    exit()

def send_bump_command():
    """auto bump"""
    while True:
        try:
            bot.triggerSlashCommand("302050872383242240", CHANNEL_ID, guildID=GUILD_ID, data=data)
            print("bumped")
        except Exception as e:
            print(f"error: {e}")
        time.sleep(7520) # you can change this to whatever, this will do it every 2 hours and 2 minutes

print("starting")
send_bump_command()
