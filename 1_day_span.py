from datetime import datetime

def day_span(date1:datetime, date2:datetime)->int:
    """Retourne le nombre de jours entre deux dates"""
    
    diff = date2 - date1

    return abs(diff.days)


d1 = datetime(2024, 12, 12)
d2 = datetime(2024, 5, 12)

diff = day_span(d1, d2)

print(f'Il y a {diff} jours entre {d1} et {d2}')