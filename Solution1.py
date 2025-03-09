
from manim import *

class Solution(Scene):
    def construct(self):
        # Section 1
        step1 = MathTex(r"\text{Given differential equation:}").to_edge(UP).scale(0.75)
        eq1 = MathTex(r"\frac{dy}{dx} + 2xy = 4x").move_to(ORIGIN).scale(0.75)

        self.play(Write(step1))
        self.play(Write(eq1))
        self.wait(2)

        # Section 2
        step2 = MathTex(r"\text{First-order linear differential equation:}").to_edge(UP).scale(0.75)
        eq2 = MathTex(r"\frac{dy}{dx} + P(x)y = Q(x)").move_to(ORIGIN).scale(0.75)

        self.play(ReplacementTransform(step1, step2), ReplacementTransform(eq1, eq2))
        self.wait(2)

        # Section 3
        step3 = MathTex(r"\text{Where } P(x) = 2x \text{ and } Q(x) = 4x").to_edge(UP).scale(0.75)
        eq3 = MathTex(r"P(x) = 2x, \, Q(x) = 4x").move_to(ORIGIN).scale(0.75)

        self.play(ReplacementTransform(step2, step3), ReplacementTransform(eq2, eq3))
        self.wait(2)

        # Section 4
        step4 = MathTex(r"\text{Integrating factor } \mu(x)").to_edge(UP).scale(0.75)
        eq4 = MathTex(r"\mu(x) = e^{\int P(x) \, dx} = e^{\int 2x \, dx}").move_to(ORIGIN).scale(0.75)

        self.play(ReplacementTransform(step3, step4), ReplacementTransform(eq3, eq4))
        self.wait(2)

        # Section 5
        step5 = MathTex(r"\text{Calculate the integral:}").to_edge(UP).scale(0.75)
        eq5 = MathTex(r"\int 2x \, dx = x^2").move_to(ORIGIN).scale(0.75)

        self.play(ReplacementTransform(step4, step5), ReplacementTransform(eq4, eq5))
        self.wait(2)

        # Section 6
        step6 = MathTex(r"\text{Thus, the integrating factor is:}").to_edge(UP).scale(0.75)
        eq6 = MathTex(r"\mu(x) = e^{x^2}").move_to(ORIGIN).scale(0.75)

        self.play(ReplacementTransform(step5, step6), ReplacementTransform(eq5, eq6))
        self.wait(2)

        # Section 7
        step7 = MathTex(r"\text{Multiply the entire equation by } \mu(x)").to_edge(UP).scale(0.75)
        eq7 = MathTex(r"e^{x^2} \frac{dy}{dx} + e^{x^2} \cdot 2xy = e^{x^2} \cdot 4x").move_to(ORIGIN).scale(0.75)

        self.play(ReplacementTransform(step6, step7), ReplacementTransform(eq6, eq7))
        self.wait(2)

        # Section 8
        step8 = MathTex(r"\text{This simplifies to:}").to_edge(UP).scale(0.75)
        eq8 = MathTex(r"\frac{d}{dx}(e^{x^2} y) = 4x e^{x^2}").move_to(ORIGIN).scale(0.75)

        self.play(ReplacementTransform(step7, step8), ReplacementTransform(eq7, eq8))
        self.wait(2)

        # Section 9
        step9 = MathTex(r"\text{Integrate both sides:}").to_edge(UP).scale(0.75)
        eq9 = MathTex(r"\int \frac{d}{dx}(e^{x^2} y) \, dx = \int 4x e^{x^2} \, dx").move_to(ORIGIN).scale(0.75)

        self.play(ReplacementTransform(step8, step9), ReplacementTransform(eq8, eq9))
        self.wait(2)

        # Section 10
        step10 = MathTex(r"\text{The left side becomes:}").to_edge(UP).scale(0.75)
        eq10 = MathTex(r"e^{x^2} y").move_to(ORIGIN).scale(0.75)

        self.play(ReplacementTransform(step9, step10), ReplacementTransform(eq9, eq10))
        self.wait(2)

        # Section 11
        step11 = MathTex(r"\text{For the right side, use substitution:}").to_edge(UP).scale(0.75)
        eq11 = MathTex(r"u = x^2, \, du = 2x \, dx, \, 2 \, du = 4x \, dx").move_to(ORIGIN).scale(0.75)

        self.play(ReplacementTransform(step10, step11), ReplacementTransform(eq10, eq11))
        self.wait(2)

        # Section 12
        step12 = MathTex(r"\text{Integrate:}").to_edge(UP).scale(0.75)
        eq12 = MathTex(r"\int 4x e^{x^2} \, dx = 2 \int e^u \, du = 2e^u + C = 2e^{x^2} + C").move_to(ORIGIN).scale(0.75)

        self.play(ReplacementTransform(step11, step12), ReplacementTransform(eq11, eq12))
        self.wait(2)

        # Section 13
        step13 = MathTex(r"\text{Thus, we have:}").to_edge(UP).scale(0.75)
        eq13 = MathTex(r"e^{x^2} y = 2e^{x^2} + C").move_to(ORIGIN).scale(0.75)

        self.play(ReplacementTransform(step12, step13), ReplacementTransform(eq12, eq13))
        self.wait(2)

        # Section 14
        step14 = MathTex(r"\text{Solve for } y:").to_edge(UP).scale(0.75)
        eq14 = MathTex(r"y = 2 + Ce^{-x^2}").move_to(ORIGIN).scale(0.75)

        self.play(ReplacementTransform(step13, step14), ReplacementTransform(eq13, eq14))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(step14), FadeOut(eq14))
