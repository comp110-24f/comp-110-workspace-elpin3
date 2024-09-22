def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match"
    return "no match!"


# print(check_first_letter("beans", "q"))


def get_weather_report() -> str:
    weather = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        return "Bring a jacket!"
    elif weather == "hot":
        return "Keep cool out there!"
    else:
        return "I don't recognize that weather"


print(get_weather_report())
