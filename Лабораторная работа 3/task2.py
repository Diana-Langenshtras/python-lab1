# TODO Напишите функцию find_common_participants
def find_common_participants(string1, string2, separator=","):
    new_string1 = string1.split(separator)
    new_string2 = string2.split(separator)
    common_members = list(set(new_string1).intersection(new_string2))
    common_members.sort()
    return common_members


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))
