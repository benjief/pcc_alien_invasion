import pygame
from pygame.sprite import Sprite
from math import sin, cos, radians

class RocketBullet(Sprite):
	"""A class to manage bullets fired from a rotating rocket."""

	def __init__(self, ai_game):
		"""Create a bullet object at the rocket's current position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.image = pygame.image.load('images/laser.png')
		# self.color = self.settings.bullet_color
		self.rocket = ai_game.rocket

		self.direction = self.rocket.direction

		# Set the bullet's rotation angle to be the same as the rocket's.
		self.rotation_angle = self.rocket.rotation_angle

		# Rotate the bullet, get its rect and set it to the right position.
		self.image = pygame.transform.rotate(self.image, self.rotation_angle)
		self.rect = self.image.get_rect(center=self.rocket.rect.center)

		# Create a bullet rect at (0, 0) and then set the correct position.
		# self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
		# 	self.settings.bullet_height)
		# self.rect.midtop = ai_game.rocket.rect.midtop

		# Store the bullet's position as a decimal value.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		self.x_movement = 0
		self.y_movement = 0


	def update(self):
		"""Move the bullet in the direction it's currently facing."""
		# Update the decimal position of the bullet.
		self.x += self.x_movement
		self.y += self.y_movement

		# Update the rect position.	
		self.rect.x = self.x
		self.rect.y = self.y


	def calculate_movement(self):
		"""
		Calculate how much to move the bullet's x and y coordinates in order
		to maintain the prescribed bullet speed.
		"""
		if self.rocket.direction == 'up':
			self.x_movement = 0
			self.y_movement = -self.settings.bullet_speed
		elif self.rocket.direction == 'left':
			self.x_movement = -self.settings.bullet_speed
			self.y_movement = 0
		elif self.rocket.direction == 'down':
			self.x_movement = 0
			self.y_movement = self.settings.bullet_speed
		elif self.rocket.direction == 'right':
			self.x_movement = self.settings.bullet_speed
			self.y_movement = 0
		else:		
			self.x_movement = (self.settings.bullet_speed * 
					sin(radians(self.rocket.converted_angle)))
			self.y_movement = (self.settings.bullet_speed *
					cos(radians(self.rocket.converted_angle)))

			self._calcualate_negative_components()

	def _calcualate_negative_components(self):
		"""Sets negative x and y components as required."""
		if self.rocket.direction == 'upleft':
			self.x_movement = -self.x_movement
			self.y_movement = -self.y_movement
		elif self.rocket.direction == 'downleft':
			self.x_movement = -self.x_movement
		elif self.rocket.direction == 'downright':
			pass
		elif self.rocket.direction == 'upright':
			self.y_movement = -self.y_movement
		

	def draw_bullet(self):
		"""Draw the bullet to the screen."""
		self.screen.blit(self.image, self.rect)
		# pygame.draw.rect(self.screen, self.color, self.rect)