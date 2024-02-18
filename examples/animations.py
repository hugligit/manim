from manim import *

class Count(Animation):# {{{
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        super().__init__(number, **kwargs)
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        interpolation_range = self.end - self.start
        value = self.start + alpha*interpolation_range
        self.mobject.set_value(value)
# }}}
class CountingScene(Scene):# {{{
    def construct(self):
        start = 7
        number = DecimalNumber(start).set_color(WHITE).scale(5)
        number.add_updater(lambda number:  number.move_to(ORIGIN))

        self.add(number)
        self.wait()
        self.play(Count(number, start, 100), run_time=4, rate_func=linear)
        self.wait()

# }}}

