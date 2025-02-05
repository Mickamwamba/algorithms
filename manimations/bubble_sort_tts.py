from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class BubbleSortTTS(VoiceoverScene):
    def construct(self):
        # Set up voiceover service
        self.set_speech_service(GTTSService(lang="en"))

        # Data to be sorted
        # arr = [5, 3, 8, 1, 4]
        arr = [25, 21, 22, 24, 23, 27, 26]
        n = len(arr)

        # Create visual elements (boxes and numbers)
        squares = VGroup(*[Square(side_length=1).shift(RIGHT * i) for i in range(n)])
        labels = VGroup(*[Text(str(arr[i]), font_size=36).move_to(squares[i]) for i in range(n)])

        # Title
        title = Text("Bubble Sort: Simple and Clear Explanation", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction voiceover
        with self.voiceover(text="Let’s talk about Bubble Sort—one of the simplest sorting algorithms out there!") as tracker:
            pass

        with self.voiceover(text="Here’s an unsorted list of numbers. Our goal? Sort them in ascending order using Bubble Sort.") as tracker:
            self.play(Create(squares), Write(labels))
            self.wait(1)

        # Bubble Sort Animation
        for i in range(n - 1):
            swapped = False

            # Pass number text
            pass_text = Text(f"Pass {i+1}", font_size=36).next_to(title, DOWN)
            self.play(Write(pass_text))

            with self.voiceover(text=f"Pass {i+1} begins."):
                pass

            for j in range(n - 1 - i):
                # Update comparison text
                comp_text = f"Is {arr[j]} > {arr[j + 1]}?"
                comparison_text = Text(comp_text, font_size=36).to_edge(LEFT)
                self.play(Write(comparison_text))
                with self.voiceover(text=f"Is {arr[j]} greater than {arr[j + 1]}?"):
                    pass

                # Highlight comparison pair
                self.play(squares[j].animate.set_color(RED), squares[j+1].animate.set_color(RED))
                self.wait(0.5)

                if arr[j] > arr[j + 1]:
                    # Update decision text (Swapping)
                    # decision_text = Text("Yes, swapping!", font_size=36).next_to(comparison_text, DOWN).shift(RIGHT * 0.2)
                    decision_text = Text("Yes, swapping!", font_size=36).next_to(squares[j], DOWN).shift(DOWN * 0.2)
                    self.play(Write(decision_text))

                    # Swap logic
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    self.play(
                        squares[j].animate.move_to(squares[j + 1].get_center()),
                        squares[j + 1].animate.move_to(squares[j].get_center()),
                        labels[j].animate.move_to(squares[j + 1].get_center()),
                        labels[j + 1].animate.move_to(squares[j].get_center()),
                        run_time=0.5
                    )
                    squares[j], squares[j + 1] = squares[j + 1], squares[j]
                    labels[j], labels[j + 1] = labels[j + 1], labels[j]
                    swapped = True
                else:
                    # Update decision text (Keeping Order)
                    # decision_text = Text("No, keeping order!", font_size=36).next_to(comparison_text, DOWN).shift(RIGHT * 0.2)
                    decision_text = Text("No, keeping order!", font_size=36).next_to(squares[j], DOWN).shift(DOWN * 0.2)
                    self.play(Write(decision_text))

                # Reset colors
                self.play(squares[j].animate.set_color(WHITE), squares[j+1].animate.set_color(WHITE))

                # Remove decision text
                self.remove(comparison_text, decision_text)

            # Mark sorted element
            self.play(squares[n - 1 - i].animate.set_color(GREEN))
            self.remove(pass_text)

            # If no swaps, array is already sorted
            if not swapped:
                break

        self.wait(1)

        # Final sorted list text
        sorted_text = Text("Sorted!", font_size=48).next_to(title, DOWN)
        self.play(Transform(pass_text, sorted_text))

        self.wait(2)