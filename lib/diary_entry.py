# File: lib/diary_entry.py
import math

class DiaryEntry():
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self.title = title
        self.contents = contents
        self._text = title + ": " + contents

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        return len(self._text.split())

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        return math.ceil(self.count_words()/ wpm)
    
    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        readable_chunk = wpm * minutes
        if len(self._text) > 0 :
            text_read = " ".join(self._text.split()[:readable_chunk])
            self._text = " ".join(self._text.split()[readable_chunk:])
        else:
            self._text = self.title + ": " + self.contents
            text_read = " ".join(self._text.split()[:readable_chunk])
            self._text = " ".join(self._text.split()[readable_chunk:])
        return text_read
    

    # 11 words to read
    # 2 wpm
    # 2 minutes reading time
    # first chunk - "Zoo trip Today I went to the zoo with my friends." ==> ZZoo trip Today I
    #  next chunk ==> went to the zoo

diary_entry_1 = DiaryEntry("Zoo trip", "Today I went to the zoo with my friends.")
diary_entry_2 = DiaryEntry("Birthday Party", "Tomorrow I will celebrate my friend's Emma's birthday.")
diary_entry_3 = DiaryEntry("Soft Play", "The day after tomorrow is Friday, soft play time!")
print(diary_entry_1.reading_chunk(2,2))
print(diary_entry_1.reading_chunk(2,2))
print(diary_entry_1.reading_chunk(2,2))
print(diary_entry_1.reading_chunk(2,2))
print(diary_entry_1.reading_chunk(2,2))
print(diary_entry_1.reading_chunk(2,2))
print(diary_entry_1.reading_chunk(2,2))
print(diary_entry_1.reading_chunk(2,2))
print(diary_entry_1.reading_chunk(2,2))
print(diary_entry_1.reading_chunk(2,2))
print(diary_entry_1.reading_chunk(2,2))
print(diary_entry_1.reading_chunk(2,2))
print(diary_entry_1.reading_chunk(2,2))
print(diary_entry_1.reading_chunk(2,2))