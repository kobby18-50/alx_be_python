task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ")

is_time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case 'high':
        if(is_time_bound == 'yes'):
            print(f"{task} is high priority task that requires immediate attention today!")
    case 'medium':
        if(is_time_bound == 'yes'):
            print(f"{task} is a medium priority task that requires immediate attention today!")
    case 'low':
        if(is_time_bound == 'no'):
            print(f"{task} is a low priority task. Consider completing it when you have free time")
    case _:
        print('Work at your own pace')

    