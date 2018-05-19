while True:
    player_one = input("\nPlayer 1, enter (r)ock, (s)cissor or (p)aper: ")
    player_two = input("Player 2, enter (r)ock, (s)cissor or (p)aper: ")

    if (player_one.upper() == "R" and player_two.upper() == "S") or (
            player_one.upper() == "S" and player_two.upper() == "P") or (
            player_one.upper() == "P" and player_two.upper() == "R"):
        print("Player 1 win!\n")
    elif (player_two.upper() == "R" and player_one.upper() == "S") or (
            player_two.upper() == "S" and player_one.upper() == "P") or (
            player_two.upper() == "P" and player_one.upper() == "R"):
        print("Player 2 win!\n")
    else:
        print("It's a tie!\n")

    if input("Quit (Y/N)? ").upper() == "Y":
        break
