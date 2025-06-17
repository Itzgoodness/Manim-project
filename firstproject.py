from manim import *
class definitefunction(Scene):
    def construct (self):
        circle = Circle(radius=1,color= YELLOW)
        circle2 = Circle(radius=2, color=GREEN)
        circle3 = Circle(radius=3, color=RED)
        circle4 = Circle(radius=4, color= BLUE)

        square = Square(side_length=1)
        square2 = Square(side_length=2)
        square3= Square(side_length=3)
        triangle =Triangle().scale(4)
        triangle.shift(UP)

        self.play(FadeIn(circle, shift = LEFT *2 + DOWN*2))
        self.play(FadeIn(circle2, shift = RIGHT *2+UP*2))
        self.play(FadeIn(circle3, shift = UP*5 + DOWN*2))
        self.play(FadeIn(circle4, shift = DOWN*5 + UP*2))
        self.play(circle.animate.set_fill(YELLOW, opacity = 0.4))
        self.play(circle2.animate.set_fill(GREEN, opacity = 0.4))
        self.play(circle3.animate.set_fill(RED_C, opacity = 0.4))
        self.play(circle4.animate.set_fill(BLUE, opacity = 0.4))
 
        self.play(Transform(circle,square))
        self.play(Transform(circle2,square2) )
        self.play(Transform(circle3,square3))
        self.play(Transform(circle4,triangle))

