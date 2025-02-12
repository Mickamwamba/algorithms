from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.openai import OpenAIService


class ShellSortVisualization(VoiceoverScene):
    def construct(self):
        # self.set_speech_service(GTTSService(lang="en"))
         # self.set_speech_service(GTTSService(lang="en"))
        self.set_speech_service(
            OpenAIService(
                voice="echo",
                model="tts-1-hd",
            )
        )

        arr = [9, 8, 3, 7, 5, 6, 4, 1]  # Example array
        n = len(arr)

        squares = VGroup(*[Square(side_length=1).shift(RIGHT * i) for i in range(n)]).move_to(ORIGIN)
        labels = VGroup(*[Text(str(num), font_size=36).move_to(square) for num, square in zip(arr, squares)])

        self.play(Create(squares), Write(labels))
        self.wait(1)

        gap = n // 2
        while gap > 0:
            with self.voiceover(f"Starting with a gap of {gap}"):
                pass
            gap_text = Text(f"Gap = {gap}", font_size=36).to_edge(LEFT)
            self.play(Write(gap_text))
            self.wait(1)

            for start in range(gap):
                indices = list(range(start, n, gap))
                sublist_elements = [arr[i] for i in indices]

                # Create sublist visualization
                sublist_squares = [squares[i].copy().shift(UP * 1.5) for i in indices]
                sublist_labels = [labels[i].copy().shift(UP * 1.5) for i in indices]

                self.play(Create(VGroup(*sublist_squares)), Create(VGroup(*sublist_labels)))
                self.wait(1)

                with self.voiceover(f"Sorting sublist: {sublist_elements}"):
                    self.play(VGroup(*sublist_squares).animate.set_color(YELLOW), VGroup(*sublist_labels).animate.set_color(YELLOW))
                    self.wait(1)

                # Sort the sublist
                sorted_sublist_elements = sorted(sublist_elements)

                # Update the original array with sorted elements
                for k, index in enumerate(indices):
                    arr[index] = sorted_sublist_elements[k]

                # Animate sorted placement back into the original list
                for k, index in enumerate(indices):
                    # Create a new label for the sorted value
                    new_label = Text(str(sorted_sublist_elements[k]), font_size=36).move_to(squares[index])

                    # Replace the old label with the new one
                    self.play(Transform(labels[index], new_label))  # Smooth transform
                    
                    # Animate the sublist square moving back
                    self.play(sublist_squares[k].animate.move_to(squares[index].get_center()), run_time = 0.5)

                self.play(VGroup(*sublist_squares).animate.set_color(WHITE), VGroup(*sublist_labels).animate.set_color(WHITE))
                self.play(FadeOut(VGroup(*sublist_squares)), FadeOut(VGroup(*sublist_labels)))

            self.remove(gap_text)
            gap //= 2

        with self.voiceover("Sorting complete!"):
            pass
        self.play(VGroup(*squares).animate.set_color(GREEN), VGroup(*labels).animate.set_color(GREEN))
        self.wait(2)