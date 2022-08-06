import uuid
from dataclasses import field
from datetime import datetime
from marshmallow_dataclass import dataclass as mm_dataclass
from typing import Optional
from dataclasses_json import dataclass_json, Undefined
@dataclass_json(undefined=Undefined.EXCLUDE)
@mm_dataclass(frozen=True)

### Format Data JSON/Dictionary
# {
#     "name": "Randy",
#     "umur": 20
# }
###

class SensorModel:
    #Variabel ajib dikirim ke server
    status: bool #true or false
    speed: float #0.001
    latitude: float
    longitude: float
    movement: bool
    
    #Autogenerate by Database
    created_at: datetime = field(metadata={ #add timestamp
        'dataclasses_json': {
            'encoder': lambda x: datetime.timestamp(x),
        }
    }, default_factory=datetime.utcnow)
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8]) # Generate id

class UserModel:
    name: str
    age: int