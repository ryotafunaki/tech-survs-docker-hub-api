from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .namespaces.namespaces_request_builder import NamespacesRequestBuilder

class V2RequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v2
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new V2RequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v2", path_parameters)
    
    @property
    def namespaces(self) -> NamespacesRequestBuilder:
        """
        The namespaces property
        """
        from .namespaces.namespaces_request_builder import NamespacesRequestBuilder

        return NamespacesRequestBuilder(self.request_adapter, self.path_parameters)
    

