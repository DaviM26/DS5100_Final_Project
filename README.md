# MonteCarloModules
This is Davi's DS5100 Final Project Repo

This Repo contains a Monte Carlo Simulator that I built

## Manifest
This Repo will contain important files, including the MonteCarloModule, the UnitTest file, the UnitTest output file, an __init__ file, a setup.py file, and an example ipynb showing usage of this package through 3 scenerios. 


## Installing:

Clone this repo and, from within the cloned directory, run python setup.py install — or python setup.py install --user if you are on a shared system where you can't write to the python directory. This will install the script MonteCarloModules into your current Python environment. The script MonteCarloModules will be callable from anywhere on your system

## Import
```
import MonteCarloModules
```

## Create Die:
The below code creates Die with faces called face1 and face2.
```
new_die = Die(["face1", "face2"])
```

## Play Game
The below code shows how to play a game using two of the above Die. The game consists of 10 rolls. 
```
new_game = Game([new_die, new_die])
new_game.play(10)
```

## Analyze Game
The below code shows how to analyze the game played above. First we will check jackpots, then combos, then face counts per roll.
```
analyze_game = analyze(new_game)
jackpots = analyze_game.jackpot()
combos = analyze_game.combos()
face_count_per_roll = analyze_game.face_count_per_roll()
```



# Description of what the modules do:

## Die Class:
A die has N sides, or “faces”, and W weights, and can be rolled to select a face. W defaults to 
1.0 for each face but can be changed after the object is created.
Note that the weights are just numbers, not a normalized probability distribution.
The die has one behavior, which is to be rolled one or more times.
Note that what we are calling a “die” here can be any discrete random variable associated with a stochastic process, such as using a deck of cards or flipping a coin or speaking a language. Our probability model for such variable is, however, very simple – since our weights apply to only to single events, we are assuming that the events are independent. This makes sense for coin tosses but not for language use.

### Initializer:
Takes an array of faces as an argument. The array's data type (dtype) may be strings or numbers.
Internally iInitializes the weights to 1.0 for each face.
Saves both faces and weights into a private dataframe that is to be shared by the other methods.
A method to change the weight of a single side.
Takes two arguments: the face value to be changed and the new weight.
Checks to see if the face passed is valid; is it in the array of weights?
Checks to see if the weight is valid; is it a float? Can it be converted to one?
A method to roll the die one or more times.
Takes a parameter of how many times the die is to be rolled; defaults to 1. 
This is essentially a random sample from the vector of faces according to the weights.
Returns a list of outcomes.
Does not store internally these results.
A method to show the user the die’s current set of faces and weights (since the latter can be changed).
Returns the dataframe created in the initializer.




## The Game class:

### General Definition:
A game consists of rolling of one or more dice of the same kind one or more times. 

Each game is initialized with one or more of similarly defined dice (Die objects).
By “same kind” and “similarly defined” we mean that each die in a given game has the same number of sides and associated faces, but each die object may have its own weights.
The class has a behavior to play a game, i.e. to rolls all of the dice a given number of times.
The class keeps the results of its most recent play. 


### An initializer:
Takes a single parameter, a list of already instantiated similar Die objects.

### A play method:
Takes a parameter to specify how many times the dice should be rolled.
Saves the result of the play to a private dataframe of shape N rolls by M dice.
The private dataframe should have the roll number is a named index.
A method to show the user the results of the most recent play.

### Show Method
This method just passes the private dataframe to the user.
Takes a parameter to return the dataframe in narrow or wide form.
This parameter defaults to wide form.
This parameter should raise an exception of the user passes an invalid option.
The narrow form of the dataframe will have a two-column index with the roll number and the die number, and a column for the face rolled.
The wide form of the dataframe will a single column index with the roll number, and each die number as a column.

## The Analyzer class
An analyzer takes the results of a single game and computes various descriptive statistical properties about it. These properties results are available as attributes of an Analyzer object. Attributes (and associated methods) include:

A face counts per roll, i.e. the number of times a given face appeared in each roll. For example, if a roll of five dice has all sixes, then the counts for this roll would be 6 for the face value '6' and 0 for the other faces.
A jackpot count, i.e. how many times a roll resulted in all faces being the same, e.g. all one for a six-sided die.
A combo count, i.e. how many combination types of faces were rolled and their counts.


### General Definition:
An analyzer takes the results of a single game and computes various descriptive statistical properties about it. These properties results are available as attributes of an Analyzer object. Attributes (and associated methods) include:

### An initializer:
Takes a game object as its input parameter. 
At initialization time, it also infers the data type of the die faces used.

### Jackpot method:
A jackpot method to compute how many times the game resulted in all faces being identical.
Returns an integer for the number times to the user.
Stores the results as a dataframe of jackpot results in a public attribute.
The dataframe should have the roll number as a named index.

### Combo method:
A combo method to compute the distinct combinations of faces rolled, along with their counts.
Combinations should be sorted and saved as a multi-columned index.
Stores the results as a dataframe in a public attribute.

### Face counts per roll method:
A face counts per roll method to compute how many times a given face is rolled in each event.
Stores the results as a dataframe in a public attribute.
The dataframe has an index of the roll number and face values as columns (i.e. it is in wide format).




