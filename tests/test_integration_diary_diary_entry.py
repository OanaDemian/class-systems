from lib.diary_entry import DiaryEntry
from lib.diary import Diary

"""
When I add a diary_entry to my diary,
This will be reflected in the list of diary entries
"""

def test_diary_adds_one_diary_entry():
    diary = Diary()
    diary_entry = DiaryEntry("Zoo trip", "Today I went to the zoo with my friends")
    diary.add(diary_entry)
    assert diary.all() == [diary_entry]

"""
When I add two diary entries to my diary,
#count_words will give me the number of words in all diary entries
"""

def test_diary_adds_one_diary_entry():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Zoo trip", "Today I went to the zoo with my friends.")
    diary_entry_2 = DiaryEntry("Birthday Party", "Tomorrow I will celebrate my friend's Emma's birthday.")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.count_words() == 21

"""
Give 3 diary entries and a total of 32 words
Given a user's reading speed of 3 wpm
# reading_time will return 11 representing an estimate of the reading time in minutes
"""

def test_diary_adds_one_diary_entry():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Zoo trip", "Today I went to the zoo with my friends.")
    diary_entry_2 = DiaryEntry("Birthday Party", "Tomorrow I will celebrate my friend's Emma's birthday.")
    diary_entry_3 = DiaryEntry("Soft Play", "The day after tomorrow is Friday, soft play time!")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)
    assert diary.reading_time(3) == 11


"""
Give 3 diary entries and a total of 32 words
Given a user's reading speed of 3 wpm and an interval of 3 minutes for reading
# find_best_entry_for_reading_time return the diary entry representing the closestentry for reading time in minutes #diary_entry_2 
"""

def test_diary_returns_diary_entry_with_closest_reading_time():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Zoo trip", "Today I went to the zoo with my friends.") #11
    diary_entry_2 = DiaryEntry("Birthday Party", "Tomorrow I will celebrate my friend's Emma's birthday.") #10
    diary_entry_3 = DiaryEntry("Soft Play", "The day after tomorrow is Friday, soft play time!") # 11
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)
    assert diary.find_best_entry_for_reading_time(3, 3) == diary_entry_2