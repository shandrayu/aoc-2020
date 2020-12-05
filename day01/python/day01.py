def sum_of_two(nums, sum):
    sorted_numbers = sorted(nums)
    left = 0
    right = len(sorted_numbers) - 1
    while (left < right):
        current_sum = sorted_numbers[left] + sorted_numbers[right]
        if current_sum == sum:
            return sorted_numbers[left]*sorted_numbers[right]
        elif current_sum > sum:
            right -= 1
        else: 
            left += 1
    return -1

def sum_of_three(nums, sum):
    sorted_numbers = sorted(nums)
    for idx in range(len(sorted_numbers)):
        left = idx + 1
        right = len(sorted_numbers) - 1
        while left < right:
            current_sum = sorted_numbers[idx] + sorted_numbers[left] + sorted_numbers[right]
            if current_sum == sum:
                return sorted_numbers[idx]*sorted_numbers[left]*sorted_numbers[right]
            elif current_sum > sum:
                right -= 1
            else:
                left += 1
    return -1

if __name__ == '__main__':
    with open('day01/input.txt') as f:
        numbers = []
        for line in f:
            numbers.append(int(line))

    TARGET_SUM = 2020
    print("Tagret sum is {}".format(TARGET_SUM))
    print("Multiplication of two numbers that sum to {} is {}".format(TARGET_SUM, sum_of_two(numbers, TARGET_SUM)))
    print("Multiplication of three numbers that sum to {} is {}".format(TARGET_SUM, sum_of_three(numbers, TARGET_SUM)))