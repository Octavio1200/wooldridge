def load():
    """name of dataset: fertil2
    no of variables: 27
    no of observations: 4361

    +----------+--------------------------------+
    | variable | label                          |
    +----------+--------------------------------+
    | mnthborn | month woman born               |
    | yearborn | year woman born                |
    | age      | age in years                   |
    | electric | =1 if has electricity          |
    | radio    | =1 if has radio                |
    | tv       | =1 if has tv                   |
    | bicycle  | =1 if has bicycle              |
    | educ     | years of education             |
    | ceb      | children ever born             |
    | agefbrth | age at first birth             |
    | children | number of living children      |
    | knowmeth | =1 if know about birth control |
    | usemeth  | =1 if ever use birth control   |
    | monthfm  | month of first marriage        |
    | yearfm   | year of first marriage         |
    | agefm    | age at first marriage          |
    | idlnchld | 'ideal' number of children     |
    | heduc    | husband's years of education   |
    | agesq    | age^2                          |
    | urban    | =1 if live in urban area       |
    | urb_educ | urban*educ                     |
    | spirit   | =1 if religion == spirit       |
    | protest  | =1 if religion == protestant   |
    | catholic | =1 if religion == catholic     |
    | frsthalf | =1 if mnthborn <= 6            |
    | educ0    | =1 if educ == 0                |
    | evermarr | =1 if ever married             |
    +----------+--------------------------------+

    These data were obtained by James Heakins, a former MSU undergraduate,
    for a term project. They come from Botswana’s 1988 Demographic and
    Health Survey."""

    import wooldridge
    return wooldridge.load(__file__, "fertil2.csv.bz2")


def wooldridge():
    import wooldridge
    print(wooldridge.dataset_list)