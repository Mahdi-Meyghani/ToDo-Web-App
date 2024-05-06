"""
This module is for get and write the rate of moods
from the moods.txt file
"""

PATH = "moods.txt"


def get_moods(filepath: str = PATH) -> list:
    """Get the mood texts as a list from moods.txt"""
    with open(filepath) as file:
        moods = file.readlines()
    return moods


def write_moods(moods: list, filepath=PATH) -> None:
    """
    Write the list of the moods for each day
    and write them into the moods.txt
    """
    with open(filepath, "w") as file:
        file.writelines(moods)


if __name__ == "__main__":
    print(get_moods())