from _typeshed import Incomplete

from influxdb_client.domain.statement import Statement

class OptionStatement(Statement):
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, type: Incomplete | None = ..., assignment: Incomplete | None = ...) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    @property
    def assignment(self): ...
    @assignment.setter
    def assignment(self, assignment) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
