from pptx.slide import Slide
from pptx.shapes.shapetree import GroupShapes
from pptx.util import Pt
from pptx.dml.color import RGBColor
from .powerpoint_generator import PowerpointGenerator
from datetime import datetime, timedelta


def generate_two_week(pg: PowerpointGenerator, slide: Slide):
    start_date = find_sunday(pg.config.get_date())

    two_week_calendar_group = find_name_in_iterable(slide.shapes, 'dates')
    generate_calendar_dates(two_week_calendar_group.shapes, start_date)


def generate_calendar_dates(group: GroupShapes, start_date: datetime):
    date = start_date
    for textbox in group:
        # assuming textboxes with name 'dayX'
        num = int(textbox.name[3:])
        this_day = date + timedelta(days=(num-1))
        textbox.text = str(this_day.day)
        textbox.text_frame.paragraphs[0].font.size = Pt(28)
        textbox.text_frame.paragraphs[0].font.color.rgb = RGBColor.from_string('000000')


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
