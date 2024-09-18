# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import SyncClientWrapper
import typing
from .types.usage_get_characters_usage_metrics_request_breakdown_type import (
    UsageGetCharactersUsageMetricsRequestBreakdownType,
)
from ..core.request_options import RequestOptions
from ..types.usage_characters_response_model import UsageCharactersResponseModel
from ..core.unchecked_base_model import construct_type
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper


class UsageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_characters_usage_metrics(
        self,
        *,
        start_unix: int,
        end_unix: int,
        include_workspace_metrics: typing.Optional[bool] = None,
        breakdown_type: typing.Optional[UsageGetCharactersUsageMetricsRequestBreakdownType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsageCharactersResponseModel:
        """
        Returns the characters usage metrics for the current user or the entire workspace they are part of. The response will return a time axis with unix timestamps for each day and daily usage along that axis. The usage will be broken down by the specified breakdown type. For example, breakdown type "voice" will return the usage of each voice along the time axis.

        Parameters
        ----------
        start_unix : int
            UTC Unix timestamp for the start of the usage window, in milliseconds. To include the first day of the window, the timestamp should be at 00:00:00 of that day.

        end_unix : int
            UTC Unix timestamp for the end of the usage window, in milliseconds. To include the last day of the window, the timestamp should be at 23:59:59 of that day.

        include_workspace_metrics : typing.Optional[bool]
            Whether or not to include the statistics of the entire workspace.

        breakdown_type : typing.Optional[UsageGetCharactersUsageMetricsRequestBreakdownType]
            How to break down the information. Cannot be "user" if include_workspace_metrics is False.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsageCharactersResponseModel
            Successful Response

        Examples
        --------
        from elevenlabs import ElevenLabs

        client = ElevenLabs(
            api_key="YOUR_API_KEY",
        )
        client.usage.get_characters_usage_metrics(
            start_unix=1,
            end_unix=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/usage/character-stats",
            method="GET",
            params={
                "start_unix": start_unix,
                "end_unix": end_unix,
                "include_workspace_metrics": include_workspace_metrics,
                "breakdown_type": breakdown_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    UsageCharactersResponseModel,
                    construct_type(
                        type_=UsageCharactersResponseModel,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncUsageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_characters_usage_metrics(
        self,
        *,
        start_unix: int,
        end_unix: int,
        include_workspace_metrics: typing.Optional[bool] = None,
        breakdown_type: typing.Optional[UsageGetCharactersUsageMetricsRequestBreakdownType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsageCharactersResponseModel:
        """
        Returns the characters usage metrics for the current user or the entire workspace they are part of. The response will return a time axis with unix timestamps for each day and daily usage along that axis. The usage will be broken down by the specified breakdown type. For example, breakdown type "voice" will return the usage of each voice along the time axis.

        Parameters
        ----------
        start_unix : int
            UTC Unix timestamp for the start of the usage window, in milliseconds. To include the first day of the window, the timestamp should be at 00:00:00 of that day.

        end_unix : int
            UTC Unix timestamp for the end of the usage window, in milliseconds. To include the last day of the window, the timestamp should be at 23:59:59 of that day.

        include_workspace_metrics : typing.Optional[bool]
            Whether or not to include the statistics of the entire workspace.

        breakdown_type : typing.Optional[UsageGetCharactersUsageMetricsRequestBreakdownType]
            How to break down the information. Cannot be "user" if include_workspace_metrics is False.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsageCharactersResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from elevenlabs import AsyncElevenLabs

        client = AsyncElevenLabs(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.usage.get_characters_usage_metrics(
                start_unix=1,
                end_unix=1,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/usage/character-stats",
            method="GET",
            params={
                "start_unix": start_unix,
                "end_unix": end_unix,
                "include_workspace_metrics": include_workspace_metrics,
                "breakdown_type": breakdown_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    UsageCharactersResponseModel,
                    construct_type(
                        type_=UsageCharactersResponseModel,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)