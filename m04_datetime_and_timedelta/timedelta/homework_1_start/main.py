from datetime import date

from new_movies.cinema_schedule import (
    generate_february_week_schedule,
    weekly_schedule,
    Weekday,
    sort_weekly_schedule,
)


def run_example():
    day_datetime_input = input("Provide day when you would like to go to the cinema in ISO format (YYYY:MM:DD): ")
    day_datetime = date.fromisoformat(day_datetime_input)
    sorted_weekly_schedule = sort_weekly_schedule(weekly_schedule)
    february_week_schedule = generate_february_week_schedule(sorted_weekly_schedule, day_datetime)
    print("During the week containing provided date you can watch:")
    for week_day in Weekday:
        print(f"On {week_day.name}:")
        for movie_showdatetime in february_week_schedule[week_day]:
            print(movie_showdatetime.showdatetime, movie_showdatetime.movie)


if __name__ == "__main__":
    run_example()
