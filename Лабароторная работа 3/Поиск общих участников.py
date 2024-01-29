# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, razdelitel = ","):
    x = list(set(first.split(razdelitel)).intersection(second.split(razdelitel)))
    x.sort()
    return x


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))
