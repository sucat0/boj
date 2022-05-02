expr = input().split('-')

sum_list = []
for plus_expr in expr:
    sum_list.append(sum(map(int, plus_expr.split('+'))))
print(sum_list[0]-sum(sum_list[1:]))