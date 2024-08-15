# importing functions 
import pandas as pd
import matplotlib.pyplot as plt

global status; status = 1

my_df = pd.read_csv("Data/spotifydataset.csv", on_bad_lines='warn', encoding='latin-1')
my_df = my_df.drop(columns = ['released_month', 'released_day', 'in_spotify_charts', 'in_spotify_playlists', 'in_shazam_charts', 'in_apple_charts', 'in_apple_playlists', 'in_deezer_charts', 'in_deezer_playlists', 'danceability_%', 'valence_%', 'energy_%', 'acousticness_%', 'instrumentalness_%', 'liveness_%', 'speechiness_%'])

def charts():
    my_df.plot(
                kind='bar',
                x='Country',
                y='AUD',
                color='blue',
                alpha=0.3,
                title='Cost of a Big Mac in AUD')
    plt.show()

def gui():
    global status
    global row
    global avg
    print('''
Spotify Dataset

Type:
1. Print Dataframe
2. Find specific dataframe
3. Find the average of a certain category (nearest number)
4. Quit
        


''')
    try:
        option = int(input('Enter Selection: '))

        if option == 1:
            print(my_df)
        elif option == 2:
            charts()
        elif option == 3:
            row = int(input("Enter row number: "))
            print(my_df.iloc[row])
        elif option == 4:
            avg = str(input("Enter name of column: ")).lower()
            print(round(my_df.loc[:, avg].mean(), 0))
        elif option == 5:
            status = 0
        else:
            print('A number between 1 and 4, come on!')

    except:
        print('Enter a number, it is not that hard.')


while status == 1:
    gui()
