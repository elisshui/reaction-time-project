import pygame
import random
import pandas as pd

import CONSTANTS

import random_numbers

from GamePlay import GamePlay
from DisplaySettings import DisplaySettings
from Squares import Squares

game = GamePlay() # create game object

# Graphics
disp = DisplaySettings()
screen = disp.createDisplay()

square_left = Squares()
square_right = Squares()
game.startingState(screen, square_left, square_right)

# color changing and detection
color_code = random_numbers.get_color_change() # what color to change to
color_clicked = None # color of mouse

# timing
game_state = "start"
color_change_time = 0
average_time = 0 # average time in general
average_time_correct = 0 # average time for correct hits
count = 0 # num of time played
num_correct = 0

# data storage
all_reaction_data = pd.DataFrame(columns=["participant_num", "distraction", "attempt", "reaction_time", "cumul_ave_time", "correct"])
ave_reaction_data = pd.DataFrame(columns=["participant_num", "distraction", "ave_of_correct", "num_correct", "accuracy"])

# experiment set up (terminal input)
distraction_type = str(input("\nEnter distraction type [None][Auditory][Cognitive]: "))
participant_number = str(input("Enter participant number [1][2]...: "))

running = True
while running and count < CONSTANTS.MAX_ATTEMPTS:
    current_time = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "start":
                game_state = "wait_for_color_change" 
                print("\n----GAME HAS STARTED----") # message - indicate game start

                # start timing
                color_change_time = current_time + random.randint(CONSTANTS.MIN_COLOR_CHANGE_TIME, CONSTANTS.MAX_COLOR_CHANGE_TIME)

            if game_state == "wait_for_reaction": 
                game_state = "wait_for_color_change" 

                # calculate reaction time
                reaction_time = (current_time - color_change_time) / 1000
                color_change_time = current_time + random.randint(CONSTANTS.MIN_COLOR_CHANGE_TIME, CONSTANTS.MAX_COLOR_CHANGE_TIME)
                count += 1
                average_time = (average_time * (count - 1) + reaction_time) / count         
                
                correctness = game.checkColorClicked(screen, color_clicked) # check color clicked on (1 = correct, 0 = WRONG)

                if correctness == 1:
                    num_correct += 1
                    average_time_correct = (average_time * (count - 1) + reaction_time) / count  

                data_row = [participant_number, distraction_type, count, reaction_time, average_time, correctness]
                all_reaction_data.loc[len(all_reaction_data)] = data_row

                if count == CONSTANTS.MAX_ATTEMPTS:
                    data_row = [participant_number, distraction_type, average_time_correct, num_correct, (num_correct/CONSTANTS.MAX_ATTEMPTS)]
                    ave_reaction_data.loc[len(ave_reaction_data)] = data_row


    if game_state == "wait_for_color_change":
        game.startingState(screen, square_left, square_right) # reset colors to yellow

        if current_time >= color_change_time:
            game.makeColorful(screen, square_left, square_right) # make squares red and green randomly
            game_state = "wait_for_reaction"   

    pygame.display.flip()

game.saveResults("data_results/single_reaction_data.csv", all_reaction_data) # saving all reaction data
game.saveResults("data_results/averaged_reaction_data.csv", ave_reaction_data) # saving all reaction data

print(f"\nRESULTS EXPORTED\n.\n.\nEXPERIMENT FOR {distraction_type}-{participant_number} COMPLETE")