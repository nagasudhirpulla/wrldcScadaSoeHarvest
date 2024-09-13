from dataclasses import dataclass, field
import json


@dataclass
class JsonConfig:
    esHost: str = field(default="")
    esUname: str = field(default="")
    esPwd: int = field(default="")
    esSoeIndex: str = field(default="")
    soeFilesBaseUrl: str = field(default="")
    daysOffset: int = field(default=1)


def loadJsonConfig(fName="config/config.json") -> JsonConfig:
    global jsonConfig
    with open(fName) as f:
        data = json.load(f)
        jsonConfig = JsonConfig(**data)
        return jsonConfig


# def getJsonConfig() -> JsonConfig:
#     global jsonConfig
#     return jsonConfig
