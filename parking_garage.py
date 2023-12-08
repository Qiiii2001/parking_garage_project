class ParkingGarage:
    def __init__(self):
        self.tickets = [i for i in range(1, 101)]  # Assuming 100 tickets/spaces
        self.parkingSpaces = [i for i in range(1, 101)]
        self.currentTicket = {}

    def takeTicket(self):
        if len(self.tickets) > 0:
            ticket_number = self.tickets.pop()
            self.parkingSpaces.pop()
            self.currentTicket[ticket_number] = {'paid': False}
            print(f"Ticket number {ticket_number} taken. Please park your car.")
        else:
            print("Sorry, no tickets available.")

    def payForParking(self):
        ticket_number = int(input("Enter your ticket number: "))
        if ticket_number in self.currentTicket and not self.currentTicket[ticket_number]['paid']:
            input("Please enter payment amount: ")
            self.currentTicket[ticket_number]['paid'] = True
            print("Your ticket has been paid. You have 15 minutes to leave.")
        else:
            print("Invalid ticket number or ticket already paid.")

    def leaveGarage(self):
        ticket_number = int(input("Please enter your ticket number again: "))
        if ticket_number in self.currentTicket:
            if self.currentTicket[ticket_number]['paid']:
                print("Thank you, have a nice day!")
                self.parkingSpaces.append(ticket_number)
                self.tickets.append(ticket_number)
            else:
                print("Your ticket has not been paid. Please pay for your parking.")
                self.payForParking()
        else:
            print("Invalid ticket number.")
    
    def runGarage(self):
        while True:
            action = input("\nWhat would you like to do? [take/pay/leave/quit]: ").lower()
            if action == "take":
                self.takeTicket()
            elif action == "pay":
                self.payForParking()
            elif action == "leave":
                self.leaveGarage()
            elif action == "quit":
                print("Thank you for using the Parking Garage!")
                break
            else:
                print("Invalid action. Please choose again.")

garage = ParkingGarage()
garage.runGarage()


