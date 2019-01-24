def load():
    """name of dataset: gpa2
    no of variables: 12
    no of observations: 4137

    +----------+----------------------------------+
    | variable | label                            |
    +----------+----------------------------------+
    | sat      | combined SAT score               |
    | tothrs   | total hours through fall semest  |
    | colgpa   | GPA after fall semester          |
    | athlete  | =1 if athlete                    |
    | verbmath | verbal/math SAT score            |
    | hsize    | size grad. class, 100s           |
    | hsrank   | rank in grad. class              |
    | hsperc   | high school percentile, from top |
    | female   | =1 if female                     |
    | white    | =1 if white                      |
    | black    | =1 if black                      |
    | hsizesq  | hsize^2                          |
    +----------+----------------------------------+

    For confidentiality reasons, I cannot provide the source of these
    data. I can say that  they come from a midsize research university
    that also supports men’s and women’s athletics at the Division I
    level."""

    import wooldridge
    return wooldridge.load(__file__, "gpa2.csv.bz2")


def wooldridge():
    import wooldridge
    print(wooldridge.dataset_list)