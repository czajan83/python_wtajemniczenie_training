from dataclasses import dataclass
from enum import Enum
from zoneinfo import ZoneInfo


@dataclass(frozen=True)
class DateAndTimeFormat:
    date_format: str
    time_format: str
    zone: ZoneInfo

    @property
    def datetime_format(self):
        return f"{self.date_format} {self.time_format}"

    def __str__(self):
        return self.datetime_format


class DatetimePreference(Enum):
    USA = DateAndTimeFormat(date_format="%m/%d/%Y", time_format="%H:%M:%S %z", zone=ZoneInfo("America/New_York"))
    EUROPE = DateAndTimeFormat(date_format="%d.%m.%Y", time_format="%H:%M:%S %z", zone=ZoneInfo("Europe/Warsaw"))
    ISO = DateAndTimeFormat(date_format="%Y-%m-%d", time_format="%H:%M:%S %z", zone=ZoneInfo("Europe/Warsaw"))
    UK = DateAndTimeFormat(date_format="%d/%m/%Y", time_format="%I:%M:%S %p %z", zone=ZoneInfo("UTC"))

    def __str__(self):
        return f"Format {self.name}: {self.value}"

    @classmethod
    def ordered_instances(cls):
        return [instance for instance in cls.__members__.values()]

    @classmethod
    def instance_by_index(cls, index):
        return cls.ordered_instances()[index]
