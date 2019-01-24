def load():
    """name of dataset: openness
    no of variables: 12
    no of observations: 114

    +----------+------------------------------+
    | variable | label                        |
    +----------+------------------------------+
    | open     | imports as % GDP ('73-)      |
    | inf      | avg. annual inflation ('73-) |
    | pcinc    | 1980 per capita inc. (U.S.$) |
    | land     | land area (square miles)     |
    | oil      | =1 if major oil producer     |
    | good     | =1 if good data              |
    | lpcinc   | log(pcinc)                   |
    | lland    | log(land)                    |
    | lopen    | log(open)                    |
    | linf     | log(inf)                     |
    | opendec  | open/100                     |
    | linfdec  | log(inf/100)                 |
    +----------+------------------------------+

    D. Romer (1993), “Openness and Inflation: Theory and Evidence,”
    Quarterly Journal of Economics 108, 869-903. The data are included in
    the article."""

    import wooldridge
    return wooldridge.load(__file__, "openness.csv.bz2")


def wooldridge():
    import wooldridge
    print(wooldridge.dataset_list)