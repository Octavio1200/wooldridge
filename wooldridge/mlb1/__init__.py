def load():
    """name of dataset: mlb1
    no of variables: 47
    no of observations: 353

    +----------+----------------------------+
    | variable | label                      |
    +----------+----------------------------+
    | salary   | 1993 season salary         |
    | teamsal  | team payroll               |
    | nl       | =1 if national league      |
    | years    | years in major leagues     |
    | games    | career games played        |
    | atbats   | career at bats             |
    | runs     | career runs scored         |
    | hits     | career hits                |
    | doubles  | career doubles             |
    | triples  | career triples             |
    | hruns    | career home runs           |
    | rbis     | career runs batted in      |
    | bavg     | career batting average     |
    | bb       | career walks               |
    | so       | career strike outs         |
    | sbases   | career stolen bases        |
    | fldperc  | career fielding perc       |
    | frstbase | = 1 if first base          |
    | scndbase | =1 if second base          |
    | shrtstop | =1 if shortstop            |
    | thrdbase | =1 if third base           |
    | outfield | =1 if outfield             |
    | catcher  | =1 if catcher              |
    | yrsallst | years as all-star          |
    | hispan   | =1 if hispanic             |
    | black    | =1 if black                |
    | whitepop | white pop. in city         |
    | blackpop | black pop. in city         |
    | hisppop  | hispanic pop. in city      |
    | pcinc    | city per capita income     |
    | gamesyr  | games per year in league   |
    | hrunsyr  | home runs per year         |
    | atbatsyr | at bats per year           |
    | allstar  | perc. of years an all-star |
    | slugavg  | career slugging average    |
    | rbisyr   | rbis per year              |
    | sbasesyr | stolen bases per year      |
    | runsyr   | runs scored per year       |
    | percwhte | percent white in city      |
    | percblck | percent black in city      |
    | perchisp | percent hispanic in city   |
    | blckpb   | black*percblck             |
    | hispph   | hispan*perchisp            |
    | whtepw   | white*percwhte             |
    | blckph   | black*perchisp             |
    | hisppb   | hispan*percblck            |
    | lsalary  | log(salary)                |
    +----------+----------------------------+

    Collected by G. Mark Holmes, a former MSU undergraduate, for a term
    project. The salary data were obtained from the New York Times, April
    11, 1993. The baseball statistics are from The Baseball Encyclopedia,
    9th edition, and the city population figures are from the Statistical
    Abstract of the United States."""

    import wooldridge
    return wooldridge.load(__file__, "mlb1.csv.bz2")


def wooldridge():
    import wooldridge
    print(wooldridge.dataset_list)