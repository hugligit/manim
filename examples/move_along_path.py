from manim import *

raise Exception("borked")

class Follow(Scene):
    def construct(self):

        vertices = [
                np.array([-1, -1, 0]),
                np.array([0, 2, 0]),
                np.array([-4, -1, 0]),
                np.array([2, 0, 0])
                ]


        # curve = CubicBezier(points=vertices)
        curve = CubicBezier(*vertices)

        self.play(Write(curve))
        self.wait()

        dot = Dot(point=np.array([-1, -1, 0]))
        dot = Circle().scale(0.25)
        s = Square().scale(0.25)
        self.play(Write(dot))
        self.wait()

        self.play(
                MoveAlongPath(mobject=dot, path=curve), 
                MoveAlongPath(mobject=s, path=curve), 
                Transform(dot, s), 
                run_time=2)
        self.wait(1)
