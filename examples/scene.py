from manim import *

DEG = PI / 180

# class SquareToCircle(Scene):# {{{
#     def construct(self):
#         circle = Circle()
#         circle.set_fill(PINK, opacity=0.5)
#         square = Square(color=BLUE)
#         square.set_fill(opacity=0.8)
#         square.rotate(PI/4)

#         self.play(Create(square))
#         self.play(Transform(square, circle))
#         self.play(FadeOut(square))
# # }}}

# class SquareAndCircle(Scene):# {{{
#     def construct(self):
#         circle = Circle()
#         circle.set_fill(PINK, opacity=0.5)

#         square = Square()
#         square.rotate(PI/4)
#         square.set_fill(BLUE, opacity=0.5)

#         square.next_to(circle, RIGHT, buff=0.5)
#         self.play(Create(circle))
#         self.play(Create(square))
#         self.play(FadeOut(circle), FadeOut(square))

#         # wait()
# # }}}

# class AnimatedSquareAndCircle(Scene):# {{{
#     def construct(self):
#         circle = Circle().shift(2* LEFT)

#         square = Square()

#         self.play(Create(square))
#         self.play(square.animate.rotate(PI/4))
#         self.play(square.animate.shift(2 * RIGHT))
#         self.play(ReplacementTransform(square, circle))
#         self.play(circle.animate.set_fill(PINK, opacity=0.5))

# # }}}



class Quirks(Scene):
    def construct(self):
        # s1 = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        # s2 = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        s1 = Square(color=BLUE, fill_opacity=0).shift(2 * LEFT)
        s2 = Square(color=GREEN, fill_opacity=0).shift(2 * RIGHT)
        self.play(Create(s1), Create(s2))
        self.play(
                s1.animate.set_fill(BLUE, opacity=0.7),
                s2.animate.set_fill(GREEN, opacity=0.7)
                )

        self.play(
                s1.animate.rotate(160*DEG),
                Rotate(s2, 160*DEG)
                )

        self.wait()
        self.play(
                FadeOut(s1),
                FadeOut(s2)
                )


