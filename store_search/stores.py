import logging

from requests import Request


class Store:
    def __init__(self, name, base_url, search_field, params):
        self.name = name
        self.base_url = base_url
        self.params = params or {}
        self.search_field = search_field
        self.logger = logging.getLogger(__name__)

    def url(self, query):
        search = {self.search_field: query}
        params = {**self.params, **search}

        req = Request("GET", self.base_url, params=params)
        url = req.prepare().url
        return url


class QFC(Store):
    details = {
        "name": "QFC",
        "base_url": "https://www.qfc.com/search",
        "search_field": "query",
    }

    def __init__(self, params=None):
        super().__init__(**self.details, params=params)


class Target(Store):
    details = {
        "name": "Target",
        "base_url": "https://www.target.com/s",
        "search_field": "searchTerm",
    }

    def __init__(self, params=None):
        super().__init__(**self.details, params=params)


class FredMeyer(Store):
    details = {
        "name": "Fred Meyer",
        "base_url": "https://www.fredmeyer.com/search",
        "search_field": "query",
    }

    def __init__(self, params=None):
        super().__init__(**self.details, params=params)


class Safeway(Store):
    details = {
        "name": "Safeway",
        "base_url": "https://shop.safeway.com/search-results.html",
        "search_field": "q",
    }

    def __init__(self, params=None):
        super().__init__(**self.details, params=params)


class WholeFoods(Store):
    details = {
        "name": "Whole Foods",
        "base_url": "https://products.wholefoodsmarket.com/search",
        "search_field": "text",
    }

    def __init__(self, params=None):
        super().__init__(**self.details, params=params)
