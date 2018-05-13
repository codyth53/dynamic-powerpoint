from pptx.slide import Slide, Slides


def _hide_slide(slide: Slide):
    slide._element.set('show', '0')


def _find_slide_with_name(slides: Slides, name) -> Slide:
    for slide in slides:
        if slide.has_notes_slide:
            if name in slide.notes_slide.notes_text_frame.text:
                return slide
    return None
