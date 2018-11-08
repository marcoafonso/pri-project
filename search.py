from collections import defaultdict
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
import csv
import operator
import sys

csv.field_size_limit(sys.maxsize)


def party_total_keywords(keywords):
    dict_party_total_keywords = defaultdict(int)

    with open('pt_docs_clean.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            words = row['text'].split()
            for w in words:
                for key in keywords:
                    if key == w:
                        dict_party_total_keywords[(row['party'], key)] += 1

    print(dict_party_total_keywords)


def party_total_manifestos(keywords):
    dict_party_total_manifestos = defaultdict(int)
    dict_manifesto_contain_key = defaultdict(str)

    with open('pt_docs_clean.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            words = row['text'].split()
            for w in words:
                for key in keywords:
                    if key == w:
                        if row['manifesto_id'] not in dict_manifesto_contain_key[key]:
                            dict_party_total_manifestos[row['party']] += 1

    print(dict_party_total_manifestos)


def manifestos_with_keywords(keywords):
    dict_tfidf = tf_idf()
    dict_ordenado = defaultdict(str)
    dict_manifesto_contain_key = defaultdict(str)

    with open('pt_docs_clean.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            words = row['text'].split()
            for w in words:
                for key in keywords:
                    if key == w:
                        if row['manifesto_id'] not in dict_manifesto_contain_key[key]:
                            dict_manifesto_contain_key[key] += str(row['manifesto_id'] + " | ")

    dict_aux = defaultdict(str)

    for value in dict_manifesto_contain_key.keys():
        for v in dict_tfidf.keys():
            if value == v:
                dict_aux[v, dict_manifesto_contain_key[v]] += str(dict_tfidf[v])

    sorted_d = sorted(dict_aux.keys(), key=operator.itemgetter(1), reverse=True)
    print(sorted_d)


def tf_idf():
    data = []

    with open('pt_docs_clean.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row[0])

    cv = CountVectorizer()
    data = cv.fit_transform(data)
    tfidf_transformer = TfidfTransformer()
    tfidf_transformer.fit_transform(data)
    tfidf_scores = dict(zip(cv.get_feature_names(), tfidf_transformer.idf_))

    return tfidf_scores


keywords = ['democratica', 'partido', 'ficar', 'justiça']
manifestos_with_keywords(keywords)
party_total_manifestos(keywords)
party_total_keywords(keywords)
