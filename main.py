class Artist:

    artist_sequence = 100
    artists = []

    def __init__(self, name, genre, dob):
        self.name = name
        self.genre = genre 
        self.dob = dob
        self.artist_id = Artist.artist_sequence
        Artist.artist_sequence += 1
    
    def artist_check():
        



grimes = Artist('Grimes', 'Pop', '3/17/88')
mitski = Artist('Mitski', 'Alternative', '9/27/90')

print(names)

# artists = []
# artists.append(Artist('Taylor Swift', 'Pop', '12/13/89'))
# artists.append(Artist('Phoebe Bridgers', 'Alternative', '8/17/94'))
# artists.append(Artist('Mitski', 'Alternative', '9/27/90'))

# grimes = Artist('Grimes', 'Pop', '3/17/88')
# mitski = Artist('Mitski', 'Alternative', '9/27/90')

# grimes.artist_check()
# mitski.artist_check()

# class Song:
#     def __init__(self, artist_id, title, length, lyrics):
#         self.artist_id = artist_id
#         self.title = title
#         self.length = length 
#         self.lyrics = lyrics

#     def song_check(artist_id):
#         for i in songs():
#             if(self.artist_id == artist.id):
#                 print(f'{self.title} is by {self.artist_id}')


