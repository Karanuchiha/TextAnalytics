import requests
import json
import pandas as pd
from io import StringIO

def l2_syntactic_complexity_analyze_text(text):
    response = requests.post("http://localhost:1234/l2sca", json={"text": text})
    response_content = json.loads(response.content)['response']

    contentIO = StringIO(response_content)
    csv = pd.read_csv(contentIO)

    l2sca_dictionary = dict()
    for col in csv.columns:
        if(col == 'Filename'):
            continue
        l2sca_dictionary[col] = csv[col][0]

    return l2sca_dictionary

