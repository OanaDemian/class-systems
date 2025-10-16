import pytest
from lib.diary import Diary

"""
Initially, has an empty list of entries
"""

def test_diary_initially_has_empty_list_of_entries():
    diary = Diary()
    assert diary.all() == []

"""
Initially, #count_words is 0
"""

def test_initially_count_words_is_0():
    diary = Diary()
    assert diary.count_words() == 0

"""
Initially, #reading_time should return an error
"""

def test_initially_reading_time_treturns_error():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.reading_time(2)
    assert str(e.value) == "No entries added yet"

"""
Initially, #find_best_reading_time should return an error
"""

def test_initially_find_best_entry_for_reading_time_treturns_error():
    diary = Diary()
    with pytest.raises(Exception) as  e:
        diary.find_best_entry_for_reading_time(1,3)
    assert str(e.value) == "No entries added yet"