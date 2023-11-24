import random

def main(voter_arr, sample_size):
    # setup: create a pseudorandom array of values representing voters distributed 52%=+1, 48%=-1
    arr = voter_arr

    sample_arr = []
    # sample from array
    chosen_voters = []
    for i in range(sample_size):
        while True:
            random_number = random.randrange(0, 1000000, 1)
            if random_number not in chosen_voters: # without replacement
                # print(f"picking voter {random_number}")
                sample_arr.append(arr[random_number])
                chosen_voters.append(random_number)
                break
    print(len(sample_arr))
    count_1 = 0
    for i in sample_arr:
        if i == 1: count_1 = count_1 + 1
    if count_1 > sample_size/2:
        return 1
    else: return 0

if __name__ == "__main__":
    sample_size = 1500
    total_count = 0
    arr = []
    for i in range(1000000):
        arr.append(999) # dummy values
    for i in range(520000):
        while True:
            random_number = random.randrange(0, 1000000, 1)
            if arr[random_number] == 999:
                arr[random_number] = 1
                break
    for i in range(480000):
        while True:
            random_number = random.randrange(0, 1000000, 1)
            if arr[random_number] == 999:
                arr[random_number] = -1
                break
    for i in range(100):
        print(f"experiment #{i}")
        res = main(voter_arr=arr, sample_size=sample_size)
        if res == 1: print("sample saw same majority")
        elif res == 0: print("sample did not see same majority")
        total_count = total_count + res
    print(f"probability of getting a sample where majority stays a majority: {total_count/100}")
