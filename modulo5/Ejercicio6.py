from bisect import bisect_right
from bisect import bisect_left

persons = []
while True:
    person = input()
    if person == '0 0':
        break
    person = person.split()
    maximum = int(person[1])
    if len(persons) < maximum:

        to_insert = bisect_left(persons, maximum)
        persons.insert(to_insert, maximum)

        to_delete = bisect_right(persons, len(persons) - 1)
        if len(persons) >= 1:
            if persons[to_delete - 1] == len(persons) - 1:
                del persons[to_delete - 1]

print(len(persons))
