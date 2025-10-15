

class MusicLibrary:

    def __init__(self):
        self._tracks = []

    def add(self, track):
        self._tracks.append(track)
        pass

    def get_tracks(self):
        return self._tracks

    def search_by_title(self, keyword):
        return list(filter((lambda track : track.get_title().find(keyword) != -1), self._tracks))
