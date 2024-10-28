def find_elligible(names: list[str], ages: list[int]) -> dict[str, int]:
    valid25 = {}
    for i in range(len(names)):
        if ages[i] >= 25:
            valid25[names[i]] = ages[i]
    return valid25


names = ["Allen", "Ken", "Barbie"]
ages = [23, 26, 25]
drivers = find_elligible(names, ages)

print(drivers)
