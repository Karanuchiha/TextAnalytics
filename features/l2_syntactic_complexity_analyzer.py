import requests

def l2_syntactic_complexity_analyze_text(text):
    response = requests.post("http://localhost:1234/l2sca", json={"text": text})
    response_content = response.content
    return response_content
    
print(l2_syntactic_complexity_analyze_text("test 1234"))