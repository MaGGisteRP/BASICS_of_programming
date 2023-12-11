def harry_potter_test():
    score = 0

    print("Добро пожаловать на психологический тест о Гарри Поттере!")
    print("Ответьте на следующие вопросы с помощью 'да' или 'нет'.\n")

    answer = input("1. Вы верите в магию? ")
    if answer.lower() == "да":
        score += 1

    answer = input("2. Вы храбры и отважный человек? ")
    if answer.lower() == "да":
        score += 1

    answer = input("3. Вы цените дружбу превыше всего? ")
    if answer.lower() == "да":
        score += 1

    answer = input("4. Вы любопытны и стремитесь учиться? ")
    if answer.lower() == "да":
        score += 1

    answer = input("5. Ты орорной? ")
    if answer.lower() == "да":
        score += 1

    answer = input("6. Являетесь ли вы преданным и надежным человеком? ")
    if answer.lower() == "да":
        score += 1

    answer = input("7. Есть ли у вас сильное чувство справедливости? ")
    if answer.lower() == "да":
        score += 1

    answer = input("8. Вы амбициозны и решительны? ")
    if answer.lower() == "да":
        score += 1

    if score >= 6:
        result = "Ты больше всего похож на Гарри Поттера!"
    elif score >= 4:
        result = "Ты больше всего похожа на Гермиону Грейнджер!"
    elif score >= 2:
        result = "Ты больше всего похож на Рона Уизли!"
    else:
        result = "Ты больше всего похож на Драко Малфоя!"

    print("\nСпасибо вам за то, что прошли тест!")
    print("Основываясь на ваших ответах, " + result)

harry_potter_test()