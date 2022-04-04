def sum_of_intervals(intervals):
    if type(intervals) != list:
        return None

    for index, interval in enumerate(intervals):
        print("index: " + str(index))
        # if index is out of bound --> break
        if index + 1 > len(intervals) - 1:
            break
        print("values: " + str(intervals[index][1]) + "; " + str(intervals[index + 1][1]))
        # if greater num 1 is greater than greater num 2 --> switch the two
        if intervals[index][1] > intervals[index + 1][1]:
            intervals[index], intervals[index + 1] = intervals[index + 1], intervals[index]
    
    print(intervals)
    return ""


print(sum_of_intervals([(1, 5), (3, 7), (0, 3)]))