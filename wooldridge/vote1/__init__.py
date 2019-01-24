def load():
    """name of dataset: vote1
    no of variables: 10
    no of observations: 173

    +----------+---------------------------------+
    | variable | label                           |
    +----------+---------------------------------+
    | state    | state postal code               |
    | district | congressional district          |
    | democA   | =1 if A is democrat             |
    | voteA    | percent vote for A              |
    | expendA  | camp. expends. by A, $1000s     |
    | expendB  | camp. expends. by B, $1000s     |
    | prtystrA | % vote for president            |
    | lexpendA | log(expendA)                    |
    | lexpendB | log(expendB)                    |
    | shareA   | 100*(expendA/(expendA+expendB)) |
    +----------+---------------------------------+

    From M. Barone and G. Ujifusa, The Almanac of American Politics, 1992.
    Washington, DC: National Journal."""

    import wooldridge
    return wooldridge.load(__file__, "vote1.csv.bz2")


def wooldridge():
    import wooldridge
    print(wooldridge.dataset_list)