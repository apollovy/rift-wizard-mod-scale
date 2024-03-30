import pygame.display

import traceback

# this can't be done, because mods are being imported in RiffWizard module
# from RiffWizard import PyGameView
for frame, _ in traceback.walk_stack(None):
    PyGameView = frame.f_locals.get("PyGameView")
    RENDER_WIDTH = frame.f_locals.get("RENDER_WIDTH")
    RENDER_HEIGHT = frame.f_locals.get("RENDER_HEIGHT")

    if PyGameView != None:
        break


def get_draw_scale(self):
    h_scale = pygame.display.get_surface().get_width() / RENDER_WIDTH
    v_scale = pygame.display.get_surface().get_height() / RENDER_HEIGHT
    scale = min(h_scale, v_scale)
    return scale

PyGameView.get_draw_scale = get_draw_scale