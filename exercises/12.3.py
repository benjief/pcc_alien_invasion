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
		self.screen_rect = self.screen.get_rect()
		pygame.display.set_caption("Exercise 12-3")

		self.rocket = Rocket(self)
		self.bullets = pygame.sprite.Group()
		

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			self._check_events()
			self.rocket.update()
			self._update_bullets()
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
			self.rocket.decelerating_right = False
			self.rocket.accelerating_right = True
			self.rocket.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.rocket.decelerating_left = False
			self.rocket.accelerating_left = True
			self.rocket.moving_left = True
		elif event.key == pygame.K_UP:
			self.rocket.decelerating_up = False
			self.rocket.accelerating_up = True
			self.rocket.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.rocket.decelerating_down = False
			self.rocket.accelerating_down = True
			self.rocket.moving_down = True
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
			self.rocket.accelerating_right = False
			self.rocket.decelerating_right = True
		elif event.key == pygame.K_LEFT:
			self.rocket.accelerating_left = False
			self.rocket.decelerating_left = True
		elif event.key == pygame.K_UP:
			self.rocket.accelerating_up = False
			self.rocket.decelerating_up = True
		elif event.key == pygame.K_DOWN:
			self.rocket.accelerating_down = False
			self.rocket.decelerating_down = True
		elif event.key == pygame.K_e:
			self.rocket.rotating_ccw = False
		elif event.key == pygame.K_r:
			self.rocket.rotating_cw = False


	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group."""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = RocketBullet(self)
			self.bullets.add(new_bullet)
			new_bullet.calculate_movement()
			

	def _update_bullets(self):
		"""Update positions of bullets and get rid of old bullets."""
		self.bullets.update()

		# Get rid of bullets that have disappeared.
		for bullet in self.bullets.copy():
			if bullet.direction == 'up':
				if bullet.rect.bottom <= 0:
					self.bullets.remove(bullet)
			elif bullet.direction == 'upright':
				if (bullet.rect.bottomleft[0] >= self.screen_rect.right or
						bullet.rect.bottomleft[1] <= 0):
					self.bullets.remove(bullet)
			elif bullet.direction == 'right':
				if bullet.rect.left >= self.screen_rect.right:
					self.bullets.remove(bullet)
			elif bullet.direction == 'downright':
				if (bullet.rect.topleft[0] >= self.screen_rect.right or
						bullet.rect.topleft[1] >= self.screen_rect.bottom):
					self.bullets.remove(bullet)
			elif bullet.direction == 'down':
				if bullet.rect.top >= self.screen_rect.bottom:
					self.bullets.remove(bullet)
			elif bullet.direction == 'downleft':
				if (bullet.rect.topright[1] >= self.screen_rect.bottom or
						bullet.rect.topright[0] <= 0):
					self.bullets.remove(bullet)
			elif bullet.direction == 'left':
				if bullet.rect.right <= 0:
					self.bullets.remove(bullet)
			elif bullet.direction == 'upleft':
				if (bullet.rect.bottomright[0] <= 0 or
						bullet.rect.bottomright[1] <= 0):
					self.bullets.remove(bullet)


	def _update_screen(self):
		# Update images on the screen and flip to the new screen.
		self.screen.fill(self.settings.bg_color)
		self.screen.blit(self.settings.bg_image, (0, 0))
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.rocket.blitme()
		pygame.display.flip()


if __name__ == '__main__':
	# Make a game instance and run the game.
	ai = RocketShip()
	ai.run_game()