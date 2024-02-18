from manim import *

class ShowBraceAnimationEffectv2(Scene):
    def construct(self):
        tex= MathTex("Fahrenheit","=","Celsius","\\times","{9","\\over","5}","+","32").scale(1.5)
        self.play(Write(tex),run_time=3)
        self.wait()        
        
        brace_fah = Brace(mobject=tex[0],direction=UP, buff=0.2)
        brace_fah_text= brace_fah.get_tex("Symbol",":","\\","^{\\circ}","F")
        self.play(GrowFromCenter(brace_fah),FadeIn(brace_fah_text),run_time=2)    
        self.wait()
        
        brace_cel = Brace(mobject=tex[2],direction=DOWN, buff=0.2)
        brace_cel_tex= brace_cel.get_tex("Symbol",":","\\,","^{\\circ}","C")
        self.play(GrowFromCenter(brace_cel),FadeIn(brace_cel_tex),run_time=2)    
        self.wait(2)
