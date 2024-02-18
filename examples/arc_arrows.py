from manim import *

class Graphic(Scene):
    def construct(self):
        curved_arrow = CurvedArrow(
                start_point=np.array([-2, 0, 0]),
                end_point=np.array([2, 1, 0]),
                )

        self.play(Create(curved_arrow))
        self.wait()


class ArcBetweenPointsExample(Scene):
    def construct(self):
        circle = Circle(radius=2, stroke_color=GREY)
        dot_1 = Dot(color=GREEN).move_to([2, 0, 0]).scale(0.5)
        dot_1_text = Tex("(2,0)").scale(0.5).next_to(dot_1, RIGHT).set_color(BLUE)
        dot_2 = Dot(color=GREEN).move_to([0, 2, 0]).scale(0.5)
        dot_2_text = Tex("(0,2)").scale(0.5).next_to(dot_2, UP).set_color(BLUE)
        arc= ArcBetweenPoints(start=2 * RIGHT, end=2 * UP, stroke_color=YELLOW)
        self.add(circle, dot_1, dot_2, dot_1_text, dot_2_text)
        self.play(Create(arc))

class ArrowBetweenPointsExample(Scene):
    def construct(self):
        circle = Circle(radius=2, stroke_color=GREY)
        dot_1 = Dot(color=GREEN).move_to([2, 0, 0]).scale(0.5)
        dot_1_text = Tex("(2,0)").scale(0.5).next_to(dot_1, RIGHT).set_color(BLUE)
        dot_2 = Dot(color=GREEN).move_to([0, 2, 0]).scale(0.5)
        dot_2_text = Tex("(0,2)").scale(0.5).next_to(dot_2, UP).set_color(BLUE)
        arc= ArcBetweenPoints(start=2 * RIGHT, end=2 * UP, stroke_color=YELLOW)

        arc = CurvedArrow(
                start_point=np.array([2, 0, 0]),
                end_point=np.array([0, 2, 0]),
                )


        self.add(circle, dot_1, dot_2, dot_1_text, dot_2_text)
        self.play(Create(arc))
