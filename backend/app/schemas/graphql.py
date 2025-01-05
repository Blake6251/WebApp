import strawberry
from typing import List

@strawberry.type
class User:
    id: int
    username: str

@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> List[User]:
        # 예시 데이터
        return [
            User(id=1, username="user1"),
            User(id=2, username="user2")
        ]

schema = strawberry.Schema(query=Query) 