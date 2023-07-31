from typing import NamedTuple

live = "live"
score = "счёт"


class ValuesType(NamedTuple):
    teams: str
    score: tuple[int, int]
    time: int


def get_index_from_arr(arr: list[str], substr: str):
    for i, str in enumerate(arr):
        if substr in str:
            return i

    return -1


def get_values(string: str) -> ValuesType | None:
    str_lower = string.lower()

    if (live not in str_lower) and (score not in str_lower):
        return None

    list_values = str_lower.split("\n")
    live_index = get_index_from_arr(list_values, live)
    live_str = list_values[live_index]

    teams = live_str[len(live) + 2 :]
    score_index = get_index_from_arr(list_values, score)
    score_str = list_values[score_index]

    first_team_goal_count_str = score_str[len(score) + 2 : len(score) + 3]
    second_team_goal_count_str = score_str[len(score) + 4 : len(score) + 5]

    time_str = score_str[-3:-1]

    return ValuesType(
        teams=teams,
        score=(int(first_team_goal_count_str), int(second_team_goal_count_str)),
        time=int(time_str),
    )
