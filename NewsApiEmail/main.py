import requests
from send_email import send_email
url="https://newsapi.org/v2/everything?q=tesla&from=2024-01-21&sortBy=publishedAt&apiKey=fcea6295107d4128a6ec92665960cce4&language=en"
api_key="fcea6295107d4128a6ec92665960cce4"

request=requests.get(url)

content=request.json()
body=""

for i in content["articles"] :
    if  (i["title"] and i["description"]) is not None:
        body=i["title"]+"\n" +i["description"]+2*"\n"

    
body=body.encode("utf-8")
send_email(message=body)
