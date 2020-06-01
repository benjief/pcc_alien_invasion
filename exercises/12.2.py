import sys

import pygame

from game_character import GameCharacter

class DisplayGameCharacter:
	"""Class that draws a character in the centre of a Pygame window."""


	def __init__(self):
		"""Initialize the game and create game resources."""
		pygame.init()

		self.screen = pygame.display.set_mode((1200, 800))
		pygame.display.set_caption("Exercise 12-2")

		self.game_character = GameCharacter(self)

		self.bg_color = (230, 230, 230)


	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			self._check_events()
			self._update_screen()

	def _check_events(self):
		# Respond to keypresses and mouse events.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()


	def _update_screen(self):
		# Update images on the screen and flip to the new image.
		self.screen.fill(self.bg_color)
		self.game_character.blitme()
		pygame.display.flip()


if __name__ == '__main__':
	# Make game instance and run it.
	ai = DisplayGameCharacter()
	ai.run_game()