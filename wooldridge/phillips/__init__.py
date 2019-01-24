def load():
    """name of dataset: phillips
    no of variables: 7
    no of observations: 56

    +----------+-------------------------------+
    | variable | label                         |
    +----------+-------------------------------+
    | year     | 1948 through 2003             |
    | unem     | civilian unemployment rate, % |
    | inf      | percentage change in CPI      |
    | inf_1    | inf[_n-1]                     |
    | unem_1   | unem[_n-1]                    |
    | cinf     | inf - inf_1                   |
    | cunem    | unem - unem_1                 |
    +----------+-------------------------------+

    Economic Report of the President, 2004, Tables B-42 and B-64."""

    import wooldridge
    return wooldridge.load(__file__, "phillips.csv.bz2")


def wooldridge():
    import wooldridge
    print(wooldridge.dataset_list)