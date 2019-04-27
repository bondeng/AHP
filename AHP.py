def fraction2float(f_str) :
    f_str = f_str.strip()
    temp = f_str.split("/")
    if (len(temp) >= 2) :
        a = float(temp[0])
        b = float(temp[1])
        return a/b
    else :
        return float(f_str)

n = int(input("평가 기준 개수 : "))
m = int(input("평가 대안 개수 : "))
print()

object = input("최종 목표 : ")
print()

c = []
for i in range(0, n) :
    c.append(input("평가 기준 " + str(i+1) + " : "))
print()

a = []
for i in range(0, m) :
    a.append(input("평가 대안 " + str(i+1) + " : "))
print()

print("# 평가 기준 쌍대 비교")
c_matrix = []
for i in range(0, n) :
    row = []
    for j in range(0, n) :
        row.append(0.0)
    c_matrix.append(row)
for i in range(0, n) :
    for j in range(0, n) :
        if (i == j) :
            c_matrix[i][j] = 1.0
        elif (i > j) :
            c_matrix[i][j] = 1/(c_matrix[j][i])
        else :
            c_matrix[i][j] = fraction2float(input(object+"에 있어서, ["+c[i]+"]이(가) ["+c[j]+"]보다 얼마나 중요한가요?: "))
print()

print("# 평가 기준 쌍대 비교 행렬")
for i in range(0, n) :
    for j in range(0, n) :
        print('%.3f' % c_matrix[i][j], end = " ")
    print()
print()

print("# 열 합계")
c_sum = []
for i in range(0, n) :
    sum = 0.0
    for j in range(0, n) :
        sum = sum + c_matrix[j][i]
    c_sum.append(sum)
for i in range(0, n) :
    print('%.3f' % c_sum[i], end = " ")
print()
print()

print("# 정규화")
for i in range(0, n) :
    for j in range(0, n) :
        c_matrix[i][j] = c_matrix[i][j]/c_sum[j]
for i in range(0, n) :
    for j in range(0, n) :
        print('%.3f' % c_matrix[i][j], end = " ")
    print()
print()

print("# 각 평가 기준의 상대적 중요도")
c_importance = []
for i in range(0, n) :
    sum = 0.0
    for j in range(0, n) :
        sum = sum + c_matrix[i][j]
    c_importance.append(sum/n)
for i in range(0, n) :
    print("["+c[i]+("]의 중요도: %.4f" % c_importance[i]))
print()

print("# 평가 대안 쌍대 비교")
a_matrix = []
for k in range(0, n) :
    temp_matrix = []
    for i in range(0, m) :
        row = []
        for j in range(0, m) :
            row.append(0.0)
        temp_matrix.append(row)
    for i in range(0, m) :
        for j in range(0, m) :
            if (i == j) :
                temp_matrix[i][j] = 1.0
            elif (i > j) :
                temp_matrix[i][j] = 1/(temp_matrix[j][i])
            else :
                temp_matrix[i][j] = fraction2float(input(c[k]+"에 있어서, ["+a[i]+"]이(가) ["+a[j]+"]보다 얼마나 중요한가요?: "))
    a_matrix.append(temp_matrix)
print()

for k in range(0, n) :
    print("# ["+c[k]+"] 쌍대 비교 행렬")
    for i in range(0, m) :
        for j in range(0, m) :
            print('%.3f' % a_matrix[k][i][j], end = " ")
        print()
    print()

importance = []
for k in range(0, n) :
    a_sum = []
    for i in range(0, m):
        sum = 0.0
        for j in range(0, m):
            sum = sum + a_matrix[k][j][i]
        a_sum.append(sum)
    print("# ["+c[k]+"] 열 합계")
    for i in range(0, m) :
        print('%.3f' % a_sum[i], end = " ")
    print()
    print()

    for i in range(0, m):
        for j in range(0, m):
            a_matrix[k][i][j] = a_matrix[k][i][j] / a_sum[j]
    print("# ["+c[k]+"] 정규화")
    for i in range(0, m) :
        for j in range(0, m) :
            print('%.3f' % a_matrix[k][i][j], end = " ")
        print()
    print()

    a_importance = []
    for i in range(0, m):
        sum = 0.0
        for j in range(0, m):
            sum = sum + a_matrix[k][i][j]
        a_importance.append(sum / m)
    importance.append(a_importance)
    print("# ["+c[k]+"]에 있어서 각 평가 대안의 상대적 중요도")
    for i in range(0, m) :
        print("["+a[i]+("]의 중요도: %.4f" % a_importance[i]))
    print()

# importance[i][j] : i번째 평가 기준에서 j번째 평가 대안의 중요성

print("# 결론 : 각 평가 대안의 중요도")
priority = []
for i in range(0, m) :
    sum = 0.0
    for j in range(0, n) :
        sum = sum + importance[j][i] * c_importance[j]
    priority.append(sum)
    print("["+a[i]+("]의 중요도: %.3f" % sum))
