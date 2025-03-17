from typing import Any
from uuid import UUID

from flask import jsonify, request
from flask.views import MethodView

from project.application.member_service import MemberService

member_service = MemberService()


class MemberAPI(MethodView):

    def get(self, member_id: UUID | None = None) -> Any:
        if member_id is None:
            members = member_service.get_all_members()
            return jsonify([member.__dict__ for member in members])
        else:
            member = member_service.get_member_by_id(member_id)
            if not member:
                return jsonify({'message': 'Member not found'}), 404
            return jsonify(member.__dict__)

    def post(self) -> Any:
        data: dict[str, Any] | None = request.json
        if data is None:
            return jsonify({'message': 'Invalid JSON payload'}), 400
        member_id = member_service.add_member(data)
        return jsonify({'message': 'Member added', 'member_id': member_id}), 201

    def patch(self, member_id: UUID) -> Any:
        data: dict[str, Any] | None = request.json
        if data is None:
            return jsonify({'message': 'Invalid JSON payload'}), 400
        try:
            member_service.update_member(member_id, data)
            return jsonify({'message': 'Member updated'})
        except ValueError as e:
            return jsonify({'message': str(e)}), 404

    def delete(self, member_id: UUID) -> Any:
        try:
            member_service.delete_member(member_id)
            return jsonify({'message': 'Member deleted'})
        except ValueError as e:
            return jsonify({'message': str(e)}), 404
