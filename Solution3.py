
from manim import *

class Solution(Scene):
    def construct(self):
        # Step 1
        step1 = MathTex(r"\text{Identify the integrating factor:}").to_edge(UP)
        eq1 = MathTex(r"\mu(x) = e^{\int k \, dx} = e^{kx}").move_to(ORIGIN)
        self.play(Write(step1))
        self.play(Write(eq1))
        self.wait(2)
        self.play(FadeOut(eq1, step1))

        # Step 2
        step2 = MathTex(r"\text{Multiply the entire differential equation by the integrating factor:}").to_edge(UP)
        eq2 = MathTex(r"e^{kx} \frac{dy}{dx} + e^{kx} ky = e^{kx} a \sin(mx)").move_to(ORIGIN)
        self.play(Write(step2))
        self.play(Write(eq2))
        self.wait(2)
        self.play(FadeOut(eq2, step2))

        # Step 3
        step3 = MathTex(r"\text{Recognize the left-hand side as the derivative of a product:}").to_edge(UP)
        eq3 = MathTex(r"\frac{d}{dx}(e^{kx} y) = e^{kx} a \sin(mx)").move_to(ORIGIN)
        self.play(Write(step3))
        self.play(Write(eq3))
        self.wait(2)
        self.play(FadeOut(eq3, step3))

        # Step 4
        step4 = MathTex(r"\text{Integrate both sides with respect to } x:").to_edge(UP)
        eq4 = MathTex(r"e^{kx} y = \int e^{kx} a \sin(mx) \, dx").move_to(ORIGIN)
        self.play(Write(step4))
        self.play(Write(eq4))
        self.wait(2)
        self.play(FadeOut(eq4, step4))

        # Step 5
        step5 = MathTex(r"\text{Solve the integral on the right-hand side using integration by parts:}").to_edge(UP)
        eq5 = MathTex(r"\int e^{kx} a \sin(mx) \, dx = -\frac{a}{m} e^{kx} \cos(mx) + \frac{a k}{m} \int e^{kx} \cos(mx) \, dx").move_to(ORIGIN)
        self.play(Write(step5))
        self.play(Write(eq5))
        self.wait(2)
        self.play(FadeOut(eq5, step5))

        # Step 6
        step6 = MathTex(r"\text{Solve the second integral using integration by parts again:}").to_edge(UP)
        eq6 = MathTex(r"\int e^{kx} \cos(mx) \, dx = \frac{1}{m} e^{kx} \sin(mx) - \frac{k}{m} \int e^{kx} \sin(mx) \, dx").move_to(ORIGIN)
        self.play(Write(step6))
        self.play(Write(eq6))
        self.wait(2)
        self.play(FadeOut(eq6, step6))

        # Step 7
        step7 = MathTex(r"\text{Substitute back and solve for the integral:}").to_edge(UP)
        eq7 = MathTex(r"I = -\frac{a}{m} e^{kx} \cos(mx) + \frac{a k}{m^2} e^{kx} \sin(mx) - \frac{a k^2}{m^2} \int e^{kx} \sin(mx) \, dx").move_to(ORIGIN)
        self.play(Write(step7))
        self.play(Write(eq7))
        self.wait(2)
        self.play(FadeOut(eq7, step7))

        # Step 8
        step8 = MathTex(r"\text{Solve for } I:").to_edge(UP)
        eq8 = MathTex(r"I = \frac{-\frac{a}{m} e^{kx} \cos(mx) + \frac{a k}{m^2} e^{kx} \sin(mx)}{1 + \frac{a k^2}{m^2}}").move_to(ORIGIN)
        self.play(Write(step8))
        self.play(Write(eq8))
        self.wait(2)
        self.play(FadeOut(eq8, step8))

        # Step 9
        step9 = MathTex(r"\text{Substitute back to find } y:").to_edge(UP)
        eq9 = MathTex(r"e^{kx} y = \frac{-\frac{a}{m} e^{kx} \cos(mx) + \frac{a k}{m^2} e^{kx} \sin(mx)}{1 + \frac{a k^2}{m^2}} + C").move_to(ORIGIN)
        self.play(Write(step9))
        self.play(Write(eq9))
        self.wait(2)
        self.play(FadeOut(eq9, step9))

        # Step 10
        step10 = MathTex(r"\text{Solve for } y:").to_edge(UP)
        eq10 = MathTex(r"y = \frac{-\frac{a}{m} \cos(mx) + \frac{a k}{m^2} \sin(mx)}{1 + \frac{a k^2}{m^2}} + Ce^{-kx}").move_to(ORIGIN)
        self.play(Write(step10))
        self.play(Write(eq10))
        self.wait(2)
        self.play(FadeOut(eq10, step10))

        # Step 11
        step11 = MathTex(r"\text{Apply the boundary condition } y(0) = 1:").to_edge(UP)
        eq11 = MathTex(r"1 = \frac{-\frac{a}{m}}{1 + \frac{a k^2}{m^2}} + C").move_to(ORIGIN)
        self.play(Write(step11))
        self.play(Write(eq11))
        self.wait(2)
        self.play(FadeOut(eq11, step11))

        # Step 12
        step12 = MathTex(r"\text{Substitute } C \text{ back into the solution:}").to_edge(UP)
        eq12 = MathTex(r"y = \frac{-\frac{a}{m} \cos(mx) + \frac{a k}{m^2} \sin(mx)}{1 + \frac{a k^2}{m^2}} + \left(1 + \frac{\frac{a}{m}}{1 + \frac{a k^2}{m^2}}\right)e^{-kx}").move_to(ORIGIN)
        self.play(Write(step12))
        self.play(Write(eq12))
        self.wait(2)
        self.play(FadeOut(eq12, step12))
