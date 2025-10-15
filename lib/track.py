# File: lib/track.py

class Track:

    def __init__(self, title, artist):
        self._title = title
        self._artist = artist

    def get_artist(self):
        return self._artist

    def get_title(self):
        return self._title

    def format(self):
        return f"{self._title} by {self._artist}"

