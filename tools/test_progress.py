import pytest

from tools.progress import streak


@pytest.mark.parametrize(
    "dates, expected",
    [
        ([], 0),                                        # no sessions
        # Dates are in the past on purpose, so today-anchored logic fails.
        (["2020-01-08"], 1),                              # single Wed
        (["2020-01-06", "2020-01-08"], 1),                # gap on Tue breaks it
        (["2020-01-03", "2020-01-06", "2020-01-07"], 3),  # Fri + Mon + Tue, weekend skipped
    ],
)
def test_streak_counts_back_from_last_session(dates, expected):
    # Must not depend on date.today(): CI runs in UTC and must reproduce PROGRESS.md.
    assert streak(dates) == expected
