
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
        step3 = MathTex(r"\text{Recognize the left side as the derivative of a product:}").to_edge(UP)
        eq3 = MathTex(r"\frac{d}{dx}(e^{kx} y) = e^{kx} a \sin(mx)").move_to(ORIGIN)
        
        self.play(ReplacementTransform(eq2, eq3), ReplacementTransform(step2, step3))
        self.wait(2)
        
        # Step 4
        step4 = MathTex(r"\text{Integrate both sides with respect to } x:").to_edge(UP)
        eq4 = MathTex(r"e^{kx} y = \int e^{kx} a \sin(mx) \, dx").move_to(ORIGIN)
        
        self.play(ReplacementTransform(eq3, eq4), ReplacementTransform(step3, step4))
        self.wait(2)
        
        # Step 5
        step5 = MathTex(r"\text{Solve the integral on the right side using integration by parts:}").to_edge(UP)
        eq5 = MathTex(r"\int e^{kx} a \sin(mx) \, dx = \frac{a}{m^2 + k^2} \left( m e^{kx} \cos(mx) - k e^{kx} \sin(mx) \right) + C").move_to(ORIGIN)
        
        self.play(ReplacementTransform(eq4, eq5), ReplacementTransform(step4, step5))
        self.wait(2)
        
        # Step 6
        step6 = MathTex(r"\text{Substitute back:}").to_edge(UP)
        eq6 = MathTex(r"e^{kx} y = \frac{a}{m^2 + k^2} \left( m e^{kx} \cos(mx) - k e^{kx} \sin(mx) \right) + C").move_to(ORIGIN)
        
        self.play(ReplacementTransform(eq5, eq6), ReplacementTransform(step5, step6))
        self.wait(2)
        
        # Step 7
        step7 = MathTex(r"\text{Solve for } y:").to_edge(UP)
        eq7 = MathTex(r"y = \frac{a}{m^2 + k^2} \left( m \cos(mx) - k \sin(mx) \right) + Ce^{-kx}").move_to(ORIGIN)
        
        self.play(ReplacementTransform(eq6, eq7), ReplacementTransform(step6, step7))
        self.wait(2)
        
        # Step 8
        step8 = MathTex(r"\text{Apply the boundary condition } y = 1 \text{ when } x = 0:").to_edge(UP)
        eq8 = MathTex(r"1 = \frac{a}{m^2 + k^2} \left( m \cdot 1 - k \cdot 0 \right) + C \cdot 1").move_to(ORIGIN)
        
        self.play(ReplacementTransform(eq7, eq8), ReplacementTransform(step7, step8))
        self.wait(2)
        
        # Step 9
        step9 = MathTex(r"\text{Solve for } C:").to_edge(UP)
        eq9 = MathTex(r"1 = \frac{am}{m^2 + k^2} + C").move_to(ORIGIN)
        eq10 = MathTex(r"C = 1 - \frac{am}{m^2 + k^2}").move_to(ORIGIN)
        
        self.play(ReplacementTransform(eq8, eq9), ReplacementTransform(step8, step9))
        self.wait(2)
        self.play(ReplacementTransform(eq9, eq10))
        self.wait(2)
        
        # Step 10
        step10 = MathTex(r"\text{Substitute } C \text{ back into the solution:}").to_edge(UP)
        eq11 = MathTex(r"y = \frac{a}{m^2 + k^2} \left( m \cos(mx) - k \sin(mx) \right) + \left(1 - \frac{am}{m^2 + k^2}\right) e^{-kx}").move_to(ORIGIN)
        
        self.play(ReplacementTransform(eq10, eq11), ReplacementTransform(step9, step10))
        self.wait(2)
        
        # Fade out
        self.play(FadeOut(eq11), FadeOut(step10))
