import pygame
import CONSTANTS

class DisplaySettings():
    """
    Class representing game display window graphics object.
    """
    def __init__(self):
        self.screenWidth = CONSTANTS.SCREEN_WIDTH
        self.screenHeight = CONSTANTS.SCREEN_HEIGHT
        self.bgColor = CONSTANTS.LIGHT_GRAY
    
    def createDisplay(self):
        """ Method to initalize and create display
        Args:
            None

        Returns:
            pygame surface: display object
        """
        pygame.init()
        display = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        display.fill(self.bgColor)
        pygame.display.set_caption("MIE237 Reaction Time Experiment")

        return display