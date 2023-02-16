"""
Class for squares to be clicked on (graphics)
"""
import pygame
import CONSTANTS

class Squares():
    """
    Class representing square object to be displayed on game screen surface.
    """
    def __init__(self):
        self.color = CONSTANTS.YELLOW

    def createSquare(self, screen, dimensions):
        """ Method to draw square object.
        Args:
            screen: surface on which game is drawn
            dimensions: dimensions of the square to be created (also gives information on its on-screen location)

        Returns:
            None
        """
        pygame.draw.rect(screen, self.color, dimensions)

    def changeColor(self, color):
        """ Method to change the color of the square object.
        Args:
            color: the color to change to.

        Returns:
            None
        """
        self.color = color # change color