# importing functions 
import pandas as pd
import matplotlib.pyplot as plt

status = 1

my_df = pd.read_csv("Data/spotifydataset.csv", on_bad_lines='warn', encoding='latin-1')

my_df = my_df.drop(columns = ['released_month', 'released_day', 'in_spotify_charts', 'in_spotify_playlists', 'in_shazam_charts', 'in_apple_charts', 'in_apple_playlists', 'in_deezer_charts', 'in_deezer_playlists', 'danceability_%', 'valence_%', 'energy_%', 'acousticness_%', 'instrumentalness_%', 'liveness_%', 'speechiness_%'])

#my_df['streams'] = my_df['streams'].astype(float)

def acharts():
    my_df.plot(
                kind='barh',
                x='track_name',
                y='streams',
                color='blue',
                alpha=0.3,
                title='Streams of top songs',
                fontsize=0.1,
                set_yticks=20(),
                set_ylabels=20)
    plt.show()

def gui():
    global status
    global row
    global avg
    print('''
Spotify Dataset

Type:
1. Print Dataframe
2. A chart of the number of streams of songs
3. Find specific dataframe
4. Find the average of a certain category (nearest number)
5. Quit
        


''')
    try:
        option = int(input('Enter Selection: '))

        if option == 1:
            print(my_df)
        elif option == 2:
            acharts()
        elif option == 3:
            row = int(input("Enter row number: "))
            print(my_df.iloc[row])
        elif option == 4:
            avg = str(input("Enter name of column: ")).lower()
            print(round(my_df.loc[:, avg].mean(), 0))
        elif option == 5:
            status = 0
        else:
            print('Pick another number! ')

    except:
        print('Enter a number! ')


while status == 1:
    gui()
