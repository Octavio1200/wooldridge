def load():
    """name of dataset: driving
    no of variables: 56
    no of observations: 1200

    +--------------+------------------------------------------------+
    | variable     | label                                          |
    +--------------+------------------------------------------------+
    | year         | 1980 through 2004                              |
    | state        | 48 continental states, alphabetical            |
    | sl55         | speed limit == 55                              |
    | sl65         | speed limit == 65                              |
    | sl70         | speed limit == 70                              |
    | sl75         | speed limit == 75                              |
    | slnone       | no speed limit                                 |
    | seatbelt     | =0 if none, =1 if primary, =2 if secondary     |
    | minage       | minimum drinking age                           |
    | zerotol      | zero tolerance law                             |
    | gdl          | graduated drivers license law                  |
    | bac10        | blood alcohol limit .10                        |
    | bac08        | blood alcohol limit .08                        |
    | perse        | administrative license revocation (per se law) |
    | totfat       | total traffic fatalities                       |
    | nghtfat      | total nighttime fatalities                     |
    | wkndfat      | total weekend fatalities                       |
    | totfatpvm    | total fatalities per 100 million miles         |
    | nghtfatpvm   | nighttime fatalities per 100 million miles     |
    | wkndfatpvm   | weekend fatalities per 100 million miles       |
    | statepop     | state population                               |
    | totfatrte    | total fatalities per 100,000 population        |
    | nghtfatrte   | nighttime fatalities per 100,000 population    |
    | wkndfatrte   | weekend accidents per 100,000 population       |
    | vehicmiles   | vehicle miles traveled, billions               |
    | unem         | unemployment rate, percent                     |
    | perc14_24    | percent population aged 14 through 24          |
    | sl70plus     | sl70 + sl75 + slnone                           |
    | sbprim       | =1 if primary seatbelt law                     |
    | sbsecon      | =1 if secondary seatbelt law                   |
    | d80          | =1 if year == 1980                             |
    | d81          |                                                |
    | d82          |                                                |
    | d83          |                                                |
    | d84          |                                                |
    | d85          |                                                |
    | d86          |                                                |
    | d87          |                                                |
    | d88          |                                                |
    | d89          |                                                |
    | d90          |                                                |
    | d91          |                                                |
    | d92          |                                                |
    | d93          |                                                |
    | d94          |                                                |
    | d95          |                                                |
    | d96          |                                                |
    | d97          |                                                |
    | d98          |                                                |
    | d99          |                                                |
    | d00          |                                                |
    | d01          |                                                |
    | d02          |                                                |
    | d03          |                                                |
    | d04          | =1 if year == 2004                             |
    | vehicmilespc |                                                |
    +--------------+------------------------------------------------+

    Freeman, D.G. (2007), “Drunk Driving Legislation and Traffic
    Fatalities: New Evidence on BAC 08 Laws,” Contemporary Economic Policy
    25, 293--308. Professor Freeman kindly provided the data."""

    import wooldridge
    return wooldridge.load(__file__, "driving.csv.bz2")


def wooldridge():
    import wooldridge
    print(wooldridge.dataset_list)