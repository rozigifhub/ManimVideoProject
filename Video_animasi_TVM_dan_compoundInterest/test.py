from manim import *

class Test(Scene):
    def construct(self):
        t = Text("Hello from venv!")
        self.play(Write(t))
        self.wait(1)
