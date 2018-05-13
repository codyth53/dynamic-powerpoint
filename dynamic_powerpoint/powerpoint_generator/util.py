from pptx.slide import Slide, Slides
from datetime import datetime, timedelta


def _hide_slide(slide: Slide):
    slide._element.set('show', '0')


def _find_slide_with_name(slides: Slides, name) -> Slide:
    for slide in slides:
        if slide.has_notes_slide:
            if name in slide.notes_slide.notes_text_frame.text:
                return slide
    return None


def _find_sunday(date: datetime) -> datetime:
    if date.weekday() == 6:
        return date
    else:
        return date - timedelta(days=date.isoweekday())


def _find_name_in_iterable(iterable, name):
    target = [x for x in iterable if x.name == name]
    if len(target) == 0:
        return None
    else:
        return target[0]
