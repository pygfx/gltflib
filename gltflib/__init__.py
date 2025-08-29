version_info = (1, 0, 13)

__version__ = ".".join(map(str, version_info))

from .enums import *
from .models import *
from .utils import *
from .gltf import GLTF
from .gltf_resource import (
    GLTFResource,
    FileResource,
    ExternalResource,
    GLBResource,
    Base64Resource,
    GLB_BINARY_CHUNK_TYPE,
    GLB_JSON_CHUNK_TYPE,
)
