from manim import *

class test(Scene):
    def construct(self):
        t = Tex("Du ","bist ","Dumm")
        t[0].set_color(RED)
        t[1].set_color(GREEN)
        t[2].set_color(BLUE)
        t2 = Tex("Ja ","Du ","Niemand ","anderes ","DU ")
        t2[0].set_color(RED)
        t2[1].set_color(GREEN)
        t2[1].weight = SEMIBOLD
        t2[2].set_color(BLUE)
        t2[3].set_color(YELLOW)
        t2[4].set_color(PURPLE)
        t2[4].weight = ULTRAHEAVY
        t2[4].font_size = 96
        t2[4].shift(RIGHT*1)
        self.play(Write(t[0]))
        self.wait(0.5)
        self.play(Write(t[1]))
        self.wait(0.5)
        self.play(Write(t[2]))
        self.wait(2)

        self.play(FadeOut(t))
        self.play(FadeIn(t2[0:2]))
        self.wait(2)
        self.play(DrawBorderThenFill(t2[2:4]))
        self.wait(2)
        self.play(Write(t2[4]), run_time=4)

        
        
        self.wait(5)
        paul = Text("Paul-Lennard ich weiß das du das siehst, schick die PPP", font_size=25).to_corner(DL, buff=0.5)
        paul2 = Text("Paul-Lennard ich weiß das du das siehst, schick die Power Point Präsentation", font_size=25).to_corner(DL, buff=0.5)
        self.play(FadeIn(paul))
        self.wait(2)
        self.play(Transform(paul, paul2))
        self.wait(6)

        self.play(FadeOut(paul2),FadeOut(t2))        