from typing import Any
from uuid import UUID

from project.infrastructure.database.schema import members
from project.infrastructure.repositories.members_repo import MemberRepository
from project.infrastructure.unit_of_work import UnitOfWork


class MemberService:
    def __init__(self) -> None:
        self.member_repo = MemberRepository()

    def get_all_members(self) -> Any:
        with UnitOfWork() as uow:
            return self.member_repo.get_all(uow.connection)

    def get_member_by_id(self, member_id: UUID) -> Any:
        with UnitOfWork() as uow:
            return self.member_repo.get_by_id(uow.connection, member_id, members.c.member_id)

    def add_member(self, data: dict[str, Any]) -> Any:
        with UnitOfWork() as uow:
            return self.member_repo.add(uow.connection, data)

    def update_member(self, member_id: UUID, data: dict[str, Any]) -> Any:
        with UnitOfWork() as uow:
            existing = self.member_repo.get_by_id(uow.connection, member_id, members.c.member_id)
            if not existing:
                raise ValueError(f'Member with ID {member_id} not found.')
            self.member_repo.update(uow.connection, member_id, data, members.c.member_id)

    def delete_member(self, member_id: UUID) -> Any:
        with UnitOfWork() as uow:
            existing = self.member_repo.get_by_id(uow.connection, member_id, members.c.member_id)
            if not existing:
                raise ValueError(f'Member with ID {member_id} not found.')
            self.member_repo.delete(uow.connection, member_id, members.c.member_id)
