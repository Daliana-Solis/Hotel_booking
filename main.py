import pandas as pd

#Make ID column a string
df = pd.read_csv("hotels.csv", dtype={"id":str})


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

    def view_hotels(self):
        pass



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




print(df)
hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)

#If hotel available
if hotel.available():
    hotel.book()
    customer_name = input("Enter your name: ")

    #Call Reservation class  and get confirmation
    reservation_confirm = ReservationConfirmation(customer_name, hotel)
    print(reservation_confirm.generate())

else:
    print("Hotel is not available")