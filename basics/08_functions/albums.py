print("Albums\n")


def print_album(album):
    print(f"• {album['title']}")
    print(f"\t• Artist: {album['artist_name']}")
    if 'songs_count' in album.keys():
        print(f"\t• Number of Songs: {album['songs_count']}")


def make_album(artist_name, album_title, songs_count=None):
    if songs_count:
        return {
            'artist_name': artist_name,
            'title': album_title, 
            'songs_count': songs_count}
    else:
        return {
            'artist_name': artist_name,
            'title': album_title, }

print_album(make_album('Abdurrahman Sudais', 'Al-Quranul-Kareem'))

print_album(make_album('Sadiq Al-Minshawi', "Al-Qur'an"))

print_album(make_album('Al-Husary', "Al-Qur'an Audio", 114))
