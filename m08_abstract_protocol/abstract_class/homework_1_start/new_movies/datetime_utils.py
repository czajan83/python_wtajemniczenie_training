from datetime import date
from dateutil.relativedelta import relativedelta  # type: ignore


def full_years_between_dates(later: date, earlier: date) -> relativedelta:
    return relativedelta(later, earlier).years
