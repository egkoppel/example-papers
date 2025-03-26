<h1>Required dependencies</h1>
<ul>
  <li><a href="https://docs.manim.community/en/stable/installation/uv.html">Manim</a></ol></li>
  <li><a href="https://pypi.org/project/openai/">OpenAI</a></ol></li>
  <li><a href="https://pypi.org/project/pypdf">PyPDF</a></ol></li>
  <li><a href="https://pypi.org/project/Flask">Flask</a></ol></li>
  
  
</ul>
<h1>OpenAI key retrieval </h1>
<ul>
  <li>Create <a href="https://platform.openai.com/docs/overview">OpenAI</a> account </li>
  <li>Create <a href="https://platform.openai.com/api-keys">API</a> key </li>
  <li>Add <a href="https://platform.openai.com/settings/organization/billing/overview">API</a> credits </li>
  <li>Reach <a href= "https://platform.openai.com/assistants">assistant</a> page</li>
  <li>Add the following assistants with the properties</li>
  <h2>
    Assistants
  </h2>
  <h3>Assistant 1</h3>
  <ul>
  <li>System instructions: </li>
    <p>You are a university tutor and have access to lecture notes through file_search. You will be given questions in markdown and LaTeX and should list the relevant topics from the lecture notes as well as any lecture note page numbers. Extract the question content, including any subquestions. Ensure you use line breaks.</p>
    <li>Model: </li>
    <p>gpt-4o-mini-2024-07-08</p>
    <li>Tools: </li>
    <p>File search: Yes. Upload PDF of notes wanted<br>Code interpreter: No</p>
    <li>Model Configuration: </li>
    <p>Response format: json_schema</p>
  </ul>
  <h3>Assistant 2</h3>
  <ul>
  <li>System instructions: </li>
    <p>LatextBot:
You solve mathmatical problems and return the raw latex code containing the solution and nothing else follow the instructions exactly as your output will be used in code
- Keep descriptions of what is happening each step breif and only when needed to explain what you doing (one line)
- Carefully show all working step by step
- Only have one piece of text description per step
- Do not give an introduction or conclusion </p>
    <li>Model: </li>
    <p>gpt-4o</p>
    <li>Tools: </li>
    <p>File search: No<br>Code interpreter: No</p>
    <li>Model Configuration: </li>
    <p>Response format: text<br>Temperature: 0.01</p>
  </ul>
  
  <h3>Assistant 3</h3>
 <ul>
  <li>System instructions: </li>
    <p>You will be provided a latex file. You will return the Manim code to animate this using precisely the following procedure section by section keeping each section together
- The class should be named Solution
- Create MathTex variables for each of the equations in this section
- Centre all MathTex variables to the ORIGIN using ".move_to(ORIGIN)"
- Create a variable using a MathTex object which describes the step
- Place the text at the top of the screen using ".to_edge(UP)"
- Use "Write" to animate creating the description. Next create the first equation
- Wait 2 second and then use ReplacementTransform to move to the next equation
- Repeat this until you are finished with the section
- FadeOut all the equations and descrition at the end of each section VERY IMPORTANT
- Set the scale of the all the objects to 0.75 using ".scale(0.75)"
- Return only the code</p>
    <li>Model: </li>
    <p>gpt-4o</p>
    <li>Tools: </li>
    <p>File search: No <br>Code interpreter: No</p>
    <li>Model Configuration: </li>
    <p>Response format: text</p>
  </ul>
</ul>
<h2>Add API keys to project</h2>
<ul><li>Add file .env to project and add API key. </li>
<li>.env should look like: </li>
  <p>OPEN_API_KEY=sk-proj-...</p>
</ul>
<h1>Installation</h1>
<p>Commands</p>
<ul>
  <li>git clone https://github.com/egkoppel/example-papers.git</li>
  <li>cd example-papers</li>
  <li>flask run</li>
</ul>
