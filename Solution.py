
from manim import *

class Solution(Scene):
    def construct(self):
        # Step 1: Rewrite in separable form
        step1 = MathTex(r"\text{Rewrite in separable form}").to_edge(UP)
        eq1 = MathTex(r"\frac{dy}{dx} = \frac{y^2 + xy}{x^2}").move_to(ORIGIN)
        eq2 = MathTex(r"\frac{dy}{dx} = \frac{y(y + x)}{x^2}").move_to(ORIGIN)

        self.play(Write(step1))
        self.play(Write(eq1))
        self.wait(2)
        self.play(ReplacementTransform(eq1, eq2))
        self.wait(2)
        self.play(FadeOut(eq2, step1))

        # Step 2: Separate the variables
        step2 = MathTex(r"\text{Separate the variables}").to_edge(UP)
        eq3 = MathTex(r"\frac{dy}{y(y + x)} = \frac{dx}{x^2}").move_to(ORIGIN)

        self.play(Write(step2))
        self.play(Write(eq3))
        self.wait(2)
        self.play(FadeOut(eq3, step2))

        # Step 3: Partial fraction decomposition
        step3 = MathTex(r"\text{Partial fraction decomposition}").to_edge(UP)
        eq4 = MathTex(r"\frac{1}{y(y + x)} = \frac{A}{y} + \frac{B}{y + x}").move_to(ORIGIN)
        eq5 = MathTex(r"1 = A(y + x) + By").move_to(ORIGIN)
        eq6 = MathTex(r"A + B = 0, \quad Ax = 1").move_to(ORIGIN)
        eq7 = MathTex(r"A = \frac{1}{x}, \quad B = -\frac{1}{x}").move_to(ORIGIN)
        eq8 = MathTex(r"\frac{1}{y(y + x)} = \frac{1}{xy} - \frac{1}{x(y + x)}").move_to(ORIGIN)

        self.play(Write(step3))
        self.play(Write(eq4))
        self.wait(2)
        self.play(ReplacementTransform(eq4, eq5))
        self.wait(2)
        self.play(ReplacementTransform(eq5, eq6))
        self.wait(2)
        self.play(ReplacementTransform(eq6, eq7))
        self.wait(2)
        self.play(ReplacementTransform(eq7, eq8))
        self.wait(2)
        self.play(FadeOut(eq8, step3))

        # Step 4: Substitute back into the integral
        step4 = MathTex(r"\text{Substitute back into the integral}").to_edge(UP)
        eq9 = MathTex(r"\int \left( \frac{1}{xy} - \frac{1}{x(y + x)} \right) \, dy = \int \frac{1}{x^2} \, dx").move_to(ORIGIN)

        self.play(Write(step4))
        self.play(Write(eq9))
        self.wait(2)
        self.play(FadeOut(eq9, step4))

        # Step 5: Integrate both sides
        step5 = MathTex(r"\text{Integrate both sides}").to_edge(UP)
        eq10 = MathTex(r"\int \frac{1}{xy} \, dy - \int \frac{1}{x(y + x)} \, dy = \int \frac{1}{x^2} \, dx").move_to(ORIGIN)
        eq11 = MathTex(r"\frac{1}{x} \ln |y| - \frac{1}{x} \ln |y + x| = -\frac{1}{x} + C").move_to(ORIGIN)

        self.play(Write(step5))
        self.play(Write(eq10))
        self.wait(2)
        self.play(ReplacementTransform(eq10, eq11))
        self.wait(2)
        self.play(FadeOut(eq11, step5))

        # Step 6: Combine the logarithms
        step6 = MathTex(r"\text{Combine the logarithms}").to_edge(UP)
        eq12 = MathTex(r"\frac{1}{x} \ln \left| \frac{y}{y + x} \right| = -\frac{1}{x} + C").move_to(ORIGIN)

        self.play(Write(step6))
        self.play(Write(eq12))
        self.wait(2)
        self.play(FadeOut(eq12, step6))

        # Step 7: Multiply through by x
        step7 = MathTex(r"\text{Multiply through by } x").to_edge(UP)
        eq13 = MathTex(r"\ln \left| \frac{y}{y + x} \right| = -1 + Cx").move_to(ORIGIN)

        self.play(Write(step7))
        self.play(Write(eq13))
        self.wait(2)
        self.play(FadeOut(eq13, step7))

        # Step 8: Exponentiate both sides
        step8 = MathTex(r"\text{Exponentiate both sides}").to_edge(UP)
        eq14 = MathTex(r"\left| \frac{y}{y + x} \right| = e^{-1 + Cx}").move_to(ORIGIN)

        self.play(Write(step8))
        self.play(Write(eq14))
        self.wait(2)
        self.play(FadeOut(eq14, step8))

        # Step 9: Let C' = e^{-1}
        step9 = MathTex(r"\text{Let } C' = e^{-1}").to_edge(UP)
        eq15 = MathTex(r"\frac{y}{y + x} = C'e^{Cx}").move_to(ORIGIN)

        self.play(Write(step9))
        self.play(Write(eq15))
        self.wait(2)
        self.play(FadeOut(eq15, step9))

        # Step 10: Rearrange to solve for y
        step10 = MathTex(r"\text{Rearrange to solve for } y").to_edge(UP)
        eq16 = MathTex(r"y = C'e^{Cx}(y + x)").move_to(ORIGIN)
        eq17 = MathTex(r"y = C'e^{Cx}y + C'e^{Cx}x").move_to(ORIGIN)
        eq18 = MathTex(r"y(1 - C'e^{Cx}) = C'e^{Cx}x").move_to(ORIGIN)
        eq19 = MathTex(r"y = \frac{C'e^{Cx}x}{1 - C'e^{Cx}}").move_to(ORIGIN)

        self.play(Write(step10))
        self.play(Write(eq16))
        self.wait(2)
        self.play(ReplacementTransform(eq16, eq17))
        self.wait(2)
        self.play(ReplacementTransform(eq17, eq18))
        self.wait(2)
        self.play(ReplacementTransform(eq18, eq19))
        self.wait(2)
        self.play(FadeOut(eq19, step10))
