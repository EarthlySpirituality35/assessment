# importing functions 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as nppi

status = 1


my_df = pd.read_csv("Data/spotifydataset.csv", on_bad_lines='warn', encoding='latin-1')
my_df = my_df.drop(columns = ['released_month', 'released_day', 'in_spotify_charts', 'in_spotify_playlists', 'in_shazam_charts', 'in_apple_charts', 'in_apple_playlists', 'in_deezer_charts', 'in_deezer_playlists', 'danceability_%', 'valence_%', 'energy_%', 'acousticness_%', 'instrumentalness_%', 'liveness_%', 'speechiness_%'])
my_df.iloc[:950]
#my_df['streams'] = my_df['streams'].astype(float)



my_df['artist_count'].plot.pie()
plt.show()

print('''
Welcome to spotify's top 950. This is where you find information about the top 950 songs that spotify has to offer. 
      ''')

def streamchart():
    my_df.plot(
                kind='bar',
                x='track_name',
                y='streams',
                color='blue',
                alpha=0.3,
                title='Streams of top songs',
                fontsize=3)
    plt.show()

def artistchart():
    artistcount = my_df['artist_count'].value_counts()
    artistcount.plot(
                    kind='bar',
                    x='artistcount',
                    y='artist_count',               
                    color='blue',
                    alpha=0.3,
                    title='Artist Count',
                    fontsize=10)

    plt.show()

def bpmchart():    
    bpmcount = my_df['bpm'].value_counts()
    bpmcount.plot(
                    kind='bar',
                    x='bpmcount',
                    y='bpm',               
                    color='blue',
                    alpha=0.3,
                    title='BPM',
                    fontsize=10)
    
    plt.show()
    
def modechart():    
    modecount = my_df['mode'].value_counts()
    modecount.plot(
                    kind='bar',
                    x='modecount',
                    y='mode',               
                    color='blue',
                    alpha=0.3,
                    title='Mode',
                    fontsize=10)
    
    plt.show() 

def keychart():    
    keycount = my_df['key'].value_counts()
    keycount.plot(
                    kind='bar',
                    x='keycount',
                    y='key',               
                    color='blue',
                    alpha=0.3,
                    title='Key',
                    fontsize=10)
    
    plt.show()

def yearchart():    
    yearcount = my_df['released_year'].value_counts()
    yearcount.plot(
                    kind='bar',
                    x='yearcount',
                    y='released_year',               
                    color='blue',
                    alpha=0.3,
                    title='Key',
                    fontsize=10)
    
    plt.show()

def gui():
    global status
    global row
    global avg

    print('''

Enter:
1. Print Dataframe
2. Visulised version of charts
3. Find specific dataframe
4. Find the average of a certain category (nearest number)
5. Find the top x songs
6. Quit
''')
    try:
        option = int(input('Enter Selection: '))

        if option == 1:
            print(my_df)
        elif option == 2:
            print('''
Which chart would you like to see?
1. Streams Chart
2. Artist Count Chart
3. BPM Chart
4. Mode Chart
5. Key Chart
6. Release Year Chart
                                ''')
            chartno = int(input('Enter Selection: '))
            if chartno == 1:
                streamchart()
            elif chartno == 2:
                artistchart()
            elif chartno == 3:
                bpmchart()
            elif chartno == 4:
                modechart()
            elif chartno == 5:
                keychart()
            elif chartno == 6:
                yearchart()
            else:
                print("Pick another number! ")
        elif option == 3:
            row = int(input("Enter row number: "))
            print(my_df.iloc[row])
        elif option == 4:
            avg = str(input("Enter name of column: ")).lower()
            print(round(my_df.loc[:, avg].mean(), 0))
        elif option == 5:
            popular = int(input('Enter the top x number that you want to find out about: '))
            print(my_df.head(popular))
        elif option == 6:
            status = 0
        else:
            print('Pick another number! ')

    except:
        print('Enter a number! ')


while status == 1:
    gui()

