def load():
    """name of dataset: approval
    no of variables: 16
    no of observations: 78

    +------------+---------------------------------------------+
    | variable   | label                                       |
    +------------+---------------------------------------------+
    | id         | id                                          |
    | month      | month                                       |
    | year       | year                                        |
    | sp500      | S&P 500 index                               |
    | cpi        | Consumer Price Index                        |
    | cpifood    | CPI for food                                |
    | approve    | Gallup approval rate - percent              |
    | gasprice   | average gas price - cents                   |
    | unemploy   | unemployment rate - percent                 |
    | katrina    | =1 for three months after Hurricane Katrina |
    | rgasprice  | real gas price - 100*(gasprice/cpi)         |
    | lrgasprice | log(rgasprice)                              |
    | sep11      | =1 for 09/2001 and two months following     |
    | iraqinvade | =1 for three months after Iraq invasion     |
    | lsp500     | log(sp500)                                  |
    | lcpifood   | log(cpifood)                                |
    +------------+---------------------------------------------+

    Harbridge, L., J. Krosnick, and J.M. Wooldridge (forthcoming),
    “Presidential Approval and Gas Prices: Sociotropic or Pocketbook
    Influence?” in New Explorations in Political Psychology, ed. J.
    Krosnick. New York: Psychology Press (Taylor and Francis Group).
    Professor Harbridge kindly provided the data, of which I have used a
    subset."""

    import wooldridge
    return wooldridge.load(__file__, "approval.csv.bz2")


def wooldridge():
    import wooldridge
    print(wooldridge.dataset_list)