"""
C-10.33 | Chapter 10: Maps, Hash Tables, and Skip Lists
Type: Creativity
Page: book p.455 (PDF p.477)    ->  python tools/show.py C-10.33
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    Our implementation of separate chaining in ChainHashMap conserves memory by
    representing empty buckets in the table as None, rather than as empty instances of a
    secondary structure. Because many of these buck- ets will hold a single item, a
    better optimization is to have those slots of the table directly reference the Item
    instance, and to reserve use of sec- ondary containers for buckets that have two or
    more items. Modify our implementation to provide this additional optimization.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
