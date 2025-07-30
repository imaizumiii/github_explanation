from manim import *

class Intro(Scene):
    def construct(self):
        title = Text("Welcome to GitHub Explanation", font_size=72)
        subtitle = Text("A Visual Guide to GitHub Features", font_size=48)

        self.play(Write(title))
        self.wait(1)
        self.play(Transform(title, subtitle))
        self.wait(1)
        self.play(FadeOut(title))