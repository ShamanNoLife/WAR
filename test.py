class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def update_score(self, points):
        self.score += points

    def __str__(self):
        return f"{self.name}: {self.score}"

class PlayerBase:
    def __init__(self):
        self.players = []

    def add_player(self, name):
        new_player = Player(name)
        self.players.append(new_player)

    def get_player(self, name):
        for player in self.players:
            if player.name == name:
                return player
        return None

    def show_players(self):
        print("\nPlayers:")
        for player in self.players:
            print(player)

if __name__ == "__main__":
    player_base = PlayerBase()

    while True:
        print("Menu:")
        print("1. Add Player")
        print("2. Update Player Score")
        print("3. Show Players")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter player name: ")
            player_base.add_player(name)
        elif choice == "2":
            name = input("Enter player name: ")
            player = player_base.get_player(name)
            if player:
                points = int(input("Enter points to update score: "))
                player.update_score(points)
            else:
                print("Player not found!")
        elif choice == "3":
            player_base.show_players()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")
