'''
pytest-cov

1:- Live coverage :- Tools that measure code coverage watch our code while a test suite is being run and keep track of
which lines are hit and which are not , calculating by dividing the total number of lines run divided by the total
lines of code.

Bracnh Coverage:- Tools also tell if all paths are taken in control statements , a measure called branch coverage.

Note:- Code coverage cannot tell if testsuite is good , it can only tell how much of the application code is getting hit
by test suite .But that in itself is usefull information.
pip install coverage
pip install pytest-cov

Note:- in our test or in our code we want to exclude any of the code from test coverage management then simply has add
ex:- hass()# pragma: no cover   :-Means this said do not count this particular block of the code for test coverage
so that way we will be able to exclude as many line as we want.
Execute commands:-
--> pytest --cov=testfile name or directory name or suite name

--> pytest --cov=single file.py

or
--> coverage run --source=name of dir or name test cases  -m pytest testsuite name

--> coverage report
-----------------------------
pytest --cov=directory name or test cases file name --cov-report =term-missing suite name  :-- to see the how many line
missing
created the report as directpryname/htmlcov/index.html

'''
# @pytest.mark.skipif(condition, reason=)
# @pytest.mark.xfail(reason=)
# # @pytest.mark.xfail(pass which condition is failed , reason=)
