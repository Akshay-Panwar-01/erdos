import calendar
from collections import Counter

day_counts = Counter()

# Iterate through 100000 years
for year in range(0, 100000):
    for month in range(1, 13):
        weekday = calendar.weekday(year, month, 15)
        day_counts[weekday] += 1

total_months = sum(day_counts.values())


day_probabilities = {day: count / total_months for day, count in day_counts.items()}


e=1
ans=0
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for i, day in enumerate(days_of_week):
    print(f"{day}: {day_probabilities[i] * 100}%")
    ans+=day_probabilities[i]*e
    e+=1
print(ans*1000000,e)
