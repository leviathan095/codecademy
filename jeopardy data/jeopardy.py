import pandas as pd
pd.set_option('display.max_colwidth', -1)

jeopardy = pd.read_csv('C:\codecademy\jeopardy.csv')

jeopardy = jeopardy.rename(columns = {" Air Date": "Air Date", " Round" : "Round", " Category": "Category", " Value": "Value", " Question":"Question", " Answer": "Answer"})
#print(jeopardy.columns)
#print(jeopardy["Question"])

def data_filter(data,words):

    filter = lambda x: all(word.lower() in x.lower() for word in words)
    return data.loc[data['Question'].apply(filter)]

king_england_filter = data_filter(jeopardy,['King','England'])


jeopardy['Float Value'] = jeopardy['Value'].apply(lambda x: float(x[1:].replace(',','')) if x != 'None' else 0 )

king_filter = data_filter(jeopardy,['King'])
print(king_filter)

print(king_filter['Float Value'].mean())

def unique_answer_counts(data):

    return data['Answer'].value_counts()

print(unique_answer_counts(king_filter))
                        