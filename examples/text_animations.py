from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

# config.background_color  = RED

class Anagram(Scene):
    def construct(self):
        src = Text("mother in law")
        tar = Text("woman hitler")
        self.play(Write(src))
        self.wait(1.5)
        self.play(TransformMatchingShapes(src, tar, path_arc=PI/2))
        self.wait(1.5)


class Voiceover(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService())
        src = Text("mother in law")
        tar = Text("woman hitler")
        self.play(Write(src))
        self.wait(1.5)
        with self.voiceover(text="This is drawn as I speak") as tracker:
            self.play(TransformMatchingShapes(src, tar, path_arc=PI/2))
        self.wait(1.5)




class MyScene2(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang='en', tld='co.uk'))
        circle = Circle()
        src = Text("mother in law")
        tar = Text("woman hitler")
        # self.play(Write(src))
        self.wait(3.5)
        # self.play(TransformMatchingShapes(src, tar, path_arc=PI/2))
        with self.voiceover(text="An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once") as tracker:
            self.play(Create(circle))

        with self.voiceover(text="Here's an example. What will this one become?") as tracker:
            self.play(Write(src))

        with self.voiceover(text="Surprise!") as tracker:
            self.wait(0.5)
            self.play(TransformMatchingShapes(src, tar, path_arc=PI/2))

        self.wait(2.5)



