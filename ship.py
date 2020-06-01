import pygame

class Ship:
	"""A class to manage the spaceship."""


	def __init__(self, ai_game):
		"""Initialize the ship and set its starting position."""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		#self.settings = ai_game.settings

		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship_small.png')
		self.rect = self.image.get_rect()

		# Start each new ship at the bottom centre of the screen.
		self.rect.midbottom = self.screen_rect.midbottom

		# Movement flags
		self.moving_right = False
		self.moving_left = False


	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)


	def update(self):
		"""Update the ship's position based on movement flags."""
		if (self.moving_right and 
				self.rect.bottomright[0] <= self.screen_rect.bottomright[0]):
			self.rect.x += 1
		if (self.moving_left and
				self.rect.bottomleft[0] >= self.screen_rect.bottomleft[0]):
			self.rect.x -= 1


	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)