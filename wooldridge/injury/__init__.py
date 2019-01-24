def load():
    """name of dataset: injury
    no of variables: 30
    no of observations: 7150

    +----------+--------------------------------+
    | variable | label                          |
    +----------+--------------------------------+
    | durat    | duration of benefits           |
    | afchnge  | =1 if after change in benefits |
    | highearn | =1 if high earner              |
    | male     | =1 if male                     |
    | married  | =1 if married                  |
    | hosp     | =1 if inj. required hosp. stay |
    | indust   | industry                       |
    | injtype  | type of injury                 |
    | age      | age at time of injury          |
    | prewage  | previous weekly wage, 1982 $   |
    | totmed   | total med. costs, 1982 $       |
    | injdes   | 4 digit injury description     |
    | benefit  | real dollar value of benefit   |
    | ky       | =1 for kentucky                |
    | mi       | =1 for michigan                |
    | ldurat   | log(durat)                     |
    | afhigh   | afchnge*highearn               |
    | lprewage | log(wage)                      |
    | lage     | log(age)                       |
    | ltotmed  | log(totmed); = 0 if totmed < 1 |
    | head     | =1 if head injury              |
    | neck     | =1 if neck injury              |
    | upextr   | =1 if upper extremities injury |
    | trunk    | =1 if trunk injury             |
    | lowback  | =1 if lower back injury        |
    | lowextr  | =1 if lower extremities injury |
    | occdis   | =1 if occupational disease     |
    | manuf    | =1 if manufacturing industry   |
    | construc | =1 if construction industry    |
    | highlpre | highearn*lprewage              |
    +----------+--------------------------------+

    B.D. Meyer, W.K. Viscusi, and D.L. Durbin (1995), “Workers’
    Compensation and Injury Duration: Evidence from a Natural Experiment,”
    American Economic Review 85, 322-340. Professor Meyer kindly provided
    the data."""

    import wooldridge
    return wooldridge.load(__file__, "injury.csv.bz2")


def wooldridge():
    import wooldridge
    print(wooldridge.dataset_list)