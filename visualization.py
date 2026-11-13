
# ==========================================
# DISK SCHEDULING GRAPH VISUALIZATION
# ==========================================

import matplotlib.pyplot as plt


# 1. Plot individual algorithm graph

def plot_algorithm(sequence, algorithm_name, disk_size):

    steps = list(range(len(sequence)))

    plt.figure(figsize=(10, 5))

    # Plot head movement
    plt.plot(
        steps,
        sequence,
        marker='o',
        linestyle='-',
        linewidth=2,
        markersize=7
    )

    # Display track numbers near points
    for i, track in enumerate(sequence):
        plt.annotate(
            str(track),
            (steps[i], track),
            textcoords="offset points",
            xytext=(0, 8),
            ha='center'
        )

    plt.title(f"{algorithm_name} Disk Scheduling")
    plt.xlabel("Head Movement Sequence")
    plt.ylabel("Disk Track Number")

    plt.xticks(steps)
    plt.yticks(range(0, disk_size, max(1, disk_size // 10)))

    plt.ylim(-5, disk_size + 5)
    plt.grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.show()


# 2. Plot all five algorithm graphs

def plot_all_algorithms(results, disk_size):

    for algorithm_name, data in results.items():

        sequence = data["sequence"]

        plot_algorithm(
            sequence,
            algorithm_name,
            disk_size
        )


# 3. Plot comparison graph of total head movement

def plot_comparison(results):

    algorithms = list(results.keys())

    movements = [
        results[name]["total_movement"]
        for name in algorithms
    ]

    plt.figure(figsize=(9, 5))

    bars = plt.bar(algorithms, movements)

    plt.title("Disk Scheduling Algorithm Comparison")
    plt.xlabel("Scheduling Algorithms")
    plt.ylabel("Total Head Movement (Tracks)")

    # Display values above bars
    for bar in bars:
        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            str(height),
            ha='center',
            va='bottom'
        )

    plt.grid(axis='y', linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.show()
