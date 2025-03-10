reports_data = []


with open("lab_2/input_2.txt") as file:
    for line in file:
        levels = line.split()
        report = [int(level) for level in levels]
        reports_data.append(report)


def is_safe_report(report):
    is_increasing = True
    is_decreasing = True
    has_valid_differences = True

    for i in range(len(report) - 1):
        if report[i] >= report[i + 1]:
            is_increasing = False
        if report[i] <= report[i + 1]:
            is_decreasing = False
        if not (1 <= (report[i] - report[i + 1]) * ((report[i] - report[i + 1]) >= 0) <= 3):
            has_valid_differences = False
    return (is_increasing or is_decreasing) and has_valid_differences


safe_reports_count = sum(1 for report in reports_data if is_safe_report(report))
print("Кількість безпечних звітів:", safe_reports_count)

#106