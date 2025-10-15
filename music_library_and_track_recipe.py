# File: lib/music_library.py

class MusicLibrary:
    # Public properties:
    #   tracks: a list of strings representing tracks

    def __init__(self):
        pass

    def add(self, track):
        # Parameters:
        #   track: an instance of Track
        # Returns:
        #   Nothing
        pass

    def search_by_title(self, keyword):
        # Parameters:
        #   keyword: a string
        # Returns:
        #   a list of Track instances with titles that include the keyword
        pass


# File: lib/track.py

class Track:
    # Public properties:
    #   title: a string
    #   artist: a string

    def __init__(self, title, artist):
        # Parameters:
        #   title: a string
        #   artist: a string
        # Side-effects:
        #   Sets the title and artist properties
        pass

    def format(self):
        # Returns:
        #   a string in the format "TITLE by ARTIST"
        pass


"""
When we add two tracks
We get the tracks back in the track list
"""
library = MusicLibrary()
track_1 = Track("Always The Hard Way", "Terror")
track_2 = Track("Higher Place", "Malevolence")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]

"""
When we add two tracks
And we search for a word in the title
We get the matching track back
"""
library = MusicLibrary()
track_1 = Track("Always The Hard Way", "Terror")
track_2 = Track("Higher Place", "Malevolence")
library.add(track_1)
library.add(track_2)
library.search_by_title("Way") # => [track_1]

"""
When we add two tracks
And we search for a small part of a word in the title
We get the matching track back
"""
library = MusicLibrary()
track_1 = Track("Always The Hard Way", "Terror")
track_2 = Track("Higher Place", "Malevolence")
library.add(track_1)
library.add(track_2)
library.search_by_title("lace") # => [track_2]

"""
When we add two tracks
And we search for a word not in any track title
We get an empty list back
"""
library = MusicLibrary()
track_1 = Track("Always The Hard Way", "Terror")
track_2 = Track("Higher Place", "Malevolence")
library.add(track_1)
library.add(track_2)
library.search_by_title("zzz") # => []

"""
Given a track with a title and artist
#format returns a string like TITLE by ARTIST
"""
track = Track("Higher Place", "Malevolence")
track.format() # => "Higher Place by Malevolence"


# File: tests/test_music_library_integration.py
from lib.music_library import MusicLibrary
from lib.track import Track


def test_music_library_integration():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("Always") == [track_1]

# ...

# File: tests/test_unit_music_library.py

def test_music_library():
    library = MusicLibrary()

  # ...

