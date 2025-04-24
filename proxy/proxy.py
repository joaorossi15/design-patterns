import requests


class Service:
    def get_values(self, name: str) -> int:
        pass


class RemoteService(Service):
    def __init__(self) -> None:
        super().__init__()
        self.api_url = 'https://api.agify.io'

    def get_values(self, name):
        print(f"fetching data for {name}...")
        name = requests.get(url=self.api_url, params={'name': name})
        return name.json()['age']


class RemoteServiceProxy(Service):
    def __init__(self) -> None:
        super().__init__()
        self.real_service = RemoteService()
        self.cache = {}

    def get_values(self, name):
        if name in self.cache:
            print(f'returning cached value for {name}')
            return self.cache[name]
        value = self.real_service.get_values(name)
        self.cache[name] = value
        return value
