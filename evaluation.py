import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import Perceptron
from sklearn.neighbors import KNeighborsClassifier

def naiveBayes(j):
    train_set = pd.read_csv('en_docs_clean.csv')
    columns = ['party', 'text']
    train_set = train_set[columns]
    train_set.columns = ['party', 'text']

    model = MultinomialNB()

    vectorizer = TfidfVectorizer(max_df=0.5,stop_words='english')

    X_train, X_test, y_train, y_test = train_test_split(train_set['text'], train_set['party'])

    X_train_vec = vectorizer.fit_transform(X_train)

    classifier = model.fit(X_train_vec, y_train)

    prediction = classifier.predict(vectorizer.transform(X_test))
    prediction_tester = classifier.predict(vectorizer.transform(['including the young and the old, men and women, those who are disabled and minority groups, including ethnic minorities and different sexual orientations']))
    print('Predicted: ' + prediction_tester[0])
    print('Expected: ' + train_set['party'][j])
    print('Text being tested: ' + train_set['text'][j])
    print(metrics.classification_report(y_test, prediction))

def linearSVC(j):
    train_set = pd.read_csv('en_docs_clean.csv')
    columns = ['party', 'text']
    train_set = train_set[columns]
    train_set.columns = ['party', 'text']

    model = LinearSVC()

    vectorizer = TfidfVectorizer(max_df=0.5, stop_words='english')

    X_train, X_test, y_train, y_test = train_test_split(train_set['text'], train_set['party'])

    X_train_vec = vectorizer.fit_transform(X_train)

    classifier = model.fit(X_train_vec, y_train)

    prediction = classifier.predict(vectorizer.transform(X_test))
    prediction_tester = classifier.predict(vectorizer.transform(['including the young and the old, men and women, those who are disabled and minority groups, including ethnic minorities and different sexual orientations']))
    print('Predicted: ' + prediction_tester[0])
    print('Expected: ' + train_set['party'][j])
    print('Text being tested: ' + train_set['text'][j])
    print(metrics.classification_report(y_test, prediction))

#VER PARAMETROS
def nearestNeighbors(j):
    train_set = pd.read_csv('en_docs_clean.csv')
    columns = ['party', 'text']
    train_set = train_set[columns]
    train_set.columns = ['party', 'text']

    model = KNeighborsClassifier()

    vectorizer = TfidfVectorizer(max_df=0.5, stop_words='english')

    X_train, X_test, y_train, y_test = train_test_split(train_set['text'], train_set['party'])

    X_train_vec = vectorizer.fit_transform(X_train)

    classifier = model.fit(X_train_vec, y_train)

    prediction = classifier.predict(vectorizer.transform(X_test))
    prediction_tester = classifier.predict(vectorizer.transform(['including the young and the old, men and women, those who are disabled and minority groups, including ethnic minorities and different sexual orientations']))
    print('Predicted: ' + prediction_tester[0])
    print('Expected: ' + train_set['party'][j])
    print('Text being tested: ' + train_set['text'][j])
    print(metrics.classification_report(y_test, prediction))

def perceptron(j):
    train_set = pd.read_csv('en_docs_clean.csv')
    columns = ['party', 'text']
    train_set = train_set[columns]
    train_set.columns = ['party', 'text']

    model = Perceptron()

    vectorizer = TfidfVectorizer(max_df=0.5, stop_words='english')

    X_train, X_test, y_train, y_test = train_test_split(train_set['text'], train_set['party'])

    X_train_vec = vectorizer.fit_transform(X_train)

    classifier = model.fit(X_train_vec, y_train)

    prediction = classifier.predict(vectorizer.transform(X_test))
    prediction_tester = classifier.predict(vectorizer.transform(['including the young and the old, men and women, those who are disabled and minority groups, including ethnic minorities and different sexual orientations']))
    print('Predicted: ' + prediction_tester[0])
    print('Expected: ' + train_set['party'][j])
    print('Text being tested: ' + train_set['text'][j])
    print(metrics.classification_report(y_test, prediction))

# VERIFICAR PARAMETROS DO TFIDF
# VERIFICAR PARAMETROS DE CADA ALGORITMO
# COMPARAR PERFORMANCES
# TIRAR PRINTS PARA O RELATORIO
# ESCOLHER ALGORITMO E FAZER MAIN/INPUT