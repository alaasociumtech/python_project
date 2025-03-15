from dataclasses import dataclass

from project.domain.base_entity import BaseEntity


@dataclass
class Member(BaseEntity):
    member_id: int
    name: str
    email: str
