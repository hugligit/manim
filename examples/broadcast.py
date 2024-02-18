from manim import *

class BradcastAnimation(Scene):
    def construct(self):
        mob = Square(side_length=4, color=TEAL)
        self.play(
                Broadcast(
                    mob,
                    focal_point=np.array([0, 0, 0]),
                    big_radius=3,
                    run_time=6
                    )
                )

        self.wait()
