# -*- coding: utf-8 -*-

from flask import *
from analyze import AnalyzeCorner

app=Flask(__name__)

@app.route("/")
def Index():
    return render_template('index.html')

@app.route("/analyze", methods=['POST'])
def Analyza():
    req=request.get_data()
    return '/'.join(AnalyzeCorner(str(req)))

if __name__=="__main__":
    app.run("0.0.0.0",debug=False)
