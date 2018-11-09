import sys
import csv
import nltk

def mostMentionedEntitiesForParty():
    csv.field_size_limit(sys.maxsize)
    with open('pt_docs_clean.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['text'])

def mostMentionedEntitiesGlobally():
    csv.field_size_limit(sys.maxsize)
    with open('pt_docs_clean.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['text'])


#Which party is mentioned more times by the other parties?


def mostMentionedPartyForOtherParties():
    csv.field_size_limit(sys.maxsize)
    parties = {'Social Democratic Center-Popular Party': 'CDS', 'Social Democratic Party': 'PSD',
               'Portuguese Communist Party': 'PCP', 'Left Bloc': 'BE', 'Ecologist Party ‘The Greens': 'PEV',
               'Socialist Party': 'PS'}
    parties_occur = {'CDS': 0, 'PSD': 0, 'PCP': 0, 'BE': 0, 'PEV': 0, 'PS': 0}
    sentences = []
    words = []
    with open('pt_docs_clean.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sentences += nltk.sent_tokenize(row['text'])
        for i in range(len(sentences)):
            words += nltk.word_tokenize(sentences[i])
        for w in words:
            for occur in parties_occur:
                if occur == w:
                    parties_occur[occur] += 1

    print("O partido mais vezes mencionado é o " + str(max(parties)))
    print(parties_occur)


def timesPartyMentionOtherParties(party):
    csv.field_size_limit(sys.maxsize)
    parties = {'Social Democratic Center-Popular Party': 'CDS', 'Social Democratic Party': 'PSD',
                'Portuguese Communist Party': 'PCP', 'Left Bloc': 'BE', 'Ecologist Party ‘The Greens': 'PEV',
                'Socialist Party': 'PS'}
    sentences = []
    words = []
    counter = 0
    with open('pt_docs_clean.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['party'] == party:
                sentences += nltk.sent_tokenize(row['text'])
        for i in range(len(sentences)):
            words += nltk.word_tokenize(sentences[i])
        parties.pop(party)
        for w in words:
            for p in parties:
                if parties[p] == w:
                    counter += 1

    print("O " + str(party) + " menciona os outros partidos " + str(counter) + " vezes.")



#mostMentionedEntitiesForParty()
#mostMentionedEntitiesGlobally()
#mostMentionedPartyForOtherParties()
#timesPartyMentionOtherParties('Socialist Party')