def life_in_weeks(age):
    year_remaining = 90 - age
    weeks_remaining = year_remaining * 52
    print(f"you have {weeks_remaining} weeks left.")

life_in_weeks(21)