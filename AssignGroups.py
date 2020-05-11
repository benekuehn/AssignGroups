import random

## People that need to be divided into groups
people = ["Anna", "Anton", "Berta", "Cedric", "Dennis", "Egon"]


membersPerGroup = 2
counterMembers = 1
group = []
members = []

lenPeople = len(people)
i = 0

while i <= lenPeople:

    if counterMembers <= membersPerGroup:
        try:
            a = random.randint(0, len(people)-1)
        except ValueError:
            a = 0
        members.append(people[a])
        people.remove(people[a])
        i += 1
        if lenPeople != i:
             counterMembers += 1
        else: ## When number of people and max per group does not fit equally distributed.
            counterMembers += 2
    elif i < lenPeople and lenPeople-1 > 1: ## Group max members reached but still more than one entry in list.
        group.append(members)
        members = []
        counterMembers = 1
    else: ## Catch last entry in list.
        group.append(members)
        members = []
        i += 1   

print(group)