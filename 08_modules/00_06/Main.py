from Generator import instance_generator as ig

def sequence(x):
    user_string = x
    low = 0
    up = 1
    flow = 0
    fup = 1
    while up < len(user_string):
        if user_string[up] != user_string[up - 1]:
            if fup - flow < up - low:
                flow, fup = low, up
            low = up
        up += 1
    if fup - flow < up - low:
        flow, fup = low, up
    return print("Najdłuższy ciąg takich samych znaków w kodzie to: ",user_string[flow:fup])

def main():
    x = ig()
    print(x)
    sequence(x)

if __name__ == "__main__":
    main()