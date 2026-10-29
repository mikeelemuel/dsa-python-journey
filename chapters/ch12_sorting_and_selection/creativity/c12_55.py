"""
C-12.55 | Chapter 12: Sorting and Selection
Type: Creativity
Page: book p.579 (PDF p.601)    ->  python tools/show.py C-12.55
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    We can make the quick-select algorithm deterministic, by choosing the pivot of an
    n-element sequence as follows: Partition the set S into ⌈n/5⌉ groups of size 5 each
    (except pos- sibly for one group). Sort each little set and identify the median
    element in this set. From this set of ⌈n/5⌉ “baby” medians, ap- ply the selection
    algorithm recursively to ﬁnd the median of the baby medians. Use this element as the
    pivot and proceed as in the quick-select algorithm. Show that this deterministic
    quick-select algorithm runs in O(n) time by answering the following questions
    (please ignore ﬂoor and ceiling func- tions if that simpliﬁes the mathematics, for
    the asymptotics are the same either way): a. How many baby medians are less than or
    equal to the chosen pivot? How many are greater than or equal to the pivot? b. For
    each baby median less than or equal to the pivot, how many other elements are less
    than or equal to the pivot? Is the same true for those greater than or equal to the
    pivot? c. Argue why the method for ﬁnding the deterministic pivot and using it to
    partition S takes O(n) time. d. Based on these estimates, write a recurrence
    equation to bound the worst-case running timet(n) for this selection algorithm (note
    that in the worst case there are two recursive calls—one to ﬁnd the median of the
    baby medians and one to recur on the larger of L and G). e. Using this recurrence
    equation, show by induction that t(n) is O(n).

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
