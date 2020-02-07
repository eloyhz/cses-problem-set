# Missing Number
# https://cses.fi/problemset/task/1083

n = int(input())
numbers = [int(x) for x in input().split()]
numbers.sort()
found = False
for i in range(n - 2):
	if numbers[i + 1] - numbers[i] > 1:
		print(numbers[i] + 1)
		found = True
		break
if not found:
	if numbers[0] != 1:
		print(1)
	else:
		print(n)
