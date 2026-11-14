my_goals = []

for i in range(3):
  new_goal = input("Add a goal: ")
  my_goals.append(new_goal)

print("Here are your goals:")
for goal in my_goals:
  print("-" , goal)
