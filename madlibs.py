# This is a matlibs project made by python 
# It tell a story of three friends 
# Enter the perfect value in the asked variables and your story will be ready 
# Or copy this code, paste in your editor and give changes to your story, add new variables, declare its value, get your story ready 
# and enjoy it.

print("Power of FriendShip......\nStory to be presented..\n")

numberOfFriends = int(input("Number of friends: \n")) # It should be 3 only
character_1 = input("Name of first character:\n")
character_2 = input("Name of second character:\n")
character_3 = input("Name of third character:\n")
man = input("Name of the man:\n")
position = input("Position:\n") # It should be related to position of palace only
position = position.lower()

madlibs = f"Once upon a time, there were {numberOfFriends} friends, they were {character_1}, {character_2} and {character_3}. They were best ones. They never fought against each other. One day a man named {man} came to them and offered them to be the {position} of the palace. {character_1} whispered to {character_2} and {character_3}, that they should become the {position}, but they refused. They weren't greedy to become {position}. They wanted their friends should become {position}. Among them no one was ready to be that. Seeing that, there friendship was superior than being a {position}, {man} offered all of  the {numberOfFriends} friends the position of a {position}."

print(madlibs)
