from manim import *

class Solution(Scene):
    def construct(self):
        # Create the first line: Fundamental relation
        line1 = MathTex(r"dU = T\,dS - p\,dV").to_edge(UP)
        self.play(Write(line1))
        self.wait(1)

        # Create the second line: Definition of G
        line2 = MathTex(r"G = U + p\,V - T\,S").next_to(line1, DOWN)
        self.play(Write(line2))
        self.wait(2)

        # Clear the screen
        self.play(FadeOut(line1), FadeOut(line2))

        # First line: Differentiate G general expression
        line1 = MathTex(r"dG = dU + p\,dV + V\,dp - T\,dS - S\,dT").to_edge(UP)
        self.play(Write(line1))
        self.wait(1)

        # Second line: Substitute dU = T\,dS - p\,dV
        line2 = MathTex(r"\text{Substitute } dU = T\,dS - p\,dV").next_to(line1, DOWN)
        self.play(Write(line2))
        self.wait(1)

        # Third line: Show expanded substitution
        line3 = MathTex(r"dG = \Bigl(T\,dS - p\,dV\Bigr) + p\,dV + V\,dp - T\,dS - S\,dT").next_to(line2, DOWN)
        self.play(Write(line3))
        self.wait(1)

        # Fourth line: Simplify to the final expression
        line4 = MathTex(r"dG = V\,dp - S\,dT").next_to(line3, DOWN)
        self.play(Write(line4))
        self.wait(2)

        # Clear the screen to prevent crowding
        self.play(FadeOut(line1), FadeOut(line2), FadeOut(line3), FadeOut(line4))

        # First line: Write the general expression for dG in terms of its partial derivatives
        line1 = MathTex(r"dG = \left(\frac{\partial G}{\partial p}\right)_T dp + \left(\frac{\partial G}{\partial T}\right)_p dT").to_edge(UP)
        self.play(Write(line1))
        self.wait(1)

        # Second line: Write the derived expression for dG
        line2 = MathTex(r"dG = V\,dp - S\,dT").next_to(line1, DOWN)
        self.play(Write(line2))
        self.wait(1)

        # Third line: Identify the partial derivative with respect to p
        line3 = MathTex(r"\left(\frac{\partial G}{\partial p}\right)_T = V").next_to(line2, DOWN)
        self.play(Write(line3))
        self.wait(1)

        # Fourth line: Identify the partial derivative with respect to T
        line4 = MathTex(r"\left(\frac{\partial G}{\partial T}\right)_p = -S").next_to(line3, DOWN)
        self.play(Write(line4))
        self.wait(2)

        # Clear the screen
        self.play(FadeOut(line1), FadeOut(line2), FadeOut(line3), FadeOut(line4))

        # First line: Start with the partial of S with respect to p
        line1 = MathTex(r"\left(\frac{\partial S}{\partial p}\right)_T = -\frac{\partial}{\partial p}\left(\frac{\partial G}{\partial T}\right)_p").to_edge(UP)
        self.play(Write(line1))
        self.wait(1)

        # Second line: Use symmetry of second derivatives
        line2 = MathTex(r"= -\frac{\partial^2 G}{\partial p\,\partial T}").next_to(line1, DOWN)
        self.play(Write(line2))
        self.wait(1)

        # Third line: Swap the order of partials
        line3 = MathTex(r"= -\frac{\partial^2 G}{\partial T\,\partial p}").next_to(line2, DOWN)
        self.play(Write(line3))
        self.wait(1)

        # Fourth line: Final identified relation
        line4 = MathTex(r"= -\left(\frac{\partial V}{\partial T}\right)_p").next_to(line3, DOWN)
        self.play(Write(line4))
        self.wait(2)

        # Clear the screen
        self.play(FadeOut(line1), FadeOut(line2), FadeOut(line3), FadeOut(line4))