from collections import deque

text = ''
snake = deque([])
length = 0
while True:
    text = input()
    if text == 'termina':
        if length > 0:
            print('cabeza', snake[0], 'cola', snake[length - 1])
        else:
            print('uroboro vacio')
        break

    elif text == 'engulle':
        if length > 0:
            if snake[0] > snake[length - 1]:
                snake.pop()
            else:
                snake.popleft()
            length -= 1
    else:
        snake.append(int(text.split()[1]))
        length += 1
