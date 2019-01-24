def load():
    """name of dataset: bwght2
    no of variables: 23
    no of observations: 1832

    +----------+---------------------------------+
    | variable | label                           |
    +----------+---------------------------------+
    | mage     | mother's age, years             |
    | meduc    | mother's educ, years            |
    | monpre   | month prenatal care began       |
    | npvis    | total number of prenatal visits |
    | fage     | father's age, years             |
    | feduc    | father's educ, years            |
    | bwght    | birth weight, grams             |
    | omaps    | one minute apgar score          |
    | fmaps    | five minute apgar score         |
    | cigs     | avg cigarettes per day          |
    | drink    | avg drinks per week             |
    | lbw      | =1 if bwght <= 2000             |
    | vlbw     | =1 if bwght <= 1500             |
    | male     | =1 if baby male                 |
    | mwhte    | =1 if mother white              |
    | mblck    | =1 if mother black              |
    | moth     | =1 if mother is other           |
    | fwhte    | =1 if father white              |
    | fblck    | =1 if father black              |
    | foth     | =1 if father is other           |
    | lbwght   | log(bwght)                      |
    | magesq   | mage^2                          |
    | npvissq  | npvis^2                         |
    +----------+---------------------------------+

-"""

    import wooldridge
    return wooldridge.load(__file__, "bwght2.csv.bz2")


def wooldridge():
    import wooldridge
    print(wooldridge.dataset_list)