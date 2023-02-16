import os
import pygame
import pandas as pd
import CONSTANTS
import random_numbers

class GamePlay():
    """
    Class representing game play object per game instance created.
    """
    def startingState(self, screen, square_left, square_right):
        """ Method to set starting state of each participant trial
        Args:
            screen: surface on which game is drawn
            square_left: left square object on screen
            square_right: right square object on screen

        Returns:
            None
        """
        square_left.createSquare(screen, CONSTANTS.DIM_LEFT)
        square_right.createSquare(screen, CONSTANTS.DIM_RIGHT)
        square_left.changeColor(CONSTANTS.YELLOW) # in case not yellow - fail safe and reset game
        square_right.changeColor(CONSTANTS.YELLOW)

    def checkColorClicked(self, screen, color_clicked):
        """ Method to check the color clicked on
        Args:
            screen: surface on which game is drawn
            color_clicked: current color clicked stored

        Returns:
            int: whether or not the color green is clicked (1 = yes, 0 = no)
        """
        rgb = screen.get_at(pygame.mouse.get_pos()) # get rgb color of a pixel at the cursor position
        if not rgb == color_clicked:     # if rgb is not equal to color_clicked:          
            color_clicked = rgb # rgb and color_clicked now have the same value which means we will not enter this if                                                               
        
        return 1 if rgb == CONSTANTS.GREEN else 0

    def makeColorful(self, screen, square_left, square_right):
        """ Method to change to color of the squares from yellow to red or green
        Args:
            screen: surface on which game is drawn
            square_left: left square object on screen
            square_right: right square object on screen

        Returns:
            None
        """
        color_code = random_numbers.get_color_change() # what color to change to

        # change color
        square_left.changeColor(color_code[0])
        square_left.createSquare(screen, CONSTANTS.DIM_LEFT)

        square_right.changeColor(color_code[1])
        square_right.createSquare(screen, CONSTANTS.DIM_RIGHT)
    
    def saveResults(self, file_path, data_to_save):
        """ Method to save the data collected for a given participant
        Args:
            file_path: location in system to write to/read from
            data_to_save: dataframe containing current participant data to save

        Returns:
            None
        """
        if os.path.exists(file_path):
            curr_all_rd = pd.DataFrame(pd.read_csv(file_path))
            curr_all_rd_clean = curr_all_rd.drop(curr_all_rd.columns[0], axis=1)

            updated_all_rd = pd.concat([curr_all_rd_clean, data_to_save], ignore_index=True)
            updated_all_rd.to_csv(file_path)

        else:          
            data_to_save.to_csv(file_path)