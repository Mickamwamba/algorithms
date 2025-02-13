from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.openai import OpenAIService

class BubbleSortTTS(VoiceoverScene):
    def construct(self):
        # Set up voiceover service
        # self.set_speech_service(GTTSService(lang="en"))
        self.set_speech_service(
            OpenAIService(
                voice="echo",
                model="tts-1-hd",
            )
        )

        # Data to be sorted
        arr = [5, 3, 8, 1, 4]
        # arr = [25, 21, 22, 24, 23, 27, 26]
        n = len(arr)

        # Create visual elements (boxes and numbers)
        squares = VGroup(*[Square(side_length=1).shift(RIGHT * i) for i in range(n)]).move_to(ORIGIN)
        labels = VGroup(*[Text(str(arr[i]), font_size=36).move_to(squares[i]) for i in range(n)])

        # Title
        title = Text("Visualizing Bubble Sort: A Step-by-Step Guide", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        with self.voiceover(text="Let’s talk about Bubble Sort, while not the most efficient algorithm, it is one of the simplest to understand and implement. It repeatedly steps through the list, compares the adjacent items, and swaps them if they are in the wrong order. Let's see how it works in action!") as tracker:
            pass

        # with self.voiceover(text="Here’s an unsorted list of numbers. Our goal? Sort them in ascending order using Bubble Sort.") as tracker:
        with self.voiceover(text="We begin with an unsorted list of numbers. Our task is to sort them in ascending order using the Bubble Sort algorithm.") as tracker:
            self.play(Create(squares), Write(labels))
            self.wait(1)

        with self.voiceover(text="Notice that at the end of each pass, larger numbers 'bubble' to the end of the list.") as tracker:
            pass
        self.wait(2)

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

                with self.voiceover(text=f"Is {arr[j]} greater than {arr[j + 1]}?"):
                    self.play(Write(comparison_text))
                     # Highlight comparison pair
                    self.play(squares[j].animate.set_color(RED), squares[j+1].animate.set_color(RED))
                    self.wait(0.5)
                    pass

                if arr[j] > arr[j + 1]:
                    # Update decision text (Swapping)
                    decision_text = Text("Yes, swapping!", font_size=36).next_to(squares[n//2], DOWN).shift(DOWN * 0.2)
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
                    decision_text = Text("No, keeping order!", font_size=36).next_to(squares[n//2], DOWN).shift(DOWN * 0.2)
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
        with self.voiceover(text="Done, our list is now sorted!") as tracker:
            # pass
            sorted_text = Text("Sorted!", font_size=48).next_to(title, DOWN)
            self.play(Transform(pass_text, sorted_text))
            self.wait(4)
        
        # Display Bubble Sort Algorithm
        code_text = '''
        def bubble_sort(arr): 
            n = len(arr)
            for i in range(n-1):
                swapped = False
                for j in range(n-i-1):
                    if(arr[j] > arr[j+1]): 
                        temp = arr[j]
                        arr[j] = arr[j+1]
                        arr[j+1] = temp
                        swapped = True
                if not swapped: 
                    break
            return arr
        '''

        code = Code(
            code_string=code_text,
            language="Python",
            background="window",
            background_config={"stroke_color": "maroon"},
        ).to_edge(DOWN).move_to(ORIGIN).shift(DOWN*0.2)

        with self.voiceover(text="Here’s the Python implementation of Bubble Sort. You can find the link to the full source code in the video description below.") as tracker:
            self.remove(squares,labels)
            self.play(Write(code))
            self.wait(2)

        with self.voiceover(text="Thank you for watching!"):
            pass

        self.wait(2)
