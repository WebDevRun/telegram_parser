import pytest
from parse_telegram.utils.check_scores import check_scores


def reverse_score(score: tuple[int, int]) -> tuple[int, int]:
    (first_score, second_score) = score

    return (second_score, first_score)


telegram_score = (1, 0)
match_score = (1, 0)


@pytest.mark.parametrize(
    "telegram_score, match_score",
    [
        (telegram_score, match_score),
        (reverse_score(telegram_score), match_score),
        (telegram_score, reverse_score(match_score)),
    ],
)
def test_return_true_when_equal_scores(
    telegram_score: tuple[int, int], match_score: tuple[int, int]
):
    assert check_scores(telegram_score, match_score) == True


telegram_score = (2, 0)
match_score = (1, 0)


@pytest.mark.parametrize(
    "telegram_score, match_score",
    [
        (telegram_score, match_score),
        (reverse_score(telegram_score), match_score),
        (telegram_score, reverse_score(match_score)),
    ],
)
def test_return_false_when_unequal_scores(
    telegram_score: tuple[int, int], match_score: tuple[int, int]
):
    assert check_scores(telegram_score, match_score) == False
