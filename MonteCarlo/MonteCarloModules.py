## Monte Carlo Module File Final Project DS 5100 
## Davi Meran

import pandas as pd
import numpy as np
import random
import matplotlib.pylab as plt

class Die: 
    '''A die has N sides, or “faces”, and W weights, and can be rolled to select a face. '''

    def __init__(self, faces):
        '''This is a die setting method. Input the number of faces and the program will create a dataframe with those faces.
        The program assumes all starting weights to be = 1 '''

        self.faces = faces
        self.weights = [1 for x in self.faces]
        self.df = pd.DataFrame({"faces": self.faces, "weights": self.weights})

    def change_weight(self, face, weight):
        '''This method is used to change the weight of a specific corresponding face. Do this by inputting the desired face and new weight.
        Face must be valid element of faces and weight must be convertable into a float and >= 0 '''

        if (face in self.faces):
            weight = float(weight)
            if (type(weight) == float and weight >= 0):
                a = self.df[self.df["faces"] == face].index.tolist()
                row_index = a[0]
                self.df.iloc[row_index, 1] = weight
            else:
                print("weight can't be converted into a float or not >= 0")
        else:
            print("the face you entered is not valid. Please try again")

    def rolls(self, n=1):
        '''This method takes in n and returns n outcomes given n die rolls with previously given faces and weights'''
        
        n = int(n)
        if (n>0):
            faces_array = np.array(self.df.faces)
            weights_array = np.array(self.df.weights)
        # generate outcomes
            return random.choices(faces_array, weights = weights_array, k = n)
        else:
            print("n, number of rolls, must be an integer > 0. Please try again")

    def print_df(self):
        '''prints the current data frame for the user to see'''
        return self.df
        

class Game:
    '''A game consists of rolling of one or more dice of the same kind one or more times. '''

    def __init__(self, list_die):
        '''initializer takes in a list of similar die objects. Must input a list of die.
        Will not work if input a non list die'''
        self.list_die = list_die
        # # check if all die faces are the same
        # all_die_faces_same = all(element == die.faces[0] for element in die.faces)
        # if (all_die_faces_same):
        #     self.die = die
        # else:
        #     print("error: die faces are not all the same")

    def return_faces(self):
        '''returns faces'''
        return self.list_die[0].print_df().faces
    
    def play(self, num_rolls):
        '''play takes in n die rolls and then rolls them
        Takes a parameter to specify how many times the dice should be rolled.
        Saves the result of the play to a private dataframe of shape N rolls by M dice.
        The private dataframe should have the roll number is a named index.'''

        self.roll_outcomes_list = []

        for i in range(len(self.list_die)):
            die_instance = self.list_die[i]
            die_df = die_instance.print_df()

            roll_outcomes = die_instance.rolls(num_rolls)
            self.roll_outcomes_list.append(roll_outcomes)

        self.df_roll_outcomes = pd.DataFrame(self.roll_outcomes_list)
        # return self.df_roll_outcomes

        ### the outcome data frame will have col names/index as roll numbers and row names/index as instance numbers


    def show(self, narrow_or_wide = "wide"):
        '''Takes a parameter to return the dataframe in narrow or wide form, default = wide.
        
        The narrow form of the dataframe will have a two-column index with the roll number and the die number, 
        and a column for the face rolled.

        The wide form of the dataframe will a single column index with the roll number, and each die number as a column.
        '''

        if (narrow_or_wide == "wide"):
            ## make data wide (data already in wide form from .play())
            self.df_to_show = self.df_roll_outcomes
            self.key_to_show = "Columns = roll number; Rows = die number"

        if (narrow_or_wide == "narrow"):
            ##make data narrow
            self.df_to_show = self.df_roll_outcomes.T
            self.key_to_show = "Columns = die number; Rows = roll number"
        
        # print(self.key_to_show)
        return self.df_to_show
        

class analyzer:
    '''An analyzer takes the results of a single game and computes various descriptive statistical properties about it'''
    
    def __init__(self, game_object):
        '''Takes a game object as its input parameter. '''
        self.game_object = game_object
        self.outcome_df = self.game_object.show("wide")
        self.narrow_outcome_df = self.game_object.show("narrow")

        self.faces = game_object.return_faces()
        self.type_of_game = type(self.faces)

        self.num_faces = len(game_object.return_faces())

    
    def jackpot(self):
        '''compute and return how many times the game resulted in all faces being identical
        stores result in dataframe'''
        
        answer = 0
        for i in range(len(self.game_object.show("narrow"))):
            if (self.outcome_df[i] == self.outcome_df[i][0]).all():
                answer += 1
        return answer

    def combo(self):
        '''compute the distinct combinations of faces rolled, along with their counts'''
        df = self.outcome_df

        combinations_list = []
        for i in range(len(df.T)):
            TEMP = [x for x in df[i]]
            combinations_list.append(tuple(TEMP))

        combinations_df = pd.DataFrame({"Combination_of_Faces": combinations_list})
        
        Combo_DF = combinations_df.apply(lambda x: pd.Series(sorted(x)), 1)\
            .value_counts().to_frame('count')

        return Combo_DF     

    def face_counts_per_roll(self):
        ''' compute how many times a given face is rolled in each event'''
        df = self.outcome_df

        def get_instances(data, instance):
            df_list = data.values.tolist()
            return sum([index.count(instance) for index in df_list])
        

        instance_list = [get_instances(df, x) for x in self.faces]
        
        newdf = pd.DataFrame({
            "face": self.faces,
            "count": instance_list
        })

        return newdf
 