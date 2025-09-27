#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get deletion-resilient hypermedia pagination information

        Args:
            index (int): The start index (default: None)
            page_size (int): The number of items per page (default: 10)

        Returns:
            Dict: Dictionary containing pagination metadata
        """
        indexed_dataset = self.indexed_dataset()
        total_items = len(indexed_dataset)

        if index is None:
            index = 0

        assert isinstance(index, int) and index >= 0 and index < total_items
        assert isinstance(page_size, int) and page_size > 0

        data = []
        current_index = index
        items_collected = 0

        while current_index < total_items and items_collected < page_size:
            if current_index in indexed_dataset:
                data.append(indexed_dataset[current_index])
                items_collected += 1
            current_index += 1

        next_index = current_index if current_index < total_items else None
 
        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }


if __name__ == "__main__":
    server = Server()

    server.indexed_dataset()

    try:
        server.get_hyper_index(300000, 100)
    except AssertionError:
        print("AssertionError raised when out of range")

    index = 3
    page_size = 2

    print("Nb items: {}".format(len(server._Server__indexed_dataset)))

    # 1- request first index
    res = server.get_hyper_index(index, page_size)
    print(res)

    # 2- request next index
    print(server.get_hyper_index(res.get('next_index'), page_size))

    # 3- remove the first index
    del server._Server__indexed_dataset[res.get('index')]
    print("Nb items: {}".format(len(server._Server__indexed_dataset)))

    # 4- request again index -> the first data retrieves is not the same
    print(server.get_hyper_index(index, page_size))

    # 5- request again initial next index -> same data page as the request 2-
    print(server.get_hyper_index(res.get('next_index'), page_size))
