import xmlrpc.client


class ErrataClient:
    def __init__(self, endpoint_url):
        self.endpoint_url = endpoint_url
        self.proxy = xmlrpc.client.ServerProxy(self.endpoint_url)

    def get_advisory_cdn_file_list(self, adv):
        return self.proxy.get_advisory_cdn_file_list(adv, False)

    def get_advisory_cdn_metadata(self, adv):
        return self.proxy.get_advisory_cdn_metadata(adv, False)


class ErrataHelper:
    def __init__(self, client):
        self.client = client

    @classmethod
    def from_endpoint_url(cls, endpoint_url):
        client = ErrataClient(endpoint_url)
        return cls(client)

    def get_repos(self, adv):
        cdn_file_list = self.client.get_advisory_cdn_file_list(adv)
        repos = [
            repo
            for item in cdn_file_list.values()
            for repo_list in item["rpms"].values()
            for repo in repo_list
        ]
        # remove duplicates from repo list
        repos = list(dict.fromkeys(repos))
        return repos

