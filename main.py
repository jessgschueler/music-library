class Artist:

    artist_sequence = 100

    def __init__(self, name, genre, dob):
        self.name = name
        self.genre = genre 
        self.dob = dob
        self.artist_id = Artist.artist_sequence
        Artist.artist_sequence += 1

    def artist_listen(self):
        print(f"Did you know that {self.name}'s birthday is {self.dob}? (artist id: {self.artist_id})")

    def artist_check(str):
        for i in artists[]:
            if(i == str):
                print('Artist is already in here!')
            else:
                print('Artist not found')

artists = []   
artists.append(Artist('Taylor Swift', 'Pop', '12/13/89'))
artists.append(Artist('Phoebe Bridgers', 'Alternative', '8/17/94'))
artists.append(Artist('Mitski', 'Alternative', '9/27/90'))

for artist in artists:
    artist.artist_check()

class Song:
    def __init__(self, artist_id, title, length, lyrics):
        self.artist_id = artist_id
        self.title = title
        self.length = length 
        self.lyrics = lyrics

    def song_check(artist_id):
        for i in songs():
            if(self.artist_id == artist.id):
                print(f'{self.title} is by {self.artist_id}')


