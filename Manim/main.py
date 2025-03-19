from manim import *

class test(Scene):
    def construct(self):
        lol = Text("Lol", fill_opacity=0.3)
        s = RoundedRectangle(color = ORANGE, corner_radius=0.2, )
        self.play(Write(s), )
        self.wait()