from lib.music_library import MusicLibrary
from unittest.mock import Mock

"""
Initially,
The track list is empty
"""

def test_library_empty():
    library = MusicLibrary()
    assert library.get_tracks() == []

"""
When we add one music track to the library,
We can see it reflected in the list of music tracks
"""

def test_library_adds_one_track():
    library = MusicLibrary()
    track_1 = "Always The Hard Way by Terror"
    track_2 = "Higher Place Malevolence"
    library.add(track_1)
    assert library.get_tracks() == [track_1]

"""
When we add two music tracks to the library,
We can see this reflected in the list of music tracks
"""

def test_library_adds_two_tracks():
    library = MusicLibrary()
    track_1 = "Always The Hard Way by Terror"
    track_2 = "Higher Place by Malevolence"
    library.add(track_1)
    library.add(track_2)
    assert library.get_tracks() == [track_1, track_2]


"""
When we add two tracks
And we search for a word in the title
We get the matching track back
"""
def test_library_seach_by_title_when_two_tracks_added():
    library = MusicLibrary()
    track_1 = Mock()
    track_2 = Mock()
    track_1.get_title.return_value = "Always The Hard Way"
    track_2.get_title.return_value = "Higher Place "
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("Way") == [track_1]


"""
When we add two tracks
And we search for a word not in any track title
We get an empty list back
"""

def test_library_when_two_tracks_added_and_searchword_not_in_any_title():
    library = MusicLibrary()
    track_1 = Mock()
    track_2 = Mock()
    library.add(track_1)
    library.add(track_2)
    track_1.get_title.return_value = "Always The Hard Way"
    track_2.get_title.return_value = "Higher Place "
    assert library.search_by_title("zzz") == []

"""
When we add two tracks
And we search for a small part of a word in the title
We get the matching track back
"""

def test_library_when_two_tracks_added_and_searchword_not_in_any_title():
    library = MusicLibrary()
    track_1 = Mock()
    track_2 = Mock()
    library.add(track_1)
    library.add(track_2)
    track_1.get_title.return_value = "Always The Hard Way"
    track_2.get_title.return_value = "Higher Place"
    assert library.search_by_title("Place") == [track_2]