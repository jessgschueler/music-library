artist_id_sequence = 100

class Artist:
    def __init__(self, artist_id, name, genre, dob):
        global artist_id_sequence
        self.artist_id = artist_id_sequence
        artist_id_sequence += 1
        self.name = name
        self.genre = genre 
        self.dob = dob

class Song:
    def __init__(self, artist_id, title, length, lyrics):
        self.artist_id = artist_id
        self.title = title
        self.length = length 
        self.lyrics = lyrics

