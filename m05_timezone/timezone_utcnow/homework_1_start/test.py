from datetime import datetime, timezone


def main():
    eee = datetime.fromisoformat("2023-03-19 18:04:38+02:00")
    fff = eee.astimezone(timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f')
    print(fff)


if __name__ == "__main__":
    main()
