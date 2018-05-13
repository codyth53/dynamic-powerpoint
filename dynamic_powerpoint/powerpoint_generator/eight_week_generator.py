from pptx.slide import Slides, Slide
from .powerpoint_generator import PowerpointGenerator
from .util import _find_sunday, _find_slide_with_name, _find_name_in_iterable
from pptx.shapes.shapetree import GroupShapes
from datetime import datetime, timedelta
from pptx.util import Pt
from pptx.dml.color import RGBColor


def generate_eight_week(pg: PowerpointGenerator, slides: Slides):
    start_date = _find_sunday(pg.config.get_date())

    eight_week_slide: Slide = _find_slide_with_name(slides, 'eight-week')

    for i in range(0, 8):
        week_group = _find_name_in_iterable(eight_week_slide.shapes, 'week' + str(i+1))
        process_week(week_group.shapes, start_date + timedelta(weeks=i))


def process_week(group: GroupShapes, start_date: datetime):
    for i in range(0, 7):
        day_block = _find_name_in_iterable(group, 'day' + str(i+1))
        day_block.text = str((start_date + timedelta(days=i)).day)
        day_block.text_frame.paragraphs[0].font.size = Pt(28)
        day_block.text_frame.paragraphs[0].font.color.rgb = RGBColor.from_string('000000')
