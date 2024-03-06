def find_start_points(matrix, checks, rows, cols):
    points = []
    for x in range(rows):
        for y in range(cols):
            if 0 < matrix[x][y] < 6:
                points.append((x, y))
                checks[x][y] = True

    return points


def dfs(matrix, checks, rows, cols):
    stack = find_start_points(matrix, checks, rows, cols)
    while stack:
        cx, cy = stack.pop()
        cam_type = matrix[cx][cy]
        moves = cams[cam_type]

        for i in range(len(moves)):
            dx, dy = moves[i]
            nx = cx + dx
            ny = cy + dy

            if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
                continue
            if checks[nx][ny] != False or matrix[nx][ny] != 0:
                continue

            if matrix[nx][ny] != 6 and checks[nx][ny] == False:
                matrix[nx][ny] = cam_type
                stack.append((cx, cy))
                checks[nx][ny] = True


if __name__ == "__main__":
    n, m = map(int, input().split())
    boards = [list(map(int, input().split())) for _ in range(n)]
    checks = [[False] * m for _ in range(n)]

    cam1 = [(0, 1)] ## 우
    cam2 = [(0, 1), (0, -1)] ## 좌, 우
    cam3 = [(-1, 0), (0, 1)] ## 상, 우
    cam4 = [(-1, 0), (0, -1), (0, 1)] ## 상, 좌, 우
    cam5 = [(-1, 0), (1, 0), (0, -1), (0, 1)] ## 상, 하, 좌, 우
    cams = {1 : cam1, 2 : cam2, 3 : cam3, 4 : cam4, 5 : cam5}

    dfs(boards, checks, n, m)