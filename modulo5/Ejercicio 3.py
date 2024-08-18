nums = []
nums_length = 0
while True:
    command = input()
    if command == 'end':
        break
    elif command == 'C':
        if nums_length > 0:
            del nums[nums_length - 1]
            nums_length -= 1
    else:
        command = command.split()
        command_length = len(command)
        if command_length == 1:
            nums.append(int(command[0]))
            nums_length += 1
        elif command_length == 2 and 0 < int(command[1]) <= nums_length:
            nums_length -= int(command[1])
            nums = nums[:nums_length]
        elif command_length == 3 and nums_length >= int(command[2]):
            print(*nums[int(command[1]) - 1:int(command[2])], sep='')
