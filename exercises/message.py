import pygame

class Message:
	"""A message that gets printed to a pygame window."""

	def __init__(self, ai_game, message):
		"""Initialize the message and set its attributes."""
		self.message = str(message)
		# Set the font
		self.font = pygame.font.SysFont('Arial', 70)

		# Get the screen's rectangle
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

	def display_message(self):
		"""Display the message in the center of the screen."""

		# Render the message as an object, get its rect and set that rect's 
		# center to the screen's center
		self.formatted_message = self.font.render(self.message, True, (0, 0, 0))
		self.message_rect = self.formatted_message.get_rect()
		self.message_rect.center = self.screen_rect.center

		# Draw the message
		self.screen.blit(self.formatted_message, self.message_rect)