def load():
    """name of dataset: wageprc
    no of variables: 20
    no of observations: 286

    +----------+----------------------------+
    | variable | label                      |
    +----------+----------------------------+
    | price    | consumer price index       |
    | wage     | nominal hourly wage        |
    | t        | time trend = 1, 2 , 3, ... |
    | lprice   | log(price)                 |
    | lwage    | log(wage)                  |
    | gprice   | lprice - lprice[_n-1]      |
    | gwage    | lwage - lwage[_n-1]        |
    | gwage_1  | gwage[_n-1]                |
    | gwage_2  | gwage[_n-2]                |
    | gwage_3  |                            |
    | gwage_4  |                            |
    | gwage_5  |                            |
    | gwage_6  |                            |
    | gwage_7  |                            |
    | gwage_8  |                            |
    | gwage_9  |                            |
    | gwage_10 |                            |
    | gwage_11 |                            |
    | gwage_12 |                            |
    | gprice_1 | gprice[_n-1]               |
    +----------+----------------------------+

    Economic Report of the President, various years."""

    import wooldridge
    return wooldridge.load(__file__, "wageprc.csv.bz2")


def wooldridge():
    import wooldridge
    print(wooldridge.dataset_list)