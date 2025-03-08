from manim import *

class Solution(Scene):
    def construct(self):
        
        df = MathTex("df = y \, dx + x \, dy")
        Write(df)
        FadeOut(df)
        
        function_identification = MathTex("f(x, y) \text{ such that } \\frac{\\partial f}{\\partial x} = y \text{ and } \\frac{\\partial f}{\\partial y} = x")
        Write(function_identification)
        FadeOut(function_identification)
        
        partial_deriv_x = MathTex("\\frac{\\partial f}{\\partial x} = y")
        Write(partial_deriv_x)
        FadeOut(partial_deriv_x)

        partial_deriv_y = MathTex("\\frac{\\partial f}{\\partial y} = x")
        Write(partial_deriv_y)
        FadeOut(partial_deriv_y)
        
        integration_x = MathTex("f(x, y) = yx + g(y)")
        Write(integration_x)
        FadeOut(integration_x)
        
        differentiation_y = MathTex("\\frac{\\partial f}{\\partial y} = x + g'(y)")
        Write(differentiation_y)
        FadeOut(differentiation_y)
        
        arbitrary_function = MathTex("g'(y) = 0 \\implies g(y) = C")
        Write(arbitrary_function)
        FadeOut(arbitrary_function)
        
        general_solution = MathTex("f(x, y) = xy + C")
        Write(general_solution)
        FadeOut(general_solution)

        final_box = MathTex("\\boxed{f(x, y) = xy + C}")
        Write(final_box)
        