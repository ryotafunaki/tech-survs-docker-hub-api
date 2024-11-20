from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .image import Image
    from .tag_status import Tag_status

@dataclass
class Tag(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # ID of the user that pushed the tag
    creator: Optional[int] = None
    # compressed size (sum of all layers) of the tagged image
    full_size: Optional[int] = None
    # tag ID
    id: Optional[int] = None
    # The images property
    images: Optional[Image] = None
    # datetime of last update
    last_updated: Optional[str] = None
    # ID of the last user that updated the tag
    last_updater: Optional[int] = None
    # Hub username of the user that updated the tag
    last_updater_username: Optional[str] = None
    # name of the tag
    name: Optional[str] = None
    # repository ID
    repository: Optional[int] = None
    # whether a tag has been pushed to or pulled in the past month
    status: Optional[Tag_status] = None
    # datetime of last pull
    tag_last_pulled: Optional[str] = None
    # datetime of last push
    tag_last_pushed: Optional[str] = None
    # repository API version
    v2: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Tag:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Tag
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Tag()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .image import Image
        from .tag_status import Tag_status

        from .image import Image
        from .tag_status import Tag_status

        fields: Dict[str, Callable[[Any], None]] = {
            "creator": lambda n : setattr(self, 'creator', n.get_int_value()),
            "full_size": lambda n : setattr(self, 'full_size', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "images": lambda n : setattr(self, 'images', n.get_object_value(Image)),
            "last_updated": lambda n : setattr(self, 'last_updated', n.get_str_value()),
            "last_updater": lambda n : setattr(self, 'last_updater', n.get_int_value()),
            "last_updater_username": lambda n : setattr(self, 'last_updater_username', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "repository": lambda n : setattr(self, 'repository', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(Tag_status)),
            "tag_last_pulled": lambda n : setattr(self, 'tag_last_pulled', n.get_str_value()),
            "tag_last_pushed": lambda n : setattr(self, 'tag_last_pushed', n.get_str_value()),
            "v2": lambda n : setattr(self, 'v2', n.get_str_value()),
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
        from .image import Image
        from .tag_status import Tag_status

        writer.write_int_value("creator", self.creator)
        writer.write_int_value("full_size", self.full_size)
        writer.write_int_value("id", self.id)
        writer.write_object_value("images", self.images)
        writer.write_str_value("last_updated", self.last_updated)
        writer.write_int_value("last_updater", self.last_updater)
        writer.write_str_value("last_updater_username", self.last_updater_username)
        writer.write_str_value("name", self.name)
        writer.write_int_value("repository", self.repository)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("tag_last_pulled", self.tag_last_pulled)
        writer.write_str_value("tag_last_pushed", self.tag_last_pushed)
        writer.write_str_value("v2", self.v2)
        writer.write_additional_data_value(self.additional_data)
    

