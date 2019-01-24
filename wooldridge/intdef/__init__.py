def load():
    """name of dataset: intdef
    no of variables: 13
    no of observations: 56

    +----------+----------------------------------+
    | variable | label                            |
    +----------+----------------------------------+
    | year     | 1948 to 2003                     |
    | i3       | 3 month T-bill rate              |
    | inf      | CPI inflation rate               |
    | rec      | federal receipts, % GDP          |
    | out      | federal outlays, % GDP           |
    | def      | out - rec                        |
    | i3_1     | i3[_n-1]                         |
    | inf_1    | inf[_n-1]                        |
    | def_1    | def[_n-1]                        |
    | ci3      | i3 - i3_1                        |
    | cinf     | inf - inf_1                      |
    | cdef     | def - def_1                      |
    | y77      | =1 if year >= 1977; change in FY |
    +----------+----------------------------------+

    Economic Report of the President, 2004, Tables B-64, B-73, and B-79."""

    import wooldridge
    return wooldridge.load(__file__, "intdef.csv.bz2")


def wooldridge():
    import wooldridge
    print(wooldridge.dataset_list)