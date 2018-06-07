import copy


class PageRank:
    """
    Calculate rank for each page in the network
    """
    def __init__(self, data_folder, n_iterations, result_file):
        self.data_folder = data_folder
        self.n_iterations = n_iterations
        self.result_file = result_file

    def _read_data(self):
        """
        Read data from file
        :return: list of tuples : (node, link to another node)
        """
        file = open(self.data_folder, "r")
        file_data = file.readlines()[4:]
        file.close()
        return [i.replace('\n', '').split('\t') for i in file_data]

    def _prepared_data(self, data):
        '''
        Prepare data fro algorithm
        :param data: list of tuples : (node, link to another node)
        :return: dict key: edge, value: all nodes linked from the edge.
        Dictionary of weights - key: node, value : 1
        '''
        prepared_dict = {}
        weights = {}

        for i in data:
            for j in i:
                if j not in prepared_dict.keys():
                    prepared_dict[j] = []
                    weights[j] = 1

        for i in data:
            key, value = i[0], i[1]
            prepared_dict[key].append(value)

        return prepared_dict, weights

    def _calculate_rank(self, weights, prepared_dict):
        '''
        Calculates the rank for each page in the network
        :param weights: dictionary of weights - key: node, value : 1
        :param prepared_dict: dict key: edge, value: all nodes linked from the edge.
        :return: dictionary key: node, value: rank of the node
        '''
        n = 0
        weights_new = copy.deepcopy(weights)
        while n <= self.n_iterations:

            weights_new, weights =  copy.deepcopy(weights), copy.deepcopy(weights_new)

            for key in prepared_dict.keys():
                edges = prepared_dict[key]

                if len(edges) != 0:
                    edge_weight = weights[key]/len(edges)

                    for edge in edges:
                        weights_new[edge] += edge_weight

            n += 1

        return weights_new

    def _write_data(self, result):
        """

        :param result: dictionary key: node, value: rank of the node
        :return: None
        """
        with open(self.result_file, 'w') as file:
            sorted_results = sorted(result, key=result.get, reverse=True)
            for key in sorted_results:
                file.write(str(key) + ' : ' + str(result[key]) + '\n')

    def run(self):
        """
        Run all methods of the class to calculate rank of each page in the network
        :return:
        """
        data = self._read_data()
        prepared_dict, weights = self._prepared_data(data)
        result = self._calculate_rank(weights, prepared_dict)
        self._write_data(result)


dataset = 'web-Google.txt'
result_file = 'page_rank_results.txt'
page_rank = PageRank(dataset, 5, result_file)
page_rank.run()
