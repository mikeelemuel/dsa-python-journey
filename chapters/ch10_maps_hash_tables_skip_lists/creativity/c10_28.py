"""
C-10.28 | Chapter 10: Maps, Hash Tables, and Skip Lists
Type: Creativity
Page: book p.454 (PDF p.476)    ->  python tools/show.py C-10.28
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    On page 406 of Section 10.1.3, we give an implementation of the method setdefault as
    it might appear in the MutableMapping abstract base class. While that method
    accomplishes the goal in a general fashion, its efﬁ- ciency is less than ideal. In
    particular, when the key is new, there will be a failed search due to the initial
    use of getitem , and then a subse- quent insertion via setitem . For a concrete
    implementation, such as the UnsortedTableMap, this is twice the work because a
    complete scan of the table will take place during the failed getitem , and then an-
    other complete scan of the table takes place due to the implementation of setitem .
    A better solution is for theUnsortedTableMapclass to over- ride setdefault to
    provide a direct solution that performs a single search. Give such an implementation
    of UnsortedTableMap.setdefault.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
