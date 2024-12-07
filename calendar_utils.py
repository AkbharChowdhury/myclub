from datetime import datetime


class CalendarUtils:
    @staticmethod
    def current_year() -> int:
        return datetime.now().year

    @staticmethod
    def current_month() -> str:
        print(datetime.month)
        return datetime.now().strftime("%B")
