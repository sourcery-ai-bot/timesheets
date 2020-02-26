from typing import Optional

from sqlalchemy.orm import subqueryload

from timesheets.data.db_session import DbSession
from timesheets.data.models.users import User
from timesheets.data.models.timesheet_rows import TimesheetRows


def get_user_by_id(user_id: int, include_timesheets=True) -> Optional[User]:
    session = DbSession.create_session()
    try:
        if not include_timesheets:
            return session.query(User).filter(User.id == user_id).first()
        else:
            return session.query(User) \
                .options(subqueryload(User.timesheet_rows)) \
                .filter(User.id == user_id) \
                .first()
    finally:
        session.close()


def get_timesheet_by_id(timesheet_id: int) -> Optional[TimesheetRows]:
    session = DbSession.create_session()
    try:
        return session.query(TimesheetRows) \
            .filter(TimesheetRows.id == timesheet_id) \
            .first()
    finally:
        session.close()


# def add_payment(amount: float, timesheet_id: int) -> Optional[TimesheetRows]:
#     session = DbSession.create_session()
#     session.expire_on_commit = False
#
#     try:
#         bill = session.query(Bill) \
#             .filter(Bill.id == timesheet_id) \
#             .first()
#
#         if not bill:
#             return None
#
#         bill.paid += amount
#         session.commit()
#
#         return bill
#     finally:
#         session.close()
