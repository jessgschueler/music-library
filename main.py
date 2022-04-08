class Artist:

    artist_sequence = 100
    artists = []
    artist_ids = []

    def __init__(self, name, genre, dob):
        self.name = name
        Artist.artists.append(name)
        self.genre = genre 
        self.dob = dob
        self.artist_id = Artist.artist_sequence
        Artist.artist_sequence += 1
        Artist.artist_ids.append(Artist.artist_sequence)
    
    def artist_check(self):
        if self.name in Artist.artists:
            print(f'{self.name} is already on the list!')
        else:
            print('Artist not found.')

class Song:

    artist_id_song = []
    titles = []

    def __init__(self, artist_id, title, length, lyrics):
        self.artist_id = artist_id
        Song.artist_id_song.append(artist_id)
        self.title = title
        Song.titles.append(title)
        self.length = length 
        self.lyrics = lyrics

    def get_artist_id(self):
        print(f'The Artist Id is {self.artist_id}')
   
atw = Song(101, 'All To Well', '10:13', 'atwlyrics')

atw.get_artist_id()

taylor = Artist('Taylor Swift', 'Pop', '12/13/89')
phoebe = Artist('Phoebe Bridgers', 'Alternative', '8/17/94')
grimes = Artist('Grimes', 'Pop', '3/17/88')
mitski = Artist('Mitski', 'Alternative', '9/27/90')

for round in range(1,3):
    a = input('Enter artist name...')
    b = input('Enter artist genre...')
    c = input('Enter artist birthday (m/d/yy)...')
    artist1 = Artist(a, b, c)
    

artist_dict = dict(zip(Artist.artist_ids, Artist.artists))
print(artist_dict)

song_dict = dict(zip(Song.artist_id_song, Song.titles))
print(song_dict)
