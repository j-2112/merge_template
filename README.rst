Merge Template
==============

This repo exists to make doing complex index matches in excel simple and
straightforward using a pandas ``dataframe.merge``

I have set this up so that one xl worksheet will be loaded as one dataframe,
and the second worksheet will be the other dataframe.



Conventions
-----------

I am using the following:

- df1, df2
- 1, 2

These are for the dataframe names and the page names (not to be confused with
the .iloc which would take an integer)

I will be running a join on df3, so that auto text and completion show up
automatically for us. This is not the case if we simply use a .merge on df1.

Our example would be `df3 = pd.merge(left, right, etc...)`


End
^^^

Our final script kicks out a dataframe 3 and then appends it to the end of the
workbook, making sure index=False

There is a lot of modification we can do with this script, but this is an
example to get us up and running

:math:`(a * b)^2`