import pygame

class Ship:
	"""A class to manage the spaceship."""


	def __init__(self, ai_game):
		"""Initialize the ship and set its starting position."""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship_small_facing_right.png')
		self.rect = self.image.get_rect()

		# Start each new ship at the bottom centre of the screen.
		# self.rect.midbottom = self.screen_rect.midbottom
		self.rect.midleft = self.screen_rect.midleft

		# Store decimal value for the ship's horizontal position.
		# self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		# Movement flags
		# self.moving_right = False
		# self.moving_left = False
		self.moving_up = False
		self.moving_down = False


	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)


	def update(self):
		"""Update the ship's position based on movement flags."""
		# Update the ship's x value, not the rect.
		# if self.moving_right and self.rect.right <= self.screen_rect.right:
		# 	self.x += self.settings.ship_speed
		if self.moving_up and self.rect.top >= 0:
			self.y -= self.settings.ship_speed

		# Note that using an elif block here would be problematic if both
		# the L and R keys were held down at once.
		# if self.moving_left and self.rect.left >= 0:
		# 	self.x -= self.settings.ship_speed
		if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
			self.y += self.settings.ship_speed

		# Update rect object from self.x.
		# self.rect.x = self.x
		self.rect.y = self.y


	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)