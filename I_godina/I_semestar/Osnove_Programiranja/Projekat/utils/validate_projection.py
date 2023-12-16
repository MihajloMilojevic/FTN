from database.models import Projection
from datetime import datetime


class Interval:
    def __init__(self, projection: Projection):
        self.id = projection.id
        self.start = projection.starting_time.hour * 60 + projection.starting_time.minute
        self.start -= self.start % 15
        self.end = projection.ending_time.hour * 60 + projection.ending_time.minute
        self.end += 15 - (self.end % 15)
    def __len__(self):
        return self.end - self.start
    def __le__(self, other: 'Interval'):
        return self.end <= other.start
    def __ge__(self, other: 'Interval'):
        return self.start >= other.end
    def overlap(self, other: 'Interval'):
        return not (self <= other or self >= other)

def validate_projection(new_projection: Projection, all_projections: list[Projection]) -> tuple[str, str]:
    projections_in_hall = [projection for projection in all_projections if projection.hall_id == new_projection.hall_id and projection.id != new_projection.id]
    projections_per_day: list[tuple[str, list[Interval]]] = []
    for day in new_projection.days:
        projections_per_day.append((day, [Interval(projection) for projection in projections_in_hall if day in projection.days]))
    new_interval = Interval(new_projection)
    for projection_in_day in projections_per_day:
        validated_day = validate_projection_day(new_interval, projection_in_day[1])
        if validated_day is not None:
            return (projection_in_day[0], validated_day.id)
    return None
    

def validate_projection_day(new_interval: Interval, interval_list: list[Interval]):
    for interval in interval_list:
        if interval.overlap(new_interval):
            return interval
    return None
