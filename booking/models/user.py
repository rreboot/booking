from fastapi_users.db import SQLAlchemyBaseUserTable

from booking.database import Base


class UserTable(Base, SQLAlchemyBaseUserTable):
    pass
