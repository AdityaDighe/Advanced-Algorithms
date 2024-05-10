def phi_bc(string: int):
    return bin(string).count("1")


def binary_counter():
    number = 0
    phi_1 = 0
    phi = 0
    number_1 = 0
    for _ in range(0, 10):
        ti = bin(number ^ number_1).count("1")
        phi = phi_bc(number)
        actual_cost = ti
        amortized_cost = actual_cost + phi - phi_1
        phi_1 = phi
        print(
            f"{number}\t\t\t{str(bin(number))[2:]}\t\t\t{phi}\t\t\t{actual_cost}\t\t\t{amortized_cost}"
        )
        number_1 = number
        number += 1


def main():
    print("Number\t\t\tBinary\t\t\tPotential\t\tActual cost\t\tAmortized cost")
    binary_counter()


main()