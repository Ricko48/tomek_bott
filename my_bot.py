import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import requests
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return


        content = message.content
        list_chars = ['.', ',', '?', '/', ';', '"', "'", '*', 'ˇ', '=', '-', '>', '<', ':', '"', "'", '|', ')', '(', '*', '&', '^', '%', '$', '#', '@', '`', '~', '{', '}', '[', ']']
        hello = ['hello', 'helo', 'ahoj', 'aho', 'servas', 'servus', 'sevas', 'nazdar', 'nandar', 'cau', 'cauko', 'Hello', 'Helo', 'Ahoj', 'Aho', 'Servas', 'Servus', 'Sevas', 'Nazdar', 'Nandar', 'Cau', 'Cauko']
        pb071 = ['programko', 'pb071', 'skuska',  'algoritmy', 'firma', 'firmy']
        pb071_response = ['to nííííč\npojdete so mnou do AT&T', 'pome robit plavcika s Rikom']
        boring = ['nuda', 'nudny']
        game = ['hra', 'hry', 'forest', 'game']
        game_response = ['moja oblubena hra jednoznacne The Forest v0.2', 'pome kupit don Starve za 8eur, bude švemba', 'som prave foresta stiahol, nedame?', 'don starve....dream game']
        for i in list_chars:
            content = content.strip(i)
        strings = content.split(" ")
        print(strings)
        response_tomek = ['no?', 'co chces']
        response_ = ['nechaj ma mam komplex teraz', 'na prechazdke som']
        response_do = ['robis', 'robiš', 'robís', 'robíš', 'porabas', 'porábaš', 'porábas', 'porabaš']

        if strings[0] == 'co' or strings[0] == 'čo' or strings[0] == 'Co' or strings[0] == 'Čo':
            await message.channel.send('nic')
            return

        for i in strings:
            if i == 'tomek' or i == 'tomas' or i == 'tomik' or i == 'Tomas' or i == 'Tomik' or i == 'Tomek':
                await message.channel.send(response_tomek[random.randint(0, len(response_tomek) - 1)])
                return

        for j in response_do:
            for k in strings:
                if j == k:
                    await message.channel.send(response_[random.randint(0, len(response_) - 1)])
                    return

        for i in strings:
            for j in boring:
                if i == j:
                    await message.channel.send('{0.author.mention} tvoj zivot je nudny'.format(message))
                    break

        for i in strings:
            for j in hello:
                if i == j:
                    await message.channel.send(hello[random.randint(0, len(hello) - 1)])
                    await message.channel.send('{0.author.mention}'.format(message))
                    break


        for i in strings:
            for j in pb071:
                if i == j:
                    await message.channel.send(pb071_response[random.randint(0, len(pb071_response) - 1)])
                    break

        for i in strings:
            for j in game:
                if i == j:
                    await message.channel.send(game_response[random.randint(0, len(game_response) - 1)])
                    break





client = MyClient()
client.run(str(os.environ.get('BOT_TOKEN')))
