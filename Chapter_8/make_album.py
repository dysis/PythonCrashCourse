def make_album(artist_name, album_title, tracks = ''):
    album = {'artist' : artist_name.title(), 'name' : album_title.title()}
    if tracks:
        album['tracks'] = tracks
    return album



while True:
    print("\nPlease give me the deatils on the album:")
    print("(At any time you type 'q' to quit.")

    alb_name = input("Input Album Name: ")
    if alb_name == 'q':
        break

    art_name = input("Input Artist Name: ")
    if art_name == 'q':
        break

    formatted_album = make_album(art_name, alb_name)
    print(formatted_album)
