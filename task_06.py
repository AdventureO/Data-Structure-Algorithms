def tsp(data):
    length_list = []
    path_list = []

    for city in range(len(data)):
        length = 0
        current_city = city
        path = [current_city]
        while len(path) != len(data):
            temp_lst = []
            for i in range(len(data)):
                if i != current_city and i not in path:
                    temp_min = ((data[current_city][0] - data[i][0])**2 + (data[current_city][1] - data[i][1])**2)**0.5
                    temp_lst.append(temp_min)
                    min_way = min(temp_lst)
                    if min_way >= temp_min:
                        min_dis_city = data.index(data[i])

            length += min(temp_lst)
            path.append(min_dis_city)
            current_city = min_dis_city

        length += ((data[current_city][0] - data[city][0])**2 + (data[current_city][1] - data[city][1])**2)**0.5
        path.append(city)
        path_list.append(path)
        length_list.append(length)

    result_length = min(length_list)
    result_path = path_list[length_list.index(result_length)]

    return result_length, result_path

data = [[1380, 939], [2848, 96], [3510, 1671], [457, 334]]

print(tsp(data))
