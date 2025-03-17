from typing import Any, Generic, Type, TypeVar

from sqlalchemy import Table, delete, insert, select, update
from sqlalchemy.engine import Connection

from project.domain.base_entity import BaseEntity

E = TypeVar('E', bound=BaseEntity)


class BaseRepository(Generic[E]):
    def __init__(self, entity: Type[E], table: Table):
        self.entity = entity
        self.table = table

    def get_all(self, connection: Connection) -> list[E]:
        query = select(self.table)
        result = connection.execute(query)
        rows = result.fetchall()
        return [self.entity(**(row._mapping)) for row in rows]

    def get_by_id(self, connection: Connection, record_id: Any, id_column: Any) -> E | None:
        query = select(self.table).where(id_column == record_id)
        result = connection.execute(query)
        row = result.fetchone()
        return self.entity(**(row._mapping)) if row else None

    def add(self, connection: Connection, data: dict[str, Any]) -> Any:
        primary_key_column = list(self.table.c)[0]
        query = insert(self.table).values(**data).returning(primary_key_column)
        result = connection.execute(query)
        inserted_id = result.scalar()
        return inserted_id

    def update(self, connection: Connection, record_id: Any, data: dict[str, Any], id_column: Any) -> None:
        query = (
            update(self.table)
            .where(id_column == record_id)
            .values(**data)
        )
        connection.execute(query)

    def delete(self, connection: Connection, record_id: Any, id_column: Any) -> None:
        query = delete(self.table).where(id_column == record_id)
        connection.execute(query)
