import pandas as pd
df=pd.read_csv("/home/test/Desktop/python/hotel-booking/hotels.csv",dtype={"id":str})
df_cards=pd.read_csv("/home/test/Desktop/python/hotel-booking/cards.csv",dtype=str).to_dict(orient="records")
df_sec=pd.read_csv("/home/test/Desktop/python/hotel-booking/card_security.csv",dtype=str)


class Hotel:
    def __init__(self,id):
        self.id=id
        self.name=df.loc[df["id"]==self.id, "name"].squeeze()
    def book(self):
        availabilty=df.loc[df["id"]==self.id, "available"]="no"
        df.to_csv("/home/test/Desktop/python/hotel-booking/hotels.csv",index=False)
    def available(self):
        availabilty=df.loc[df["id"]==self.id, "available"].squeeze()
        print(availabilty)
        if availabilty=="yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self,customer_name,hotel_object):
        self.customer_name=customer_name
        self.hotel=hotel_object
    def generate(self):
        content=f"""
    Thank you for the reservation!
    Here is your booking data:
    Name: {self.customer_name}
    Hotel Name: {self.hotel.name}    
    """
        return content


class CreditCard:
    def __init__(self,number):
        self.number=number
    def validate(self,expiration,holder,cvc):
        card_data={"number": self.number,"expiration": expiration,
                   "holder": holder,"cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False
        

class SecureCreditCard(CreditCard):
    def authenticate(self,given_pass):
        password=df_sec.loc[df_sec["number"]==self.number, "password"].squeeze()
        if password==given_pass:
            return True
        else:
            return False


print(df)
id=input("Enter the ID of the hotel")
hotel=Hotel(id)
if hotel.available():
    credit_card=SecureCreditCard(number="1234")
    if credit_card.validate(expiration="12/26",holder="JOHN SMITH",cvc="123"):
        if credit_card.authenticate(given_pass="mypass"):    
            hotel.book()
            name=input("Enter your name")
            reservation=ReservationTicket(customer_name=name,hotel_object=hotel)
            print(reservation.generate())
        else:
            print("Card authentication failed")
    else:
        print("Payment error...")
else:
    print("Hotel is not free")