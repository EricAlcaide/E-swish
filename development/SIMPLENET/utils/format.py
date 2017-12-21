import numpy as np 

def rounder(x):
	if x-int(x) >= 0.5: x += 1
	return int(x)

arr = 10000 * np.array([0.92669999999999997, 0.92800000000000005, 0.92810000000000004, 0.9244, 0.92710000000000004, 0.92510000000000003, 0.92330000000000001, 0.92500000000000004, 0.92600000000000005, 0.92900000000000005, 0.9304, 0.93079999999999996, 0.92679999999999996, 0.92720000000000002, 0.92679999999999996, 0.9294, 0.92269999999999996, 0.92859999999999998, 0.92369999999999997, 0.92479999999999996, 0.92710000000000004, 0.9294, 0.92800000000000005, 0.92679999999999996, 0.92400000000000004])
def format(arr):
	return [rounder(x)/100.0 for x in arr]

print(format(arr))

arr_1 = np.array([]) 

arr_2 = np.array([])

def locate(alpha, arr):
	for i, x in enumerate(arr):
		if x >= alpha:
			return i+1

	return None

# for alpha in [85, 87.5, 89, 90, 90.5, 91]:
	# print("First ", alpha, " : ", locate(alpha, arr_2))