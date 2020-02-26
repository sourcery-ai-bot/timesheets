import json
import os
import random
from typing import List

import dateutil.parser
from sqlalchemy.orm import Session

from timesheets.data.db_session import DbSession
from timesheets.data.models.timesheet_rows import TimesheetRows
from timesheets.data.models.users import User


def load_starter_data():
    print("Loading starter data...")
    session = DbSession.create_session()
    if session.query(TimesheetRows).count() > 0:
        session.close()
        print("Data already loaded...")
        return

    session.expire_on_commit = False

    users = add_users(session)
    add_timesheet_rows(users)

    session.commit()
    session.close()


def add_users(session: Session) -> List[User]:
    users = []
    data_file = os.path.join(DbSession.db_folder, 'MOCK_USERS.json')
    with open(data_file, 'r', encoding='utf-8') as fin:
        data = json.load(fin)

    for u in data:
        user = User()
        users.append(user)
        user.email = u.get('email')
        user.first_name = u.get('first_name')
        user.last_name = u.get('last_name')
        # user.created_date = dateutil.parser.parse(u.get('created_date'))
        # user.last_login = dateutil.parser.parse(u.get('last_login'))
        # user.last_login = dateutil.parser.parse(u.get('last_login'))
        # user.hashed_password = u.get('hashed_password')
        session.add(user)

    return users


def add_timesheet_rows(users: List[User]):
    data_file = os.path.join(DbSession.db_folder, 'MOCK_TIMESHEET_ROWS.json')
    with open(data_file, 'r', encoding='utf-8') as fin:
        data = json.load(fin)

    for p in data:
        user = random.choice(users)

        timesheet = TimesheetRows()
        timesheet.date = dateutil.parser.parse(p.get('date'))
        timesheet.client = p.get('client')
        timesheet.hours = p.get('hours')
        timesheet.activity_code = p.get('activity_code')
        timesheet.activity_detail = p.get('activity_detail')
        timesheet.job = p.get('job')
        timesheet.start_time = p.get('start_time')
        timesheet.finish_time = p.get('finish_time')

        # timesheet.description = p.get('description')
        # timesheet.total = int(p.get('total'))
        # timesheet.paid = min(timesheet.total, int(p.get('paid')))

        user.timesheet_rows.append(timesheet)
