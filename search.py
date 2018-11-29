from collections import defaultdict
from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh import scoring
from whoosh.fields import *
from whoosh.qparser import *
import csv
import sys
import nltk

import matplotlib.pyplot as plt

csv.field_size_limit(sys.maxsize)


# index documents
def index_documents():
    schema = Schema(text=TEXT(stored=True), id=TEXT(stored=True), title=TEXT, party=TEXT(stored=True), date=DATETIME)
    ix = create_in('indexdir', schema)
    writer = ix.writer()

    with open('en_docs_clean.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            text = row.get('text')
            id = row.get('manifesto_id')
            title = row.get('title')
            party = row.get('party')
            date = row.get('date')
            writer.add_document(text=text, id=id, title=title, party=party, date=date)
        writer.commit()


# search over a index os documents
def search_over_index(keywords):
    keys = nltk.word_tokenize(keywords)
    manifestos_list = []
    party_mentions_keyword = defaultdict(int)

    ix = open_dir("indexdir")
    with ix.searcher(weighting=scoring.TF_IDF()) as searcher:
        for k in keys:
            qp = QueryParser('text', ix.schema, group=OrGroup).parse(k)
            results = searcher.search(qp, limit=None)
            for r in results:
                # List with all the manifestos containing keywords
                if r['id'] not in manifestos_list:
                    manifestos_list.append(r['id'])
                party_mentions_keyword[(r['party'], k)] += 1

    print("\nAll the manifestos containing the keywords:")
    for manifesto in manifestos_list:
        print(manifesto)

    print("\nHow many times each party mentions each keyword:")
    for key, value in party_mentions_keyword.items():
        print('{0:30}{1:40}{2:30}'.format(key[1], key[0], value))

    manifestos_keywords(manifestos_list)


def manifestos_keywords(manifestos_list):
    party_total_manifestos = defaultdict(list)
    final_dict = defaultdict(str)

    with open('en_docs_clean.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for manifesto_id in manifestos_list:
                if row['manifesto_id'] == manifesto_id:
                    if manifesto_id not in party_total_manifestos[row['party']]:
                        party_total_manifestos[row['party']].append(manifesto_id)

    for key, value in party_total_manifestos.items():
        final_dict[key] = len(party_total_manifestos[key])

    print("\nFor each party how many manifestos are in the results returned:")
    for key, value in final_dict.items():
        print('{0:40}{1:40}'.format(key, value))


def main():
    var = input("Please enter something: ")

    keywords = var
    index_documents()
    search_over_index(keywords)


#keywords = 'force injustice'
#index_documents()
#search_over_index(keywords)

main()