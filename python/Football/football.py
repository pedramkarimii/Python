import random

all_teams = []

class Human:
    """
    integer age name
    """

    def __init__(self, name, age):
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self.name = name
        self.age = age


class Player(Human):
    """
    player age (15-30)
    performance (0-100)
    Entering rights
    Enter plyer post
    """

    def __init__(self, name, age, salary, position, performance):
        super().__init__(name, age)

        if salary < 0:
            raise ValueError("Salary cannot be negative.")
        if not 15 <= age <= 30:
            raise ValueError("Age should be between 15 and 30.")
        if not 0 <= performance <= 100:
            raise ValueError("Performance should be in the range of 0 to 100.")

        self.salary = salary
        self.position = position
        self.performance = performance


class Coach(Human):
    """
    player age (15-30)
    Entering rights
    Beginning and end of the contract
    """

    def __init__(self, name, age, salary, contract_start_date, contract_end_date):
        super().__init__(name, age)

        if not 30 <= age <= 65:
            raise ValueError("Coach's age should be between 30 and 65.")
        if salary < 0:
            raise ValueError("Salary cannot be negative.")

        self.salary = salary
        self.contract_start_date = contract_start_date
        self.contract_end_date = contract_end_date


class Team:
    """
    Enter team information
    ENumber of players
    Enter the player
    Enter the coach
    Enter player salary
    Enter salary salary
    """

    def __init__(self, name, initial_balance):
        self.name = name
        self.players = []
        self.coach = None
        self.balance = initial_balance
        self.points = 0

    def check_if_full(self):
        return len(self.players) == 11

    def add_player(self, player):
        if not self.check_if_full():
            self.players.append(player)
            print(f"{player.name} added to {self.name}.")
        else:
            print(f"{self.name} already has 11 players.")

    def set_coach(self, coach, all_teams):
        if coach not in [team.coach for team in all_teams]:
            self.coach = coach
            print(f"{coach.name} assigned as the coach of {self.name}.")
        else:
            print(f"{coach.name} is already a coach in another team.")

    def buy_player(self, player, other_team, transfer_fee):
        if player in other_team.players and self.balance >= transfer_fee:
            self.players.append(player)
            other_team.players.remove(player)
            self.balance -= transfer_fee
            other_team.balance += transfer_fee
            print(f"{player.name} bought successfully by {self.name}.")
        else:
            print(f"{player.name} could not be bought by {self.name}.")

    def __lt__(self, other):
        return self.points < other.points

    def __eq__(self, other):
        return self.points == other.points


class League:
    def __init__(self):
        self.teams = []

    def add_team(self, team):
        self.teams.append(team)

    def select_teams_for_match(self):
        selected_teams = random.sample(self.teams, 2)

        for team in selected_teams:
            if not team.check_if_full() or team.coach is None:
                print(f"Selected teams do not have 11 players or a coach. Match cannot be played.")
                return None

        print(f"Teams selected for the match: {selected_teams[0].name} vs {selected_teams[1].name}")
        return selected_teams

    # Function to simulate a round of matches
    def simulate_round(self):
        for _ in range(len(self.teams) // 2):
            selected_teams = self.select_teams_for_match()
            if selected_teams is not None:
                # Simulate match result
                winner = random.choice(selected_teams)
                loser = [team for team in selected_teams if team != winner][0]

                # Update points
                winner.points += 3
                loser.points += 1

                print(f"{winner.name} won the match against {loser.name}. Points updated.")


# Function to create a team with user input
def create_team():
    name = input("Enter team name: ")
    initial_balance = int(input("Enter initial balance: "))
    return Team(name, initial_balance)


# Function to create a player with user input
def create_player():
    name = input("Enter player name: ")
    age = int(input("Enter player age: "))
    salary = int(input("Enter player salary: "))
    position = input("Enter player position: ")
    performance = int(input("Enter player performance: "))
    return Player(name, age, salary, position, performance)


# Function to create a coach with user input
def create_coach():
    name = input("Enter coach name: ")
    age = int(input("Enter coach age: "))
    salary = int(input("Enter coach salary: "))
    contract_start_date = input("Enter contract start date: ")
    contract_end_date = input("Enter contract end date: ")
    return Coach(name, age, salary, contract_start_date, contract_end_date)


# Main program loop
league = League()  # Initialize an instance of the League class
while True:
    print("\nChoose an option:")
    print("1. Create Team")
    print("2. Create Player")
    print("3. Create Coach")
    print("4. Simulate Round")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        team = create_team()
        all_teams.append(team)
        league.add_team(team)  # Add the team to the league
    elif choice == "2":
        player = create_player()
        team_index = int(input("Enter the index of the team to add the player: "))
        all_teams[team_index - 1].add_player(player)
    elif choice == "3":
        coach = create_coach()
        team_index = int(input("Enter the index of the team to set the coach: "))
        all_teams[team_index - 1].set_coach(coach, all_teams)
    elif choice == "4":
        league.simulate_round()
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
