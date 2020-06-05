import pygame

class Rocket:
	"""A class to manage the rocket for exercise 12-3."""


	def __init__(self, ai_game):
		"""Initialize the rocket and set its starting position."""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		# Load the rocket image and get its rect.
		self.image = pygame.image.load('images/rocket_small.png')
		self.rect = self.image.get_rect()

		# Start each new ship in the centre centre of the screen.
		self.rect.center = self.screen_rect.center

		# Store decimal values for the ship's horizontal and vertical positions.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		# Movement flags
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

		# Rocket speed
		self.rocket_speed = 3.5

		self.rotated_rect = None


	def blitme(self):
		"""Draw the rocket at its current location."""
		self.screen.blit(self.image, self.rect)


	def update(self):
		"""Update the rocket's position based on movement flags."""
		# Update the rocket's x and y values, not the rect.
		if self.moving_right and self.rect.right <= self.screen_rect.right:
			self.x += self.rocket_speed
		# Note that using an elif block here would be problematic if both
		# the L and R keys were held down at once.
		if self.moving_left and self.rect.left >= 0:
			self.x -= self.rocket_speed
		if self.moving_up and self.rect.top >= 0:
			self.y -= self.rocket_speed
		if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
			self.y += self.rocket_speed

		# Update rect object from self.x and self.y.
		self.rect.x = self.x
		self.rect.y = self.y


	def rotate_ccw(self):
		"""Rotate the rocket counter-clockwise."""
		self.rotated_rocket = pygame.transform.rotate(self.image, 90)
		self._rotate_rect()


	def rotate_cw(self):
		"""Rotate the rocket clockwise."""
		self.rotated_rocket = pygame.transform.rotate(self.image, -90)
		self._rotate_rect()


	def _rotate_rect(self):
		self.rotated_rect = self.rotated_rocket.get_rect(center=self.rect.center)
		self.image = self.rotated_rocket
		self.rect = self.rotated_rect
		self.x = self.rotated_rect.x
		self.y = self.rotated_rect.y


	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)