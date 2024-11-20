from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_namespace_item_request_builder import WithNamespaceItemRequestBuilder

class NamespacesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v2/namespaces
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new NamespacesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v2/namespaces", path_parameters)
    
    def by_namespace(self,namespace: str) -> WithNamespaceItemRequestBuilder:
        """
        Gets an item from the client.v2.namespaces.item collection
        param namespace: Unique identifier of the item
        Returns: WithNamespaceItemRequestBuilder
        """
        if namespace is None:
            raise TypeError("namespace cannot be null.")
        from .item.with_namespace_item_request_builder import WithNamespaceItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["namespace"] = namespace
        return WithNamespaceItemRequestBuilder(self.request_adapter, url_tpl_params)
    

