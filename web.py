from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '''
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/4.10.38/pdf.min.mjs" type="module"></script>
    <iframe id="pdf-js-viewer" src="/static/pdfjs-4/web/viewer.html?file=/static/L24fullnotesp2.pdf" title="webviewer" frameborder="0" style="width:50%;height:100%"></iframe>
    <div style="display: inline-block; width:50%; float:rifgh">
    <ul>
    <li><a onclick="document.getElementById(&quot;pdf-js-viewer&quot;).contentWindow.PDFViewerApplication.page=1">Page 1</a></li>
    <li><a onclick="document.getElementById(&quot;pdf-js-viewer&quot;).contentWindow.PDFViewerApplication.page=2">Page 2</a></li>
    <li><a onclick="document.getElementById(&quot;pdf-js-viewer&quot;).contentWindow.PDFViewerApplication.page=3">Page 3</a></li>
    </ul>
    </div>
    '''
