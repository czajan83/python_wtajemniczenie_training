from datetime import date

from dateutil.relativedelta import relativedelta


def full_years_between_dates(later: relativedelta, earlier: relativedelta) -> int:
    return relativedelta(later, earlier).years
