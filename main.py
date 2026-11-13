
# ==========================================
# DISK SCHEDULING COMPARISON TOOL
# MAIN CONTROLLER
# ==========================================

from comparison import compare_algorithms
from visualization import plot_all_algorithms, plot_comparison


# 1. Take input from user

def get_input():

    print("\n======================================")
    print("       DISK SCHEDULING SIMULATOR")
    print("======================================")

    disk_size = int(input("\nEnter total number of disk tracks: "))

    if disk_size <= 0:
        raise ValueError("Disk size must be positive.")

    head = int(input("Enter initial head position: "))

    if head < 0 or head >= disk_size:
        raise ValueError("Invalid initial head position.")

    n = int(input("Enter number of disk requests: "))

    if n < 0:
        raise ValueError("Number of requests cannot be negative.")

    requests = []

    if n > 0:
        print("Enter disk requests separated by spaces:")
        requests = list(map(int, input().split()))

    if len(requests) != n:
        raise ValueError("Number of requests does not match the input.")

    for request in requests:
        if request < 0 or request >= disk_size:
            raise ValueError(f"Invalid track number: {request}")

    direction = input(
        "Enter initial direction (left/right): "
    ).strip().lower()

    if direction not in ["left", "right"]:
        raise ValueError("Direction must be left or right.")

    seek_time = float(
        input("Enter seek time per track (in ms): ")
    )

    if seek_time < 0:
        raise ValueError("Seek time cannot be negative.")

    return disk_size, head, requests, direction, seek_time


# 2. Display movement sequences

def display_sequences(results):

    print("\n======================================")
    print("       HEAD MOVEMENT SEQUENCES")
    print("======================================")

    for name, data in results.items():

        sequence = data["sequence"]

        print(f"\n{name}:")
        print(" -> ".join(map(str, sequence)))


# 3. Display performance comparison

def display_comparison(results):

    print("\n==============================================")
    print("       PERFORMANCE COMPARISON")
    print("==============================================")

    print(
        f"{'Algorithm':<12}"
        f"{'Total Movement':<18}"
        f"{'Avg Movement':<17}"
        f"{'Avg Seek Time':<15}"
    )

    print("-" * 62)

    for name, data in results.items():

        print(
            f"{name:<12}"
            f"{data['total_movement']:<18}"
            f"{data['average_movement']:<17.2f}"
            f"{data['average_seek_time']:<15.3f}"
        )

    # Find algorithm with minimum head movement

    best_algorithm = min(
        results,
        key=lambda name: results[name]["total_movement"]
    )

    print("\nBest Algorithm (Minimum Head Movement):",
          best_algorithm)


# 4. Main function

def main():

    try:

        # Get user input
        disk_size, head, requests, direction, seek_time = get_input()

        # Run all algorithms and calculate performance
        results = compare_algorithms(
            requests,
            head,
            disk_size,
            direction,
            seek_time
        )

        # Display movement sequences
        display_sequences(results)

        # Display comparison table
        display_comparison(results)

        # Generate individual algorithm graphs
        print("\nDisplaying individual algorithm graphs...")

        plot_all_algorithms(results, disk_size)

        # Generate comparison graph
        print("\nDisplaying performance comparison graph...")

        plot_comparison(results)

    except ValueError as error:

        print("\nInput Error:", error)


# ==========================================
# PROGRAM EXECUTION
# ==========================================

if __name__ == "__main__":
    main()
