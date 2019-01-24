def load():
    """name of dataset: traffic1
    no of variables: 13
    no of observations: 51

    +----------+---------------------------------+
    | variable | label                           |
    +----------+---------------------------------+
    | state    |                                 |
    | admn90   | =1 if admin. revoc., '90        |
    | admn85   | =1 if admin. revoc., '85        |
    | open90   | =1 if open cont. law, '90       |
    | open85   | =1 if open cont. law, '85       |
    | dthrte90 | deaths per 100 mill. miles, '90 |
    | dthrte85 | deaths per 100 mill. miles, '85 |
    | speed90  | =1 if 65 mph, 1990              |
    | speed85  | =0 always                       |
    | cdthrte  | dthrte90 - dthrte85             |
    | cadmn    | admn90 - admn85                 |
    | copen    | open90 - open85                 |
    | cspeed   | speed90 - speed85               |
    +----------+---------------------------------+

    I collected these data from two sources, the 1992 Statistical Abstract
    of the United States (Tables 1009, 1012) and A Digest of State
    Alcohol-Highway Safety Related Legislation, 1985 and 1990, published
    by the U.S. National Highway Traffic Safety Administration."""

    import wooldridge
    return wooldridge.load(__file__, "traffic1.csv.bz2")


def wooldridge():
    import wooldridge
    print(wooldridge.dataset_list)