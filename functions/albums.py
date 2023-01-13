def make_album(artist, title, no_songs = None):
	album = {artist.title() : title.title(),}
	if no_songs:
		album = {artist.title() : title.title(), 'songs' : no_songs}
	else:
		album = {artist.title() : title.title()}

	return album

while True:
	artist_name = input('Enter artist name: (Enter q to exit)\n')
	album_name = input('Enter album_name:\n')


	if artist_name == 'q' or album_name == 'q':
		break
	else:
		print(make_album(artist_name, album_name))