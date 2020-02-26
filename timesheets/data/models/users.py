import datetime
from typing import List

import sqlalchemy
from sqlalchemy import orm
from timesheets.data.modelbase import SqlAlchemyBase
from timesheets.data.models.timesheet_rows import TimesheetRows


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    first_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    last_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=True)
    # hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True, index=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    last_login = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)

    # noinspection PyUnresolvedReferences
    timesheet_rows = orm.relation("TimesheetRows", order_by=TimesheetRows.date.desc(), back_populates='user')

    # @property
    # def paid_bills(self) -> List[TimesheetRows]:
    #     return [b for b in self.bills if b.paid >= b.total]
    #
    # @property
    # def open_bills(self) -> List[TimesheetRows]:
    #     return [b for b in self.bills if b.paid < b.total]
    #
    # @property
    # def total_owed(self) -> float:
    #     return sum(b.total - b.paid for b in self.open_bills)
    #
    # @property
    # def total_paid_off(self) -> float:
    #     return sum(b.total for b in self.paid_bills)
