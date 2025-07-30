import copy
import json

# Attributes is a special case, it can have custom attrs
class Attributes:
    def __init__(
        self,
        POSITION=None,
        NORMAL=None,
        TANGENT=None,
        TEXCOORD_0=None,
        TEXCOORD_1=None,
        COLOR_0: int = None,
        JOINTS_0: int = None,
        WEIGHTS_0=None,
        *args,
        **kwargs
    ):
        self.POSITION = POSITION
        self.NORMAL = NORMAL
        self.TANGENT = TANGENT
        self.TEXCOORD_0 = TEXCOORD_0
        self.TEXCOORD_1 = TEXCOORD_1
        self.COLOR_0 = COLOR_0
        self.JOINTS_0 = JOINTS_0
        self.WEIGHTS_0 = WEIGHTS_0
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return self.__class__.__qualname__ + '(' + ', '.join([f"{f}={v}" for f, v in self.__dict__.items()]) + ')'

    def to_json(self, *args, **kwargs):
        data = copy.deepcopy(self.__dict__)
        return json.dumps(data)

