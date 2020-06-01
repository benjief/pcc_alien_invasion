import pygame

class GameCharacter:
	"""Class to manage a game character."""


	def __init__(self, ai_game):
		# Initialize the character and set its position.
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		# Load the character and get its rect.
		self.image = pygame.image.load('kikwi_small.png')
		self.rect = self.image.get_rect()

		# Put the character in the centre of the screen.
		self.rect.center = self.screen_rect.center


	def blitme(self):
		# Draw the character in its current location.
		self.screen.blit(self.image, self.rect)