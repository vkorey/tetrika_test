import dataclasses
from enum import Enum


class EventType(Enum):
    LESSON_START = 0
    LESSON_END = 1
    PUPIL_IN = 2
    PUPIL_OUT = 3
    TUTOR_IN = 4
    TUTOR_OUT = 5


@dataclasses.dataclass
class Event:
    timestamp: int
    type: EventType


def appearance(intervals):
    lesson = intervals["lesson"]
    pupil = intervals["pupil"]
    tutor = intervals["tutor"]
    events = []
    lesson_start, lesson_end = lesson
    lesson_event = Event(timestamp=lesson_start, type=EventType.LESSON_START)
    events.append(lesson_event)
    lesson_event = Event(timestamp=lesson_end, type=EventType.LESSON_END)
    events.append(lesson_event)

    t = EventType.PUPIL_IN
    for ts in pupil:
        e = Event(ts, t)
        events.append(e)
        t = EventType.PUPIL_OUT if t == EventType.PUPIL_IN else EventType.PUPIL_IN

    t = EventType.TUTOR_IN
    for ts in tutor:
        e = Event(ts, t)
        events.append(e)
        t = EventType.TUTOR_OUT if t == EventType.TUTOR_IN else EventType.TUTOR_IN

    sorted_events = sorted(events, key=lambda x: x.timestamp)
    from pprint import pprint as pp

    pp(sorted_events)
    lesson_flag = False
    pupil_flag = False
    tutor_flag = False
    begin = None
    result = 0

    for event in sorted_events:
        pp(event)
        if event.type == EventType.LESSON_START:
            lesson_flag = True
        elif event.type == EventType.LESSON_END:
            lesson_flag = False
        elif event.type == EventType.PUPIL_IN:
            pupil_flag = True
        elif event.type == EventType.PUPIL_OUT:
            pupil_flag = False
        elif event.type == EventType.TUTOR_IN:
            tutor_flag = True
        elif event.type == EventType.TUTOR_OUT:
            tutor_flag = False

        if lesson_flag and pupil_flag and tutor_flag:
            pp("HIT")
            begin = event.timestamp
        else:
            pp("END")
            if begin is not None:
                result += event.timestamp - begin
                begin = None
        print("result", result)

    return result


tests = [
    {
        "data": {
            "lesson": [1594663200, 1594666800],
            "pupil": [
                1594663340,
                1594663389,
                1594663390,
                1594663395,
                1594663396,
                1594666472,
            ],
            "tutor": [1594663290, 1594663430, 1594663443, 1594666473],
        },
        "answer": 3117,
    },
    {
        "data": {
            "lesson": [1594702800, 1594706400],
            "pupil": [
                1594702789,
                1594704500,
                1594702807,
                1594704542,
                1594704512,
                1594704513,
                1594704564,
                1594705150,
                1594704581,
                1594704582,
                1594704734,
                1594705009,
                1594705095,
                1594705096,
                1594705106,
                1594706480,
                1594705158,
                1594705773,
                1594705849,
                1594706480,
                1594706500,
                1594706875,
                1594706502,
                1594706503,
                1594706524,
                1594706524,
                1594706579,
                1594706641,
            ],
            "tutor": [
                1594700035,
                1594700364,
                1594702749,
                1594705148,
                1594705149,
                1594706463,
            ],
        },
        "answer": 3577,
    },
    {
        "data": {
            "lesson": [1594692000, 1594695600],
            "pupil": [1594692033, 1594696347],
            "tutor": [1594692017, 1594692066, 1594692068, 1594696341],
        },
        "answer": 3565,
    },
]

if __name__ == "__main__":
    for i, test in enumerate(tests):
        test_answer = appearance(test["data"])
        assert (
            test_answer == test["answer"]
        ), f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
