import datetime
import sqlalchemy
from sqlalchemy import orm
from timesheets.data.modelbase import SqlAlchemyBase


class TimesheetRows(SqlAlchemyBase):
    __tablename__ = 'timesheet_rows'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    client = sqlalchemy.Column(sqlalchemy.String)
    hours = sqlalchemy.Column(sqlalchemy.Float)
    activity_code = sqlalchemy.Column(sqlalchemy.String)
    activity_detail = sqlalchemy.Column(sqlalchemy.String)
    job = sqlalchemy.Column(sqlalchemy.String)
    start_time = sqlalchemy.Column(sqlalchemy.Time)
    finish_time = sqlalchemy.Column(sqlalchemy.Time)

    # User's relationship
    user_id_fk = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    user = orm.relation('User', back_populates='timesheet_rows')

    # @property
    # def is_paid(self):
    #     return self.total <= self.paid
