#Statistical Analysis Group 7
#
#Sofia Albuquerque 84581
#Marco Afonso 84610
#João Vizoso 85251

import sys
import spacy
import pandas

from collections import Counter

#Setup
df = pandas.read_csv('en_docs_clean.csv')
nlp = spacy.load('en_core_web_sm')

#What are the most mentioned entities for each party?

def mostMentionedEntitiesForParty():
    partiesD = {'Labour Party': [], 'Conservative Party': [],
                'Liberal Democrats': [], 'Scottish National Party': [], 'Green Party of England and Wales': [],
                'We Ourselves': [], 'Social Democratic and Labour Party': [], 'Ulster Unionist Party': [],
                'The Party of Wales': [], 'Democratic Unionist Party': [], 'United Kingdom Independence Party': []}
    for i in range(len(df.party)):
        doc = nlp(df.text[i])
        for entity in doc.ents:
            partiesD[df.party[i]].append(entity.label_)
    for p in partiesD:
        c = Counter(partiesD[p])
        partiesD[p] = c.most_common(3)
    print(partiesD)

#What are the most mentioned entities globally?

def mostMentionedEntitiesGlobally():
    enti = []
    for i in range(len(df.text)):
        doc = nlp(df.text[i])
        for entity in doc.ents:
            enti.append(entity.label_)
    c = Counter(enti)
    mostMentionedEntities = c.most_common(3)
    print(mostMentionedEntities)

#Which party is mentioned more times by the other parties?

def mostMentionedPartyForOtherParties():
    partiesText = {'Labour Party': "", 'Conservative Party': "",
                'Liberal Democrats': "", 'Scottish National Party': "", 'Green Party of England and Wales': "",
                'We Ourselves': "", 'Social Democratic and Labour Party': "", 'Ulster Unionist Party': "",
                'The Party of Wales': "", 'Democratic Unionist Party': "", 'United Kingdom Independence Party': ""}
    partiesOccur = {'Labour Party': 0, 'Conservative Party': 0,
                'Liberal Democrats': 0, 'Scottish National Party': 0, 'Green Party of England and Wales': 0,
                'We Ourselves': 0, 'Social Democratic and Labour Party': 0, 'Ulster Unionist Party': 0,
                'The Party of Wales': 0, 'Democratic Unionist Party': 0, 'United Kingdom Independence Party': 0}
    for i in range(len(df.party)):
        partiesText[df.party[i]] += df.text[i]
    for p in partiesOccur:
        for pt in partiesText:
            if p == pt:
                continue
            else:
                partiesOccur[p] += partiesText[pt].count(p)
    print(partiesOccur)
    print("The most mentioned party by other parties is " + str(max(partiesOccur, key=partiesOccur.get)) + ".")

#How many times does any given party mention other parties?

def timesPartyMentionOtherParties():
    partiesText = {'Labour Party': "", 'Conservative Party': "",
                   'Liberal Democrats': "", 'Scottish National Party': "", 'Green Party of England and Wales': "",
                   'We Ourselves': "", 'Social Democratic and Labour Party': "", 'Ulster Unionist Party': "",
                   'The Party of Wales': "", 'Democratic Unionist Party': "", 'United Kingdom Independence Party': ""}
    partiesOccur = {'Labour Party': 0, 'Conservative Party': 0,
                'Liberal Democrats': 0, 'Scottish National Party': 0, 'Green Party of England and Wales': 0,
                'We Ourselves': 0, 'Social Democratic and Labour Party': 0, 'Ulster Unionist Party': 0,
                'The Party of Wales': 0, 'Democratic Unionist Party': 0, 'United Kingdom Independence Party': 0}
    for i in range(len(df.party)):
        partiesText[df.party[i]] += df.text[i]
    for p in partiesOccur:
        for pt in partiesText:
            if p == pt:
                continue
            else:
                partiesOccur[p] += partiesText[p].count(pt)
    print(partiesOccur)

#Explain all the entities mentioned.

def explainEntities():
    enti = []
    for i in range(len(df.text)):
        doc = nlp(df.text[i])
        for entity in doc.ents:
            if entity.label_ not in enti:
                enti.append(entity.label_)
    for e in enti:
        print("Entity " + e + " refers to " + spacy.explain(e))


def usage(progName):
    print('Processamento e Recuperação de Informação - Instituto Superior Tecnico / Universidade Lisboa')
    print('Statistical analysis of the subjects mentioned.\n')
    print('')
    print('Usage:')
    print('  %s entitiesForParty, entitiesGlobally, mentionedPartyForOtherParties, timesPartyMentionOtherParties or explainEntities' % progName)
    print('')
    sys.exit()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage(sys.argv[0])
    if sys.argv[1] == 'entitiesForParty':
        mostMentionedEntitiesForParty()
    if sys.argv[1] == 'entitiesGlobally':
        mostMentionedEntitiesGlobally()
    if sys.argv[1] == 'mentionedPartyForOtherParties':
        mostMentionedPartyForOtherParties()
    if sys.argv[1] == 'timesPartyMentionOtherParties':
        timesPartyMentionOtherParties()
    if sys.argv[1] == 'explainEntities':
        explainEntities()