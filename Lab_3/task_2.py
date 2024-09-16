# TODO Напишите функцию find_common_participants

def find_common_participants(first_group, second_group, sep=','):

    first_group_list = first_group.split(sep)
    second_group_list = second_group.split(sep)

    participants_in_both_groups = set(first_group_list).intersection(second_group_list)
    participants_in_both_groups_alph = sorted(participants_in_both_groups)

    return participants_in_both_groups_alph


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, sep='|'))
