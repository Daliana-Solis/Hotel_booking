import pandas as pd

#Make ID column a string
df = pd.read_csv("hotels.csv", dtype={"id":str})

df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_card_security = pd.read_csv("card_security.csv", dtype=str)

class Hotel:
    def __init__(self, hotel_ID):
        self.hotel_id = hotel_ID
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def available(self):
        """Checks if hotel is available """
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()

        if availability == "yes":
            return True
        else:
            return False

    def book(self):
        """Books hotel by changing availability status to no """
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        #updates the CSV file
        df.to_csv("hotels.csv", index=False)


class ReservationConfirmation:
    def __init__(self, customer_name,  hotel):
        self.customer_name = customer_name
        self.hotel = hotel

    def generate(self):
        content = f"""
        Thank you for your reservation! 
        Here is your booking data:
        
        Name: {self.customer_name}
        Hotel Name: {self.hotel.name}
        """
        return content

class CreditCard:
    def __init__(self, card_num):
        self.num = card_num

    def validate(self, exp_date, cvs, name):
        card_info = {"number": self.num, "expiration": exp_date,
                     "holder": name, "cvc": cvs}

        if card_info in df_cards:
            return True
        return False

class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_card_security.loc[df_card_security["number"] == self.num, "password"].squeeze()
        if password == given_password:
            return True
        return False


print(df)

#Get ID user wants to book
hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)

#If hotel available, book
if hotel.available():

    credit_card = SecureCreditCard('1234567890123456')

    #If valid credit card, then process with booking
    if credit_card.validate('12/26', '123', 'JOHN SMITH'):

        if credit_card.authenticate('mypass'):
            hotel.book()
            customer_name = input("Enter your name: ")

            #Call Reservation class  and get confirmation
            reservation_confirm = ReservationConfirmation(customer_name, hotel)
            print(reservation_confirm.generate())
        else:
            print("Credit card authentication failed.")

    else:
        print("There was a problem with your payment.")

else:
    print("Hotel is not available")