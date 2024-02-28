from client import Client
from service import Service

import yaml

from dependency_injector import containers, providers

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    client = providers.Singleton(Client, config.client.host, config.client.port)
    service = providers.Factory(Service, client=client, timeout=config.service.timeout)


if __name__=="__main__":
    container = Container()

    container.config.from_yaml("config.yml", loader=yaml.UnsafeLoader)
    
    service = container.service()
    service.report()

