from manim import *

class WaveAnimation(Scene):
    def construct(self):
        annulus = Annulus()
        circle = Square().next_to(annulus, LEFT, buff=1)
        text = Text("Hello World").next_to(annulus, RIGHT, buff=1)

        self.play(
                ApplyWave(circle),
                ApplyWave(annulus),
                ApplyWave(text),
                )

        self.wait




class ApplyingWaves(Scene):
    def construct(self):
        tex = Tex("WaveWaveWaveWaveWave").scale(2)

        # self.play(ApplyWave(tex))

        self.play(ApplyWave(
            tex,
            direction=[1, -10, 0 ],
            time_width=1.5,
            ripples=6,
            rate_func=linear,
            amplitude=1
        ), run_time=7)

        self.play(ApplyWave(
            tex,
            direction=[1, -1, 0 ],
            time_width=1.5,
            ripples=6,
            rate_func=linear,
            amplitude=1
        ), run_time=7)

        # self.play(ApplyWave(
        #     tex,
        #     rate_func=linear,
        #     ripples=4
        # ))
