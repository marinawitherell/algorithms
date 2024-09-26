from collections import deque

def is_valid_move(puzzle, x, y):
    """Check if the move is valid."""
    rows, cols = len(puzzle), len(puzzle[0])
    return 0 <= x < rows and 0 <= y < cols and puzzle[x][y] != '#'

def solve_puzzle(Board, Source, Destination):
    if Source == Destination:
        return [Source]

    rows, cols = len(Board), len(Board[0])
    visited = set()
    queue = deque([(Source, [Source], "")])

    while queue:
        (x, y), path, directions = queue.popleft()

        if (x, y) == Destination:
            return path, directions

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy, direction  in [(0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U'), (1, 0, 'D')]:
            nx, ny = x + dx, y + dy
            if is_valid_move(Board, nx, ny):
                new_path = path + [(nx, ny)]
                new_directions = directions + direction
                queue.append(((nx, ny), new_path, new_directions))

    # If destination not reached
    return None

