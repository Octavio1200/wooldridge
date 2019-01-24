def load():
    """name of dataset: earns
    no of variables: 14
    no of observations: 41

    +----------+---------------------------+
    | variable | label                     |
    +----------+---------------------------+
    | year     | 1947 to 1987              |
    | wkearns  | avg. real weekly earnings |
    | wkhours  | avg. weekly hours         |
    | outphr   | output per labor hour     |
    | hrwage   | wkearns/wkhours           |
    | lhrwage  | log(hrwage)               |
    | loutphr  | log(outphr)               |
    | t        | time trend:  t=1 to 47    |
    | ghrwage  | lhrwage - lhrwage[_n-1]   |
    | goutphr  | loutphr - loutphr[_n-1]   |
    | ghrwge_1 | ghrwage[_n-1]             |
    | goutph_1 | goutphr[_n-1]             |
    | goutph_2 | goutphr[_n-2]             |
    | lwkhours | log(wkhours)              |
    +----------+---------------------------+

    Economic Report of the President, 1989, Table B-47. The data are for
    the non-farm business sector."""

    import wooldridge
    return wooldridge.load(__file__, "earns.csv.bz2")


def wooldridge():
    import wooldridge
    print(wooldridge.dataset_list)