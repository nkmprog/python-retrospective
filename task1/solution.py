zodiacs = ["Козирог", "Водолей", "Риби", "Овен", "Телец", "Близнаци",
           "Рак", "Лъв", "Дева", "Везни", "Скорпион", "Стрелец"]

split = [19, 18, 20, 20, 20, 20, 21, 22, 22, 22, 21, 21]


def what_is_my_sign(day, month):
    if day <= split[month - 1]:
        return zodiacs[month - 1]
    elif month != 12:
        return zodiacs[month]
    else:
        return zodiacs[0]
