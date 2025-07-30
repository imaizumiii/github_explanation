def format_text(text, font_size=24):
    """Formats text for display in animations."""
    from manim import Text
    return Text(text, font_size=font_size)

def create_circle(radius=1, color='WHITE'):
    """Creates a circle with the specified radius and color."""
    from manim import Circle
    return Circle(radius=radius, color=color)

def fade_in(mobject, duration=1):
    """Fades in a mobject over the specified duration."""
    from manim import FadeIn
    return FadeIn(mobject, run_time=duration)

def wait_and_fade_out(mobject, duration=1):
    """Waits for a moment and then fades out the mobject."""
    from manim import FadeOut, Wait
    return [Wait(duration), FadeOut(mobject)]