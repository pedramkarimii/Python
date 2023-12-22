"""
This project is for billet sales
It has an administrator who only has access to the system
has an event that (name, number of tickets, date, number of tickets to reserve)
The customer can (reserve tickets, cancel tickets, confirm)
Operations are saved in a text file
"""
import hashlib
import json
from datetime import datetime


class TheManager:
    """Class representing a manager
    functions: hash password,log operation,display operations,view_remaining sold tickets,
    view_tickets_sold_in_period,display_canceled_customers

     username,password,event,start_date,end_date :arg
     username, password,title,date,total_capacity,sold_tickets :returns
    """
    def __init__(self, username, password):
        self.username = username
        self.password = self.hash_password(password)
        self.operations = []

    def hash_password(self, password):
        """Hash the password using SHA-256."""
        hash256 = hashlib.sha256()
        hash256.update(password.encode('utf-8'))
        return hash256.hexdigest()

    def log_operation(self, operation):
        """Log the performed operation."""
        self.operations.append(operation)

    def display_operations(self):
        """Display all performed operations with details."""
        print("\nPerformed Operations:")
        for operation in self.operations:
            if "Event Addition" in operation:
                print(f"{operation}")  # View the entire event in detail
                print("-------------------------------------------------------------------")

            elif "Reservation" in operation or "Cancellation" in operation or "Confirmation" in operation:
                print(f"{operation}")  # View all customer's activity for purchases in detail
                print("-------------------------------------------------------------------")

            else:
                print(f"{operation}")  # it shows (Performed Operations:)
                print("----------------------------------------")

    def view_remaining_sold_tickets(self, event):
        """View the number of remaining sold tickets for an event."""
        print(f"\nRemaining Sold Tickets for Event '{event.title}': {event.sold_tickets}")
        print("----------------------------------------")

    def view_tickets_sold_in_period(self, start_date, end_date):
        """View the number of tickets sold in a period for each event and all events."""
        print("\nTickets Sold in the Specified Period:")
        for event in events:
            if start_date <= event.date <= end_date:
                print(f"Event Title: {event.title}")
                print(f"Tickets Sold: {event.sold_tickets}")
                print("----------------------------------------")
        total_tickets_sold = sum(event.sold_tickets for event in events if start_date <= event.date <= end_date)
        print(f"Total Tickets Sold in the Specified Period: {total_tickets_sold}")
        print("----------------------------------------")

    def display_canceled_customers(self, canceled_customers):
        """Display canceled customer details."""
        print("\nCanceled Customers:")
        if len(canceled_customers) > 1:
            for customer in canceled_customers:
                print(f"Customer Name: {customer['name']}")
                print(f"Event Title: {customer['event_title']}")
                print(f"Number of Canceled Tickets: {customer['num_tickets']}")
                print("----------------------------------------")
        else:
            print(f"There is no cancellation")


class InvalidPassword(Exception):
    """Exception for invalid password."""


class InvalidUsername(Exception):
    """Exception for invalid username."""


class AddUser:
    """Class for adding users
    functions: add events manager,login

     username,password :arg
     username, password,new_manager :returns
     InvalidPassword, InvalidUsername:raise
    """
    def __init__(self):
        self.users = []
        self.events_manager_user = None

    def add_events_manager(self, username, password):
        """Add an events manager user."""
        if self.events_manager_user is not None:
            raise ValueError("An events manager user already exists.")
        new_manager = TheManager(username, password)
        self.users.append(new_manager)
        self.events_manager_user = new_manager
        return new_manager

    def login(self, username, password):
        """Login with username and password."""
        for user in self.users:
            if user.username == username:
                if user.password == user.hash_password(password):
                    print("Login successful.")
                    print("----------------------------------------")
                    return user
                else:
                    raise InvalidPassword("Invalid password.")
        raise InvalidUsername("Invalid username.")


class Customer:
    """Class representing a customer
    functions: display customer info

      name, email, phone_number, personal_code :arg
      name, email, phone_number, personal_code :returns
    """
    def __init__(self, name, email, phone_number, personal_code):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.personal_code = personal_code

    def display_customer_info(self):
        """Display customer information."""
        print(f"\nCustomer Information:")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Personal Code: {self.personal_code}")
        print("----------------------------------------")


class Event:
    """Class representing an event
    functions: Display event details , Reserve tickets for an event

    title=None, total_capacity=None, date=None, remaining_capacity=None, subject=None :arg
    title, total_capacity, date, remaining_capacity, subject :returns
    """
    def __init__(self, title=None, total_capacity=None, date=None, remaining_capacity=None, subject=None):
        self.title = title
        self.total_capacity = total_capacity
        self.remaining_capacity = remaining_capacity
        self.date = date
        self.subject = subject
        self.reservations = []
        self.sold_tickets = 0

    def display_event_details(self):
        """Display event details."""
        print(f"\nEvent Title: {self.title}")
        print(f"Total Capacity: {self.total_capacity}")
        print(f"Remaining Capacity: {self.remaining_capacity}")
        print(f"Sold Tickets: {self.sold_tickets}")
        print(f"Date: {self.date}")
        print(f"Subject: {self.subject}")
        print("----------------------------------------")

    def reserve_tickets(self, num_tickets, customer, subject):
        """Reserve tickets for an event."""
        if num_tickets <= 0:
            print("Invalid number of tickets. Please reserve at least one ticket.")
            print("----------------------------------------")
            return
        if num_tickets <= self.remaining_capacity:
            print(f"\nEvent Details for '{self.title}': ")
            print(f"Total Capacity: {self.total_capacity}")
            print(f"Remaining Capacity: {self.remaining_capacity}")
            print(f"Number of Reserved Tickets: {self.total_capacity - self.remaining_capacity}")
            print("----------------------------------------")
            reservation_id = len(self.reservations) + 1
            self.reservations.append({"reservation_id": reservation_id,
                                      "customer": customer.__dict__, "num_tickets": num_tickets,
                                      "subject": subject, "confirmed": False})
            self.remaining_capacity -= num_tickets  # Reducing the number of reserved tickets
            self.sold_tickets += num_tickets  # Increment sold tickets count
            print(f"Reservation successful! {num_tickets} tickets reserved. Reservation ID: {reservation_id}")
            print("----------------------------------------")
            # Log the reservation operation
            manager.log_operation(
                f"Reservation: Event '{self.title}', Tickets: {num_tickets}, Customer: {customer.name}")
        else:
            print(f"\nEvent Details for '{self.title}': ")
            print(f"Total Capacity: {self.total_capacity}")
            print(f"Remaining Capacity: {self.remaining_capacity}")
            print(f"Number of Reserved Tickets: {self.total_capacity - self.remaining_capacity}")
            print(f"Insufficient capacity. Only {self.remaining_capacity} tickets available.")
            print("----------------------------------------")


class CustomerReservation:
    """Class representing customer reservations
    functions: Cancel a reservation,Confirm a reservation,Display customer reservations

    reservation_id, event, customer :arg
    reservation_id, event, customer :returns
    """
    def __init__(self):
        self.reservations = []

    def confirm_reservation(self, reservation_id, event, customer):
        """Confirm a reservation."""
        for reservation in event.reservations:
            if (reservation["reservation_id"] == reservation_id
                    and not reservation["confirmed"]
                    and reservation["customer"]["personal_code"] == customer.personal_code):
                reservation["confirmed"] = True
                print(f"Reservation with ID {reservation_id} confirmed.")
                print("----------------------------------------")
                # Log the confirmation operation
                manager.log_operation(f"Confirmation: Reservation ID {reservation_id} confirmed.")
                return
        print(f"Reservation with ID {reservation_id} not found, already confirmed, or incorrect personal code.")
        print("----------------------------------------")

    def display_customer_reservations(self, events, customer):
        """Display customer reservations."""
        print(f"\nReservations for Customer {customer.name} (Personal Code: {customer.personal_code}):")
        for event in events:
            for reservation in event.reservations:
                if reservation["customer"]["personal_code"] == customer.personal_code:
                    print(f"Reservation ID: {reservation['reservation_id']}")
                    print(f"Event: {event.title}")
                    print(f"Tickets: {reservation['num_tickets']}")
                    print(f"Subject: {reservation['subject']}")
                    print(f"Confirmed: {'Yes' if reservation['confirmed'] else 'No'}")
                    print("----------------------------------------")


def display_events_between_dates(events, start_date, end_date):
    """Display events between the given start date and end date

    events, start_date, end_date :arg
    title,date,total_capacity,remaining_capacity,sold_tickets,subject :returns
    """
    print(f"\nEvents between {start_date} and {end_date}: ")
    for event in events:
        if start_date <= event.date <= end_date:
            print(f"Event Title: {event.title}\nDate: {event.date}")
            print(f"Total Capacity: {event.total_capacity}")
            print(f"Remaining Capacity: {event.remaining_capacity}")
            print(f"Sold Tickets: {event.sold_tickets}")
            print(f"Subject: {event.subject}")
            print("----------------------------------------")


def save_to_file(data,
                 filename=r"C:\Users\Dell\OneDrive\Desktop\hw\hw5\Pedram_Karimi_HW5_Maktab105\Ticket_sales_system.txt"):
    """Save data to a file in JSON format."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)  # indent == space for better reading
        file.write('\n')


def load_canceled_customers(
        filename=r"C:\Users\Dell\OneDrive\Desktop\hw\hw5\Pedram_Karimi_HW5_Maktab105\Ticket_sales_system.txt"):
    """Load canceled customers from a file."""
    try:
        with open(filename, "r") as file:
            canceled_customers = json.load(file)
        return canceled_customers
    except FileNotFoundError:
        return []


def save_all_data(events, manager,
                  filename=r"C:\Users\Dell\OneDrive\Desktop\hw\hw5\Pedram_Karimi_HW5_Maktab105\Ticket_sales_system.txt"):
    """Save all data to a file."""
    data = {"events": [event.__dict__ for event in events],
            "manager": manager.__dict__ if manager else None}
    save_to_file(data, filename)


try:
    if __name__ == '__main__':
        add_user_instance = AddUser()
        manager = None
        events_manager_user = None
        events = []
        while True:
            print("\nOptions:\n1.Add Manager\n2.Login as Events Manager\n3.Add Event\n"
                  "4.Reserve Tickets\n5.Cancel Reservation\n6.Confirm Reservation\n7.View Operations\n"
                  "8.View Event Details\n9.View Customer Reservations\n10.View Events between Dates\n"
                  "11.View Remaining Sold Tickets\n12.View Tickets Sold in Period\n"
                  "13.displaying canceled customers\n14.save\n15.Exit\n----------------------------------------")
            option = input("\tEnter your choice (1-14): ")
            print("----------------------------------------")
            if option == "1":
                if manager is None:
                    manager = add_user_instance.add_events_manager(
                        input("Enter manager username: "), input("Enter manager password: "))
                else:
                    print("A manager user already exists.")
                    print("----------------------------------------")
            elif option == "2":
                if manager is None:
                    username = input("Enter manager username: ")
                    password = input("Enter manager password: ")
                    manager = add_user_instance.login(username, password)
                else:
                    print("You are already logged in as a manager.")
                    print("----------------------------------------")
            elif option == "3":
                if manager is not None:
                    username = input("Enter manager username: ")
                    password = input("Enter manager password: ")
                    manager = add_user_instance.login(username, password)
                    event = Event(
                        title=input("Enter event title: "),
                        total_capacity=int(input("Enter total capacity:")),
                        date=input("Enter event date (YYYY-MM-DD): "),
                        remaining_capacity=int(input("Enter remaining capacity: ")),
                        subject=input("Enter event subject: "))
                    events.append(event)
                    print("Event added successfully.")
                    print("----------------------------------------")
                    # Log the event addition operation
                    manager.log_operation(f"Event Addition: '{event.title}', Capacity: {event.total_capacity}, "
                                          f"Date: {event.date}, Remaining Capacity: {event.remaining_capacity}, "
                                          f"Subject: {event.subject}")
                else:
                    print("Please log in as a manager to add events.")
                    print("----------------------------------------")
            elif option == "4":
                if events:
                    print("\nAll Events:")
                    for event in events:
                        event.display_event_details()
                else:
                    print("No events available. Please add an event first.")
                    print("----------------------------------------")
                if manager:
                    event_title = input("Enter the title of the event to reserve tickets for: ")
                    event_to_reserve = next((e for e in events if e.title == event_title), None)
                    if event_to_reserve:
                        num_tickets_to_reserve = int(
                            input(f"Enter the number of tickets to reserve for {event_title}: "))
                        customer_name = input("Enter customer name: ")
                        customer_email = input("Enter customer email: ")
                        customer_phone = input("Enter customer phone number: ")
                        customer_personal_code = input("Enter customer personal code: ")
                        customer = Customer(customer_name, customer_email, customer_phone, customer_personal_code)
                        subject = input("Enter the subject of the event to reserve for (optional): ")
                        event_to_reserve.reserve_tickets(num_tickets_to_reserve, customer, subject)
                    else:
                        print(f"Event with title '{event_title}' not found.")
                        print("----------------------------------------")
                else:
                    print("Please log in as a manager to reserve tickets.")
                    print("----------------------------------------")
            elif option == "5":
                if manager:
                    reservation_id_to_cancel = int(input("Enter the reservation ID to cancel: "))
                    customer_personal_code = input("Enter your Personal Code to cancel the reservation: ")

                    canceled_customers = []  # List to store details of canceled customers

                    event_found = False
                    for event in events:
                        for reservation in event.reservations:
                            if (reservation["reservation_id"] == reservation_id_to_cancel
                                    and not reservation["confirmed"]
                                    and reservation["customer"]["personal_code"] == customer_personal_code):
                                canceled_customer_details = {
                                    'name': reservation["customer"]["name"],
                                    'event_title': event.title,
                                    'num_tickets': reservation["num_tickets"]
                                }
                                canceled_customers.append(canceled_customer_details)

                                event.remaining_capacity += reservation[
                                    "num_tickets"]  # Increasing the number of reserved tickets
                                event.sold_tickets -= reservation["num_tickets"]
                                event.reservations.remove(reservation)
                                print(f"Reservation with ID {reservation_id_to_cancel} canceled.")
                                print("----------------------------------------")
                                # Log the cancellation operation
                                manager.log_operation(
                                    f"Cancellation: Reservation ID {reservation_id_to_cancel} canceled.")
                                event_found = True
                                break
                    if not event_found:
                        print(
                            f"Reservation with ID {reservation_id_to_cancel}"
                            f" not found, already confirmed, or incorrect personal code.")
                        print("----------------------------------------")

                    # Save canceled customers to file
                    save_to_file(canceled_customers, "canceled_customers.json")

                else:
                    print("Please log in as a manager to cancel reservations.")
                    print("----------------------------------------")
            elif option == "6":
                if manager:
                    reservation_id_to_confirm = int(input("Enter the reservation ID to confirm: "))
                    event_found = False
                    for event in events:
                        if any(
                                reservation["reservation_id"] == reservation_id_to_confirm
                                for reservation in event.reservations):
                            customer_personal_code = input("Enter your Personal Code to confirm the reservation: ")
                            customer = Customer("", "", "", customer_personal_code)
                            customer_reservation = CustomerReservation()
                            customer_reservation.confirm_reservation(reservation_id_to_confirm, event, customer)
                            event_found = True
                            break
                    if not event_found:
                        print(f"Reservation with ID {reservation_id_to_confirm} not found.")
                        print("----------------------------------------")
                else:
                    print("Please log in as a manager to confirm reservations.")
                    print("----------------------------------------")
            elif option == "7":
                if manager is not None:
                    username = input("Enter manager username: ")
                    password = input("Enter manager password: ")
                    manager = add_user_instance.login(username, password)
                    manager.display_operations()
                else:
                    print("Please log in as a manager to view operations.")
                    print("----------------------------------------")
            elif option == "8":
                if events:
                    event_title = input("Enter the title of the event to view details: ")
                    event_to_display = next((e for e in events if e.title == event_title), None)
                    if event_to_display:
                        event_to_display.display_event_details()
                    else:
                        print(f"Event with title '{event_title}' not found.")
                        print("----------------------------------------")
                else:
                    print("No events available. Please add an event first.")
                    print("----------------------------------------")
            elif option == "9":
                if events:
                    customer_personal_code = input("Enter your Personal Code to view your reservations: ")
                    customer = Customer("", "", "", customer_personal_code)
                    customer_reservation = CustomerReservation()
                    customer_reservation.display_customer_reservations(events, customer)
                else:
                    print("No events available. Please add an event first.")
                    print("----------------------------------------")
            elif option == "10":
                start_date = input("Enter the start date (YYYY-MM-DD): ")
                end_date = input("Enter the end date (YYYY-MM-DD): ")
                try:
                    datetime.strptime(start_date, '%Y-%m-%d')
                    datetime.strptime(end_date, '%Y-%m-%d')
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
                    print("----------------------------------------")
                    continue
                display_events_between_dates(events, start_date, end_date)
            elif option == "11":
                if manager is not None:
                    username = input("Enter manager username: ")
                    password = input("Enter manager password: ")
                    manager = add_user_instance.login(username, password)
                    start_date = input("Enter the start date (YYYY-MM-DD): ")
                    end_date = input("Enter the end date (YYYY-MM-DD): ")
                    try:
                        datetime.strptime(start_date, '%Y-%m-%d')
                        datetime.strptime(end_date, '%Y-%m-%d')
                    except ValueError:
                        print("Invalid date format. Please use YYYY-MM-DD.")
                        print("----------------------------------------")
                        continue
                    manager.view_tickets_sold_in_period(start_date, end_date)
                else:
                    print("Please log in as an events manager to view tickets sold in a period.")
                    print("----------------------------------------")
            elif option == "12":
                if manager is not None:
                    username = input("Enter manager username: ")
                    password = input("Enter manager password: ")
                    manager = add_user_instance.login(username, password)
                    event_title = input("Enter the title of the event to view remaining sold tickets: ")
                    event_to_display = next((e for e in events if e.title == event_title), None)
                    if event_to_display:
                        manager.view_remaining_sold_tickets(event_to_display)
                    else:
                        print(f"Event with title '{event_title}' not found.")
                        print("----------------------------------------")
                else:
                    print("Please log in as an events manager to view remaining sold tickets.")
                    print("----------------------------------------")
            elif option == "13":
                if manager:
                    username = input("Enter manager username: ")
                    password = input("Enter manager password: ")
                    manager = add_user_instance.login(username, password)
                    canceled_customers = load_canceled_customers("canceled_customers.json")
                    manager.display_canceled_customers(canceled_customers)
                else:
                    print("Please log in as a manager to view canceled customers.")
                    print("----------------------------------------")
            elif option == "14":
                if manager is not None:
                    username = input("Enter manager username: ")
                    password = input("Enter manager password: ")
                    manager = add_user_instance.login(username, password)
                    save_all_data(events, manager)
                    print("Data saved.")
                    print("----------------------------------------")
                else:
                    print("No manager logged in. Data not saved.")
                    print("----------------------------------------")
                    break
            elif option == "15":
                print("Exiting the Ticket sales system.")
                print("----------------------------------------")
                break
            else:
                print("Invalid option. Please enter a number between 1 and 14.")
                print("----------------------------------------")
except ValueError as e:
    print(f"Error!!!!{e}")
except TypeError as e:
    print(f"Error!!!!{e}")
except InvalidPassword as e:
    print(f"Error!!!!{e}")
except InvalidUsername as e:
    print(f"Error!!!!{e}")

