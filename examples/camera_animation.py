
from manim import *

class ChangingCameraWidthAndRestore(MovingCameraScene):
    def construct(self):
        text = Text("Hello World").set_color(BLUE)
        self.add(text)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=text.width * 1.2))
        self.wait(0.3)
        self.play(Restore(self.camera.frame))




class MovingCameraCenter(MovingCameraScene):
    def construct(self):
        s = Square(color=RED, fill_opacity=0.5).move_to(2 * LEFT)
        t = Triangle(color=GREEN, fill_opacity=0.5).move_to(2 * RIGHT)
        self.wait(0.3)
        self.add(s, t)
        self.play(self.camera.frame.animate.move_to(s))
        self.wait(0.3)
        self.play(self.camera.frame.animate.move_to(t))



class MovingAndZoomingCamera(MovingCameraScene):
    def construct(self):
        s = Square(color=BLUE, fill_opacity=0.5).move_to(2 * LEFT)
        t = Triangle(color=YELLOW, fill_opacity=0.5).move_to(2 * RIGHT)
        self.add(s, t)
        self.play(self.camera.frame.animate.move_to(s).set(width=s.width*2))
        self.wait(0.3)
        self.play(self.camera.frame.animate.move_to(t).set(width=t.width*2))

        self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=14))


class MovingCameraOnGraph(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        ax = Axes(x_range=[-1, 10], y_range=[-1, 1])
        graph = ax.plot(lambda x: np.sin(x), color=WHITE, x_range=[0, 3 * PI])

        dot_1 = Dot(ax.i2gp(graph.t_min, graph))
        dot_2 = Dot(ax.i2gp(graph.t_max, graph))
        self.add(ax, graph, dot_1, dot_2)

        self.play(self.camera.frame.animate.scale(0.5).move_to(dot_1))
        self.play(self.camera.frame.animate.move_to(dot_2))
        self.play(Restore(self.camera.frame))
        self.wait()
