import numpy as np 
import matplotlib.pyplot as plt

# e_swish_2
arr_e_swish_2_acc_train = np.array([
	40.27, 56.11, 62.84, 66.48, 69.09, 70.96, 72.45, 73.63, 74.54, 75.69,
	76.34, 76.64, 77.70, 77.90, 78.60, 78.89, 79.44, 79.67, 79.71, 80.20,
	80.65, 80.84, 81.08, 81.31, 81.53, 81.60, 81.99, 82.22, 81.93, 82.27,
	82.27, 82.51, 82.82, 83.01, 83.09, 83.16, 83.43, 83.22, 83.47, 83.39, 
	83.90, 83.68, 84.16, 83.87, 83.98, 84.02, 84.28, 84.26, 84.31, 84.36, 
	84.24, 84.64, 84.61, 84.67, 84.85, 84.72, 84.73, 85.02, 84.78, 84.68, 
	84.92, 85.04, 84.80, 85.16, 85.08, 85.18, 85.24, 85.37, 85.23, 85.39, 
	85.40, 85.36, 85.35, 85.39, 85.55
	])

arr_e_swish_2_acc_test = np.array([
	58.59, 65.36, 69.08, 72.68, 74.98, 77.76, 77.97, 78.08, 80.26, 80.34,
	81.01, 80.58, 82.22, 82.62, 83.33, 82.48, 82.76, 83.76, 84.20, 84.50,
	83.32, 83.91, 85.15, 85.42, 85.94, 86.61, 85.44, 85.69, 85.55, 85.97, 
	87.00, 85.75, 85.90, 86.68, 86.93, 86.89, 86.68, 86.70, 86.96, 87.07,
	87.38, 87.54, 87.18, 87.21, 87.17, 87.41, 87.21, 87.14, 87.75, 87.38,
	87.58, 87.31, 87.52, 88.02, 87.92, 86.69, 87.95, 87.81, 87.79, 87.89,
	87.27, 87.90, 88.31, 87.78, 87.86, 88.01, 87.92, 88.25, 87.14, 87.32,
	87.38, 88.66, 87.94, 87.75, 88.32,
	89.31, 89.44, 89.69, 89.82, 89.34, 89.86, 89.74, 89.60, 89.80, 89.97,
	89.72, 89.80, 89.92, 89.77, 89.62, 89.92, 89.81, 89.86, 89.50, 89.46,
	89.73, 89.64, 89.86, 89.89, 89.71,
	90.13, 90.35, 90.33, 90.60, 90.19, 90.86, 90.33, 90.46, 90.57, 90.25,
	90.31, 90.64, 90.26, 90.46, 90.51, 90.27, 90.23, 90.66, 90.51, 90.36,
	90.89, 90.31, 90.25, 90.48, 90.42,

	90.82, 90.74, 91.05, 90.84, 90.79, 90.76, 90.86, 90.68, 90.96, 90.79,
	90.97, 90.73, 91.11, 90.62, 90.81, 90.87, 90.97, 90.94, 90.79, 91.09,
	91.04, 91.03, 90.89, 90.85, 91.11,
	91.01, 91.27, 91.12, 91.10, 91.19, 91.10, 91.03, 91.04, 91.14, 91.09,
	91.24, 91.03, 91.11, 91.18, 91.30, 91.17, 91.24, 91.16, 91.04, 91.09,
	91.17, 91.11, 91.14, 91.20, 91.40,
	91.33, 91.34, 91.39, 91.23, 91.39, 91.47, 91.28, 91.36, 91.44, 91.32,
	91.37, 91.37, 91.37, 91.30, 91.40, 91.28, 91.34, 91.34, 91.38, 91.16,
	91.34, 91.37, 91.34, 91.38, 91.32,
	91.39, 91.35, 91.30, 91.25, 91.32, 91.41, 91.36, 91.34, 91.35, 91.33,
	91.32, 91.37, 91.42, 91.38, 91.36, 91.37, 91.31, 91.40, 91.39, 91.30,
	91.27, 91.37, 91.42, 91.34, 91.41,
	91.43, 91.41, 91.40, 91.46, 91.44, 91.46, 91.39, 91.43, 91.44, 91.39,
	91.42, 91.42, 91.34, 91.26, 91.30, 91.36, 91.34, 91.34, 91.35, 91.32,
	91.35, 91.38, 91.43, 91.42, 91.45
	])
	# 91.27, 91.34, 91.26, 91.26, 91.42,
	# 91.37, 91.29, 91.45, 91.36, 91.31,
	# 91.31, 91.32, 91.46, 91.38, 91.37


# e_swish_1
arr_e_swish_1_acc_train = np.array([
	0
	])

arr_e_swish_1_acc_test = np.array([
	44.48, 59.80, 69.45, 72.68, 72.15, 75.04, 77.38, 78.66, 79.61, 79.18,
	80.57, 80.08, 81.56, 82.17, 82.66, 82.03, 82.76, 81.87, 83.87, 83.25,
	83.15, 84.53, 84.60, 84.48, 84.20, 83.42, 85.45, 84.21, 85.20, 84.91,
	85.03, 85.23, 84.53, 85.74, 85.38, 84.68, 85.23, 84.92, 85.90, 86.17,
	85.99, 86.21, 85.79, 85.00, 86.68, 86.61, 85.25, 86.97, 86.81, 86.58,
	87.01, 87.18, 86.36, 86.85, 86.76, 87.57, 87.43, 86.94, 87.18, 86.83,
	87.22, 87.13, 87.64, 86.96, 87.33, 87.60, 87.16, 87.46, 87.58, 87.83,
	87.61, 87.82, 87.46, 88.04, 88.12,
	88.76, 89.06, 88.43, 89.13, 89.32, 88.95, 89.18, 89.30, 89.29, 89.08,
	89.40, 89.01, 89.23, 89.49, 89.05, 88.88, 89.66, 89.28, 89.21, 88.72,
	88.75, 89.54, 89.59, 89.44, 89.36,
	89.70, 90.22, 90.02, 89.99, 90.19, 90.15, 89.87, 90.04, 89.96, 90.23,
	90.05, 89.57, 90.03, 90.35, 90.25, 89.94, 89.98, 90.09, 90.24, 90.18,
	89.96, 89.89, 90.27, 90.35, 90.06,
	90.42, 90.37, 90.65, 90.49, 90.65, 90.67, 90.63, 90.51, 90.75, 90.55,
	90.83, 90.75, 90.81, 90.60, 90.80, 90.57, 90.58, 90.72, 90.54, 90.57,
	90.58, 90.83, 90.74, 90.91, 90.51,
	90.77, 90.94, 90.95, 90.83, 90.77, 90.78, 90.82, 90.87, 90.97, 90.98,
	91.13, 91.08, 91.30, 91.23, 91.05, 91.01, 90.93, 91.04, 91.01, 91.00,
	91.11, 90.81, 90.93, 91.04, 90.98,
	91.10, 91.13, 91.08, 91.10, 91.15, 91.08, 91.02, 91.13, 91.09, 91.11,
	91.15, 91.04, 91.15, 91.14, 91.18, 91.19, 91.39, 91.10, 91.17, 91.20,
	91.23, 91.17, 91.24, 91.28, 91.18,
	91.15, 91.16, 91.19, 91.23, 91.17, 91.11, 91.16, 91.21, 91.16, 91.17,
	91.18, 91.21, 91.06, 91.17, 91.24, 91.18, 91.13, 91.18, 91.19, 91.14,
	91.25, 91.10, 91.19, 91.18, 91.16,
	91.22, 91.20, 91.19, 91.23, 91.16, 91.18, 91.12, 91.19, 91.22, 91.20,
	91.16, 91.12, 91.18, 91.16, 91.17, 91.24, 91.18, 91.12, 91.22, 91.29,
	91.16, 91.23, 91.25, 91.22, 91.24
	])


# swish
arr_swish_acc_train  = np.array([
	41.88, 57.20, 63.29, 66.74, 69.43, 70.26, 71.97, 73.42, 74.25, 74.82,
	75.00, 76.08, 76.25, 76.57, 77.16, 77.76, 77.93, 78.21, 78.28, 78.78,
	79.11, 79.22, 79.54, 79.89, 79.61, 79.89, 80.37, 80.04, 80.75, 80.84,
	81.04, 81.17, 81.11, 81.18, 81.30, 81.41, 81.63, 81.74, 81.80, 81.82,
	81.90, 80.63, 81.00, 81.33, 82.10, 82.36, 82.54, 82.56, 82.44, 82.87, 
	82.89, 82.77, 82.74, 82.78, 82.76, 82.84, 83.20, 83.15, 83.08, 83.09, 
	83.07, 83.49, 83.61, 83.38, 83.42, 83.27, 83.50, 83.39, 83.79, 83.70, 
	83.65, 83.69, 83.63, 83.95, 83.71
	])

arr_swish_acc_test = np.array([
	47.13, 67.31, 70.21, 73.61, 74.31, 76.89, 78.80, 79.79, 78.76, 78.86,
	79.40, 80.75, 80.40, 81.92, 82.34, 82.01, 82.99, 82.70, 83.11, 83.49,
	83.74, 83.32, 83.43, 84.47, 83.30, 85.01, 83.96, 83.56, 84.08, 85.38, 
	84.89, 86.03, 85.33, 85.70, 84.59, 85.88, 85.01, 85.36, 85.76, 85.45, 
	86.35, 83.91, 84.50, 85.12, 85.79, 86.35, 85.36, 86.09, 86.55, 85.80, 
	86.38, 86.69, 86.12, 86.84, 86.66, 86.05, 86.49, 86.04, 86.71, 86.29, 
	86.72, 87.47, 86.21, 87.00, 87.09, 86.71, 87.12, 86.31, 86.84, 86.05, 
	86.34, 86.51, 87.20, 87.23, 86.82,
	88.41, 88.58, 88.53, 88.98, 88.25, 88.67, 88.66, 88.53, 88.61, 88.78, 
	88.51, 88.76, 89.15, 89.22, 88.48, 88.86, 88.77, 89.08, 88.72, 89.19, 
	88.53, 88.62, 89.07, 89.13, 89.14,
	89.30, 89.75, 89.55, 89.54, 89.34, 89.30, 89.66, 89.20, 89.70, 89.47, 
	89.63, 89.48, 89.53, 89.76, 89.39, 89.41, 89.61, 89.75, 89.77, 89.68, 
	89.71, 89.95, 89.59, 89.96, 89.70, 

	89.68, 89.78, 90.04, 90.22, 89.99, 90.12, 90.12, 90.08, 90.21, 90.05,
	89.95, 90.31, 90.06, 90.41, 90.38, 90.49, 90.40, 90.26, 90.51, 90.00,
	90.14, 90.32, 90.38, 90.22, 90.41,
	90.49, 90.44, 90.48, 90.31, 90.38, 90.43, 90.32, 90.46, 90.47, 90.41,
	90.51, 90.38, 90.48, 90.36, 90.42, 90.39, 90.36, 90.22, 90.50, 90.53,
	90.34, 90.59, 90.40, 90.32, 90.47,
	90.62, 90.41, 90.59, 90.48, 90.59, 90.56, 90.75, 90.61, 90.57, 90.61,
	90.66, 90.38, 90.73, 90.56, 90.64, 90.79, 90.68, 90.72, 90.81, 90.68,
	90.75, 90.69, 90.69, 90.80, 90.62,
	90.66, 90.69, 90.61, 90.64, 90.82, 90.74, 90.85, 90.68, 90.71, 90.76,
	90.66, 90.63, 90.66, 90.62, 90.64, 90.76, 90.78, 90.78, 90.67, 90.70,
	90.74, 90.72, 90.78, 90.89, 90.70,
	90.67, 90.73, 90.66, 90.67, 90.63, 90.67, 90.64, 90.67, 90.65, 90.77,
	90.68, 90.67, 90.75, 90.70, 90.63, 90.62, 90.69, 90.71, 90.64, 90.66,
	90.74, 90.75, 90.68, 90.68, 90.58
	])
	# 90.57, 90.49, 90.46, 90.42, 90.54,
	# 90.57, 90.54, 90.53, 90.54, 90.64,
	# 90.56, 90.57, 90.60, 90.60, 90.70

# ReLU
arr_relu_acc_train  = np.array([
	41.23, 56.78, 62.44, 65.01, 66.99, 68.17, 70.17, 70.66, 71.25, 73.16,
	72.78, 73.45, 74.36, 74.60, 75.51, 75.87, 76.64, 76.80, 77.39, 77.77, 
	77.98, 77.96, 78.39, 78.94, 78.81, 79.29, 79.57, 79.92, 80.09, 80.16, 
	80.50, 80.11, 80.44, 80.57, 80.67, 81.09, 80.89, 81.02, 81.09, 81.15,
	81.38, 81.13, 81.41, 81.90, 81.76, 82.08
	])

arr_relu_acc_test = np.array([
	50.36, 65.05, 64.17, 71.95, 70.28, 75.51, 76.57, 76.61, 76.66, 75.13, 
	76.97, 78.90, 79.38, 81.17, 80.71, 80.40, 81.84, 81.64, 81.72, 82.01,
	82.35, 83.33, 83.09, 84.14, 83.80, 83.83, 83.30, 82.08, 83.25, 84.29,
	84.05, 83.16, 84.19, 84.02, 84.58, 84.25, 84.91, 83.39, 85.68, 85.11, 
	85.05, 84.84, 84.93, 84.48, 85.54, 85.05, 85.39, 85.25, 85.99, 84.90,
	86.01, 85.53, 85.93, 86.08, 86.35, 86.51, 85.07, 86.37, 86.15, 86.10,
	85.96, 86.73, 86.37, 86.06, 86.87, 86.54, 86.73, 86.67, 86.91, 86.57, 
	85.65, 85.92, 86.42, 86.20, 86.99,
	88.47, 88.67, 88.10, 88.50, 89.10, 88.37, 89.11, 88.92, 89.01, 88.70, 
	88.63, 88.81, 88.98, 89.34, 88.53, 88.74, 89.04, 88.37, 88.97, 88.87,
	89.06, 88.80, 88.83, 88.63, 88.89,
	89.49, 89.45, 89.44, 89.50, 89.54, 89.55, 89.42, 89.08, 89.52, 89.88,
	89.44, 89.77, 89.54, 89.86, 89.82, 89.79, 89.68, 89.67, 89.59, 89.30,
	89.50, 89.89, 89.99, 89.63, 90.12,

	90.31, 90.20, 90.30, 90.27, 90.31, 90.27, 90.28, 90.25, 90.50, 90.50,
	90.45, 90.47, 90.22, 90.10, 90.36, 90.28, 90.34, 90.44, 90.68, 90.52,
	90.42, 90.26, 90.40, 90.48, 90.66,
	90.64, 90.87, 90.79, 90.87, 90.81, 90.72, 90.71, 90.95, 90.92, 90.69,
	90.79, 90.86, 90.79, 90.83, 90.80, 90.66, 90.77, 90.95, 90.85, 90.73,
	90.80, 91.00, 90.92, 90.67, 90.88,
	90.92, 90.93, 91.07, 90.89, 90.95, 91.08, 90.91, 90.96, 91.02, 91.01,
	90.95, 90.83, 91.11, 91.06, 91.08, 91.02, 91.18, 91.12, 91.25, 90.95,
	90.94, 90.92, 91.17, 91.01, 91.02,
	91.06, 91.09, 90.97, 91.03, 91.08, 91.09, 91.10, 91.08, 91.19, 91.17,
	91.17, 91.19, 91.12, 91.07, 91.09, 91.18, 91.19, 91.16, 91.07, 91.13,
	91.13, 91.10, 91.13, 91.10, 91.15,
	91.16, 91.13, 91.23, 91.19, 91.19, 91.27, 91.22, 91.27, 91.14, 91.18,
	91.16, 91.20, 91.14, 91.16, 91.16, 91.20, 91.21, 91.13, 91.17, 91.20,
	91.15, 91.16, 91.19, 91.12, 91.17
	])
	# 91.07, 91.05, 91.06, 91.11, 91.04,
	# 91.11, 91.12, 91.14, 91.08, 91.10, 
	# 91.15, 91.00, 91.22, 91.22, 91.20


# leaky ReLU
arr_leaky_acc_train = np.array([
	39.93, 54.61, 60.8, 63.30, 65.69, 67.44, 69.14, 70.24, 71.31, 72.29, 
	73.37, 73.66, 74.07, 74.87, 75.45, 75.48, 75.90, 76.31, 76.46, 76.65, 
	77.10, 77.39, 77.65, 77.78, 78.08, 78.17, 78.18, 78.53, 78.44, 78.57,
	78.89, 79.23, 79.29, 79.02, 79.45, 79.63, 79.73, 79.74, 79.62, 79.91, 
	80.10, 80.19, 80.24, 80.11, 80.24, 80.55, 80.70, 80.52, 80.80, 80.79, 
	80.68, 80.79, 81.01, 80.89, 81.20, 80.86, 81.18, 81.13, 81.06, 81.30, 
	81.55, 81.39, 81.47, 81.30, 81.44, 81.72, 81.85, 81.33, 81.73, 81.54, 
	81.66, 81.65, 81.83, 82.04, 81.89,
	83.44, 83.85, 83.87, 84.06, 84.12, 84.16, 84.23, 84.53, 84.43, 84.42,
	84.36, 84.56, 84.49, 84.71, 84.77, 84.59, 84.54, 84.59, 84.60, 84.84,
	84.76, 84.96, 84.65, 84.63, 84.84,
	85.38, 85.80, 86.05, 85.82, 86.10, 85.98, 85.91, 86.04, 86.22, 86.20,
	86.43, 86.28, 86.33, 86.39, 86.37, 86.46, 86.30, 86.38, 86.40, 86.47, 
	86.19, 86.50, 86.38, 86.38, 86.58
	])

arr_leaky_acc_test = np.array([
	39.16, 64.29, 69.69, 70.73, 75.68, 74.82, 76.12, 76.96, 78.74, 79.47,
	79.55, 80.12, 80.92, 80.04, 81.19, 81.91, 80.54, 80.02, 81.67, 82.32, 
	82.61, 82.82, 82.63, 82.20, 83.35, 83.30, 84.09, 83.59, 83.43, 83.10, 
	83.38, 83.45, 84.60, 84.01, 84.72, 83.75, 83.24, 83.88, 84.18, 84.88, 
	85.05, 85.28, 84.72, 83.58, 84.69, 83.99, 84.48, 84.87, 85.50, 85.79, 
	85.20, 85.14, 86.19, 85.71, 85.18, 85.51, 84.80, 84.20, 85.74, 86.32, 
	85.57, 86.57, 84.84, 85.84, 85.97, 85.78, 85.62, 85.44, 86.34, 84.91, 
	85.14, 86.24, 86.41, 85.67, 85.65,
	87.68, 87.92, 86.91, 87.76, 87.66, 87.43, 87.84, 87.72, 87.34, 86.94, 
	87.95, 87.71, 88.19, 88.00, 87.60, 87.81, 87.49, 87.78, 88.11, 87.43, 
	87.35, 88.40, 87.95, 87.30, 87.83,
	88.28, 88.64, 88.82, 88.74, 88.78, 88.69, 88.72, 88.48, 89.05, 89.44, 
	88.83, 88.83, 89.08, 88.98, 88.85, 89.16, 88.51, 89.51, 89.10, 89.19,
	89.32, 89.03, 88.78, 88.98, 89.14,

	89.68, 89.69, 89.67, 90.04, 89.88, 90.05, 89.79, 89.44, 90.07, 89.63,
	90.01, 90.10, 89.77, 89.99, 89.75, 90.23, 89.94, 89.87, 90.25, 89.75,
	90.06, 90.00, 89.72, 89.82, 90.12,
	90.35, 90.01, 90.31, 90.20, 90.59, 90.15, 90.25, 90.35, 90.32, 90.63,
	90.61, 90.43, 90.47, 90.27, 90.54, 90.25, 90.34, 90.39, 90.40, 90.31,
	90.44, 90.43, 90.46, 90.23, 90.54,
	90.48, 90.45, 90.43, 90.43, 90.56, 90.49, 90.59, 90.38, 90.51, 90.58,
	90.55, 90.40, 90.56, 90.68, 90.50, 90.42, 90.54, 90.38, 90.82, 90.56,
	90.57, 90.51, 90.58, 90.87, 90.59,
	90.66, 90.66, 90.68, 90.69, 90.67, 90.68, 90.63, 90.66, 90.72, 90.65,
	90.50, 90.76, 90.77, 90.77, 90.60, 90.59, 90.61, 90.82, 90.76, 90.73,
	90.71, 90.72, 90.91, 90.63, 90.78,
	90.90, 90.76, 90.66, 90.70, 90.81, 90.73, 90.68, 90.60, 90.68, 90.66,
	90.65, 90.64, 90.74, 90.71, 90.75, 90.74, 90.64, 90.71, 90.77, 90.64,
	90.67, 90.69, 90.64, 90.71, 90.75
	])


# ELU
arr_elu_acc_train = np.array([
	0
	])

arr_elu_acc_test = np.array([
	58.09, 66.12, 71.87, 73.43, 73.69, 76.96, 78.26, 80.51, 79.66, 82.33,
	81.66, 81.41, 82.79, 83.68, 83.21, 84.26, 84.22, 83.70, 83.33, 85.03,
	84.62, 85.11, 85.11, 85.68, 86.10, 85.44, 84.41, 85.85, 84.94, 86.00,
	86.60, 86.47, 86.20, 85.38, 86.67, 87.25, 85.54, 86.25, 86.37, 86.11, 
	87.05, 86.89, 86.74, 86.57, 87.26, 86.44, 86.69, 87.41, 86.96, 85.75, 
	86.16, 86.92, 86.74, 87.75, 87.74, 87.45, 85.96, 87.91, 86.48, 86.94,
	87.76, 87.45, 87.08, 87.99, 87.75, 88.11, 87.87, 87.69, 87.50, 87.32, 
	88.09, 87.50, 87.60, 87.66, 88.33,
	89.18, 89.42, 89.18, 89.53, 89.53, 89.59, 89.65, 89.54, 89.35, 89.99, 
	89.50, 89.06, 89.21, 89.64, 89.56, 89.41, 89.72, 90.00, 89.68, 89.76, 
	89.64, 89.35, 89.69, 89.77, 89.77,
	90.00, 89.95, 89.95, 90.06, 90.27, 90.20, 89.82, 89.70, 89.86, 90.10, 
	90.05, 90.24, 90.10, 89.90, 90.25, 90.21, 90.62, 90.51, 90.05, 90.04, 
	90.41, 90.29, 90.11, 89.76, 90.20,

	90.39, 90.39, 90.60, 90.74, 90.48, 90.52, 90.33, 90.69, 90.61, 90.60,
	90.70, 90.34, 90.58, 90.53, 90.23, 90.72, 90.35, 90.71, 90.45, 90.42,
	90.36, 90.57, 90.48, 90.87, 90.29,
	90.75, 90.78, 90.77, 90.85, 90.96, 90.72, 90.71, 90.62, 90.75, 90.71,
	90.61, 90.72, 90.92, 90.72, 90.68, 90.85, 91.01, 90.93, 90.78, 90.92,
	90.82, 90.90, 91.20, 90.97, 90.86,
	90.91, 91.03, 91.04, 90.94, 90.99, 90.87, 91.12, 90.84, 90.9, 90.93,
	90.86, 90.98, 91.08, 90.85, 90.92, 90.83, 90.89, 90.88, 90.85, 90.99,
	90.96, 90.89, 91.00, 90.94, 90.94,
	90.90, 91.04, 91.00, 90.99, 91.05, 90.89, 91.00, 90.95, 90.98, 91.07,
	90.99, 90.94, 90.95, 90.94, 90.94, 91.07, 91.12, 90.92, 90.95, 91.04,
	91.01, 91.02, 90.92, 90.98, 91.11,
	91.08, 91.05, 91.06, 91.04, 91.14, 91.11, 91.11, 91.25, 91.07, 90.96,
	91.10, 91.09, 91.18, 91.20, 91.15, 91.09, 91.14, 90.99, 90.96, 91.10,
	91.04, 91.01, 91.00, 91.00, 91.05
	])

	# 90.95, 91.00, 90.99, 90.90, 90.86,
	# 90.94, 91.02, 90.99, 90.95, 91.01,
	# 91.00, 90.90, 91.01, 90.94, 90.98


labels_train = ["acc_train e-swish-2", "acc_train swish", "acc_train relu", "acc_train leaky",
				"acc_train elu", "acc_train e-swish-1"]
labels_test =  ["acc_test e-swish-2", "acc_test swish", "acc_test relu", "acc_test leaky",
				"acc_test elu", "acc_test e-swish-1"]

content_train = [arr_e_swish_2_acc_train, arr_swish_acc_train, arr_relu_acc_train,
				 arr_leaky_acc_train, arr_elu_acc_train, arr_e_swish_1_acc_train]
content_test =  [arr_e_swish_2_acc_test, arr_swish_acc_test, arr_relu_acc_test,
				 arr_leaky_acc_test, arr_elu_acc_test, arr_e_swish_1_acc_test]


def difference(arr_1, arr_2):
	# total = np.sum(arr_e_swish_acc_test - arr_2)
	partial = []
	for i in range(min(int(len(arr_1)/25), int(len(arr_2)/25))+1):
		try:
			partial.append(np.sum(arr_1[i*25:(i+1)*25] - arr_2[i*25:(i+1)*25]))
		except:
			try:
				partial.append(np.sum(arr_1[i*25:191] - arr_2[i*25:191]))
			except:pass

	return partial #, total

for i,act in enumerate(content_test):
	print("Diff with "+labels_test[i], difference(arr_e_swish_2_acc_test, act))


# Training
plt.figure()
plt.title("Accuracy of different activations on CIFAR-10")
plt.xlabel("Number of epochs")
plt.ylabel("Accurary(%)")
plt.grid()
for thing in content_test:
	plt.plot(thing, "-")
	# a = 5
	# plt.plot(np.array([np.sum(thing[i:i+a])/a for i in range(len(thing)-a)]), "-")

# for thing in content_test:
	# plt.plot(thing, '-o')

# labels_train.extend(labels_test)
plt.legend(labels_test, loc="lower right")
# plt.ylim((85,92))
# plt.xlim((60,190))
plt.show()

# Testing
# plt.figure()
# plt.title("Accuracy e-swish vs swish vs relu in testing")
# plt.xlabel("Number of epochs")
# plt.ylabel("Accurary(%)")
# plt.grid()
# for thing in content_test:
#	plt.plot(thing, '-o')

# plt.legend(labels_test, loc="lower right")

# plt.show()
