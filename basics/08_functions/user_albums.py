""" 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that 
information, call make_album() with the user’s input and print the dictionary 
that’s created. Be sure to include a quit value in the while loop. """

print("User Albums")


def print_album(album):
    print("\nHere's your album")
    print(f"• {album['title']}")
    print(f"\t• Artist: {album['artist_name']}")
    if 'songs_count' in album.keys():
        print(f"\t• Number of Songs: {album['songs_count']}")


def make_album(artist_name, album_title, songs_count=None):
    print("Making Album ...")
    if songs_count:
        return {
            'artist_name': artist_name,
            'title': album_title, 
            'songs_count': songs_count}
    else:
        return {
            'artist_name': artist_name,
            'title': album_title, }


print("\nWelcome to Python Audio")
print("Kindly enter the details of the ablum you want " + 
    "so we can get it for you.")

while True:
    print("\nAlbum Details")
    artist_name = input("• Artist Name: ")
    album_title = input("• Title: ")
    songs_count = int(input("• Number of Songs: "))

    print_album(make_album(artist_name, album_title, songs_count))

    print("\nDo you still want to get another album?")
    quit_response = input("Enter 'y' for yes, 'n' for no: ")
    if quit_response == 'y':
        print("\nEnter Again.")
        continue
    elif quit_response == 'n':
        break
    else:
        print("\nYou entered a wrong value, we'll continue anyways.")
        continue

