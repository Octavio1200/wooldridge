def load():
    """name of dataset: fringe
    no of variables: 39
    no of observations: 616

    +----------+-------------------------------+
    | variable | label                         |
    +----------+-------------------------------+
    | annearn  | annual earnings, $            |
    | hrearn   | hourly earnings, $            |
    | exper    | years work experience         |
    | age      | age in years                  |
    | depends  | number of dependents          |
    | married  | =1 if married                 |
    | tenure   | years with current employer   |
    | educ     | years schooling               |
    | nrtheast | =1 if live in northeast       |
    | nrthcen  | =1 if live in north central   |
    | south    | =1 if live in south           |
    | male     | =1 if male                    |
    | white    | =1 if white                   |
    | union    | =1 if union member            |
    | office   |                               |
    | annhrs   | annual hours worked           |
    | ind1     | industry dummy                |
    | ind2     |                               |
    | ind3     |                               |
    | ind4     |                               |
    | ind5     |                               |
    | ind6     |                               |
    | ind7     |                               |
    | ind8     |                               |
    | ind9     |                               |
    | vacdays  | $ value of vac. days          |
    | sicklve  | $ value of sick leave         |
    | insur    | $ value of employee insur     |
    | pension  | $ value of employee pension   |
    | annbens  | vacdays+sicklve+insur+pension |
    | hrbens   | hourly benefits, $            |
    | annhrssq | annhrs^2                      |
    | beratio  | annbens/annearn               |
    | lannhrs  | log(annhrs)                   |
    | tenuresq | tenure^2                      |
    | expersq  | exper^2                       |
    | lannearn | log(annearn)                  |
    | peratio  | pension/annearn               |
    | vserat   | (vacdays+sicklve)/annearn     |
    +----------+-------------------------------+

    F. Vella (1993), “A Simple Estimator for Simultaneous Models with
    Censored Endogenous Regressors,” International Economic Review 34,
    441-457. Professor Vella kindly provided the data."""

    import wooldridge
    return wooldridge.load(__file__, "fringe.csv.bz2")


def wooldridge():
    import wooldridge
    print(wooldridge.dataset_list)