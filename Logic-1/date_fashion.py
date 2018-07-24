def date_fashion(you, date):
    hot = (you > 2 and date >= 8) or (you >= 8 and date > 2)
    not_hot = you <= 2 or date <= 2
    return 2 if hot else 0 if not_hot else 1
