from manim import *

class CreatingMobjects(Scene):# {{{
    def construct(self):
        c1 = Circle()
        self.add(c1)
        self.wait(1)
        self.remove(c1)
        self.wait(1)
# }}}
class Shapes(Scene):# {{{
    def construct(self):
        s = Square()
        c = Circle()
        t = Triangle()

        c.shift(0 * LEFT)
        t.shift(0 * RIGHT)
        s.shift(0 * UP)

        self.add(c, s, t)
        self.wait(1)
# }}}
class Placement(Scene):# {{{
    def construct(self):
        s = Square()
        c = Circle()
        t = Triangle()

        c.shift(0 * UP)
        t.shift(0 * RIGHT)
        s.shift(0 * UP)

        self.add(c, s, t)

        self.play(c.animate.move_to([1, 2, 0]))
        self.wait(1)
        self.play(s.animate.next_to(c, buff=0).shift([0, -2, 0]).rotate(PI/8))
        self.wait(1)

# }}}

print(PINK)

class Styling(Scene):# {{{
    def construct(self):
        t = Triangle().shift(RIGHT)
        c = Circle().shift(LEFT)
        s = Square().shift(UP)

        c.set_stroke(
                color=GREEN,
                width=20
                )

        s.set_fill(
                YELLOW,
                opacity=1
                )

        t.set_fill(
                PINK,
                opacity=0.5
                )

        t.set_stroke(
                color="#00ffff",
                width=20
                )


        self.add(t, s, c)
        self.wait()
        self.play(s.animate.rotate(PI/4), run_time=8)
        self.wait()
# }}}
