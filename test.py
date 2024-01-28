
def speeding_ticket(speed, is_birthday):
    # Your code goes here
    # Implement the logic based on the driver's speed and birthday condition
    while not is_birthday:
        if speed < 60:
            return "No Ticket"
        elif speed>61 and speed<=80:
            return "Small Ticket"
        else:
            if speed >81:
                return "Big Ticket"


    return speeding_ticket(speed-5,True)



# Test cases
print(speeding_ticket(60, False))  # Expected output: "No Ticket"
print(speeding_ticket(75, False))  # Expected output: "Small Ticket"
print(speeding_ticket(85, False))  # Expected output: "Big Ticket"
print(speeding_ticket(65, True))  # Expected output: "No Ticket"
print(speeding_ticket(85, True))  # Expected output: "Small Ticket"


