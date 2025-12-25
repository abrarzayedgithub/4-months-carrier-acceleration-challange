timetable = {
    "day1": ["math","physics"],
    "day2": ["chemistry","biology"]
}
for day,exams in timetable.items():
    print(day)
    for exam in exams:
        print("-",exam)