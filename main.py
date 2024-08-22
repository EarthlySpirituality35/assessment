# importing functions 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as nppi

status = 1
original_df = pd.read_csv("Data/spotifydataset.csv", on_bad_lines='warn', encoding='latin-1')
my_df = pd.read_csv("Data/spotifydataset.csv", on_bad_lines='warn', encoding='latin-1')
my_df = my_df.drop(columns = ['released_month', 'released_day', 'in_spotify_charts', 'in_spotify_playlists', 'in_shazam_charts', 'in_apple_charts', 'in_apple_playlists', 'in_deezer_charts', 'in_deezer_playlists', 'danceability_%', 'valence_%', 'energy_%', 'acousticness_%', 'instrumentalness_%', 'liveness_%', 'speechiness_%'])

my_df['key'] = my_df['key'].fillna('C')
       

    
my_df.iloc[:950]
#my_df['streams'] = my_df['streams'].astype(float)

print('''
Welcome to spotify's top 950. This is where you find information about the top 950 songs that spotify has to offer. 
      ''')

def streamchart():
    temp_df = my_df.iloc[:250]
    temp_df.plot(
                kind='bar',
                x='track_name',
                y='streams',
                color='blue',
                alpha=0.3,
                title='Streams of top songs',
                fontsize=3)
    plt.savefig('streams.pdf')
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

    
    plt.savefig('artistcount.pdf')
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
    
    
    plt.savefig('bpm.pdf')
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
    

    plt.savefig('mode.pdf') 
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
    plt.savefig('key.pdf')
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
    plt.savefig('yearrelease.pdf')    
    plt.show()


def gui():
    global status
    global row
    global avg

    print('''

Enter:
1. Print Original Dataframe
2. Print Dataframe
3. Visulised version of charts
4. Find specific dataframe
5. Find the average of a certain category (bpm, aritst_count, released year to the nearest number)
6. Find the average of a certain category (bpm, aritst_count, released year to the nearest number)       
7. Find the average of a certain category (bpm, aritst_count, released year to the nearest number)
8. Find the top x songs
9. Quit
''')
    try:
        option = int(input('Enter Selection: '))

        if option ==1:
            print(original_df)
        elif option ==2:
            print(my_df)
        elif option == 3:
            print('''
Which chart would you like to see?
1. Top 250 Streams Chart 
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
        elif option == 4:
            row = int(input("Enter row number: "))
            print(my_df.iloc[row])
        elif option == 5:
            avg = str(input("Enter name of column: ")).lower()
            print(round(my_df.loc[:, avg].mean(), 0))
        elif option == 6:
            med = str(input("Enter name of column: ")).lower()
            print(round(my_df.loc[:, med].median(), 0))
        elif option == 7:            
            mode = str(input("Enter name of column: ")).lower()
            print(round(my_df.loc[:, mode].mode(), 0))
        elif option == 8:
            popular = int(input('Enter the top x number that you want to find out about: '))
            print(my_df.head(popular))
        elif option == 9:
            status = 0
        else:
            print('Pick another number! ')

    except:
        print('Enter a number! ')


while status == 1:
    gui()

