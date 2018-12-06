#Classification of documents
# Group 7
#
#Sofia Albuquerque 84581
#Marco Afonso 84610
#João Vizoso 85251

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.svm import LinearSVC

def linearSVC_tester(j,doc):
    train_set = pd.read_csv(doc)
    columns = ['party', 'text']
    train_set = train_set[columns]
    train_set.columns = ['party', 'text']

    model = LinearSVC()

    vectorizer = TfidfVectorizer(use_idf=False, max_df=0.90, min_df=3, norm='l2', max_features=20000)

    X_train, X_test, y_train, y_test = train_test_split(train_set['text'], train_set['party'], test_size = 0.2)

    X_train_vec = vectorizer.fit_transform(X_train)

    classifier = model.fit(X_train_vec, y_train)

    prediction_tester = classifier.predict(vectorizer.transform([str(train_set['text'][j])]))
    print('Predicted: ' + prediction_tester[0])
    print('Expected: ' + train_set['party'][j])
    print('Text being tested: ' + train_set['text'][j])

def linearSVC(var,doc):
    train_set = pd.read_csv(doc)
    columns = ['party', 'text']
    train_set = train_set[columns]
    train_set.columns = ['party', 'text']

    model = LinearSVC()

    X_train, X_test, y_train, y_test = train_test_split(train_set['text'], train_set['party'], test_size = 0.2)

    vectorizer = TfidfVectorizer(max_df=0.90, min_df=3, ngram_range=(1, 2))
    X_train_vec = vectorizer.fit_transform(X_train)

    classifier = model.fit(X_train_vec, y_train)
    prediction = classifier.predict(vectorizer.transform(X_test))
    prediction_tester = classifier.predict(vectorizer.transform([str(var)]))

    print('Party most likely to have produced such text: ' + prediction_tester[0])
    print(metrics.classification_report(y_test, prediction))
    print("Score: " + str(metrics.accuracy_score(y_test, prediction)))

if __name__ == "__main__":
    print('Processamento e Recuperação de Informação - Instituto Superior Tecnico / Universidade Lisboa')
    print('Classification of documents according to their political affiliation.\n')
    print('\n')
    language = input("Please choose the document language (PT/EN): ")

    if language == 'PT':
        doc = 'pt_docs_clean.csv'
        var = input("Please enter something: ")
        if var == 'p_tester':
            r = input("Position: ")
            linearSVC_tester(int(r),doc)
        else:
            linearSVC(var,doc)

    elif language == 'EN':
        doc = 'en_docs_clean.csv'
        var = input("Please enter something: ")
        if var == 'p_tester':
            r = input("Position: ")
            linearSVC_tester(int(r),doc)
        else:
            linearSVC(var,doc)

    else:
        print('Language not available')

