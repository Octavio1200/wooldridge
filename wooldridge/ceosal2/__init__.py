def load():
    """name of dataset: ceosal2
    no of variables: 15
    no of observations: 177

    +----------+--------------------------------+
    | variable | label                          |
    +----------+--------------------------------+
    | salary   | 1990 compensation, $1000s      |
    | age      | in years                       |
    | college  | =1 if attended college         |
    | grad     | =1 if attended graduate school |
    | comten   | years with company             |
    | ceoten   | years as ceo with company      |
    | sales    | 1990 firm sales, millions      |
    | profits  | 1990 profits, millions         |
    | mktval   | market value, end 1990, mills. |
    | lsalary  | log(salary)                    |
    | lsales   | log(sales)                     |
    | lmktval  | log(mktval)                    |
    | comtensq | comten^2                       |
    | ceotensq | ceoten^2                       |
    | profmarg | profits as % of sales          |
    +----------+--------------------------------+

    See CEOSAL1.RAW"""

    import wooldridge
    return wooldridge.load(__file__, "ceosal2.csv.bz2")


def wooldridge():
    import wooldridge
    print(wooldridge.dataset_list)