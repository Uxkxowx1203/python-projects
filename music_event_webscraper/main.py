import requests
import selectorlib
import smtplib, ssl
import sqlite3

URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

class Event:
    def scrape(self, url):
        response = requests.get(url,headers = HEADERS)
        source = response.text
        return source

    def extract(self, source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)["tours"]
        return value

class Email:
    def send(message):
        host = "smtp.gmail.com"
        port = 465

        username = "anshsharma.as331@gmail.com"
        password = "dsrnsbczjjdchjyj"
        reciever = "anshsharma.as331@gmail.com"
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, reciever, message)
        print("email sent")

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("data.db")
    
    def store(self, extracted):
        row = extracted.split()
        row = [item.strip() for item in row]
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
        self.connection.commit()


    def read(self, extracted):
        row = extracted.split()
        row = [item.strip() for item in row]

        band, city, date = row
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM event band=?, city=? AND date=?, (band,city,date)")
        rows = cursor.fetchall()
        return(rows)

if __name__ == "__main__":
    while True:
        event = Event()
        scraped = event.scrape(URL)
        extracted = event.extract(scraped)
        print(extracted)
        
        if extracted != "No upcoming tours":
            db = Database()
            row = db.read(extracted)
            if not row:
                db.store(extracted)
                email = Email()
                email.send(message = "New event was found")
    time.sleep(5)