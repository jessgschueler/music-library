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

    @staticmethod
    def print_artists():
        for a in Artist.artists:
            print(f'{a}')

    @staticmethod
    def print_artist_ids():
        for a in Artist.artist_ids:
            print(f'{a}')

class Song:

    def __init__(self, artist_id, title, length, lyrics):
        self.artist_id = artist_id
        self.title = title
        self.length = length 
        self.lyrics = lyrics

    def get_artist_id(self):
        print(f'The Artist Id is {self.artist_id}')
   
atw = Song('101', 'All To Well', '10:13', 'atwlyrics')

atw.get_artist_id()

taylor = Artist('Taylor Swift', 'Pop', '12/13/89')
phoebe = Artist('Phoebe Bridgers', 'Alternative', '8/17/94')
grimes = Artist('Grimes', 'Pop', '3/17/88')
mitski = Artist('Mitski', 'Alternative', '9/27/90')

Artist.print_artists()
Artist.print_artist_ids()

artist_dict = dict(zip(Artist.artist_ids, Artist.artists))

print(artist_dict)