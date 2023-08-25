def check_scores(telegram_score: tuple[int, int], match: tuple[int, int]) -> bool:
    is_equal_first_variant = (
        telegram_score[0] == match[0] and telegram_score[1] == match[1]
    )
    is_equal_second_variant = (
        telegram_score[0] == match[1] and telegram_score[1] == match[0]
    )

    if is_equal_first_variant or is_equal_second_variant:
        return True

    return False
