
from manim import *

class Solution(Scene):
    def construct(self):
        # Step 1
        step1 = MathTex(r"\text{Identify the integrating factor:}").to_edge(UP)
        eq1 = MathTex(r"\mu(x) = e^{\int k \, dx} = e^{kx}").move_to(ORIGIN)
        self.play(Write(step1))
        self.play(Write(eq1))
        self.wait(2)

        # Step 2
        step2 = MathTex(r"\text{Multiply the entire differential equation by the integrating factor:}").to_edge(UP)
        eq2 = MathTex(r"e^{kx} \frac{dy}{dx} + e^{kx} ky = e^{kx} a \sin(mx)").move_to(ORIGIN)
        self.play(ReplacementTransform(eq1, eq2), ReplacementTransform(step1, step2))
        self.wait(2)

        # Step 3
        step3 = MathTex(r"\text{Recognize the left-hand side as the derivative of a product:}").to_edge(UP)
        eq3 = MathTex(r"\frac{d}{dx}(e^{kx} y) = e^{kx} a \sin(mx)").move_to(ORIGIN)
        self.play(ReplacementTransform(eq2, eq3), ReplacementTransform(step2, step3))
        self.wait(2)

        # Step 4
        step4 = MathTex(r"\text{Integrate both sides with respect to } x:").to_edge(UP)
        eq4 = MathTex(r"e^{kx} y = \int e^{kx} a \sin(mx) \, dx").move_to(ORIGIN)
        self.play(ReplacementTransform(eq3, eq4), ReplacementTransform(step3, step4))
        self.wait(2)

        # Step 5
        step5 = MathTex(r"\text{Solve the integral on the right-hand side using integration by parts:}").to_edge(UP)
        eq5 = MathTex(r"\int e^{kx} a \sin(mx) \, dx = -\frac{a}{m} e^{kx} \cos(mx) - \int -\frac{a}{m} \cos(mx) ke^{kx} \, dx").move_to(ORIGIN)
        self.play(ReplacementTransform(eq4, eq5), ReplacementTransform(step4, step5))
        self.wait(2)

        # Step 6
        step6 = MathTex(r"\text{Solve the remaining integral:}").to_edge(UP)
        eq6 = MathTex(r"\int e^{kx} \cos(mx) \, dx = \frac{e^{kx}(k \cos(mx) + m \sin(mx))}{k^2 + m^2}").move_to(ORIGIN)
        self.play(ReplacementTransform(eq5, eq6), ReplacementTransform(step5, step6))
        self.wait(2)

        # Step 7
        step7 = MathTex(r"\text{Substitute back:}").to_edge(UP)
        eq7 = MathTex(r"e^{kx} y = -\frac{a}{m} e^{kx} \cos(mx) + \frac{a}{k^2 + m^2} e^{kx} (k \cos(mx) + m \sin(mx)) + C").move_to(ORIGIN)
        self.play(ReplacementTransform(eq6, eq7), ReplacementTransform(step6, step7))
        self.wait(2)

        # Step 8
        step8 = MathTex(r"\text{Simplify:}").to_edge(UP)
        eq8 = MathTex(r"e^{kx} y = \frac{a}{k^2 + m^2} e^{kx} (k \cos(mx) + m \sin(mx)) + C").move_to(ORIGIN)
        self.play(ReplacementTransform(eq7, eq8), ReplacementTransform(step7, step8))
        self.wait(2)

        # Step 9
        step9 = MathTex(r"\text{Solve for } y:").to_edge(UP)
        eq9 = MathTex(r"y = \frac{a}{k^2 + m^2} (k \cos(mx) + m \sin(mx)) + Ce^{-kx}").move_to(ORIGIN)
        self.play(ReplacementTransform(eq8, eq9), ReplacementTransform(step8, step9))
        self.wait(2)

        # Step 10
        step10 = MathTex(r"\text{Apply the boundary condition } y(0) = 1:").to_edge(UP)
        eq10 = MathTex(r"1 = \frac{a}{k^2 + m^2} (k \cdot 1 + m \cdot 0) + C").move_to(ORIGIN)
        self.play(ReplacementTransform(eq9, eq10), ReplacementTransform(step9, step10))
        self.wait(2)

        # Step 11
        step11 = MathTex(r"\text{Solve for } C:").to_edge(UP)
        eq11 = MathTex(r"1 = \frac{ak}{k^2 + m^2} + C").move_to(ORIGIN)
        eq11_2 = MathTex(r"C = 1 - \frac{ak}{k^2 + m^2}").move_to(ORIGIN)
        self.play(ReplacementTransform(eq10, eq11), ReplacementTransform(step10, step11))
        self.wait(2)
        self.play(ReplacementTransform(eq11, eq11_2))
        self.wait(2)

        # Step 12
        step12 = MathTex(r"\text{Substitute } C \text{ back into the solution:}").to_edge(UP)
        eq12 = MathTex(r"y = \frac{a}{k^2 + m^2} (k \cos(mx) + m \sin(mx)) + \left(1 - \frac{ak}{k^2 + m^2}\right) e^{-kx}").move_to(ORIGIN)
        self.play(ReplacementTransform(eq11_2, eq12), ReplacementTransform(step11, step12))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(eq12), FadeOut(step12))
