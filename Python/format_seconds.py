def format_duration(seconds):
    # value from which i have to start counting (default=year because of how later script works)
    bigger_value = 60*60*24*365
    # list of "times" to concatenate (example=["3 hours", "2 minutes", "43 seconds"])
    solution_steps = []
    solution = ""
    time_steps = {
        "seconds":1,
        "minutes":60,
        "hours":60*60,
        "days":60*60*24,
        "years":60*60*24*365
    }

    if seconds == 0:
        return "now"

    if seconds == 1:
        return "1 second"

    if seconds < 60:
        return str(seconds) + " seconds"

    # gets value of "bigger_value"
    for index, value in enumerate(list(time_steps.values())):
        if value > seconds:
            bigger_value = list(time_steps.values())[index - 1]
            break

    # gets the list of solution_steps
    for i in range(list(time_steps.values()).index(bigger_value), -1, -1):
        time = int(seconds / list(time_steps.values())[i])
        # ignore if time is 0 (we want to avoid "3 hours, 0 minutes and 3 seconds", but we want "3 hours and 3 seconds")
        if time == 0:
            continue
        # singular if time is 1 (we want "1 second" not "1 seconds")
        if time == 1:
            solution_steps.append(str(time) + " " + list(time_steps.keys())[i][:-1])
        else:
            solution_steps.append(str(time) + " " + list(time_steps.keys())[i])
        # each time he adds a value to the list it reduces that same amount of time
        seconds -= time * list(time_steps.values())[i]

    # if more than 1 element, concatenates with commas and the final " and "
    if len(solution_steps) > 1:
        solution += ", ".join(solution_steps[:-1])
        solution += " and " + solution_steps[len(solution_steps) - 1]
    # just returns it if there's only 1 element
    else:
        solution = solution_steps[0]

    return solution


print(format_duration(1245983490))