def knapsack(items, max_weight):
    best_values_matrix = []
    for i in range(len(items) + 1):
        best_values_matrix.append({})

    def best_value(row, value):
        if value in best_values_matrix[row]:
            lst = best_values_matrix[row][value]
            return lst
        else:
            weight = values_list[row - 1][1]
            if row == 0: return 0

            if weight > value:
                best_values_matrix[row][value] = 0
                return 0

            else:
                best_values_matrix[row][value] = max(best_value(row - 1, value), best_value(row - 1, value - weight) + values_list[row - 1][0])
                lst = best_values_matrix[row][value]
                return lst

    values_list = sorted(items, key=lambda x: x[1])

    def result_forming(max_weight):
        temp_lst = []
        for i in range(len(values_list), 0, -1):
            if best_value(i, max_weight) != best_value(i- 1, max_weight):
                temp_lst.append(values_list[i - 1])
                max_weight -= values_list[i - 1][1]

        temp_lst.reverse()
        result_items = [items.index(i) for i in temp_lst]
        total_value = sum(i[0] for i in temp_lst)

        return total_value, result_items
    return result_forming(max_weight)
