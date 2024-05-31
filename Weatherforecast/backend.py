API_KEY="e928426bf0a7543e2868931f88e42619"
import requests

def get_days(place, forecast_days,kind):
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response=requests.get(url)
    data=response.json()
    filtered_data=data["list"]
    nr_values=8*forecast_days
    filtered_data=filtered_data[:nr_values]
 
          
    return filtered_data


if __name__=="__main__":
    a=get_days("delhi",2,"sky")
    print(a)
