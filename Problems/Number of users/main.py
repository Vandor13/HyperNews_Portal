# write your code here
with open("users.json") as file:
    users = json.load(file)["users"]
print(len(users))
