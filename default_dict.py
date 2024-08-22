from collections import defaultdict


class Cookbook:
    pass


def create_author_count_manning(cookbooks: list[Cookbook]):
    counter = defaultdict(lambda: 0)
    for cookbook in cookbooks:
        counter[cookbook.author] += 1
    return counter

