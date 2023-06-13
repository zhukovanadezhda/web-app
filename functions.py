import requests

def call_wiki(req):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": req,
        "prop": "extracts",
        "exintro": True,
        "explaintext": True
    }

    response = requests.get(url, params=params)
    data = response.json()

    page_id = next(iter(data["query"]["pages"]))
    content = data["query"]["pages"][page_id]
    #["extract"]

    return content