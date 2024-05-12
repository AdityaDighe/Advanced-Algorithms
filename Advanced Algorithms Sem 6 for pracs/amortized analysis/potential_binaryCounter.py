number = 0
phi_1 = 0
phi = 0
number_1 = 0


for _ in range(10):
    actual_cost = bin(number ^ number_1).count("1")
    phi = bin(number).count("1")
    amortized_cost = actual_cost + phi - phi_1
    print("Number: ",number," Binary: ",str(bin(number))[2:]," Potential: ",phi," Cost: ",actual_cost,"Ammortized Cost: ",amortized_cost)
    phi_1 = phi
    number_1 = number
    number += 1
