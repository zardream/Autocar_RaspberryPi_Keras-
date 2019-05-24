import os

os.environ['SDL_VIDEORIVER']='dummy'
import pygame
pygame.init()
pygame.display.set_mode((300,300))

while True:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.KEYDOWN:
			key_input = pygame.key.get_pressed()
			print(key_input[pygame.K_w])