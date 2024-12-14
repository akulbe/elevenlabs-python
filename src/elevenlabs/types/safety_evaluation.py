# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .safety_rule import SafetyRule
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class SafetyEvaluation(UncheckedBaseModel):
    """
    Safety evaluation of the agent. Prompt and first message is taken into account.
    The unsafe reason is provided from the evaluation
    """

    is_unsafe: typing.Optional[bool] = None
    llm_reason: typing.Optional[str] = None
    safety_prompt_version: typing.Optional[int] = None
    matched_rule_id: typing.Optional[typing.List[SafetyRule]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
