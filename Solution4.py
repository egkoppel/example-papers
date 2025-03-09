
from manim import *

class Solution(Scene):
    def construct(self):
        # Step 1
        step1 = MathTex(r"\text{Change of Variables: Let } v = y^{-4}. \text{ Then } y = v^{-1/4}.").to_edge(UP).scale(0.75)
        eq1 = MathTex(r"v = y^{-4}").move_to(ORIGIN).scale(0.75)
        eq2 = MathTex(r"y = v^{-1/4}").move_to(ORIGIN).scale(0.75)

        self.play(Write(step1))
        self.play(Write(eq1))
        self.wait(2)
        self.play(ReplacementTransform(eq1, eq2))
        self.wait(2)
        self.play(FadeOut(step1, eq2))

        # Step 2
        step2 = MathTex(r"\text{Differentiate } v \text{ with respect to } x:").to_edge(UP).scale(0.75)
        eq3 = MathTex(r"\frac{dv}{dx} = -4y^{-5}\frac{dy}{dx}").move_to(ORIGIN).scale(0.75)

        self.play(Write(step2))
        self.play(Write(eq3))
        self.wait(2)
        self.play(FadeOut(step2, eq3))

        # Step 3
        step3 = MathTex(r"\text{Substitute } \frac{dy}{dx} \text{ from the original equation:}").to_edge(UP).scale(0.75)
        eq4 = MathTex(r"\frac{dy}{dx} = y + xy^5").move_to(ORIGIN).scale(0.75)

        self.play(Write(step3))
        self.play(Write(eq4))
        self.wait(2)
        self.play(FadeOut(step3, eq4))

        # Step 4
        step4 = MathTex(r"\text{Substitute } y = v^{-1/4} \text{ and } \frac{dy}{dx} \text{ into the equation:}").to_edge(UP).scale(0.75)
        eq5 = MathTex(r"-\frac{1}{4}v^{-5/4}\frac{dv}{dx} = v^{-1/4} + x").move_to(ORIGIN).scale(0.75)

        self.play(Write(step4))
        self.play(Write(eq5))
        self.wait(2)
        self.play(FadeOut(step4, eq5))

        # Step 5
        step5 = MathTex(r"\text{Multiply through by } -4v^{5/4}:").to_edge(UP).scale(0.75)
        eq6 = MathTex(r"\frac{dv}{dx} = -4v + 4xv^{5/4}").move_to(ORIGIN).scale(0.75)

        self.play(Write(step5))
        self.play(Write(eq6))
        self.wait(2)
        self.play(FadeOut(step5, eq6))

        # Step 6
        step6 = MathTex(r"\text{Rearrange to form a linear differential equation:}").to_edge(UP).scale(0.75)
        eq7 = MathTex(r"\frac{dv}{dx} + 4v = 4xv^{5/4}").move_to(ORIGIN).scale(0.75)

        self.play(Write(step6))
        self.play(Write(eq7))
        self.wait(2)
        self.play(FadeOut(step6, eq7))

        # Step 7
        step7 = MathTex(r"\text{Integrating Factor:}").to_edge(UP).scale(0.75)
        eq8 = MathTex(r"e^{\int 4 \, dx} = e^{4x}").move_to(ORIGIN).scale(0.75)

        self.play(Write(step7))
        self.play(Write(eq8))
        self.wait(2)
        self.play(FadeOut(step7, eq8))

        # Step 8
        step8 = MathTex(r"\text{Multiply through by the integrating factor:}").to_edge(UP).scale(0.75)
        eq9 = MathTex(r"e^{4x}\frac{dv}{dx} + 4e^{4x}v = 4xe^{4x}v^{5/4}").move_to(ORIGIN).scale(0.75)

        self.play(Write(step8))
        self.play(Write(eq9))
        self.wait(2)
        self.play(FadeOut(step8, eq9))

        # Step 9
        step9 = MathTex(r"\text{Left side becomes the derivative of a product:}").to_edge(UP).scale(0.75)
        eq10 = MathTex(r"\frac{d}{dx}(e^{4x}v) = 4xe^{4x}v^{5/4}").move_to(ORIGIN).scale(0.75)

        self.play(Write(step9))
        self.play(Write(eq10))
        self.wait(2)
        self.play(FadeOut(step9, eq10))

        # Step 10
        step10 = MathTex(r"\text{Integrate both sides:}").to_edge(UP).scale(0.75)
        eq11 = MathTex(r"e^{4x}v = \int 4xe^{4x}v^{5/4} \, dx").move_to(ORIGIN).scale(0.75)

        self.play(Write(step10))
        self.play(Write(eq11))
        self.wait(2)
        self.play(FadeOut(step10, eq11))

        # Step 11
        step11 = MathTex(r"\text{Solve the integral:}").to_edge(UP).scale(0.75)
        eq12 = MathTex(r"\text{This integral is complex and requires substitution or numerical methods.}").move_to(ORIGIN).scale(0.75)

        self.play(Write(step11))
        self.play(Write(eq12))
        self.wait(2)
        self.play(FadeOut(step11, eq12))

        # Step 12
        step12 = MathTex(r"\text{Back-substitute } v = y^{-4}:").to_edge(UP).scale(0.75)
        eq13 = MathTex(r"\text{Once } v(x) \text{ is found, substitute back to find } y(x) = v(x)^{-1/4}.").move_to(ORIGIN).scale(0.75)

        self.play(Write(step12))
        self.play(Write(eq13))
        self.wait(2)
        self.play(FadeOut(step12, eq13))
