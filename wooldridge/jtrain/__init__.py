def load():
    """name of dataset: jtrain
    no of variables: 30
    no of observations: 471

    +----------+---------------------------------+
    | variable | label                           |
    +----------+---------------------------------+
    | year     | 1987, 1988, or 1989             |
    | fcode    | firm code number                |
    | employ   | # employees at plant            |
    | sales    | annual sales, $                 |
    | avgsal   | average employee salary         |
    | scrap    | scrap rate (per 100 items)      |
    | rework   | rework rate (per 100 items)     |
    | tothrs   | total hours training            |
    | union    | =1 if unionized                 |
    | grant    | = 1 if received grant           |
    | d89      | = 1 if year = 1989              |
    | d88      | = 1 if year = 1988              |
    | totrain  | total employees trained         |
    | hrsemp   | tothrs/totrain                  |
    | lscrap   | log(scrap)                      |
    | lemploy  | log(employ)                     |
    | lsales   | log(sales)                      |
    | lrework  | log(rework)                     |
    | lhrsemp  | log(1 + hrsemp)                 |
    | lscrap_1 | lagged lscrap; missing 1987     |
    | grant_1  | lagged grant; assumed 0 in 1987 |
    | clscrap  | lscrap - lscrap_1; year > 1987  |
    | cgrant   | grant - grant_1                 |
    | clemploy | lemploy - lemploy[_n-1]         |
    | clsales  | lavgsal - lavgsal[_n-1]         |
    | lavgsal  | log(avgsal)                     |
    | clavgsal | lavgsal - lavgsal[_n-1]         |
    | cgrant_1 | cgrant[_n-1]                    |
    | chrsemp  | hrsemp - hrsemp[_n-1]           |
    | clhrsemp | lhrsemp - lhrsemp[_n-1]         |
    +----------+---------------------------------+

    H. Holzer, R. Block, M. Cheatham, and J. Knott (1993), “Are Training
    Subsidies Effective? The Michigan Experience,” Industrial and Labor
    Relations Review 46, 625-636. The authors kindly provided the data."""

    import wooldridge
    return wooldridge.load(__file__, "jtrain.csv.bz2")


def wooldridge():
    import wooldridge
    print(wooldridge.dataset_list)