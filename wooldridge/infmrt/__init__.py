def load():
    """name of dataset: infmrt
    no of variables: 12
    no of observations: 102

    +----------+--------------------------------+
    | variable | label                          |
    +----------+--------------------------------+
    | year     | 1987 or 1990                   |
    | infmort  | deaths per 1,000 live births   |
    | afdcprt  | afdc partic., 1000s            |
    | popul    | population, 1000s              |
    | pcinc    | per capita income              |
    | physic   | drs. per 100,000 civilian pop. |
    | afdcper  | percent on AFDC                |
    | d90      | =1 if year == 1990             |
    | lpcinc   | log(pcinc)                     |
    | lphysic  | log(physic)                    |
    | DC       | =1 for Washington DC           |
    | lpopul   | log(popul)                     |
    +----------+--------------------------------+

    Statistical Abstract of the United States, 1990 and 1994. (For
    example, the infant mortality rates come from Table 113 in 1990 and
    Table 123 in 1994.)"""

    import wooldridge
    return wooldridge.load(__file__, "infmrt.csv.bz2")


def wooldridge():
    import wooldridge
    print(wooldridge.dataset_list)