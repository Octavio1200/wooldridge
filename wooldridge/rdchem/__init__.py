def load():
    """name of dataset: rdchem
    no of variables: 8
    no of observations: 32

    +----------+-----------------------------+
    | variable | label                       |
    +----------+-----------------------------+
    | rd       | R&D spending, millions      |
    | sales    | firm sales, millions        |
    | profits  | profits, millions           |
    | rdintens | rd as percent of sales      |
    | profmarg | profits as percent of sales |
    | salessq  | sales^2                     |
    | lsales   | log(sales)                  |
    | lrd      | log(rd)                     |
    +----------+-----------------------------+

    From Businessweek R&D Scoreboard, October 25, 1991."""

    import wooldridge
    return wooldridge.load(__file__, "rdchem.csv.bz2")


def wooldridge():
    import wooldridge
    print(wooldridge.dataset_list)