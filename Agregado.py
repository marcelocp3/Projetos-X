import random


class Team:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def update_points(self, points):
        self.points += points

def simulate_league(teams):
    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            # Simulate away game
            away_score = simulate_game()
            teams[i].update_points(away_score)
            teams[j].update_points(away_score)

            # Simulate home game
            home_score = simulate_game()
            teams[i].update_points(home_score)
            teams[j].update_points(home_score)

def simulate_game():
    # Simulate the score of a game
    # You can implement your own logic here
    # For simplicity, let's assume the score is a random number between 0 and 5
    return random.randint(0, 5)

# Create teams
team1 = Team("Team 1")
team2 = Team("Team 2")
team3 = Team("Team 3")
team4 = Team("Team 4")

# Simulate the league
teams = [team1, team2, team3, team4]
simulate_league(teams)

# Print the points total for each team
for team in teams:
    print(f"{team.name}: {team.points} points")