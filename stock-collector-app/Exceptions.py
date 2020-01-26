
class ApiCallException(Exception):

    MESSAGE_TEMPLATE = "[ApiCallError] On url: {0}. With error: {1}"

    def __init__(self, *args):
        if args:
            self.exception = args[0]
            self.url = args[1]

    def __str__(self):
        if self.error:
            return ApiCallException.MESSAGE_TEMPLATE.format(self.url, self.exception)
        else:
            return 'ApiCallError has been raised'
