import json
import subprocess
from services.execute_query_service import execute_query

from flask import Flask, render_template, request
app = Flask("app")


@app.route('/')
def home():
   return render_template('index.html')

@app.route("/sparql", methods=['GET'])
def get_query():
    args = request.args
    query = args.get('query')
    results = execute_query(query)
    return results

if __name__ == '__main__':
    banner = """
 _____  _____  _____  _____  _____  __       _____         _                 _           _    _____            _           
|   __||  _  ||  _  || __  ||     ||  |     |   __| ___  _| | ___  ___  ___ | |_  ___  _| |  |   __| ___  ___ |_| ___  ___ 
|__   ||   __||     ||    -||  |  ||  |__   |   __|| -_|| . || -_||  _|| .'||  _|| -_|| . |  |   __||   || . || ||   || -_|
|_____||__|   |__|__||__|__||__  _||_____|  |__|   |___||___||___||_|  |__,||_|  |___||___|  |_____||_|_||_  ||_||_|_||___|
                               |__|                                                                      |___|   v0.0.2          
      © Ontology Engineering Group at Universidad Politéctnica de Madrid
      	Authors: Salvador González Gerpe
"""
    
    print(banner)
    app.run(debug=True, host="0.0.0.0", port=5005)