import json, requests

def get_data():
    url = "https://api.open-meteo.com/v1/forecast?latitude=39.77&longitude=-74.26&hourly=temperature_2m"
    
    resp = requests.get(url)
    json_object = json.dumps(resp.text, indent=4)

    with open("sample.json", "w") as outfile:
        outfile.write(json_object)

get_data()
