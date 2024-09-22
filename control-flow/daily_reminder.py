task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ")

is_time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case 'high':
        if is_time_bound.lower() == 'yes':
            print(f"{task} is a high priority task that requires immediate attention today!")
        else:
            print(f"{task} is a high priority task but is not time-bound. Don't neglect it!")
    case 'medium':
        if is_time_bound.lower() == 'yes':
            print(f"{task} is a medium priority task that requires immediate attention today!")
        else:
            print(f"{task} is a medium priority task. Plan to complete it soon.")
    case 'low':
        if is_time_bound.lower() == 'no':
            print(f"{task} is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"{task} is a low priority task but it’s time-bound. Don’t ignore it!")
    case _:
        print("Work at your own pace.")
