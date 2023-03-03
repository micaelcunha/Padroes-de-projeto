import datetime


class ReservaDataQuery:
    def __init__(self, data_ida: datetime, data_volta: datetime, local_id: int) -> None:
        self.data_ida = data_ida
        self.data_volta = data_volta
        self.local_id = local_id