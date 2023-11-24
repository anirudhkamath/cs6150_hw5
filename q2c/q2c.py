import random
import statistics


def main(t):
    arr = [0]  # hold x_i values. first value x_0 = 0
    number_of_origin_crosses = 0
    for i in range(t):
        random_number = random.randrange(0, 100, 1)
        if random_number < 50:
            # move -1
            arr.append(arr[i] - 1)
        else:
            # move +1
            arr.append(arr[i] + 1)
        if arr[i] == 0:
            # origin cross
            number_of_origin_crosses = number_of_origin_crosses + 1

    print(f"{arr[-1]} is the final x_{t} value")
    print(f"number of origin crosses: {number_of_origin_crosses}")
    return number_of_origin_crosses


if __name__ == "__main__":
    t = int(input("Enter the value for t: "))
    total_origin_crosses = 0
    origin_crosses_arr = []
    for turn in range(50):
        origin_crosses = main(t)
        origin_crosses_arr.append(origin_crosses)
        total_origin_crosses = total_origin_crosses + origin_crosses
    print(f"average origin crosses: {total_origin_crosses/50}")
    print(
        "standard deviation of origin crosses:"
        + f"{statistics.stdev(origin_crosses_arr)}"
    )
