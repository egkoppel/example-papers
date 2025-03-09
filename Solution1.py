
from manim import *

class Solution(Scene):
    def construct(self):
        # Step 1
        step1 = MathTex(r"\text{Rewrite the equation:}").to_edge(UP)
        eq1 = MathTex(r"\frac{dy}{dx} = \frac{y(y + x)}{x^2}").move_to(ORIGIN)
        self.play(Write(step1))
        self.play(Write(eq1))
        self.wait(2)

        # Step 2
        step2 = MathTex(r"\text{Separate variables:}").to_edge(UP)
        eq2 = MathTex(r"\frac{dy}{y(y + x)} = \frac{dx}{x^2}").move_to(ORIGIN)
        self.play(ReplacementTransform(eq1, eq2), ReplacementTransform(step1, step2))
        self.wait(2)

        # Step 3
        step3 = MathTex(r"\text{Integrate both sides:}").to_edge(UP)
        eq3 = MathTex(r"\int \frac{dy}{y(y + x)} = \int \frac{dx}{x^2}").move_to(ORIGIN)
        self.play(ReplacementTransform(eq2, eq3), ReplacementTransform(step2, step3))
        self.wait(2)

        # Step 4
        step4 = MathTex(r"\text{Use partial fraction decomposition:}").to_edge(UP)
        eq4 = MathTex(r"\frac{1}{y(y + x)} = \frac{A}{y} + \frac{B}{y + x}").move_to(ORIGIN)
        self.play(ReplacementTransform(eq3, eq4), ReplacementTransform(step3, step4))
        self.wait(2)

        # Step 5
        step5 = MathTex(r"\text{Solve for } A \text{ and } B:").to_edge(UP)
        eq5_1 = MathTex(r"1 = A(y + x) + By").move_to(ORIGIN)
        eq5_2 = MathTex(r"1 = Ay + Ax + By").move_to(ORIGIN)
        eq5_3 = MathTex(r"1 = (A + B)y + Ax").move_to(ORIGIN)
        eq5_4 = MathTex(r"A + B = 0, \quad Ax = 1").move_to(ORIGIN)
        eq5_5 = MathTex(r"A = \frac{1}{x}, \quad B = -\frac{1}{x}").move_to(ORIGIN)
        self.play(ReplacementTransform(eq4, eq5_1), ReplacementTransform(step4, step5))
        self.wait(2)
        self.play(ReplacementTransform(eq5_1, eq5_2))
        self.wait(2)
        self.play(ReplacementTransform(eq5_2, eq5_3))
        self.wait(2)
        self.play(ReplacementTransform(eq5_3, eq5_4))
        self.wait(2)
        self.play(ReplacementTransform(eq5_4, eq5_5))
        self.wait(2)

        # Step 6
        step6 = MathTex(r"\text{Substitute back:}").to_edge(UP)
        eq6 = MathTex(r"\int \left(\frac{1}{x} \cdot \frac{1}{y} - \frac{1}{x} \cdot \frac{1}{y + x}\right) dy = \int \frac{dx}{x^2}").move_to(ORIGIN)
        self.play(ReplacementTransform(eq5_5, eq6), ReplacementTransform(step5, step6))
        self.wait(2)

        # Step 7
        step7 = MathTex(r"\text{Integrate:}").to_edge(UP)
        eq7 = MathTex(r"\frac{1}{x} \left(\ln |y| - \ln |y + x|\right) = -\frac{1}{x} + C").move_to(ORIGIN)
        self.play(ReplacementTransform(eq6, eq7), ReplacementTransform(step6, step7))
        self.wait(2)

        # Step 8
        step8 = MathTex(r"\text{Simplify:}").to_edge(UP)
        eq8 = MathTex(r"\ln \left|\frac{y}{y + x}\right| = -1 + Cx").move_to(ORIGIN)
        self.play(ReplacementTransform(eq7, eq8), ReplacementTransform(step7, step8))
        self.wait(2)

        # Step 9
        step9 = MathTex(r"\text{Exponentiate both sides:}").to_edge(UP)
        eq9 = MathTex(r"\left|\frac{y}{y + x}\right| = e^{-1 + Cx}").move_to(ORIGIN)
        self.play(ReplacementTransform(eq8, eq9), ReplacementTransform(step8, step9))
        self.wait(2)

        # Step 10
        step10 = MathTex(r"\text{Solve for } y:").to_edge(UP)
        eq10 = MathTex(r"y = \frac{y + x}{e^{1 - Cx}}").move_to(ORIGIN)
        self.play(ReplacementTransform(eq9, eq10), ReplacementTransform(step9, step10))
        self.wait(2)

        # Fade out
        self.play(FadeOut(eq10), FadeOut(step10))
