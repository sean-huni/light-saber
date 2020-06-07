class Utility:
    @staticmethod
    def getStrDate() -> str:
        lDateTime = dumps(dt.datetime.now(), indent=4, sort_keys=True, default=str)
        resp = str(lDateTime).strip('"')
        return resp
