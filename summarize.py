from openai import OpenAI
import pypdf
import dotenv

dotenv.load_dotenv()

def main(pdf_path):
    lecture_notes = ""
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        reader = pypdf.PdfReader(file)
        # Loop through all the pages and extract text
        for page_number,page in enumerate(reader.pages):
            page_text = page.extract_text()
            if page_text:  # Check if text is found on the page
                lecture_notes += f"======{page_number}======"
                lecture_notes += page_text

    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.01,
        messages=[
            {"role": "developer", "content": "You are a helpful assistant who is being asked by a lecturer to summarise their lecture notes. When asked, only provide the summary of each page, and do not include any messages before or after the content."},
            {
                "role": "user",
                "content": """Here are some pages of lecture notes, where each new page is denoted by the sequence ======N====== where N is the page number of the new page. Provide a brief list of the content on each page, combining consecutive pages into one page where they share similar content. Output in the same format as the input, but use ======N-M====== to denote a range of pages.

======0====== Natural Sciences Tripos, Part IA Lent Term 2024 Mathematical Methods II, Course B Prof Natalia Berloﬀ Section 2 ======1====== Natural Sciences Tripos, Part IA · Lent Term 2023 Mathematical Methods II, Course B · Prof Natalia Berloﬀ 2 FUNCTIONS OF MORE THAN ONE VARIABLE 2.1 Introduction Functions of more than one variable are frequently encountered in scientiﬁc applications when we think about quantities that vary in more than one direction in space, or that vary in space and time. The temperature in this room is an example of a scalar ﬁeld . Its value is a real number (when expressed in some units such as degrees Celsius) that depends on three spatial coordinates x, y and z (and also time t). If we wanted to construct a theory of how the temperature evolves in space and time, involving processes such as thermal conduction, we would ﬁrst need to understand how to do calculus in more than one variable. How do we deﬁne the temperature gradient when the temperature depends on three spatial coordinates? How do we ﬁnd the points of minimum and maximum temperature? These and related questions are answered in this section of the course. 1 ======2====== 2.2 Partial diﬀerentiation 2.2.1 Ordinary derivative A function f ( x) of one variable x, where x and f are both real numbers, can be visualized as the curve y = f ( x) in the ( x,y ) plane, which is known as the graph of the function. y=f(x) x x+h h f(x+h)-f(x) f(x) f(x+h) y The (ordinary) derivative of the function is deﬁned by d f d x = f ′( x) = lim h→0 [ f ( x + h) − f ( x) h ] . Thus d f/ d x is the limiting value of the ratio δf/δx of small increments in the function and its argument. The function is said to be diﬀerentiable at the point x if this limit exists. 2 ======3====== d f/ d x is the local rate of change of the function f ( x) with the variable x. Geometrically, it is the local gradient of the curve y = f ( x), i.e. the gradient of the straight line that is tangent to the curve at the point x. The derivative provides the best linear approximation to the function near the point considered. 2.2.2 Partial derivatives A function f ( x,y ) of two variables x and y, where x, y and f are all real numbers, can be visualized as the surface z = f ( x,y ) in the ( x,y,z ) space, which is also known as the graph of the function. Another way to visualize the function is to plot a selection of contour lines f ( x,y ) = constant in the ( x,y ) plane. This is equivalent to ﬁnding the intersection of the surface z = f ( x,y ) with a selection of horizontal planes z = constant. (Usually, equally spaced contour values are used.) 3 ======4====== -2.5 -2 -1.5 -1 -0.5 0 0.5 1 1.5 2 2.5 -2.5 -2 -1.5 -1 -0.5 0 0.5 1 1.5 2 2.5 z1 z3z10 The partial derivatives of the function are deﬁned by ∂f ∂x = fx = lim h→0 [ f ( x + h,y ) − f ( x,y ) h ] , ∂f ∂y = fy = lim h→0 [ f ( x,y + h) − f ( x,y ) h ] . Therefore ∂f/∂x is the rate of change of f with x at constant y, while ∂f/∂y is the rate of change of f with y at constant x. The fact that two diﬀerent derivatives exist reﬂects the fact that f depends on two independent variables. Holding y at a particular constant value means that f ( x,y ) becomes eﬀectively a function of one variable only. The ordinary derivative of this function is exactly the same as the partial derivative ∂f/∂x . ∂f/∂x is the local gradient of the surface z = f ( x,y ) when travelling in the x-direction, while ∂f/∂y is the gradient when travelling in the y-direction. These are the gradients of straight lines that are 4 ======5====== tangent to the surface and perpendicular to the y- and x-axes, respectively. Together, these two gradients deﬁne the orientation of the tangent plane , which is the best linear approximation to the surface near the point considered. Other notations used for partial derivatives are ∂f ∂x = ( ∂f ∂x ) y = fx = f,x = ∂xf. We will use the ﬁrst three. The notation ( ∂f ∂x ) y or ∂f ∂x ⏐ ⏐ ⏐ ⏐ y states explicitly which variable (in this case y) is held constant while carrying out the derivative. This notation is particularly useful when changing independent variables, e.g. from ( x,y ) to ( x,v ), where v 5
======6====== can be expressed as a function of x and y. In such cases there is a very important distinction between( ∂f ∂x ) y and ( ∂f ∂x ) v (see Section 2.2.8 later). The use of a subscript to denote diﬀerentiation, as in fx, is compact but potentially ambiguous; we may want to use a subscript to denote a component of a vector, or for some other purpose. ∂ is sometimes pronounced ‘del’ rather than ‘dee’ to distinguish it from the ordinary diﬀerential operator d. A vector can be formed with x and y components equal to fx and fy . This vector is called the gradient of f and may be written as grad f = ∇ f = ( ∂f ∂x , ∂f ∂y ) = i ∂f ∂x + j ∂f ∂y . The symbol ∇ = ( ∂ ∂x , ∂ ∂y ) = i ∂ ∂x + j ∂ ∂y is the gradient operator , a vector diﬀerential operator. It is pronounced ‘grad’, ‘del’ or ‘nabla’. Like the diﬀerential operator d d x , it acts on whatever is written to the right of it. 6 ======7====== 2.2.3 Second derivatives Second derivatives can be deﬁned by repeated partial diﬀerentiation: ∂2 f ∂x 2 = fxx = ∂ ∂x ( ∂f ∂x ) , ∂2 f ∂y 2 = fyy = ∂ ∂y ( ∂f ∂y ) , ∂2 f ∂y∂x = fxy = ∂ ∂y ( ∂f ∂x ) , ∂2 f ∂x∂y = fyx = ∂ ∂x ( ∂f ∂y ) . While the ﬁrst two of these just mean the second derivative of f with respect to one variable while the other is held constant, the last two mean something diﬀerent and are known as mixed partial derivatives . 7 ======8====== Example : f ( x,y ) = e −x2 −y2 ∂f ∂x = fx = −2 x e −x2 −y2 ∂f ∂y = fy = −2 y e −x2 −y2 ∂2 f ∂x 2 = fxx = ∂ ∂x ( −2 x e −x2 −y2 ) = ( −2 + 4 x2 ) e −x2 −y2 ∂2 f ∂y 2 = fyy = ∂ ∂y ( −2 y e −x2 −y2 ) = ( −2 + 4 y2 ) e −x2 −y2 ∂2 f ∂y∂x = fxy = ∂ ∂y ( −2 x e −x2 −y2 ) = 4 xy e −x2 −y2 ∂2 f ∂x∂y = fyx = ∂ ∂x ( −2 y e −x2 −y2 ) = 4 xy e −x2 −y2 Example : f ( x,y ) = 1 x + y2 ∂f ∂x = fx = − 1 ( x + y2 ) 2 ∂f ∂y = fy = − 2 y ( x + y2 ) 2 8 ======9====== ∂2 f ∂x 2 = fxx = ∂ ∂x [ − 1 ( x + y2 ) 2 ] = 2 ( x + y2 ) 3 ∂2 f ∂y 2 = fyy = ∂ ∂y [ − 2 y ( x + y2 ) 2 ] = − 2 ( x + y2 ) 2 + 8 y2 ( x + y2 ) 3 ∂2 f ∂y∂x = fxy = ∂ ∂y [ − 1 ( x + y2 ) 2 ] = 4 y ( x + y2 ) 3 ∂2 f ∂x∂y = fyx = ∂ ∂x [ − 2 y ( x + y2 ) 2 ] = 4 y ( x + y2 ) 3 In both examples we observe the symmetry of mixed partial derivatives ∂ ∂y ( ∂f ∂x ) = ∂ ∂x ( ∂f ∂y ) . This important property holds for all functions (provided that certain smoothness properties are satisﬁed). We are therefore free to use any of the following notation: ∂2 f ∂x∂y = ∂2 f ∂y∂x = fxy = fyx . 9 ======10====== To see where this property comes from, let a = f ( x,y ) , b = f ( x + h,y ) , c = f ( x,y + k) , d = f ( x + h,y + k) . From the deﬁnition, ∂2 f ∂y∂x = lim k→0 1 k [ lim h→0 ( d − c h ) − lim h→0 ( b − a h )] while ∂2 f ∂x∂y = lim h→0 1 h [ lim k→0 ( d − b k ) − lim k→0 ( c − a k )] . In both cases, therefore, we are interested in the limit of d − c − b + a hk as both h and k tend to zero. For suﬃciently smooth functions f it can be shown that these two double limits produce the same answer. 10"""
            },
            {
                "role": "assistant",
                "content": """======0======
Natural Sciences Tripos Mathematical Methods
======1======
Introduction to functions of more than one variable
======2-6======
Ordinary and partial derivatives
Contour lines
======7-10======
Second partial derivatives"""
            },
            {
                "role": "user",
                "content": f"""Here are some pages of lecture notes, where each new page is denoted by the sequence ======N====== where N is the page number of the new page. Provide a brief list of the content on each page, combining consecutive pages into one page where they share similar content. Output in the same format as the input, but use ======N-M====== to denote a range of pages.\n\n{lecture_notes}"""
            }
        ]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content


if __name__ == "__main__":
    print(main("static/L24fullnotesp2.pdf"))
