
# ==========================================
# DISK SCHEDULING PERFORMANCE COMPARISON
# ==========================================

from algorithms import fcfs, sstf, scan, c_scan, look


# 1. Calculate Total Head Movement

def calculate_total_movement(sequence):

    total = 0

    for i in range(1, len(sequence)):
        total += abs(sequence[i] - sequence[i - 1])

    return total


# 2. Calculate Average Head Movement

def calculate_average_movement(total_movement, total_requests):

    if total_requests == 0:
        return 0

    return total_movement / total_requests


# 3. Calculate Total Seek Time

def calculate_total_seek_time(total_movement, seek_time_per_track):

    return total_movement * seek_time_per_track


# 4. Calculate Average Seek Time

def calculate_average_seek_time(total_seek_time, total_requests):

    if total_requests == 0:
        return 0

    return total_seek_time / total_requests


# 5. Compare All Algorithms

def compare_algorithms(requests, head, disk_size, direction,
                       seek_time_per_track=0.1):

    # Get movement sequences from algorithms.py

    results = {
        "FCFS": fcfs(requests, head),

        "SSTF": sstf(requests, head),

        "SCAN": scan(requests, head, disk_size, direction),

        "C-SCAN": c_scan(requests, head, disk_size, direction),

        "LOOK": look(requests, head, direction)
    }

    comparison = {}

    for name, sequence in results.items():

        # Calculate total movement
        total = calculate_total_movement(sequence)

        # Calculate average movement
        average = calculate_average_movement(total, len(requests))

        # Calculate total seek time
        total_seek = calculate_total_seek_time(
            total, seek_time_per_track
        )

        # Calculate average seek time
        average_seek = calculate_average_seek_time(
            total_seek, len(requests)
        )

        comparison[name] = {
            "sequence": sequence,
            "total_movement": total,
            "average_movement": average,
            "total_seek_time": total_seek,
            "average_seek_time": average_seek
        }

    return comparison


# ==========================================
# TESTING COMPARISON MODULE
# ==========================================

if __name__ == "__main__":

    requests = [98, 183, 37, 122, 14, 124, 65, 67]

    head = 53
    disk_size = 200
    direction = "right"

    seek_time_per_track = 0.1  # milliseconds

    results = compare_algorithms(
        requests,
        head,
        disk_size,
        direction,
        seek_time_per_track
    )

    print("\nDISK SCHEDULING PERFORMANCE COMPARISON")
    print("=" * 85)

    print(
        f"{'Algorithm':<12}"
        f"{'Total Movement':<20}"
        f"{'Avg Movement':<18}"
        f"{'Avg Seek Time':<18}"
    )

    print("-" * 85)

    for name, data in results.items():

        print(
            f"{name:<12}"
            f"{data['total_movement']:<20}"
            f"{data['average_movement']:<18.2f}"
            f"{data['average_seek_time']:<18.2f}"
        )

    # Find algorithm with minimum head movement

    best_algorithm = min(
        results,
        key=lambda name: results[name]["total_movement"]
    )

    print("\nBest Algorithm (Minimum Head Movement):", best_algorithm)
