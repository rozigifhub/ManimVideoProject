from manim import *

class Introduction(Scene):
    def construct(self):
        logo = ImageMobject("asset/logo.png")
        logo.scale(1.5)            # opsional: perbesar sedikit
        self.play(FadeIn(logo))    # fade in logo
        self.wait(2)