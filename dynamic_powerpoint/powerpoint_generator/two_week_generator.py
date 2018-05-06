from pptx.slide import Slide
from pptx.shapes.shapetree import GroupShapes
from pptx.util import Pt
from pptx.dml.color import RGBColor
from .powerpoint_generator import PowerpointGenerator
from datetime import datetime, timedelta


def generate_two_week(pg: PowerpointGenerator, slide: Slide):
    two_week_calendar_group = slide.shapes[5]
    generate_calendar_dates(two_week_calendar_group.shapes, pg.config.get_date())


def generate_calendar_dates(group: GroupShapes, start_date: datetime):
    date = start_date
    for textbox in group:
        textbox.text = str(date.day)
        textbox.text_frame.paragraphs[0].font.size = Pt(28)
        textbox.text_frame.paragraphs[0].font.color.rgb = RGBColor.from_string('000000')
        date = date + timedelta(days=1)
