import pygame

class Rocket:
	"""A class to manage the rocket for exercise 12-3."""


	def __init__(self, ai_game):
		"""Initialize the rocket and set its starting position."""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load the rocket image and get its rect.
		self.image = pygame.image.load('images/rocket_small.png')
		# Make a copy of the image to use for rotation purposes.
		self.clean_image = self.image.copy()
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

		# Rotation flags and angle
		self.rotating_ccw = False
		self.rotating_cw = False
		self.rotation_angle = self.settings.rotation_angle
		self.converted_angle = 0

		# Direction flag
		self.direction = 'up'

	def blitme(self):
		"""Draw the rocket at its current location."""
		self.screen.blit(self.image, self.rect)


	def update(self):
		"""Update the rocket's position and rotation based on flags."""
		# Update the rocket's x and y values, not the rect.
		if self.moving_right and self.rect.right <= self.screen_rect.right:
			self.x += self.settings.rocket_speed
		# Note that using an elif block here would be problematic if both
		# the L and R keys were held down at once.
		if self.moving_left and self.rect.left >= 0:
			self.x -= self.settings.rocket_speed
		if self.moving_up and self.rect.top >= 0:
			self.y -= self.settings.rocket_speed
		if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
			self.y += self.settings.rocket_speed

		if (self.rotating_ccw) or (self.rotating_cw):
			self._rotate()

		# Update rect object from self.x and self.y.
		self.rect.x = self.x
		self.rect.y = self.y


	def _rotate(self):
		"""Rotate the rocket."""
		self._calculate_rotation_angle()
		self.rotated_rocket = pygame.transform.rotate(self.clean_image,
			self.rotation_angle)
		self._rotate_rect()


	def _calculate_rotation_angle(self):
		"""Calculate the rotation angle of the rocket."""
		if self.rotating_ccw:
			self.rotation_angle += self.settings.rotation_speed
			# self.rotation_angle += 90
		if self.rotating_cw:
			self.rotation_angle -= self.settings.rotation_speed
			# self.rotation_angle -= 90

		# Normalize all angles so that they're between 0 and 360
		self.rotation_angle = self.rotation_angle % 360

		# Set the current direction of the rocket.
		self._set_direction()


	def _set_direction(self):
		"""
		Calculates which direction the rocket is currently facing.
		Also normalized the rotation angle to be between 0 and 90 degrees, if 
		it isn't already.
		"""
		if self.rotation_angle == 0:
			self.direction = 'up'
			self.converted_angle = self.rotation_angle
		elif 0 < self.rotation_angle < 90:
			self.direction = 'upleft'
			self.converted_angle = self.rotation_angle
		elif self.rotation_angle == 90:
			self.direction = 'left'
			self.converted_angle = self.rotation_angle
		elif 90 < self.rotation_angle < 180:
			self.direction = 'downleft'
			self.converted_angle = abs(self.rotation_angle - 180)
		elif self.rotation_angle == 180:
			self.direction = 'down'
			self.converted_angle = 0
		elif 180 < self.rotation_angle < 270:
			self.direction = 'downright'
			self.converted_angle = self.rotation_angle - 180
		elif self.rotation_angle == 270:
			self.direction = 'right'
			self.converted_angle = 90
		elif 270 < self.rotation_angle < 360:
			self.direction = 'upright'
			self.converted_angle = abs(self.rotation_angle - 360)

		
	def _rotate_rect(self):
		"""Get the rotated image's rect and assign it self.rect."""
		self.rotated_rect = self.rotated_rocket.get_rect(
			center=self.rect.center)
		self.image = self.rotated_rocket
		self.rect = self.rotated_rect
		self.x = float(self.rotated_rect.x)
		self.y = float(self.rotated_rect.y)


	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)