# The code defines a MovieTicketSystem class, which simulates a movie ticket booking system. 
# It allows users to book adult and kid tickets for a specific movie, and calculates the total cost based on ticket types and prices.
# The programmer understands basic object-oriented principles, such as using classes, constructors, and methods. 
# This is question 2 of 3 in the final exam. 
class MovieTicketSystem:
    title = ''
    seats = 0
    adult_price = 0.0
    kid_price = 0.0
    def __init__(self, title, seats, adult_price,kid_price):
        self.title = title
        self.seats = seats
        self.adult_price = adult_price
        self.kid_price = kid_price
    def bookTickets(self,adult_tickets,kid_tickets):
        tickets_total = adult_tickets + kid_tickets
        seats_avaliable = tickets_total - self.seats
        if seats_avaliable > 0:
            remaining_seats = seats_avaliable - tickets_total
            total_cost = round(float((adult_tickets * self.adult_price) + (kid_tickets * self.kid_price)),2)
            print('Ticket booked successfully for', self.title)
            print('Adult tickets:',adult_tickets)
            print('Kid tickets',kid_tickets)
            print('Total cost:',total_cost)
            print('Remaining seats',remaining_seats)
        else:
            print('Not enough seats available for your order')
if __name__ == '__main__':
    movie = MovieTicketSystem('The Matrix', 100, 12.0, 8.0)
    print('Welcome to the Movie Ticket Booking System!')
    print('Movie avaliable', movie.title)
    adult_tickets = int(input('Enter the number of adult tickets you want to book: '))
    kid_tickets = int(input('Enter the number of kid tickets you want to book:  '))
    movie.bookTickets(adult_tickets,kid_tickets)
