from pptx.slide import Slide
from pptx.shapes.shapetree import GroupShapes
from pptx.util import Pt
from pptx.dml.color import RGBColor
from .powerpoint_generator import PowerpointGenerator
from ..calendar_utils import CalendarEvent
from datetime import datetime, timedelta
from typing import List


def generate_two_week(pg: PowerpointGenerator, slide: Slide):
    start_date = find_sunday(pg.config.get_date())

    two_week_calendar_group = find_name_in_iterable(slide.shapes, 'dates')
    generate_calendar_dates(two_week_calendar_group.shapes, start_date)

    events = pg.calendar.get_events(start=start_date, end=start_date + timedelta(days=14))
    event_marker_group = find_name_in_iterable(slide.shapes, 'event-markers')
    generate_event_markers(event_marker_group.shapes, events, start_date)


def generate_calendar_dates(group: GroupShapes, start_date: datetime):
    date = start_date
    for textbox in group:
        # assuming textboxes with name 'dayX'
        num = int(textbox.name[3:])
        this_day = date + timedelta(days=(num-1))
        textbox.text = str(this_day.day)
        textbox.text_frame.paragraphs[0].font.size = Pt(28)
        textbox.text_frame.paragraphs[0].font.color.rgb = RGBColor.from_string('000000')


def generate_event_markers(group: GroupShapes, events: List[CalendarEvent], start_date: datetime):
    for event_group in group:
        # assuming group with name 'eventX'
        num = int(event_group.name[5:])
        this_day = start_date + timedelta(days=(num-1))
        this_day_events = [x for x in events if x.start >= this_day and x.end <= this_day + timedelta(days=1)]
        print("Day {0} has {1} events".format(this_day, len(this_day_events)))
        if len(this_day_events) < 2:
            second_marker = find_name_in_iterable(event_group.shapes, 'event2')
            ele = second_marker.element
            ele.getparent().remove(ele)
        if len(this_day_events) < 1:
            first_marker = find_name_in_iterable(event_group.shapes, 'event1')
            ele = first_marker.element
            ele.getparent().remove(ele)


def find_sunday(date: datetime) -> datetime:
    if date.weekday() == 6:
        return date
    else:
        return date - timedelta(days=date.isoweekday())


def find_name_in_iterable(iterable, name):
    target = [x for x in iterable if x.name == name]
    if len(target) == 0:
        return None
    else:
        return target[0]
