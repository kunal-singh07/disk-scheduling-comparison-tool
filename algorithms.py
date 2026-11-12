
# ==========================================
# DISK SCHEDULING ALGORITHMS
# FCFS, SSTF, SCAN, C-SCAN, LOOK
# ==========================================


# 1. FCFS - First Come First Serve

def fcfs(requests, head):
    sequence = [head]

    for request in requests:
        sequence.append(request)

    return sequence


# 2. SSTF - Shortest Seek Time First

def sstf(requests, head):
    pending = requests.copy()
    sequence = [head]

    current = head

    while pending:
        # Find the request nearest to current head
        nearest = min(pending, key=lambda x: abs(x - current))

        sequence.append(nearest)

        # Update head position
        current = nearest

        # Remove completed request
        pending.remove(nearest)

    return sequence


# 3. SCAN - Elevator Algorithm

def scan(requests, head, disk_size, direction):
    sequence = [head]

    left = []
    right = []

    for request in requests:
        if request < head:
            left.append(request)
        elif request > head:
            right.append(request)

    left.sort()
    right.sort()

    if direction.lower() == "right":

        # Move towards higher track numbers
        sequence.extend(right)

        # Reach the right boundary
        if sequence[-1] != disk_size - 1:
            sequence.append(disk_size - 1)

        # Reverse direction
        sequence.extend(reversed(left))

    elif direction.lower() == "left":

        # Move towards lower track numbers
        sequence.extend(reversed(left))

        # Reach the left boundary
        if sequence[-1] != 0:
            sequence.append(0)

        # Reverse direction
        sequence.extend(right)

    else:
        raise ValueError("Direction must be 'left' or 'right'")

    return sequence


# 4. C-SCAN - Circular SCAN

def c_scan(requests, head, disk_size, direction):
    sequence = [head]

    left = []
    right = []

    for request in requests:
        if request < head:
            left.append(request)
        elif request > head:
            right.append(request)

    left.sort()
    right.sort()

    if direction.lower() == "right":

        # Service requests towards right
        sequence.extend(right)

        # Reach the last track
        if sequence[-1] != disk_size - 1:
            sequence.append(disk_size - 1)

        # Jump to track 0
        if left:
            sequence.append(0)

        # Continue in the same direction
        sequence.extend(left)

    elif direction.lower() == "left":

        # Service requests towards left
        sequence.extend(reversed(left))

        # Reach track 0
        if sequence[-1] != 0:
            sequence.append(0)

        # Jump to the last track
        if right:
            sequence.append(disk_size - 1)

        # Continue in the same direction
        sequence.extend(reversed(right))

    else:
        raise ValueError("Direction must be 'left' or 'right'")

    return sequence


# 5. LOOK Algorithm

def look(requests, head, direction):
    sequence = [head]

    left = []
    right = []

    for request in requests:
        if request < head:
            left.append(request)
        elif request > head:
            right.append(request)

    left.sort()
    right.sort()

    if direction.lower() == "right":

        # Move towards higher requests
        sequence.extend(right)

        # Reverse at the last pending request
        sequence.extend(reversed(left))

    elif direction.lower() == "left":

        # Move towards lower requests
        sequence.extend(reversed(left))

        # Reverse at the last pending request
        sequence.extend(right)

    else:
        raise ValueError("Direction must be 'left' or 'right'")

    return sequence


# ==========================================
# TESTING ALL FIVE ALGORITHMS
# ==========================================

if __name__ == "__main__":

    requests = [98, 183, 37, 122, 14, 124, 65, 67]

    head = 53
    disk_size = 200
    direction = "right"

    print("DISK SCHEDULING ALGORITHMS")
    print("=" * 45)

    results = {
        "FCFS": fcfs(requests, head),
        "SSTF": sstf(requests, head),
        "SCAN": scan(requests, head, disk_size, direction),
        "C-SCAN": c_scan(requests, head, disk_size, direction),
        "LOOK": look(requests, head, direction)
    }

    for name, sequence in results.items():

        total_movement = sum(
            abs(sequence[i] - sequence[i - 1])
            for i in range(1, len(sequence))
        )

        print(f"\n{name}")
        print("Sequence:", " -> ".join(map(str, sequence)))
        print("Total Head Movement:", total_movement)
