import pygame.display

import __main__ as RiftWizard


def get_draw_scale(self):
    h_scale = pygame.display.get_surface().get_width() / RiftWizard.RENDER_WIDTH
    v_scale = pygame.display.get_surface().get_height() / RiftWizard.RENDER_HEIGHT
    scale = min(h_scale, v_scale)
    return scale

RiftWizard.PyGameView.get_draw_scale = get_draw_scale