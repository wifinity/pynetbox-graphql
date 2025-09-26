import pynetbox


def api(*args, **kwargs):
    return ApiWithGraphQl(*args, **kwargs)


class ApiWithGraphQl(pynetbox.api):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gql_url = self.base_url.replace("/api", "/graphql/")

    def gql(self, query):
        payload = {"query": query}
        response = self.http_session.post(
            self.gql_url, json=payload, headers={"Authorization": f"Token {self.token}"}
        )
        return response.json()
