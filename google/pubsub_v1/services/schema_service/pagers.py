# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core import retry_async as retries_async
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Sequence,
    Tuple,
    Optional,
    Iterator,
    Union,
)

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
    OptionalAsyncRetry = Union[
        retries_async.AsyncRetry, gapic_v1.method._MethodDefault, None
    ]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore
    OptionalAsyncRetry = Union[retries_async.AsyncRetry, object, None]  # type: ignore

from google.pubsub_v1.types import schema


class ListSchemasPager:
    """A pager for iterating through ``list_schemas`` requests.

    This class thinly wraps an initial
    :class:`google.pubsub_v1.types.ListSchemasResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``schemas`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSchemas`` requests and continue to iterate
    through the ``schemas`` field on the
    corresponding responses.

    All the usual :class:`google.pubsub_v1.types.ListSchemasResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., schema.ListSchemasResponse],
        request: schema.ListSchemasRequest,
        response: schema.ListSchemasResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.pubsub_v1.types.ListSchemasRequest):
                The initial request object.
            response (google.pubsub_v1.types.ListSchemasResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = schema.ListSchemasRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[schema.ListSchemasResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __iter__(self) -> Iterator[schema.Schema]:
        for page in self.pages:
            yield from page.schemas

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSchemasAsyncPager:
    """A pager for iterating through ``list_schemas`` requests.

    This class thinly wraps an initial
    :class:`google.pubsub_v1.types.ListSchemasResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``schemas`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSchemas`` requests and continue to iterate
    through the ``schemas`` field on the
    corresponding responses.

    All the usual :class:`google.pubsub_v1.types.ListSchemasResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[schema.ListSchemasResponse]],
        request: schema.ListSchemasRequest,
        response: schema.ListSchemasResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.pubsub_v1.types.ListSchemasRequest):
                The initial request object.
            response (google.pubsub_v1.types.ListSchemasResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = schema.ListSchemasRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[schema.ListSchemasResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __aiter__(self) -> AsyncIterator[schema.Schema]:
        async def async_generator():
            async for page in self.pages:
                for response in page.schemas:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSchemaRevisionsPager:
    """A pager for iterating through ``list_schema_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.pubsub_v1.types.ListSchemaRevisionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``schemas`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSchemaRevisions`` requests and continue to iterate
    through the ``schemas`` field on the
    corresponding responses.

    All the usual :class:`google.pubsub_v1.types.ListSchemaRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., schema.ListSchemaRevisionsResponse],
        request: schema.ListSchemaRevisionsRequest,
        response: schema.ListSchemaRevisionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.pubsub_v1.types.ListSchemaRevisionsRequest):
                The initial request object.
            response (google.pubsub_v1.types.ListSchemaRevisionsResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = schema.ListSchemaRevisionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[schema.ListSchemaRevisionsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __iter__(self) -> Iterator[schema.Schema]:
        for page in self.pages:
            yield from page.schemas

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSchemaRevisionsAsyncPager:
    """A pager for iterating through ``list_schema_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.pubsub_v1.types.ListSchemaRevisionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``schemas`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSchemaRevisions`` requests and continue to iterate
    through the ``schemas`` field on the
    corresponding responses.

    All the usual :class:`google.pubsub_v1.types.ListSchemaRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[schema.ListSchemaRevisionsResponse]],
        request: schema.ListSchemaRevisionsRequest,
        response: schema.ListSchemaRevisionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.pubsub_v1.types.ListSchemaRevisionsRequest):
                The initial request object.
            response (google.pubsub_v1.types.ListSchemaRevisionsResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = schema.ListSchemaRevisionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[schema.ListSchemaRevisionsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __aiter__(self) -> AsyncIterator[schema.Schema]:
        async def async_generator():
            async for page in self.pages:
                for response in page.schemas:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
