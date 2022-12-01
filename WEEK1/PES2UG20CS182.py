import numpy as np
import pandas as pd


def create_numpy_ones_array(shape: tuple):
    return np.ones(shape)


#Numpy Ones
print(create_numpy_ones_array((5, 6)))


def create_numpy_zeros_array(shape: tuple):
    return np.zeros(shape)


#Numpy Zeros
print(create_numpy_zeros_array((5, 6)))


def create_identity_numpy_array(shape: int):
    return np.identity(shape)


#Numpy Identity Matrix
print(create_identity_numpy_array(4))


def matrix_cofactor(array: np.array):
    return np.linalg.inv(array).T * np.linalg.det(array)


#Cofactor Matrix
print(matrix_cofactor(np.array([[1, 2], [2, 3]])))

def f1(X1, coef1, X2, coef2, seed1, seed2, seed3, shape1, shape2):
    np.random.seed(seed1)
    W1 = np.random.rand(shape1)
    np.random.seed(seed2)
    W2 = np.random.rand(shape2)
    try:
        W = W1*(X1*coef1)+W2(X2**coef2)+seed3
        return W
    except:
        return -1

# Multiple Operations
print(f1(np.array([[1, 2], [3, 4]]), 2, np.array(
    [[5, 6], [2, 1]]), 2, 3, 4, 5, 2, 2))


def fill_with_mode(filename, column):
    file = pd.read_csv(filename)
    mode = file[column].mode()[0]
    file[column].fillna(mode, inplace=True)
    return file


#Fill NaN with Mode
print(fill_with_mode("example.csv", "Attribute A"))


def fill_with_group_average(df, group, column):
    avg = df[column].mean()
    df[column].fillna(avg, inplace=True)
    return df


#Fill NaN with group average
print(fill_with_group_average(pd.read_csv("example.csv"), None, "Attribute A"))


def get_rows_greater_than(df, column):
    return df[df[column] > df[column].mean()]


#Rows with values greater than average
print(get_rows_greater_than(pd.read_csv('example.csv'), 'Attribute B'))