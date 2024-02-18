from manim import *

class SurroudingFrame(Scene):# {{{
    def construct(self):
        tex = MathTex(
                "Fahrenheit", "=",
                "Celsius", "\\times",
                "{9", "\\over", "5}",
                "+", "32"
                ).scale(1.5)


        self.play(Write(tex), run_time=1)

        surrounding_rectangle_celsius = SurroundingRectangle(
                mobject=tex[2:3], 
                color=YELLOW, 
                buff=0.15,
                corner_radius=[
                    0.1,
                    0.2,
                    0.3,
                    0.0
                    ]
                )

        surrounding_rectangle_fraction = SurroundingRectangle(
                mobject=tex[4:7], 
                color="#00ffff", 
                buff=0.15,
                corner_radius=[
                    0.0,
                    0.0,
                    0.0,
                    0.1
                    ]
                )

        self.play(Create(surrounding_rectangle_celsius))
        self.wait(8)
        self.play(Transform(surrounding_rectangle_celsius, surrounding_rectangle_fraction))

        self.wait(8)
# }}}

class HighlightingFrame(Scene):# {{{
    def construct(self):
        tex = MathTex(
                "Fahrenheit", "=",
                "Celsius", "\\times",
                "{9", "\\over", "5}",
                "+", "32"
                ).scale(1.5)


        self.play(Write(tex), run_time=1)

        surrounding_rectangle_celsius = BackgroundRectangle(
                mobject=tex[2:3], 
                color=YELLOW, 
                buff=0.15,
                fill_opacity=0.7,
                corner_radius=[
                    0.1,
                    0.2,
                    0.3,
                    0.0
                    ]
                )

        surrounding_rectangle_fraction = BackgroundRectangle(
                mobject=tex[4:7], 
                color="#00ffff", 
                buff=0.15,
                fill_opacity=0.7,
                corner_radius=[
                    0.0,
                    0.0,
                    0.0,
                    0.1
                    ]
                )

        self.play(Create(surrounding_rectangle_celsius))
        self.play(Transform(surrounding_rectangle_celsius, surrounding_rectangle_fraction))

        self.wait(8)
# }}}

class CrossFrame(Scene):# {{{
    def construct(self):
        tex = MathTex(
                "Fahrenheit", "=",
                "Celsius", "\\times",
                "{9", "\\over", "5}",
                "+", "32"
                ).scale(1.5)


        self.play(Write(tex), run_time=1)

        surrounding_rectangle_celsius = Cross(
                mobject=tex[2:3], 
                stroke_color=YELLOW, 
                stroke_width=8
                )

        surrounding_rectangle_fraction = Cross(
                mobject=tex[4:7], 
                stroke_color="#00ffff", 
                stroke_width=8
                )

        self.play(Create(surrounding_rectangle_celsius))
        self.play(Transform(surrounding_rectangle_celsius, surrounding_rectangle_fraction))

        self.wait(8)
# }}}
