from chapters.ch01_python_primer.projects.p01_36 import list_of_words


def test_counts_each_word():
    words = "the cat and the hat the end".split()
    assert list_of_words(words) == {"the": 3, "cat": 1, "and": 1, "hat": 1, "end": 1}


def test_empty_list_gives_empty_dict():
    assert list_of_words([]) == {}


def test_case_sensitive():
    assert list_of_words(["The", "the"]) == {"The": 1, "the": 1}
