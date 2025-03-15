from project.domain.members import Member
from project.infrastructure.database.schema import members
from project.infrastructure.repositories.base_repo import BaseRepository


class MemberRepository(BaseRepository[Member]):
    def __init__(self) -> None:
        super().__init__(Member, members)
