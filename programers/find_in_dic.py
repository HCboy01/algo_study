def solution(spell, dic):
    dicc = {}
    
    for i in range(len(dic)) :
        init_dic(dicc, spell)
        for j in range(len(dic[i])) :
            if (dic[i][j] in spell) :
                dicc[dic[i][j]] += 1
        if chk_dic(dicc, spell) == 1 :
            return (1)
    return (2)

def init_dic(dicc, spell) :
    for i in spell :
        dicc[i] = 0
        
def chk_dic(dicc, spell) :
    
    for i in spell:
        if dicc[i] != 1:
            return (0)
    return (1)

print(solution(	['p', 'o', 's'], ["sod", "eocd", "qixm", "adio", "soo"]))