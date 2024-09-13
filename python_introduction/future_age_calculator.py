age = int(input('How old are you? '))

# new age = currentdate - futuredate
current_date, future_date = 2023, 2050
added_age = future_date - current_date


new_age = age + added_age

print('In', future_date, 'you will be', new_age, 'years old')