# design a class called Album
class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist
 
    def __str__(self):
        return f"{self.album_name} by {self.album_artist} ({self.number_of_songs})"
# Create a new list called albums1, add five Album objects to it, and print out the list
albums1 = [hotel_california := Album("Hotel California", 9, "Eagles"),
           thriller := Album("Thriller", 9, "Michael Jackson"),
              back_in_black := Album("Back in Black", 10, "AC/DC"),
              master_of_puppets := Album("Master of Puppets", 8, "Metallica"),
              pink_floyd_the_wall := Album("The Wall", 26, "Pink Floyd")]
print("Albums List:")
for album in albums1:
    print(album)
# Sort the list according to the number_of_songs and print it out
albums1.sort(key=lambda x: x.number_of_songs)
print("\nSorted Albums List by Number of Songs:")
for album in albums1:
    print(album)
#Swap the element at position 1 (index 0) of albums1 with the element at position 2 (index 1) and print it out
albums1[0], albums1[1] = albums1[1], albums1[0]
print("\nAlbums List after swapping first two elements:")
for album in albums1:
    print(album)

#Create a new list called albums2. Add five Album objects to the albums2 list, and print out the list
albums2 = [abbey_road := Album("Abbey Road", 17, "The Beatles"),
           madonna_like_a_virgin := Album("Like a Virgin", 10, "Madonna"),
           the_bodyguard := Album("The Bodyguard", 12, "Whitney Houston"),
           rumor := Album("Rumours", 11, "Fleetwood Mac"),
           born_to_run := Album("Born to Run", 8, "Bruce Springsteen")]   
# Copy all of the albums from albums1 into albums2
albums2.extend(albums1)
# Add the following two albums to albums2: Dark Side of the Moon, Pink Floyd, 9, Oops!... I Did It Again, Britney Spears, 16
albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
albums2.append(Album("Oops!... I Did It Again", 16, "Britney Spears"))
#Sort the albums in albums2 alphabetically according to the album name and print out the sorted list
albums2.sort(key=lambda x: x.album_name)
print("\nSorted Albums List by Album Name:")
for album in albums2:
    print(album)
# Search for the album Dark Side of the Moon in albums2 and print out the index of the album in the albums2 list
def find_album_index(albums, album_name):
    for index, album in enumerate(albums):
        if album.album_name == album_name:
            return index
    return -1
index = find_album_index(albums2, "Dark Side of the Moon")
if index != -1:
    print(f"\nThe album 'Dark Side of the Moon' is found at index: {index}")
else:
    print("\nThe album 'Dark Side of the Moon' is not found in the list.")
    