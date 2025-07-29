# cube = [
#   [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
#   [[10,11,12],[13,14,15],[16,17,18]],
#   [[19,20,21],[22,23,24],[25,26,27]]
# ]

# line = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(sum(line, []))

# print(sum(cube, []))

# print(sum(sum(sum(cube, []), [])))

import matplotlib.pyplot as plt

# Predefined bell patterns
patterns = {
    1: [1],
    2: [2, 2],
    3: [3, 4, 3],
    4: [4, 6, 6, 4],
    5: [5, 8, 9, 8, 5],
    6: [6, 10, 12, 12, 10, 6],
    7: [7, 12, 15, 16, 15, 12, 7],
    8: [8, 14, 18, 20, 20, 18, 14, 8],
    9: [9, 16, 21, 24, 25, 24, 21, 16, 9],
    10: [10, 18, 24, 28, 30, 30, 28, 24, 18, 10],
    11: [11, 20, 27, 32, 35, 36, 35, 32, 27, 20, 11],
    12: [12, 22, 30, 36, 40, 42, 42, 40, 36, 30, 22, 12],
}


# Function to plot each pattern
def plot_bell(n, pattern):
    plt.figure(figsize=(10, 5))
    plt.plot(pattern, marker="o", linestyle="-", color="b")

    # Set plot title and labels
    plt.title(f"Bell Pattern for n = {n}")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)

    # Show the plot
    plt.show()


# Display all predefined bell patterns
# for n, pattern in patterns.items():
# plot_bell(11, patterns[11])
def bell(n):
    # Base cases
    if n == 1:
        return [1]
    elif n == 2:
        return [2, 2]
    elif n == 3:
        return [3, 4, 3]

    # Start with the previous row
    rows = [[1], [2, 2], [3, 4, 3]]  # The first three predefined rows

    for i in range(4, n + 1):
        # Start a new row with first and last value as i
        row = [i]

        # Generate the rest of the row based on the previous row's values
        prev_row = rows[i - 3]  # Get the previous row (i-2 because of zero-indexing)

        # next value in row is whatever i is + prev_row[index of whateverelemt we now look at -1]
        for j in range(1, i - 1):
            row.append(i + prev_row[j - 1])

        # Add the last value to the row
        row.append(i)

        # Add the row to the list of rows
        rows.append(row)

        print(i)
        print(row)

    return rows[n - 1]


# compare the two by plotting them
plt.figure(figsize=(10, 5))
plt.plot(patterns[11], marker="o", linestyle="-", color="b", label="Predefined")
plt.plot(bell(11), marker="x", linestyle="--", color="r", label="Calculated")

# Set plot title and labels
plt.title("Bell Pattern Comparison")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
