"""
P-9.57 | Chapter 9: Priority Queues
Type: Project
Page: book p.400 (PDF p.422)    ->  python tools/show.py P-9.57
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    One of the main applications of priority queues is in operating systems— for
    scheduling jobs on a CPU. In this project you are to build a program that schedules
    simulated CPU jobs. Your program should run in a loop, each iteration of which
    corresponds to a time slice for the CPU. Each job is assigned a priority, which is
    an integer between −20 (highest priority) and 19 (lowest priority), inclusive. From
    among all jobs waiting to be pro- cessed in a time slice, the CPU must work on a job
    with highest priority. In this simulation, each job will also come with alength
    value, which is an integer between 1 and 100, inclusive, indicating the number of
    time slices that are needed to process this job. For simplicity, you may assume jobs
    cannot be interrupted—once it is scheduled on the CPU, a job runs for a number of
    time slices equal to its length. Your simulator must output the name of the job
    running on the CPU in each time slice and must process a sequence of commands, one
    per time slice, each of which is of the form “add job name with length n and
    priority p” or “no new job this slice”.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
