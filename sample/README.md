# Problem `meta` format

Extract files from the [Sample](problem_meta.zip). The configuration is described in [`meta.json`](meta.json).

+   `"basic"`
    +   `"score_type"`
        +   `0`: sum of the scores of all test cases
        +   `1`: minimum of the scores of all test cases
    +   `"title"`: the displayed name of the problem
    +   `file`: `.pdf` file for the problem description
        +   Must be a `.pdf`
+   `"testdata"`: description of the test cases. Should be a list.
    +   `"output_limit"`: the unit is kilobytes.
    +   `"memory_limit"`: the unit is kilobytes.
    +   `"time_limit"`: the unit is minisecond.
    +   `"score"`: score weighting. Not supported in ACM-ICPC format.
    +   `"input"`: filename of the input.
    +   `"output"`: filename of the output.
+   `"verdict"`: description of the validator. If you don't specify it, then the default is a token-based `diff`.
    +   `"file"`: the source code of the validator
    +   `"execute_type_id"`: execution enviroment of the validator. See the list below `"executes"`
+   `"executes"`: a list of execution environment settings
    +   `1`: C++14
    +   `2`: C++11
    +   `3`: C
    +   `4`: Java
    +   `5`: Python 3
    +   `6`: Python 2

# User list in `.csv` format

An [sample](user_list.csv). The columns are defined as follows.
+   Column 1: account
+   Column 2: displayed team name
+   Column 3: password
+   Column 4: access level
    +   0: Administrator
    +   1: Testing team
    +   2: Unofficial participant
        +   Ranking with unofficial teams and official teams
    +   3: Official participant
        +   Ranking with official teams