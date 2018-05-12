import codecs
import numpy as np
with codecs.open("train_data_non_EMOJI.txt", encoding='utf-8') as f:
    data = [line.split('\t') for line in f.read().splitlines()]

X = list(zip(*data))[0]
y = np.array(list(zip(*data))[1], dtype=int)

from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from konlpy.tag import Hannanum
from konlpy.tag import Twitter

hannanum = Hannanum()
twitter = Twitter()
model1 = Pipeline([
    ('vect', HashingVectorizer(tokenizer=twitter.nouns)), 
    ('mb', MultinomialNB()),
    ])
print('1')
model1.fit(X, y)
print('2')
#from sklearn.externals import joblib
#joblib.dump(model1, 'model1.pkl')

import codecs
with codecs.open("test_data_non_EMOJI.txt", encoding='utf-8') as f:
    data_test = [line.split('\t') for line in f.read().splitlines()]
    
X_test = list(zip(*data_test))[0]
y_test = np.array(list(zip(*data_test))[1], dtype=int)

print('3')
print(classification_report(y_test, model1.predict(X_test)))
print('4')