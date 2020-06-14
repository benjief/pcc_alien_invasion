import sys

import pygame

from rocket import Rocket
from rocket_settings import RocketSettings
from rocket_bullet import RocketBullet

class RocketShip:
	"""Overall class to manage a cartoon rocket's assets and behavior."""

	
	def __init__(self):
		"""Initialize the game and create game resources."""
		pygame.init()

		self.settings = RocketSettings()

		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		pygame.display.set_caption("Exercise 12-3")

		self.rocket = Rocket(self)
		self.bullets = pygame.sprite.Group()
		

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			self._check_events()
			self.rocket.update()
			self.bullets.update()
			self._update_screen()


	def _check_events(self):
		"""Respond to keypresses and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)


	def _check_keydown_events(self, event):
		"""Respond to keypresses"""
		if event.key == pygame.K_RIGHT:
			self.rocket.moving_right = True
			print(self.rocket.direction)
			print(self.rocket.rotation_angle)
		elif event.key == pygame.K_LEFT:
			self.rocket.moving_left = True
			print(self.rocket.direction)
			print(self.rocket.rotation_angle)
		elif event.key == pygame.K_UP:
			self.rocket.moving_up = True
			print(self.rocket.direction)
			print(self.rocket.rotation_angle)
		elif event.key == pygame.K_DOWN:
			self.rocket.moving_down = True
			print(self.rocket.direction)
			print(self.rocket.rotation_angle)
		elif (event.key == pygame.K_q) or (event.key == pygame.K_ESCAPE):
			sys.exit()
		elif event.key == pygame.K_e:
			self.rocket.rotating_ccw = True
		elif event.key == pygame.K_r:
			self.rocket.rotating_cw = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()


	def _check_keyup_events(self, event):
		"""Respond to key releases."""
		if event.key == pygame.K_RIGHT:
			self.rocket.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.rocket.moving_left = False
		elif event.key == pygame.K_UP:
			self.rocket.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.rocket.moving_down = False
		elif event.key == pygame.K_e:
			self.rocket.rotating_ccw = False
		elif event.key == pygame.K_r:
			self.rocket.rotating_cw = False


	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group."""
		new_bullet = RocketBullet(self)
		self.bullets.add(new_bullet)
		new_bullet.calculate_movement()
		print(new_bullet.rotation_angle)
		print(new_bullet.rocket.converted_angle)
		print(new_bullet.x_movement)
		print(new_bullet.y_movement)


	def _update_screen(self):
		# Update images on the screen and flip to the new screen.
		self.screen.fill(self.settings.bg_color)
		#self.screen.blit(self.settings.bg_image, (0, 0))
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.rocket.blitme()
		pygame.display.flip()


if __name__ == '__main__':
	# Make a game instance and run the game.
	ai = RocketShip()
	ai.run_game()