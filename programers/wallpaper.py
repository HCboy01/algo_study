def solution(wallpaper):
    lux = len(wallpaper)
    luy = len(wallpaper[0])
    rux = 0
    ruy = 0

    for i in range(len(wallpaper)) :
        for j in range(len(wallpaper[i])) :
            if wallpaper[i][j] == '#':
                if lux > i :
                    lux = i
                if luy > j :
                    luy = j
                if rux < i :
                    rux = i
                if ruy < j :
                    ruy = j
    return([lux, luy, rux + 1, ruy + 1])

print(solution([".....", "....#"]))
