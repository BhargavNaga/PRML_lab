import numpy as np

def get_matrix_from_user():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    print("Enter the elements of the matrix row-wise:")
    for i in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    return np.array(matrix)

def print_menu():
    print("\n------ Matrix Operations ------")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Scalar Matrix Multiplication")
    print("4. Elementwise Matrix Multiplication")
    print("5. Matrix Multiplication")
    print("6. Matrix Transpose")
    print("7. Trace of a Matrix")
    print("8. Solve System of Linear Equations")
    print("9. Determinant")
    print("10. Inverse")
    print("11. Eigen Value and Eigen Vector")
    print("12. Exit")

def matrix_addition(matrix1, matrix2):
    return matrix1 + matrix2

def matrix_subtraction(matrix1, matrix2):
    return matrix1 - matrix2

def scalar_matrix_multiplication(scalar, matrix):
    return scalar * matrix

def elementwise_matrix_multiplication(matrix1, matrix2):
    return np.multiply(matrix1, matrix2)

def matrix_multiplication(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)

def matrix_transpose(matrix):
    return np.transpose(matrix)

def matrix_trace(matrix):
    return np.trace(matrix)

def solve_linear_equations(matrix, vector):
    return np.linalg.solve(matrix, vector)

def matrix_determinant(matrix):
    return np.linalg.det(matrix)

def matrix_inverse(matrix):
    return np.linalg.inv(matrix)

def matrix_eigen(matrix):
    eigen_values, eigen_vectors = np.linalg.eig(matrix)
    return eigen_values, eigen_vectors

def main():
    while True:
        print_menu()
        choice = int(input("Enter your choice (1-12): "))

        if choice == 1:
            matrix1 = get_matrix_from_user()
            matrix2 = get_matrix_from_user()
            print("Result:")
            print(matrix_addition(matrix1, matrix2))

        elif choice == 2:
            matrix1 = get_matrix_from_user()
            matrix2 = get_matrix_from_user()
            print("Result:")
            print(matrix_subtraction(matrix1, matrix2))

        elif choice == 3:
            scalar = float(input("Enter the scalar: "))
            matrix = get_matrix_from_user()
            print("Result:")
            print(scalar_matrix_multiplication(scalar, matrix))

        elif choice == 4:
            matrix1 = get_matrix_from_user()
            matrix2 = get_matrix_from_user()
            print("Result:")
            print(elementwise_matrix_multiplication(matrix1, matrix2))

        elif choice == 5:
            matrix1 = get_matrix_from_user()
            matrix2 = get_matrix_from_user()
            print("Result:")
            print(matrix_multiplication(matrix1, matrix2))

        elif choice == 6:
            matrix = get_matrix_from_user()
            print("Result:")
            print(matrix_transpose(matrix))

        elif choice == 7:
            matrix = get_matrix_from_user()
            print("Result:")
            print(matrix_trace(matrix))

        elif choice == 8:
            matrix = get_matrix_from_user()
            vector = get_matrix_from_user().flatten()
            print("Result:")
            print(solve_linear_equations(matrix, vector))

        elif choice == 9:
            matrix = get_matrix_from_user()
            print("Result:")
            print(matrix_determinant(matrix))

        elif choice == 10:
            matrix = get_matrix_from_user()
            print("Result:")
            print(matrix_inverse(matrix))

        elif choice == 11:
            matrix = get_matrix_from_user()
            print("Result:")
            eigen_values, eigen_vectors = matrix_eigen(matrix)
            print("Eigen Values:")
            print(eigen_values)
            print("Eigen Vectors:")
            print(eigen_vectors)

        elif choice == 12:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
