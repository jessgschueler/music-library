class Artist:

    artist_sequence = 100
    artists = []

    def __init__(self, name, genre, dob):
        self.name = name
        Artist.artists.append(name)
        self.genre = genre 
        self.dob = dob
        self.artist_id = Artist.artist_sequence
        Artist.artist_sequence += 1
    
    def artist_check(self):
        if self.name in Artist.artists:
            print(f'{self.name} is already on the list!')
        else:
            print('Artist not found.')

taylor = Artist('Taylor Swift', 'Pop', '12/13/89')
phoebe = Artist('Phoebe Bridgers', 'Alternative', '8/17/94')
grimes = Artist('Grimes', 'Pop', '3/17/88')
mitski = Artist('Mitski', 'Alternative', '9/27/90')
grimes = Artist('Grimes', 'Pop', '3/17/88')


artist_dict = {
    '{self.artist_id}':'{self.name}'
}


class Song:
    def __init__(self, artist_id, title, length, lyrics):
        self.artist_id = artist_id
        self.title = title
        self.length = length 
        self.lyrics = lyrics

    def get_artist_id(self):
        print(f'The Artist Id is {self.artist_id}')
   

atw = Song('100', 'All To Well', '10:13', 'atwlyrics')

atw.get_artist_id()