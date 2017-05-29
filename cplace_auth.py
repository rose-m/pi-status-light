from requests.auth import AuthBase


class CplaceAuthenticator(AuthBase):
    CPLACE_AUTHENTICATION_HEADER = 'X-Cplace-Api-Token'

    def __init__(self, token):
        if not token:
            raise ValueError('missing token')
        self.token = token

    def __call__(self, request):
        """
        Adds the cplace authentication header
        :param request:
        :type request: requests.Request
        :return:
        """
        request.headers[CplaceAuthenticator.CPLACE_AUTHENTICATION_HEADER] = self.token
        return request
