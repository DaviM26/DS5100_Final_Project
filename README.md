# DS5100_Final_Project
This is my DS5100 Final Project Repo
This repo contains a Monte Carlo Simulator


Description of what the modules do:

## The Game class:

### General Definition
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

### Show
A method to show the user the results of the most recent play.

## The Analyzer class

### General Definition:
An analyzer takes the results of a single game and computes various descriptive statistical properties about it. These properties results are available as attributes of an Analyzer object. Attributes (and associated methods) include:

### An initializer:
Takes a game object as its input parameter. 
At initialization time, it also infers the data type of the die faces used.

### A jackpot method:
to compute how many times the game resulted in all faces being identical.

### A combo method:
to compute the distinct combinations of faces rolled, along with their counts.

### A face counts per roll method:
to compute how many times a given face is rolled in each event.






