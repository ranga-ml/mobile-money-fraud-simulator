from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Event:

    event_id: str

    timestamp: datetime

    event_type: str

    entity_type: str

    entity_id: str

    actor_id: str | None

    region: str

    metadata: dict