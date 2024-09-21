"""
@Author: Alice-Yuan
@File: PageHelper.py
@Time: 2024/09/17 16:08
"""
from fastapi.encoders import jsonable_encoder


class Page:
    pageList: list
    total: int
    pageNum: int
    pageSize: int

    def __init__(self, pageList: list, total: int, pageNum: int, pageSize: int):
        self.pageList = pageList
        self.total = total
        self.pageNum = pageNum
        self.pageSize = pageSize


class PageHelper:
    page: int
    size: int
    limit: int
    offset: int

    def __init__(self, page: int, size: int, limit: int, offset: int):
        self.page = page
        self.size = size
        self.limit = limit
        self.offset = offset

    @classmethod
    def start_page(cls, page: int, size: int):
        limit = size
        offset = (page - 1) * size
        return cls(page, size, limit, offset)

    def of(self, data):
        data_list = [jsonable_encoder(item) for item in data[self.offset:self.offset + self.limit]]
        data_total = len(data)
        page = Page(data_list, data_total, self.page, self.size)
        return jsonable_encoder(page)
