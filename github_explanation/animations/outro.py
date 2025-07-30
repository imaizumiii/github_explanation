from manim import *

class Outro(Scene):
    def construct(self):
        # Create a title for the outro
        title = Text("Thank You for Watching!", font_size=72)
        subtitle = Text("Explore GitHub and start collaborating!", font_size=36)

        # Position the title and subtitle
        title.move_to(UP)
        subtitle.next_to(title, DOWN)

        # Create a closing message
        closing_message = Text("Visit: github.com/your_project", font_size=24)
        closing_message.next_to(subtitle, DOWN)

        # Add all elements to the scene
        self.play(Write(title))
        self.play(Write(subtitle))
        self.play(Write(closing_message))

        # Wait for a moment before ending the scene
        self.wait(3)