from manim import *

class Axes(Scene):
    def construct(self):
        axes = Axes()






      
        

class ContinuousMotion(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(func, stroke_width=2, max_anchors_per_line=30)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)


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


class demo(Scene):
    def construct(self):
        t = Text("Was haltet ihr")
        t2 = Text("von diesen Animationen?")
        t3 = Text("?", color = RED, font_size=150)
        t4 = Text("?", color = RED, font_size=100000)
        s = Circle(color = RED)
        s2 = Circle(color = RED, fill_opacity=0.5, radius=4)
        r = Rectangle(height=4, width=4, color=BLUE, fill_opacity=0.05)
        self.wait(1)
        self.play(Write(t))
        self.wait(0.5)
        self.play(Transform(t, t2))
        self.wait(1)
        self.play(Transform(t, t3))
        self.play(Transform(t, t4))
        self.wait(1)
        self.play(FadeOut(t), FadeIn(s))
        self.wait(1)
        self.play(Transform(s, s2),DrawBorderThenFill(r), run_time=2)
        self.wait(1)
        r3 = []
        for i in range(10):
            r3.append(Rectangle(height=4, width=4, color=BLUE, fill_opacity=i/10))
            self.play(Transform(r, r3[i]))
        self.wait(2)
        