import os
from dependency_injector import containers, providers

from .services.projects import ProjectService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".views"])

    project_service = providers.Factory(
        ProjectService,
    )
