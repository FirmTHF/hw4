from collections import deque

def maze_solver_with_teleport(maze: list, portals: dict):
    rows, cols = len(maze), len(maze[0])
    
    # ค้นหาตำแหน่งเริ่มต้น (S) และสิ้นสุด (E)
    start, end = None, None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)

    # ถ้าไม่มีจุดเริ่มต้นหรือสิ้นสุด
    if not start or not end:
        return -1, []
    
    # BFS setup
    queue = deque([(start[0], start[1], 0, [start])])  # (row, col, distance, path)
    visited = set()
    visited.add(start)
    
    # ทิศทางการเคลื่อนที่ (ขวา, ซ้าย, ลง, ขึ้น)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        r, c, dist, path = queue.popleft()

        # ถ้าเจอจุดสิ้นสุด 'E'
        if (r, c) == end:
            return dist, path

        # ถ้าอยู่ที่พอร์ทัล ให้เทเลพอร์ตไปยังพอร์ทัลที่เชื่อมต่อก่อนที่จะเดิน
        if (r, c) in portals:
            portal_dest = portals[(r, c)]
            if portal_dest not in visited:
                visited.add(portal_dest)
                # เทเลพอร์ตไม่ต้องเพิ่มระยะทาง (dist) แต่เพิ่มเฉพาะเส้นทาง (path)
                queue.append((portal_dest[0], portal_dest[1], dist, path + [portal_dest]))
                continue  # ข้ามการเดินปกติในกรณีที่ใช้พอร์ทัล

        # สำรวจทิศทางทั้ง 4 ด้าน
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and maze[nr][nc] != '#':
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1, path + [(nr, nc)]))

    # ถ้าไม่มีเส้นทางถึงจุดสิ้นสุด
    return -1, []



if __name__ == "__main__":
    # Example 1
    maze = [
        ['S', '.', '.', 'P'],
        ['#', '#', '.', '#'],
        ['P', '.', '.', 'E'],
        ['#', '#', '#', '#']
    ]

    portals = {
        (0, 3): (2, 0),  # Portal from (0, 3) to (2, 0)
        (2, 0): (0, 3)   # Portal from (2, 0) to (0, 3)
    }

    distance, path = maze_solver_with_teleport(maze, portals)
    print(f"Distance: {distance}, Path: {path}")
    # Output: Distance: 5, Path: [(0, 0), (0, 1), (0, 2), (0, 3), (2, 0), (2, 1), (2, 2), (2, 3)]


    # Example 2
    maze = [
        ['S', '.', '#', 'P', '#', 'P'],
        ['#', '.', '#', '.', '#', '.'],
        ['#', '.', 'P', '.', '.', 'E'],
        ['P', '#', '#', '#', '#', '#'],
        ['#', '.', '.', 'P', '.', '.']
    ]

    portals = {
        (0, 3): (3, 0),  # Portal from (0, 3) to (3, 0)
        (3, 0): (0, 3),  # Portal from (3, 0) to (0, 3)
        (0, 5): (2, 2),  # Portal from (0, 5) to (2, 2)
        (2, 2): (0, 5)   # Portal from (2, 2) to (0, 5)
    }

    distance, path = maze_solver_with_teleport(maze, portals)
    print(f"Distance: {distance}, Path: {path}")
    # Expected Output: Distance: 6, Path: [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (0, 5), (1, 5), (2, 5)]
