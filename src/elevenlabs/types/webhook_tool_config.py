# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.unchecked_base_model import UncheckedBaseModel
from .array_json_schema_property import ArrayJsonSchemaProperty
from .object_json_schema_property import ObjectJsonSchemaProperty
from .webhook_tool_api_schema_config import WebhookToolApiSchemaConfig
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic
from ..core.pydantic_utilities import update_forward_refs


class WebhookToolConfig(UncheckedBaseModel):
    """
    A webhook tool is a tool that calls an external webhook from our server
    """

    name: str
    description: str
    api_schema: WebhookToolApiSchemaConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ArrayJsonSchemaProperty, WebhookToolConfig=WebhookToolConfig)
update_forward_refs(ObjectJsonSchemaProperty, WebhookToolConfig=WebhookToolConfig)