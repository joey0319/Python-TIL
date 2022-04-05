# 3차원 배열 (백준 2206 벽부수고 이동하기)

# 벽을 한번 부수고 미로를 찾는 문제에서 3차원 배열을 통해 벽을 부쉈는지 안부쉈는지 정보를 함께 전송
N = 4
visited = [[[0] *2 for _ in range(N)] for _ in range(N)]

# visited[i][j][crack] 순서이다.

# 통로가 0 벽이 1으로 미로가 주어질 때
# bfs를 돌리면서 0을 만나면 안부수고 그대로 가고
# 1을 만나면 부수고 간다.

# 벽을 부수는 경우 Q.append(ni, nj, 1)
# 벽을 부수지 않는 경우 Q.append(ni, nj, crack) / crack에는 0이 들어갈 수도 1이 들어갈 수도 있다.(이미 부순경우 1)
