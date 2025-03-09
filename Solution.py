
from manim import *

class Solution(Scene):
    def construct(self):
        # Section 1: Find the partial derivatives
        description1 = MathTex(r"\text{Find the partial derivatives:}").to_edge(UP)
        eq1_1 = MathTex(r"g_x = \frac{\partial}{\partial x}(1 - \cos x + \frac{1}{2} y^2) = \sin x").move_to(ORIGIN)
        eq1_2 = MathTex(r"g_y = \frac{\partial}{\partial y}(1 - \cos x + \frac{1}{2} y^2) = y").move_to(ORIGIN)

        self.play(Write(description1))
        self.play(Write(eq1_1))
        self.wait(2)
        self.play(ReplacementTransform(eq1_1, eq1_2))
        self.wait(2)
        self.play(FadeOut(description1, eq1_2))

        # Section 2: Set the partial derivatives to zero
        description2 = MathTex(r"\text{Set the partial derivatives to zero:}").to_edge(UP)
        eq2_1 = MathTex(r"\sin x = 0 \quad \Rightarrow \quad x = n\pi, \quad n \in \mathbb{Z}").move_to(ORIGIN)
        eq2_2 = MathTex(r"y = 0").move_to(ORIGIN)

        self.play(Write(description2))
        self.play(Write(eq2_1))
        self.wait(2)
        self.play(ReplacementTransform(eq2_1, eq2_2))
        self.wait(2)
        self.play(FadeOut(description2, eq2_2))

        # Section 3: Stationary points
        description3 = MathTex(r"\text{Stationary points:}").to_edge(UP)
        eq3_1 = MathTex(r"(x, y) = (n\pi, 0)").move_to(ORIGIN)

        self.play(Write(description3))
        self.play(Write(eq3_1))
        self.wait(2)
        self.play(FadeOut(description3, eq3_1))

        # Section 4: Classify the stationary points
        description4 = MathTex(r"\text{Classify the stationary points:}").to_edge(UP)
        eq4_1 = MathTex(r"g_{xx} = \cos x").move_to(ORIGIN)
        eq4_2 = MathTex(r"g_{yy} = 1").move_to(ORIGIN)
        eq4_3 = MathTex(r"g_{xy} = 0").move_to(ORIGIN)
        eq4_4 = MathTex(r"H = g_{xx}g_{yy} - (g_{xy})^2 = \cos x").move_to(ORIGIN)

        self.play(Write(description4))
        self.play(Write(eq4_1))
        self.wait(2)
        self.play(ReplacementTransform(eq4_1, eq4_2))
        self.wait(2)
        self.play(ReplacementTransform(eq4_2, eq4_3))
        self.wait(2)
        self.play(ReplacementTransform(eq4_3, eq4_4))
        self.wait(2)
        self.play(FadeOut(description4, eq4_4))

        # Section 5: Evaluate the stationary values
        description5 = MathTex(r"\text{Evaluate the stationary values:}").to_edge(UP)
        eq5_1 = MathTex(r"g(n\pi, 0) = 1 - \cos(n\pi) + \frac{1}{2} \cdot 0^2 = 1 - (-1)^n").move_to(ORIGIN)
        eq5_2 = MathTex(r"\text{For even } n, \, g(n\pi, 0) = 0").move_to(ORIGIN)
        eq5_3 = MathTex(r"\text{For odd } n, \, g(n\pi, 0) = 2").move_to(ORIGIN)

        self.play(Write(description5))
        self.play(Write(eq5_1))
        self.wait(2)
        self.play(ReplacementTransform(eq5_1, eq5_2))
        self.wait(2)
        self.play(ReplacementTransform(eq5_2, eq5_3))
        self.wait(2)
        self.play(FadeOut(description5, eq5_3))

        # Section 6: Sketch the contours
        description6 = MathTex(r"\text{Sketch the contours:}").to_edge(UP)
        eq6_1 = MathTex(r"g(x, y) = c").move_to(ORIGIN)
        eq6_2 = MathTex(r"1 - \cos x + \frac{1}{2} y^2 = c").move_to(ORIGIN)
        eq6_3 = MathTex(r"c = 0: \, \cos x = 1, \, y = 0").move_to(ORIGIN)
        eq6_4 = MathTex(r"c = 2: \, \cos x = -1, \, y = 0").move_to(ORIGIN)

        self.play(Write(description6))
        self.play(Write(eq6_1))
        self.wait(2)
        self.play(ReplacementTransform(eq6_1, eq6_2))
        self.wait(2)
        self.play(ReplacementTransform(eq6_2, eq6_3))
        self.wait(2)
        self.play(ReplacementTransform(eq6_3, eq6_4))
        self.wait(2)
        self.play(FadeOut(description6, eq6_4))
