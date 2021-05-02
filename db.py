import couchdb


class DB:
    """
        CouchDB API Reference: https://couchdb-python.readthedocs.io/en/latest/
    """

    def __init__(self, url, name):
        self.db = couchdb.Server(url)[name]

    def find(self, short_url=None, long_url=None):
        key = 'short_url' if short_url else 'long_url'
        res_key = 'long_url' if short_url else 'short_url'
        value = short_url if short_url else long_url
        equals_query = {
            "selector": {
                key: {
                    "$eq": value
                }
            }
        }
        print(equals_query)
        res = self.db.find(equals_query)
        res_list = list(res)
        if not res or len(res_list) == 0:
            return None
        return res_list[0][res_key]

    def save(self, doc=None):
        if not doc:
            return
        self.db.save(doc)
