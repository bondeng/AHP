def fraction2float(f_str) :
    f_str = f_str.strip()
    temp = f_str.split("/")
    if (len(temp) >= 2) :
        a = float(temp[0])
        b = float(temp[1])
        return a/b
    else :
        return float(f_str)

n = int(input("평가 기준 개수: "))
m = int(input("평가 대안 개수: "))
print()

object = input("최종 목표: ")
print()

c = []
for i in range(0, n) :
    c.append(input("평가 기준 " + str(i+1) + ": "))
print()

a = []
for i in range(0, m) :
    a.append(input("평가 대안 " + str(i+1) + ": "))
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

c_sum = []
for i in range(0, n) :
    sum = 0.0
    for j in range(0, n) :
        sum = sum + c_matrix[j][i]
    c_sum.append(sum)
for i in range(0, n) :
    for j in range(0, n) :
        c_matrix[i][j] = c_matrix[i][j]/c_sum[j]
c_importance = []
for i in range(0, n) :
    sum = 0.0
    for j in range(0, n) :
        sum = sum + c_matrix[i][j]
    c_importance.append(sum/n)
    print(str(i+1)+"번째 평가 기준["+c[i]+"]의 중요도:", sum/n)

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

importance = []
for k in range(0, n) :
    a_sum = []
    for i in range(0, m):
        sum = 0.0
        for j in range(0, m):
            sum = sum + a_matrix[k][j][i]
        a_sum.append(sum)
    for i in range(0, m):
        for j in range(0, m):
            a_matrix[k][i][j] = a_matrix[k][i][j] / a_sum[j]
    a_importance = []
    for i in range(0, m):
        sum = 0.0
        for j in range(0, m):
            sum = sum + a_matrix[k][i][j]
        a_importance.append(sum / m)
    importance.append(a_importance)

# importance[i][j] : i번째 평가 기준에서 j번째 평가 대안의 중요성

priority = []
for i in range(0, m) :
    sum = 0.0
    for j in range(0, n) :
        sum = sum + importance[j][i] * c_importance[j]
    priority.append(sum)
    print(str(i+1)+"번째 평가 대안["+a[i]+"]의 중요도:", sum)

