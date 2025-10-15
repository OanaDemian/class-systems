
from lib.track import Track

"""
When we add a new track
We can get its title back
"""
def test_get_title_when_track_added():
    track = Track("Title", "Artist")
    assert track.get_title()  == "Title"
"""
When we add a new track
We can get its artist back
"""
def test_get_artist_when_track_added():
    track = Track("Title", "Artist")
    assert track.get_artist()  == "Artist"

def test_formats_the_track():
    track = Track("Title", "Artist")
    assert track.format() == "Title by Artist"