members_list = []
with open('members.txt', 'r') as file:
    for member in file:
        members_list.append(member)

for i, member in enumerate(members_list):
    n = member.replace("\n", "")
    members_list[i] = n

while True:
    member = input("Add a new member: ")
    members_list.append(member)
    file = open('members.txt', 'w')
    for member in members_list:
        file.writelines(member.title()  + "\n")
    file.close()
