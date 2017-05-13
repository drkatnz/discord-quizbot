# -*- coding: utf-8 -*-
"""
Discord Bot

Using https://github.com/Rapptz/discord.py installed from source
API: http://discordpy.readthedocs.io/en/latest/api.html

@author: drkatnz
"""

import discord
import sys

import quiz

client = discord.Client()
quiz = quiz.Quiz(client)

@client.event
async def on_ready():
    print('Logged in as: ' + client.user.name)
    print('User ID: ' + client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!logoff'):
        await client.send_message(message.channel, 'Leaving server. BYE!')
        await client.close()
        exit()
        
    elif (message.content.startswith('!halt') or 
          message.content.startswith('!stop')):
        await quiz.stop()

    elif (message.content.startswith('!quiz') or 
          message.content.startswith('!ask')):
        await quiz.start(message.channel)      
    elif (message.content.startswith('!scores')):
        await quiz.print_scores()    
    elif (message.content.startswith('!next')):
        await quiz.next_question(message.channel)
    elif quiz is not None and quiz.started():
        #check if we have a question pending
        await quiz.answer_question(message)
        #check quiz question correct


#run the program!
if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print('Usage: python bot.py APP_BOT_USER_TOKEN')
        exit()
        
    # logs into channel    
    try:
        client.run(sys.argv[1])
    except:        
        client.close()