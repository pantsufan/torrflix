#TorFlix Clone
import requests # Used for fetching the resukts from th API
import subprocess # Used to call npm commands
import sys # Used to verify which OS is used

def main():
    movie_name = input("Enter Movie Name\n") #takes the user input
    base_url = f"https://api.sumanjay.cf/torrent/?query={movie_name}" #appends the input to the API
    # Fetches the Results
    movie_results = requests.get(base_url).json()
    index = 1 #set the index inorder to select the movie
    magnet = [] #stores the magnet links in a list
    for result in movie_results: #Loop through the results
        if 'movie' in result['type'].lower(): #checks if the type is of movie or not
            if index <= 10: # shows only the top 10 results
                print(index, ") ", result['name']," Size:", result['size']) #prints the name and size of the movie
                index +=1 #increment the index
                magnet.append(result['magnet']) #adds the magnet links to the list

    choice = int(input("Enter Your Choice Index\n")) #takes the user choice
    magnet_link = magnet[choice-1] #selects the magnet link from the choice -1 is beacuse of index=1
    download = False #sets download parameter to false
    stream_choice = int(input("Press 1 to Stream or Press 2 to Download\n")) #gives user 2 options
    if stream_choice == 1: 
        download = False #sets again to false
    elif stream_choice == 2:
        download = True #sets True
    else:
        print("Wrong Input\n Exiting...")
    handler(magnet_link,download) #calls the handler function

def handler(magnet_link, download): # handler functions creates a list (cmd) and appends the webtorrent commands
    cmd = []
    cmd.append("webtorrent")
    cmd.append(magnet_link)
    if not download:
        cmd.append('--mpv') #appends the mpv player command (refer webtorrent github for other players)
    if sys.platform.startswith('linux'):
        subprocess.call(cmd) # executes the webtorrent command on linux
    elif sys.platform.startswith('win32'):
        subprocess.call(cmd,shell=True) # execute the webtorrent command on windows

main() # calls the main function