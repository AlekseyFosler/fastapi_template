from typing import Annotated
from uuid import UUID

from pydantic import Field

TemplateUserUuid = Annotated[
    UUID,
    Field(title='user_uuid', description='user_uuid'),
]
TemplateStatesUuid = Annotated[
    UUID,
    Field(title='status_uuid', description='status_uuid'),
]
TemplateData = Annotated[
    str,
    Field(title='базовая информация', description='TemplateData'),
]

ATemplateStates = Annotated[
    dict[TemplateStatesUuid, list[TemplateData]],
    Field(
        title='ATemplateStates',
        description='ATemplateStates',
    ),
]
ATemplateUsers = Annotated[
    dict[TemplateUserUuid, list[ATemplateStates]],
    Field(
        title='ATemplateUsers',
        description='ATemplateUsers',
    ),
]
