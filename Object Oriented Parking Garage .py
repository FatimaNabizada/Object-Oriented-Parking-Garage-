class ParkingGarage:
    def __init__(self, total_tickets, total_parking_spaces):
        self.tickets = list(range(1, total_tickets + 1))
        self.parkingSpaces = list(range(1, total_parking_spaces + 1))
        self.currentTicket = {}

    def takeTicket(self):
        if self.tickets:
            ticket = self.tickets.pop(0)
            space = self.parkingSpaces.pop(0)
            self.currentTicket = {'ticket': ticket, 'space': space, 'paid': False}
            print(f"Ticket {ticket} issued. Park in space {space}.")
        else:
            print("Sorry, the parking garage is full.")

    def payForParking(self):
        if 'ticket' in self.currentTicket:
            amount = input("Enter the amount to pay for parking: ")
            if amount:
                print("Ticket paid. You have 15 minutes to leave.")
                self.currentTicket['paid'] = True
            else:
                print("Payment not provided. Ticket not paid.")

    def leaveGarage(self):
        if self.currentTicket.get('paid'):
            print("Thank you! Have a nice day.")
            self.parkingSpaces.append(self.currentTicket['space'])
            self.tickets.append(self.currentTicket['ticket'])
            self.currentTicket = {}
        else:
            self.payForParking()
            self.leaveGarage()

# Example Usage
if __name__ == "__main__":
    garage = ParkingGarage(total_tickets=10, total_parking_spaces=10)

    while True:
        action = input("Enter '1' to take a ticket, '2' to pay for parking, '3' to leave, or 'q' to quit: ")

        if action == '1':
            garage.takeTicket()
        elif action == '2':
            garage.payForParking()
        elif action == '3':
            garage.leaveGarage()
        elif action.lower() == 'q':
            print("Exiting the parking garage program.")
            break
        else:
            print("Invalid choice. Please enter '1', '2', '3', or 'q'.")
