def update_money_damages(damages: list):
    conversions = {
        "M": 1000000,
        "B": 1000000000
    }
    updated_damages = []

    for money in damages:
        if money == "Damages not recorded":
            updated_damages.append(money)
        else:
            conversion_prefix = money[-1]
            number_to_convert = money.replace(conversion_prefix, "").replace(".", "")
            converted_money = float(int(number_to_convert) * conversions[conversion_prefix])
            updated_damages.append(converted_money)

    return updated_damages

