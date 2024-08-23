# importing functions 
import pandas as pd # importing pandas
import matplotlib.pyplot as plt # importing matplotlib
import numpy as nppi # importing numpy

status = 1 # status, whether it is running or not being 1 which means on
original_df = pd.read_csv("Data/spotifydataset.csv", on_bad_lines='warn', encoding='latin-1') # reading the data, making the var original_df the original dataset.
my_df = pd.read_csv("Data/spotifydataset.csv", on_bad_lines='warn', encoding='latin-1')  # reading the data, making the var my_df the original dataset.
my_df = my_df.drop(columns = ['released_month', 'released_day', 'in_spotify_charts', 'in_spotify_playlists', 'in_shazam_charts', 'in_apple_charts', 'in_apple_playlists', 'in_deezer_charts', 'in_deezer_playlists', 'danceability_%', 'valence_%', 'energy_%', 'acousticness_%', 'instrumentalness_%', 'liveness_%', 'speechiness_%']) # removing all unnecessary columns in the my_df dataset
my_df['key'] = my_df['key'].fillna('C') # changing every frame with no key in it to "C"
my_df.to_csv('spotifydata.csv', index=False) # making a clone of the .csv file

    
my_df.iloc[:950] # limiting the file to 950 lines
#my_df['streams'] = my_df['streams'].astype(float) # making the streams var type a float

# printing the welcome statement
print('''
Welcome to spotify's top 950. This is where you find information about the top 950 songs that spotify has to offer. 
      ''')
# making a chart of total streams
def streamchart():
    temp_df = my_df.iloc[:250] # limiting it to 250 lines to make it seeable, rather than just a block of black
    # plotting the graph
    temp_df.plot(
                kind='bar',
                x='track_name',
                y='streams',
                color='blue',
                alpha=0.3,
                title='Streams of top songs',
                fontsize=3)
    plt.savefig('streams.pdf') # saving an image of the graph
    plt.show() # displaying the graph to user

# making a chart of the artist count
def artistchart():
    artistcount = my_df['artist_count'].value_counts() # finding the number of artists in every song, compacting it so it isn't just a long string
    # plotting the graph
    artistcount.plot(
                    kind='bar',
                    x='artistcount',
                    y='artist_count',               
                    color='blue',
                    alpha=0.3,
                    title='Artist Count',
                    fontsize=10)

    
    plt.savefig('artistcount.pdf') # saving an image of the graph
    plt.show() # displaying the graph to user

# making a graph of the bpm
def bpmchart():    
    bpmcount = my_df['bpm'].value_counts() # finding the bpm of every song, compacting it so it isn't just a long string
    # plotting the graph
    bpmcount.plot(
                    kind='bar',
                    x='bpmcount',
                    y='bpm',               
                    color='blue',
                    alpha=0.3,
                    title='BPM',
                    fontsize=10)
    
    
    plt.savefig('bpm.pdf') # saving an image of the graph
    plt.show() # displaying the graph to user

# making a chart of the mode
def modechart():    
    modecount = my_df['mode'].value_counts() # finding the mode of every song, compacting it so it isn't just a long string
    # plotting the graph
    modecount.plot(
                    kind='bar',
                    x='modecount',
                    y='mode',               
                    color='blue',
                    alpha=0.3,
                    title='Mode',
                    fontsize=10)
    

    plt.savefig('mode.pdf') # saving an image of the graph 
    plt.show() # displaying the graph to user

# making a chart of the key
def keychart():    
    keycount = my_df['key'].value_counts() # finding the key of every song, compacting it so it isn't just a long string
    # plotting the graph
    keycount.plot(
                    kind='bar',
                    x='keycount',
                    y='key',               
                    color='blue',
                    alpha=0.3,
                    title='Key',
                    fontsize=10)
    plt.savefig('key.pdf') # saving an image of the graph
    plt.show() # displaying the graph to user

# making a chart of the release years
def yearchart():    
    yearcount = my_df['released_year'].value_counts() # finding the release year of every song, compacting it so it isn't just a long string
    # plotting the graph
    yearcount.plot(
                    kind='bar',
                    x='yearcount',
                    y='released_year',               
                    color='blue',
                    alpha=0.3,
                    title='Key',
                    fontsize=10)
    plt.savefig('yearrelease.pdf') # saving an image of the graph    
    plt.show() # displaying the graph to user

# gui function
def gui():
    global status # making the var status global
    global row # making the var row global
    global avg # making teh var avg global


# printing the gui
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
        option = int(input('Enter Selection: ')) # asking for an option

        if option ==1: 
            print(original_df) # print the original df if option is 1
        elif option ==2:
            print(my_df) # print the cleansed df if option is 2
        elif option == 3:
            # printing a new gui of option is 3
            print('''
Which chart would you like to see?
1. Top 250 Streams Chart 
2. Artist Count Chart
3. BPM Chart
4. Mode Chart
5. Key Chart
6. Release Year Chart
                                ''')
            chartno = int(input('Enter Selection: ')) # asking for option
            if chartno == 1: 
                streamchart() # calling the function stream chart if chart option is 1
            elif chartno == 2:
                artistchart() # calling the function artist chart if chart option is 2
            elif chartno == 3:
                bpmchart() # calling the function bpm chart if chart option is 3
            elif chartno == 4:
                modechart() # calling the function mode chart if chart option is 4
            elif chartno == 5:
                keychart() # calling the function key chart if chart option is 5
            elif chartno == 6:
                yearchart() # calling the function release year chart if chart option is 6
            else:
                print("Pick another number! ") # error code if number is bad
        elif option == 4:
            row = int(input("Enter row number: ")) # if option is 4, ask for a new row number
            print(my_df.iloc[row]) # finding the row of that song and printing it
        elif option == 5:
            avg = str(input("Enter name of column: ")).lower() # if option is 5, ask for a column name
            print(round(my_df.loc[:, avg].mean(), 0)) # find the avg of the df columnn to the nearest number
        elif option == 6:
            med = str(input("Enter name of column: ")).lower() # if option is 6, ask for a column name
            print(round(my_df.loc[:, med].median(), 0)) # find the median of the df columnn to the nearest number
        elif option == 7:            
            mode = str(input("Enter name of column: ")).lower() # if option is 7, ask for a column name
            print(round(my_df.loc[:, mode].mode(), 0)) # find the mode of the df columnn to the nearest number
        elif option == 8:
            popular = int(input('Enter the top x number that you want to find out about: ')) # if option is 8, ask for row number
            print(my_df.head(popular)) # print the rows and all of them below it
        elif option == 9:
            status = 0 # if option is 9, stop the program
        else:
            print('Pick another number! ') # error code if the number is bad

    except:
        print('Enter a number! ') # error code if number is bad


while status == 1: # while the code is running
    gui() # call gui function

