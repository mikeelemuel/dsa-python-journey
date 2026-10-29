"""
P-6.35 | Chapter 6: Stacks, Queues, and Deques
Type: Project
Page: book p.253 (PDF p.275)    ->  python tools/show.py P-6.35
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    The introduction of Section 6.1 notes that stacks are often used to provide “undo”
    support in applications like a Web browser or text editor. While support for undo
    can be implemented with an unbounded stack, many applications provide only limited
    support for such an undo history, with a ﬁxed-capacity stack. When push is invoked
    with the stack at full capacity, rather than throwing a Full exception (as described
    in Exercise C-6.16), a more typical semantic is to accept the pushed element at the
    top while “leaking” the oldest element from the bottom of the stack to make room.
    Give an implementation of such aLeakyStack abstraction, using a circular array with
    appropriate storage capacity. This class should have a public interface similar to
    the bounded-capacity stack in Exercise C-6.16, but with the desired leaky semantics
    when full.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
