import pandas as pd
import numpy as np
import sys
import random
songs= pd.read_csv("tracks.csv")

songs['loudness'] = -((songs['loudness'])/10)
songs['tempo'] = songs['tempo']/250

songs1 = songs.drop(['id','name','uri','artist','key','mode','time_signature','duration_ms'],axis = 1)
Genre = []

for i in range(0,len(songs1)):
    if (max(songs1.loc[i]) == songs.loc[i,'acousticness']):
        Genre.append("Slow & Somber Acoustics")

    elif (max(songs1.loc[i]) == songs.loc[i,'danceability']):
        Genre.append("Happy & Danceable Instrumentals")

    elif (max(songs1.loc[i]) == songs.loc[i,'valence']):
        Genre.append("Sad ")

    elif (max(songs1.loc[i]) == songs.loc[i,'liveness']):
        Genre.append("Upbeat Songs With Cheerful Vocals")

    elif (max(songs1.loc[i]) == songs.loc[i,'energy']):
        Genre.append("Fast & Danceable")

    elif (max(songs1.loc[i]) == songs.loc[i,'tempo']):
        Genre.append("Fast, Upbeat & Cheerful")

    elif (max(songs1.loc[i]) == songs.loc[i,'speechiness']):
        Genre.append("Rap")

    elif (max(songs1.loc[i]) == songs.loc[i,'loudness']):
        Genre.append("Full of energy")

    else :
        Genre.append("Happy & Upbeat Instrumentals")
        
songs['Genre']   = Genre
X = songs[['acousticness', 'danceability', 'energy', 'instrumentalness','liveness', 'loudness', 'speechiness', 'tempo', 'valence']]
y = songs.Genre

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(X)

scaled_df = pd.DataFrame(X, columns=X.columns)

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier

X_train, X_test, y_train, y_test = train_test_split(scaled_df, y, test_size=0.2, random_state=3)

forest = RandomForestClassifier(n_estimators=100, max_depth= 5)
forest.fit(X_train, y_train)


song_input =sys.argv[1]

a = songs['id'].where(songs['name'] == '{}'.format(song_input)).any()
a = songs[['acousticness', 'danceability', 'energy', 'instrumentalness','liveness', 'loudness', 'speechiness', 'tempo', 'valence']].where(songs['name'] == song_input)
a= a.dropna()
pred = forest.predict(a)

print(pred[0])

z = songs.groupby('Genre').groups[pred[0]]

i=random.randint(0,67)
j=i+10
print(songs["name"].iloc[i:j])
songs["name"].iloc[z][i:j].to_excel("temp.xlsx")
# songs["name"].iloc[z].head(10).to_excel("newtemp.xlsx")