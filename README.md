# WeightedChoices

## Explanation

**Weighted Choices** Is an alternative to the bracket system of comparison and prediction. The reason for this project is to help cure the flaws in the bracket system, these being if a set of teams is arranged in one way, a certain outcome will arise, but certain teams could have progressed further if they were put up against others.
**For example:**![[bracket_examples-01.png]]
![[bracket_examples-02.png]]
While these brackets contain the same four teams, and finish with the same team, but the second round selection differs because of the changes in the 1st Round lineup. This is more profound with larger brackets, leading to inaccuracies in collected data. 

### Choices
**This is different in Weighted Choices** because everything is compared against everything.
**An Example From WCTbCB's Breakfast Edition Being**:

```Python
Pancakes or Bacon
Pancakes or Eggs
Pancakes or Grits
Pancakes or Waffles
Pancakes or Bagels
Pancakes or Sausage
Bacon or Eggs
Bacon or Grits
Bacon or Waffles
Bacon or Bagles
Bacon or Sausage
Eggs or Grits
Eggs or Waffles
Eggs or Bagles
Eggs or Sausage
Grits or Waffles
Grits or Bagles
Grits or Sausage
Waffles or Bagles
Waffles or Sausage
Bagles or Sausage
```

We can see how WeightedChoices compares each option without, comparing two of the same nor two reversed, but same options. Example: *A vs B* and *B vs A*.

### Weights
Every time a choice is answered, a temporary sqlite3 database is updated, with the winning option being upped by a point (0.1), and the latter being demoted a point (-0.1). Once everything is answered you are provided with a *Results* section, reading from the database and organizing the data in a easy-to-read way that looks like this:
```Python
|=========================================|
|=Your Results:===========================|
|=Rank-Item-Weight========================|
| 1 Pancakes 0.6                          |
|=========================================|
| 2 Bacon 0.4                             |
|=========================================|
| 3 Eggs 0.2                              |
|=========================================|
| 4 Grits -0.0                            |
|=========================================|
| 5 Waffles -0.2                          |
|=========================================|
| 6 Bagles -0.4                           |
|=========================================|
| 7 Sausage -0.6                          |
|=========================================|
```
The reason of using weights over a bracket is because the data is repeatable, the choices stay the same, therefore providing reliable data.
## Releases

### Python (Recommended)
I recommend this most because of its reliability and ease of use, you can clone this repo, or just download WCTbCB.py from the main branch. and run WCTbCB.py with python 3.9 or higher (You could go lower, i think, but I have only tested it on a minimum of 3.9). 
### MacOS
*Note: Tested on MacBook Air M1 2020, MacOS 15.5*
In the latest release is a install DMG for MacOS. Ensure that the app is in your application folder before running, the main shell file checks for the compiled executable in the applications folder. **Just drag the app to Applications!**# WeightedChoices