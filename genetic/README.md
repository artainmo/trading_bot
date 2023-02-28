# An extended look to the genetics program possibility

## Goal
The goal of the genetics program is to find new potential algorithms in places never thought of before

## Explanation
Genetic program starts with one program that can have children on its own. Each program is technically a trading algorithm, the trading algorithm genes are written in the algo confiration file of the program, the program is a copy of the simulation algorithm, that is able to test on its own and puts its result in its own result file.
A program only survives and has children if it made profit.

Each child will consist of the parent with a derivation on one variable. (One derivation means one variable value forward or backward)
It will create a child for each isolated variable or "gene" with one forward or one backward value change.
The children are under the same rules as the parent and can become a parent themselves.

If population becomes too big, virus kills the weakest, leaving only the strongest 10 algorithms alive, with 100 being the max population. Season change is made by external program that goes in all existing directories and kills the weakest ones, if more than 100 directories exist.
Let the seasons change, meaning here you change the market for all existing coins, this will kill some of them if they are not robust enough to survive in another "climate" or in another market. Season change is made by external program that goes into all the existing directories and changes their market.

Create different continents, each continent contains processes that try to survive based on a particular climate, here the climate being an uptrend, downtrend, neutraltrend or all trend.

Let the geneticist run continuously with new data that comes out. Create one program that always spots the current best performing algorithm.

## IMPLEMENTATION
Threads and processes can be used to fasten.

To use the genetic algorithm that will search for the best algorithm, go in the genetic directory and use python2.7 genetic.py. In the result directory you can see the best algo for each trend.
To test each possible algorithm is way too long, solution to this is to test each independent variable for its best values and continue going down keeping the best variable values at top, values for independent variable are linear, meaning once you found a less ideal value, you can stop searching down the line. The algo would test for different trends and with different markets to expose it to as much data as possible.
Other solution could be to invent a completely different algorithm, maybe use deep learning for example.
-> Use machine learning as it does that automatically and simultaneously for all features
-> Or continue creating semi-random algos speed up with threads and processes

## In the end...
The genetic-algorithm-based-trading-bot started off as an idea that hasn't been finalized after speculating on the total time it would necessitate to evolve being way too long.
