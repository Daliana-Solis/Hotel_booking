import pandas as pd


df = pd.read_csv("hotels.csv")
class Hotel:

    def __int__(self, hotel_id):
        self.hotel_id = hotel_id

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
        content = f"Name of the customer hotel"
        return content


print(df)

hotel_id = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_id)

#If hotel available
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")

    #Call Reservation class  and get confirmation
    reservation_confirm = ReservationConfirmation(name, hotel)
    print(reservation_confirm.generate())

else:
    print("Hotel is not available")