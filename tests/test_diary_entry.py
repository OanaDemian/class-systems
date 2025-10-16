from lib.diary_entry import DiaryEntry

"""
When I initialize with a title and contents
I get that title and contents back
"""

def test_constructs_and_gets_title_and_contents():
    diary_entry_1 = DiaryEntry("Zoo trip", "Today I went to the zoo with my friends.")
    assert diary_entry_1.title == "Zoo trip"
    assert diary_entry_1.contents == "Today I went to the zoo with my friends."

"""
When I initialise with a 2 words title and a nine words contents
That would be reflected in the count_words() result 11
"""


def test_constructs_and_gets_title_and_contents():
    diary_entry_1 = DiaryEntry("Zoo trip", "Today I went to the zoo with my friends.")
    assert diary_entry_1.count_words() == 11

"""
When I initialise with a 1 word title and a 4 words contents
tne #reading_time with a wpm of 2 should return 3
"""


def test_reading_time():
    diary_entry_1 = DiaryEntry("Zoo", "I visited the zoo.")
    assert diary_entry_1.reading_time(2) == 3


"""
When I initialise with a 5 words title and contents
then, at  first, #reading_chunk should return the first chunk readable in the given time 
"""


def test_reading_chunk_initial_chunk():
    diary_entry_1 = DiaryEntry("Zoo", "I visited the zoo.")
    assert diary_entry_1.reading_chunk(1, 2) == "Zoo: I"

"""
When I initialise with a 5 words title and contents
then, called twice, #reading_chunk should return the second chunk readable in the given time 
"""


def test_reading_chunk_second_chunk():
    diary_entry_1 = DiaryEntry("Zoo", "I visited the zoo.")
    assert diary_entry_1.reading_chunk(1, 2) == "Zoo: I"
    assert diary_entry_1.reading_chunk(1, 2) == "visited the"
    
"""
When I initialise with a 5 words title and contents
then, called twice, #reading_chunk should return the second chunk readable in the given time 
"""


def test_reading_chunk_last_chunk():
    diary_entry_1 = DiaryEntry("Zoo", "I visited the zoo.")
    assert diary_entry_1.reading_chunk(1, 2) == "Zoo: I"
    assert diary_entry_1.reading_chunk(1, 2) == "visited the"
    assert diary_entry_1.reading_chunk(1, 2) == "zoo."

"""
When I initialise with a5  words title and contents
then, called 4 times with 1wpm and an interval of 2 minutes
#reading_chunk should start reading the entry again
"""


def test_reading_chunk_restarts():
    diary_entry_1 = DiaryEntry("Zoo", "I visited the zoo.")
    assert diary_entry_1.reading_chunk(1, 2) == "Zoo: I"
    assert diary_entry_1.reading_chunk(1, 2) == "visited the"
    assert diary_entry_1.reading_chunk(1, 2) == "zoo."
    assert diary_entry_1.reading_chunk(1, 2) == "Zoo: I"