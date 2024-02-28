class Client:
    def __init__(self, host: str, port: str):
        self.host = host
        self.port = port

    def get_info(
        self,
    ):
        return self.host, self.port
