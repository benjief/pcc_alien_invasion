import pygame

class RocketSettings:
	"""A class to store all settings for my unexpected rocket game."""


	def __init__(self):
		"""Initialize the game's settings."""
		# Screen size settings
		# Note that these values are commented out because we're using
		# full screen mode.
		#self.screen_width = 1200
		#self.screen_height = 600

		# Color definitions and background/color setting
		midnight_blue = (0, 3, 36)
		black = (0, 0, 0)
		white = (255, 255, 255)
		self.bg_color = midnight_blue

		self.bg_image = pygame.image.load('images/space_bg.jpg')

		# Rocket settings
		self.rocket_speed = 3
		self.rotation_speed = 3
		# Starts facing upwards
		self.rotation_angle = 0

		# Bullet settings
		self.bullet_speed = 2
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3