from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .image_status import Image_status
    from .layer import Layer

@dataclass
class Image(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # CPU architecture
    architecture: Optional[str] = None
    # image digest
    digest: Optional[str] = None
    # CPU features
    features: Optional[str] = None
    # datetime of last pull
    last_pulled: Optional[str] = None
    # datetime of last push
    last_pushed: Optional[str] = None
    # The layers property
    layers: Optional[List[Layer]] = None
    # operating system
    os: Optional[str] = None
    # OS features
    os_features: Optional[str] = None
    # OS version
    os_version: Optional[str] = None
    # size of the image
    size: Optional[int] = None
    # Status of the image
    status: Optional[Image_status] = None
    # CPU variant
    variant: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Image:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Image
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Image()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .image_status import Image_status
        from .layer import Layer

        from .image_status import Image_status
        from .layer import Layer

        fields: Dict[str, Callable[[Any], None]] = {
            "architecture": lambda n : setattr(self, 'architecture', n.get_str_value()),
            "digest": lambda n : setattr(self, 'digest', n.get_str_value()),
            "features": lambda n : setattr(self, 'features', n.get_str_value()),
            "last_pulled": lambda n : setattr(self, 'last_pulled', n.get_str_value()),
            "last_pushed": lambda n : setattr(self, 'last_pushed', n.get_str_value()),
            "layers": lambda n : setattr(self, 'layers', n.get_collection_of_object_values(Layer)),
            "os": lambda n : setattr(self, 'os', n.get_str_value()),
            "os_features": lambda n : setattr(self, 'os_features', n.get_str_value()),
            "os_version": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(Image_status)),
            "variant": lambda n : setattr(self, 'variant', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        from .image_status import Image_status
        from .layer import Layer

        writer.write_str_value("architecture", self.architecture)
        writer.write_str_value("digest", self.digest)
        writer.write_str_value("features", self.features)
        writer.write_str_value("last_pulled", self.last_pulled)
        writer.write_str_value("last_pushed", self.last_pushed)
        writer.write_collection_of_object_values("layers", self.layers)
        writer.write_str_value("os", self.os)
        writer.write_str_value("os_features", self.os_features)
        writer.write_str_value("os_version", self.os_version)
        writer.write_int_value("size", self.size)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("variant", self.variant)
        writer.write_additional_data_value(self.additional_data)
    

