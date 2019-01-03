from textwrap import dedent

def check_room( room ):

    if room == "death":
        return True

    elif room == "exit":
        return True
    else:
        return False

def game_over( next_room, plants_win ):

    if plants_win:
        print(dedent(
        """
        Game over.
        The plants have overgrown the building.
        You are stuck in here forever.
        """))

    if next_room == "exit":
        print(dedent(
        """
        Game over, you win!
        You got out before the plants overwhelmed the room!
        """
        ))

    if next_room == "death":
        print(dedent(
        """
        You fall into a pit full of worms.
        As you flail about.
        You slowly suffucate.

        Game over.
        """))
