def MatrixChallenge(strArr):
    if not strArr:
        return 0

    rows = len(strArr)
    cols = len(strArr[0])
    mat = [[int(ch) for ch in row] for row in strArr]

    # pré-computa vizinhos válidos para cada célula
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    adj = {}
    for r in range(rows):
        for c in range(cols):
            nbrs = []
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    nbrs.append((nr, nc))
            adj[(r, c)] = nbrs

    best = 0
    # percorre todos caminhos de 3 células: (r,c) -> n1 -> n2, sem reuso
    for r in range(rows):
        for c in range(cols):
            v0 = mat[r][c]
            for (r1, c1) in adj[(r, c)]:
                v1 = mat[r1][c1]
                for (r2, c2) in adj[(r1, c1)]:
                    # não pode reutilizar células
                    if (r2, c2) == (r, c) or (r2, c2) == (r1, c1):
                        continue
                    v2 = mat[r2][c2]
                    s = v0 + v1 + v2
                    if s < 10:
                        rr, cc = 0, s
                    else:
                        rr, cc = s // 10, s % 10
                    if 0 <= rr < rows and 0 <= cc < cols:
                        if s > best:
                            best = s
    return best

# exemplos
if __name__ == "__main__":
    print(MatrixChallenge(["345","326","221"]))  # 12
    print(MatrixChallenge(["234","999","999"]))  # 22
    print(MatrixChallenge(["11111","22222"]))    # 4
