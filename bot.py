import os
import random
import discord
from discord.ext import commands
from discord.permissions import permission_alias
import time
import spacy
import nltk
import string
from private import token

#Classes
class Serveur:

    def __init__(self, id):
        self.id=id
        self.etat=False
        self.personnageBot=liste_personnage[0]
    
    def on(self):
        self.etat=True

    def off(self):
        self.etat=False

    def changer_personnage(self,personnageBot):
        self.personnageBot=personnageBot
    

class Personnage:

    def __init__(self, nom):
        self.nom=str(nom).title()
        self.ListeCitations=list()
    
    def addCitation(self,citation):
        self.ListeCitations.append(citation)
    
    def randomCitation(self):
        i=random.choice(range(len(self.ListeCitations)))
        return self.ListeCitations[i].citation


class Citation :


    MOTS_USELESS= []

    def __init__(self,phrase,citation_prec):
        #Karadoc : Ah ouais  Eh ben ?
        phrase=phrase.split(":")
        #nettoyage du nom de l'auteur
        personnage=phrase[0].lower().strip(" ")
        personnage=personnage.split(" ")
        if personnage[0]=="dame" and personnage[1]=="séli":
            personnage="séli"
        elif personnage[0]=="ddl" or personnage[0]=='ddlac' or (personnage[0]=="dame" and personnage[2]=="lac") or personnage[0]=="dame":
            personnage="dame du lac"
        elif personnage[0]=="venec" or personnage[0]=="vénec":
            personnage="vénec"
        elif personnage[0]=="leodagan" or personnage[0]=="léodagan":
            personnage="léodagan"
        elif personnage[0]=="interprète" or personnage[0]=="l'interprète" or personnage[0]=="interprête":
            personnage="interprète"
        elif personnage[0]=="voix":
            personnage=personnage[2]
        elif personnage[0]=="père" or personnage[0]=='blaise':
            personnage="père blaise"
        elif personnage[0]=="maître":
            personnage="maître d'armes"
        elif personnage[0]=="roi" or personnage[0]=="arthur(réfléchit)":
            personnage="arthur"
        elif personnage[0]=="le":
            personnage="tavernier"
        else:
            personnage=personnage[0]
        self.personnage=personnage.title()
        self.citation=phrase[1].strip(" ")
        self.citation_prec=citation_prec
        self.vecteur=nlp(process_text(self.citation))


    def correspondance(self,phrase):
        if self.citation_prec=="":
            return 0
        res=0
        phrase=phrase.split(" ")
        phrase = list(dict.fromkeys(phrase))
        phraseTest=self.citation_prec.citation.split(" ")
        phraseTest=list(dict.fromkeys(phraseTest))
        for mot in self.MOTS_USELESS:
            for i in range(len(phraseTest)):
                if mot.lower() == phraseTest[i].lower():
                    phraseTest.remove(i)
        for mot in phrase:
            for mot2 in phraseTest:
                if mot==mot2:
                    res=res+1
        return res/len(phraseTest)

    def correspondanceVect2Word(self,phraseVect):
        if self.citation_prec=="":
            return 0
        return phraseVect.similarity(self.citation_prec.vecteur)

#fonctions

def calculate_similarity(text1, text2):
    base = nlp(process_text(text1))
    compare = nlp(process_text(text2))
    return base.similarity(compare)


def process_text(phrase):
    global ponctuations
    global mots_vides
    res=list()
    for char in list(phrase):
        test=False
        for ponct in ponctuations :
            if char == ponct :
                test=True
        if test:
            res.append(" ")
        else:
            res.append(char)
    phrase="".join(res)
    phrase=phrase.lower()
    res=list()
    phrase=phrase.split()
    for i in range(len(phrase)):
        for inutile in mots_vides:
            if phrase[i]==inutile:
                res.append(i)
    for i in range(len(res)):
        phrase.pop(res[i]-i)
    phrase=" ".join(phrase)
    return phrase




#global variables
liste_citations=list()
liste_personnage=list()
liste_serveur=list()
#personnageBot=str()
#etat=False
mots_vides = nltk.corpus.stopwords.words('french')
ponctuations = list(string.punctuation)
ponctuations.append("…")
ponctuations.append('’')
nlp = ""

#Bot

bot = commands.Bot(command_prefix='!k ')

@bot.listen('on_ready')
async def allumage():
    global nlp
    global liste_citations
    global liste_personnage
    global liste_serveur
    #global personnageBot
    #await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name='Initialisation'))
    nlp = spacy.load('fr_core_news_lg')
    fichier = open("data.txt", encoding='utf-8')
    contenu = str(fichier.read())
    contenu=contenu.split('\n')
    fichier.close()
    liste_citations.append(Citation(contenu[0],""))
    liste_personnage.append(liste_citations[0].personnage)
    for i in range(1,len(contenu)):
        liste_citations.append(Citation(contenu[i],liste_citations[i-1]))
        liste_personnage.append(liste_citations[i].personnage)
    liste_personnage=list(dict.fromkeys(liste_personnage))
    for i in range(len(liste_personnage)):
        liste_personnage[i]=Personnage(liste_personnage[i])
    for personnage in liste_personnage:
        for i in range(len(liste_citations)):
            if liste_citations[i].personnage==personnage.nom:
                personnage.addCitation(liste_citations[i])
    for i in range(len(bot.guilds)):
        liste_serveur.append(Serveur(bot.guilds[i].id))
    #personnageBot=liste_personnage[0]
    await bot.change_presence(activity=discord.Game(name='!k help'))
    print("Bot actif")

@bot.listen('on_message_delete')
async def delete(message):
    res=random.randint(0,10)
    for j in range(len(liste_serveur)):
        if message.guild.id==liste_serveur[j].id:
            etat=liste_serveur[j].etat
            break
    if res==0 and etat==True:
        await message.channel.send("*Arthur" +": Je crois qu’il faut que vous arrêtiez d’essayer de dire des trucs*" )
    elif res==1 and etat==True:
        await message.channel.send("*Karadoc: Quel con !! Pourquoi il avait écrit \""+message.content+"\" ?*" )
    else:
        return

@bot.listen('on_message_edit')
async def edit(message,after):
    res=random.randint(0,10)
    for j in range(len(liste_serveur)):
        if message.guild.id==liste_serveur[j].id:
            etat=liste_serveur[j].etat
            break
    if res==0 and etat==True:
        await message.channel.send("*Kadoc" +": Elle est où la boulette ?*" )
    elif res==1 and etat==True:
        await message.channel.send("*Perceval: Ah le boulet !! Il avait écrit \""+message.content+"\" !!!*" )
    else:
        return

@bot.listen('on_guild_join')
async def join(guild):
    global liste_serveur
    await liste_serveur.append(Serveur(guild.id))


@bot.command(name='personnage', help='change le personnage joué par le bot (!k personnage "personnage")') 
async def changerPersonnage(ctx, nom: str):
    global liste_personnage
    for i in range(len(liste_personnage)):
        if nom.lower()==liste_personnage[i].nom.lower():
            for j in range(len(liste_serveur)):
                if ctx.message.guild.id==liste_serveur[j].id:
                    liste_serveur[j].changer_personnage(liste_personnage[i])
                    break
    await ctx.send(liste_serveur[j].personnageBot.nom +': Je suis ' + liste_serveur[j].personnageBot.nom +" !!!" )


@bot.command(name='liste', help='affiche la liste des personnages') 
async def liste(ctx):
    global liste_personnage
    res=list()
    for i in range(len(liste_personnage)):
        res.append(liste_personnage[i].nom +" ("+str(len(liste_personnage[i].ListeCitations))+")")
    await ctx.send(" / ".join(res))


@bot.command(name='start', help='active les réponses du bot') 
async def start(ctx):
    for j in range(len(liste_serveur)):
                if ctx.message.guild.id==liste_serveur[j].id:
                    liste_serveur[j].on()
                    break
    await ctx.send("*"+ctx.author.name+' a ouvert le clapet de ' + liste_serveur[j].personnageBot.nom+"*")


@bot.command(name='stop', help='désactive les réponses du bot') 
async def start(ctx):
    for j in range(len(liste_serveur)):
                if ctx.message.guild.id==liste_serveur[j].id:
                    liste_serveur[j].off()
                    break
    await ctx.send("*"+ctx.author.name+' a fermé le clapet de ' + liste_serveur[j].personnageBot.nom+"*")

@bot.command(name='citation', help=' (!k citation "personnage") ecrit une citation aléatoire du personnage') 
async def start(ctx, nom: str):
    global liste_personnage
    for i in range(len(liste_personnage)):
        if nom.lower()==liste_personnage[i].nom.lower():
            await ctx.send(liste_personnage[i].nom+': '+liste_personnage[i].randomCitation())
            return
    res=random.randint(0,1)
    if res==0:
        await ctx.send('Bot: Ouais, c est pas faux')
    else:
        await ctx.send('Bot: Heu, j ai pas compris la question')

@bot.command(name='citationPrec', help='écrit la citation précédente (doit être entre guillemets)') 
async def start(ctx, citation: str):
    global liste_citations
    for i in range(len(liste_citations)):
        if citation.lower().strip(" ")==liste_citations[i].citation.lower().strip(" "):
            if liste_citations[i].citation_prec=="":
                await ctx.send("C'est la première phrase de Kaamelott. Inculte !! Au bûcher !!!")
                return
            await ctx.send(liste_citations[i].citation_prec.personnage+ ": "+liste_citations[i].citation_prec.citation)
            return
    res=random.randint(0,1)
    if res==0:
        await ctx.send('Bot: Ouais, c est pas faux')
    else:
        await ctx.send('Bot: Heu, j ai pas compris la question')
    
@bot.command(name='sloubi', help='joue à compte sloubi (!k sloubi nbr)') 
async def start(ctx, nbr: int):
    listsloubi=list()
    for i in range(nbr):
        listsloubi.append("sloubi "+str(i+1))
    await ctx.send("Perceval: "+" ".join(listsloubi))

@bot.event
async def on_command_error(ctx, error):
    res=random.randint(0,1)
    if res==0:
        await ctx.send('Bot: Ouais, c est pas faux')
    else:
        await ctx.send('Bot: Heu, j ai pas compris la question')
    
@bot.listen('on_message') # Message envoyé dans un canal
async def test(message):
    for j in range(len(liste_serveur)):
                if message.guild.id==liste_serveur[j].id:
                    personnageBot=liste_serveur[j].personnageBot
                    etat=liste_serveur[j].etat
                    break
    if message.author == bot.user or message.content.split(" ")[0]=="!k" or etat==False:
        return
    else:
        contenu=message.content
        contenuVect=nlp(process_text(contenu))
        liste_citations_test=personnageBot.ListeCitations
        correspondance=list()
        for i in range(len(liste_citations_test)):
            correspondance.append(liste_citations_test[i].correspondanceVect2Word(contenuVect))
        reponse=liste_citations_test[correspondance.index(max(correspondance))]
        print(max(correspondance))
        await message.channel.send(reponse.personnage+": "+reponse.citation +" ("+str(int(max(correspondance)*100))+"%)")



bot.run(token)
