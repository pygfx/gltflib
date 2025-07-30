import json
from dataclasses import dataclass, asdict
from dataclasses_json import DataClassJsonMixin
from dataclasses_json.core import _decode_dataclass
from typing import List, Optional, Type
from ..utils import del_none
from .accessor import Accessor
from .animation import Animation
from .asset import Asset
from .base_model import BaseModel
from .buffer import Buffer
from .buffer_view import BufferView
from .camera import Camera
from .image import Image
from .material import Material
from .mesh import Mesh
from .node import Node
from .sampler import Sampler
from .scene import Scene
from .skin import Skin
from .texture import Texture
from .attributes import Attributes


@dataclass
class GLTFModel(DataClassJsonMixin, BaseModel):
    accessors: Optional[List[Accessor]] = None
    animations: Optional[List[Animation]] = None
    asset: Asset = None
    buffers: Optional[List[Buffer]] = None
    bufferViews: Optional[List[BufferView]] = None
    cameras: Optional[List[Camera]] = None
    images: Optional[List[Image]] = None
    materials: Optional[List[Material]] = None
    meshes: Optional[List[Mesh]] = None
    nodes: Optional[List[Node]] = None
    samplers: Optional[List[Sampler]] = None
    scene: Optional[int] = None
    scenes: Optional[List[Scene]] = None
    skins: Optional[List[Skin]] = None
    textures: Optional[List[Texture]] = None
    extensionsRequired: Optional[List[str]] = None
    extensionsUsed: Optional[List[str]] = None

    def to_json(self, **kwargs):
        data = del_none(asdict(self))
        return json.dumps(data, **kwargs)
    
    @classmethod
    def from_json(
        cls: Type['GLTFModel'],
        s: str,
        *,
        parse_float=None,
        parse_int=None,
        parse_constant=None,
        infer_missing=False,
        **kw
    ) -> 'GLTFModel':
        
        init_kwargs = json.loads(
            s,
            parse_float=parse_float,
            parse_int=parse_int,
            parse_constant=parse_constant,
            **kw
        )

        result = _decode_dataclass(cls, init_kwargs, infer_missing)
        for mesh in result.meshes:
            for primitive in mesh.primitives:
                raw_attributes = primitive.attributes
                if raw_attributes:
                    attributes = Attributes(**raw_attributes)
                    primitive.attributes = attributes

                raw_targets = primitive.targets
                if raw_targets:
                    primitive.targets = [Attributes(**target) for target in raw_targets]

        return result
