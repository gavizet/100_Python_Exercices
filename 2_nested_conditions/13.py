# 13. Créer un programme qui vérifie si une année est bissextile ou non.

def is_it_leap_year(year: int) -> bool:
    if year % 4 == 0:
        return True
    return False

years_list = [-12, 0, 320, 1997, 2020, 2026, 20237]
# should be [True, True, True, False, True, False, False]
for curr_year in years_list:
    print(f"Is {curr_year} a leap year ? {is_it_leap_year(curr_year)}")