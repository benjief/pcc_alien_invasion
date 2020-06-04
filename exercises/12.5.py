import sys

import pygame

from message import Message

class EventPrinter:
	"""Overall class to manage a game rocket's assets and behavior."""

	
	def __init__(self):
		"""Initialize the game and create game resources."""
		pygame.init()

		self.screen = pygame.display.set_mode((1200, 800))
		pygame.display.set_caption("Exercise 12-5")

		# Attributes specific to exercise 12-5.
		self.text = Message(self, '')

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			self._check_events()
			self._update_screen()


	def _check_events(self):
		"""Respond to keypresses and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if (event.key == pygame.K_q) or (event.key == pygame.K_ESCAPE):
					sys.exit()
				else:
					self.text = Message(self, event.key)


	def _update_screen(self):
		# Update images on the screen and flip to the new screen.
		self.screen.fill((230, 230, 230))
		self.text.display_message()
		pygame.display.flip()


if __name__ == '__main__':
	# Make a game instance and run the game.
	ai = EventPrinter()
	ai.run_game()