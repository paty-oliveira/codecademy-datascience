def update_money_damages(damages: list) -> list:
    conversions = {"M": 1000000, "B": 1000000000}
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


def aggregate_hurricane_info(names: list,
                             months: list,
                             years: list,
                             winds: list,
                             areas: list,
                             damages: list,
                             deaths: list) -> dict:
    return {
        names[i]: {"Name": names[i],
                   "Month": months[i],
                   "Year": years[i],
                   "Max Sustained Wind": winds[i],
                   "Areas Affected": areas[i],
                   "Damage": damages[i],
                   "Deaths": deaths[i]
                   }
        for i in range(len(names))
    }
