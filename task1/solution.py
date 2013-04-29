ZODIACS = ["Козирог", "Водолей", "Риби", "Овен", "Телец", "Близнаци",
           "Рак", "Лъв", "Дева", "Везни", "Скорпион", "Стрелец", "Козирог"]

SPLIT = [19, 18, 20, 20, 20, 20, 21, 22, 22, 22, 21, 21]


def what_is_my_sign(day, month):
    if day <= SPLIT[month - 1]:
        return ZODIACS[month - 1]
    return ZODIACS[month]
