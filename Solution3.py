
from manim import *

class Solution(Scene):
    def construct(self):
        # Step 1: Introduce change of variables
        step1 = MathTex(r"\text{Introduce change of variables: } v = x + y + 1").to_edge(UP).scale(0.75)
        eq1 = MathTex(r"y = v - x - 1").move_to(ORIGIN).scale(0.75)
        self.play(Write(step1))
        self.play(Write(eq1))
        self.wait(2)

        # Step 2: Derivative transformation
        step2 = MathTex(r"\text{Derivative transformation: } \frac{dy}{dx} = \frac{dv}{dx} - 1").to_edge(UP).scale(0.75)
        eq2 = MathTex(r"\frac{dy}{dx} = \frac{dv}{dx} - 1").move_to(ORIGIN).scale(0.75)
        self.play(ReplacementTransform(eq1, eq2))
        self.play(ReplacementTransform(step1, step2))
        self.wait(2)

        # Step 3: Substitute into original equation
        step3 = MathTex(r"\text{Substitute into original equation: }").to_edge(UP).scale(0.75)
        eq3 = MathTex(r"v^2 \left(\frac{dv}{dx} - 1\right) + v^2 + x^3 = 0").move_to(ORIGIN).scale(0.75)
        self.play(ReplacementTransform(eq2, eq3))
        self.play(ReplacementTransform(step2, step3))
        self.wait(2)

        # Step 4: Simplify the equation
        step4 = MathTex(r"\text{Simplify the equation: }").to_edge(UP).scale(0.75)
        eq4 = MathTex(r"v^2 \frac{dv}{dx} + x^3 = 0").move_to(ORIGIN).scale(0.75)
        self.play(ReplacementTransform(eq3, eq4))
        self.play(ReplacementTransform(step3, step4))
        self.wait(2)

        # Step 5: Separate the variables
        step5 = MathTex(r"\text{Separate the variables: }").to_edge(UP).scale(0.75)
        eq5 = MathTex(r"v^2 dv = -x^3 dx").move_to(ORIGIN).scale(0.75)
        self.play(ReplacementTransform(eq4, eq5))
        self.play(ReplacementTransform(step4, step5))
        self.wait(2)

        # Step 6: Integrate both sides
        step6 = MathTex(r"\text{Integrate both sides: }").to_edge(UP).scale(0.75)
        eq6 = MathTex(r"\int v^2 \, dv = \int -x^3 \, dx").move_to(ORIGIN).scale(0.75)
        self.play(ReplacementTransform(eq5, eq6))
        self.play(ReplacementTransform(step5, step6))
        self.wait(2)

        # Step 7: Calculate the integrals
        step7 = MathTex(r"\text{Calculate the integrals: }").to_edge(UP).scale(0.75)
        eq7 = MathTex(r"\frac{v^3}{3} = -\frac{x^4}{4} + C").move_to(ORIGIN).scale(0.75)
        self.play(ReplacementTransform(eq6, eq7))
        self.play(ReplacementTransform(step6, step7))
        self.wait(2)

        # Step 8: Multiply through by 12
        step8 = MathTex(r"\text{Multiply through by 12: }").to_edge(UP).scale(0.75)
        eq8 = MathTex(r"4v^3 = -3x^4 + 12C").move_to(ORIGIN).scale(0.75)
        self.play(ReplacementTransform(eq7, eq8))
        self.play(ReplacementTransform(step7, step8))
        self.wait(2)

        # Step 9: Substitute back
        step9 = MathTex(r"\text{Substitute back } v = x + y + 1:").to_edge(UP).scale(0.75)
        eq9 = MathTex(r"4(x + y + 1)^3 = -3x^4 + 12C").move_to(ORIGIN).scale(0.75)
        self.play(ReplacementTransform(eq8, eq9))
        self.play(ReplacementTransform(step8, step9))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(eq9), FadeOut(step9))
