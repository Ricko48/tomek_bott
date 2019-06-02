import discord
from random import randint

answer = []

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if answer and message.content.startswith('!'):
            content = strip(message.content)
            string_content = content[0]
            if not string_content:
                return

            list_true = ['ano', 'Ano', 'True', 'true', '1', 'áno', 'Áno', 'pravda', 'Pravda', 'y', 'yes', 'Y', 'Yes']
            list_false = ['nie', 'ee', 'Nie', 'False', 'false', '0', 'ne', 'nepravda', 'Nepravda', 'n', 'no', 'N', 'No']

            answerr = answer.pop()
            answ = 'non'

            for i in list_true:
                if i == string_content:
                    answ = True

            for i in list_false:
                if i == string_content:
                    answ = False

            if answ == 'non':
                answer.append(answerr)
                return

            if answerr == answ:
                await message.channel.send('Správna odpoveď')
            else:
                await message.channel.send('Nesprávna odpoveď')
            return


        if message.content.startswith('drill'):
            question, answer_ = drill()
            await message.channel.send(question)
            while answer:
                answer.pop()
            answer.append(answer_)
            return

        hello = ['hello', 'helo', 'ahoj', 'aho', 'servas', 'servus', 'sevas', 'nazdar', 'nandar', 'cau', 'cauko', 'Hello', 'Helo', 'Ahoj', 'Aho', 'Servas', 'Servus', 'Sevas', 'Nazdar', 'Nandar', 'Cau', 'Cauko']
        pb071 = ['programko', 'pb071', 'skuska',  'algoritmy', 'firma', 'firmy', 'skola', 'uloha']
        pb071_response = ['to nííííč\npojdete so mnou do AT&T', 'pome robit plavcika s Rikom', 'to niiiiic som cakal ze to bude skola kde sa da presadiť', 'idem napisat Janovi nech poradi ulohu']
        boring = ['nuda', 'nudny', 'zivot']
        game = ['hra', 'hry', 'forest', 'game', 'hru']
        game_response = ['moja oblubena hra jednoznacne The Forest v0.2', 'pome kupit don Starve za 8eur, bude švemba', 'som prave foresta stiahol, nedame?', 'don starve....dream game']

        strings = strip(message.content)
        response_tomek = ['no?', 'co chces']
        response_ = ['nechaj ma mam komplex teraz', 'na prechazdke som']
        response_do = ['robis', 'robiš', 'robís', 'robíš', 'porabas', 'porábaš', 'porábas', 'porabaš']

        if (strings[0] == 'co' or strings[0] == 'čo' or strings[0] == 'Co' or strings[0] == 'Čo') and len(strings) == 1:
            await message.channel.send('nic')
            return

        for i in strings:
            if i == 'tomek' or i == 'tomas' or i == 'tomik' or i == 'Tomas' or i == 'Tomik' or i == 'Tomek':
                await message.channel.send(response_tomek[randint(0, len(response_tomek) - 1)])
                return

        for j in response_do:
            for k in strings:
                if j == k:
                    await message.channel.send(response_[randint(0, len(response_) - 1)])
                    return

        for i in strings:
            for j in boring:
                if i == j:
                    await message.channel.send('{0.author.mention} tvoj zivot je nudny'.format(message))
                    break

        for i in strings:
            for j in hello:
                if i == j:
                    await message.channel.send(hello[randint(0, len(hello) - 1)])
                    await message.channel.send('{0.author.mention}'.format(message))
                    break


        for i in strings:
            for j in pb071:
                if i == j:
                    await message.channel.send(pb071_response[randint(0, len(pb071_response) - 1)])
                    break

        for i in strings:
            for j in game:
                if i == j:
                    await message.channel.send(game_response[randint(0, len(game_response) - 1)])
                    break


def strip(content):
    list_chars = ['.', ',', '?', '/', ';', '"', "'", '*', 'ˇ', '=', '-', '>', '<', ':', '"', "'", '|', ')', '(', '*',
                  '&', '^', '%', '$', '#', '@', '`', '~', '{', '}', '[', ']', '!']
    for i in list_chars:
        content = content.strip(i)
    return content.split(" ")

def drill():
    file = open("drill.txt", 'r')
    number = randint(0, 322)
    count = 0
    count2 = number * 13 + 3
    true_index = count2 + 3
    for k in file.readlines():
        count += 1
        if count2 == count:
            k = k.replace('"name":', "")
            k = k.replace('"', "")
            k = k.replace("\\", "")
            k = k.strip()
            k = list(k)
            k.pop()
            question = "".join(k)

        if true_index == count:
            k = k.replace('"right":', "")
            k = k.replace('"', '')
            k = k.replace(',', '')
            k = k.strip()
            if k == 'true':
                return question, True
            else:
                return question, False

client = MyClient()
client.run(str(os.environ.get('BOT_TOKEN')))
