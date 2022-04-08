from ssl import ALERT_DESCRIPTION_USER_CANCELLED


class Artist:

    artist_id_sequence = 100

    def __init__(self, artist_id, name, genre, dob):
        self.artist_id = Artist.artist_id_sequence
        artist_id_sequence += 1
        self.name = name
        self.genre = genre 
        self.dob = dob

    def artist_check(self):
        for i in artists():
            if(i == self):
                print('Artist is already in here!')


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


