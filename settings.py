class Settings:
	"""A class to store all settings for Alien Invasion."""


	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		# Note that these values are commented out because we're using
		# full screen mode.
		#self.screen_width = 1200
		#self.screen_height = 600
		self.bg_color = (194, 243, 255)

		# Ship settings
		self.ship_speed = 1.5