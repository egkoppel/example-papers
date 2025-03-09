
from manim import *

class Solution(Scene):
    def construct(self):
        # Section 1: Find (∂a/∂b)_c
        description1 = MathTex(r"\text{Find } \left( \frac{\partial a}{\partial b} \right)_c").to_edge(UP)
        eq1_1 = MathTex(r"a = \frac{bc(b^2 - c^2)}{(b^2 + c^2)^2}").move_to(ORIGIN)
        eq1_2 = MathTex(r"\frac{\partial a}{\partial b} = \frac{\partial}{\partial b} \left( \frac{bc(b^2 - c^2)}{(b^2 + c^2)^2} \right)").move_to(ORIGIN)
        eq1_3 = MathTex(r"\frac{\partial a}{\partial b} = \frac{(b^2 + c^2)^2 \cdot c(3b^2 - c^2) - bc(b^2 - c^2) \cdot 4b(b^2 + c^2)}{(b^2 + c^2)^4}").move_to(ORIGIN)

        self.play(Write(description1))
        self.play(Write(eq1_1))
        self.wait(2)
        self.play(ReplacementTransform(eq1_1, eq1_2))
        self.wait(2)
        self.play(ReplacementTransform(eq1_2, eq1_3))
        self.wait(2)
        self.play(FadeOut(eq1_3, description1))

        # Section 2: Find (∂b/∂c)_a
        description2 = MathTex(r"\text{Find } \left( \frac{\partial b}{\partial c} \right)_a").to_edge(UP)
        eq2_1 = MathTex(r"a(b^2 + c^2)^2 = bc(b^2 - c^2)").move_to(ORIGIN)
        eq2_2 = MathTex(r"4ac(b^2 + c^2) = b(b^2 - 3c^2)").move_to(ORIGIN)
        eq2_3 = MathTex(r"\frac{\partial b}{\partial c} = \frac{4ac(b^2 + c^2)}{b(b^2 - 3c^2)}").move_to(ORIGIN)

        self.play(Write(description2))
        self.play(Write(eq2_1))
        self.wait(2)
        self.play(ReplacementTransform(eq2_1, eq2_2))
        self.wait(2)
        self.play(ReplacementTransform(eq2_2, eq2_3))
        self.wait(2)
        self.play(FadeOut(eq2_3, description2))

        # Section 3: Find (∂c/∂a)_b
        description3 = MathTex(r"\text{Find } \left( \frac{\partial c}{\partial a} \right)_b").to_edge(UP)
        eq3_1 = MathTex(r"a(b^2 + c^2)^2 = bc(b^2 - c^2)").move_to(ORIGIN)
        eq3_2 = MathTex(r"(b^2 + c^2)^2 = 0").move_to(ORIGIN)
        eq3_3 = MathTex(r"\frac{\partial c}{\partial a} = \frac{(b^2 + c^2)^2}{bc(b^2 - c^2)}").move_to(ORIGIN)

        self.play(Write(description3))
        self.play(Write(eq3_1))
        self.wait(2)
        self.play(ReplacementTransform(eq3_1, eq3_2))
        self.wait(2)
        self.play(ReplacementTransform(eq3_2, eq3_3))
        self.wait(2)
        self.play(FadeOut(eq3_3, description3))

        # Section 4: Multiply the partial derivatives
        description4 = MathTex(r"\text{Multiply the partial derivatives}").to_edge(UP)
        eq4_1 = MathTex(r"\left( \frac{\partial a}{\partial b} \right)_c \left( \frac{\partial b}{\partial c} \right)_a \left( \frac{\partial c}{\partial a} \right)_b").move_to(ORIGIN)
        eq4_2 = MathTex(r"= \left( \frac{(b^2 + c^2)^2 \cdot c(3b^2 - c^2) - bc(b^2 - c^2) \cdot 4b(b^2 + c^2)}{(b^2 + c^2)^4} \right)").move_to(ORIGIN)
        eq4_3 = MathTex(r"\cdot \left( \frac{4ac(b^2 + c^2)}{b(b^2 - 3c^2)} \right) \cdot \left( \frac{(b^2 + c^2)^2}{bc(b^2 - c^2)} \right)").move_to(ORIGIN)
        eq4_4 = MathTex(r"= -1").move_to(ORIGIN)

        self.play(Write(description4))
        self.play(Write(eq4_1))
        self.wait(2)
        self.play(ReplacementTransform(eq4_1, eq4_2))
        self.wait(2)
        self.play(ReplacementTransform(eq4_2, eq4_3))
        self.wait(2)
        self.play(ReplacementTransform(eq4_3, eq4_4))
        self.wait(2)
        self.play(FadeOut(eq4_4, description4))
