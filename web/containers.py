import os
from dependency_injector import containers, providers

from .services.projects import WorkspaceService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=['.views.api'])

    project_service = providers.Factory(
        WorkspaceService,
        workspace_directory=os.getenv('WORKSPACE_DIRECTORY')
    )
