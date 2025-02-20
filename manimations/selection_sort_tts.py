from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.openai import OpenAIService


class SelectionSortTTS(VoiceoverScene):
    def construct(self):
        # Set up voiceover service
        self.set_speech_service(
            OpenAIService(
                voice="echo",
                model="tts-1-hd",
            )
        )

        # Data to be sorted
        arr = [25, 21, 23, 24, 26]
        n = len(arr)

        # Create visual elements (boxes and numbers)
        squares = VGroup(*[Square(side_length=1).shift(RIGHT * i) for i in range(n)])
        labels = VGroup(*[Text(str(arr[i]), font_size=36).move_to(squares[i]) for i in range(n)])
        arrow = Triangle().scale(0.5).rotate(PI)

        # Title
        title = Text("Selection Sort: Step-by-Step Visualization", font_size=48).to_edge(UP)
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)

        # Introduction voiceover
        with self.voiceover(text="Welcome to this step-by-step visualization of Selection Sort, a straightforward sorting algorithm that works by repeatedly finding the minimum element."):
            self.wait(0.5)

        with self.voiceover(text="Let's start with this unsorted array of five numbers. We'll go through each position, find the smallest remaining number, and place it in its correct position."):
            self.play(Create(squares), run_time=1)
            self.play(Write(labels), run_time=1)
            self.wait(0.5)

        # Selection Sort Animation
        for i in range(n - 1):
            min_idx = i
            if i == 0:
                self.play(Create(arrow), run_time=0.5)
            self.play(arrow.animate.next_to(squares[i], UP), run_time=0.5)

            # Pass number text
            pass_text = Text(f"Pass {i+1}", font_size=36).next_to(title, DOWN)
            self.play(Write(pass_text), run_time=0.5)

            with self.voiceover(text=f"In pass {i+1}, we start from position {i+1} and mark {arr[i]} as our temporary minimum."):
                self.play(squares[i].animate.set_color(YELLOW), run_time=0.5)
                self.wait(0.3)

            for j in range(i + 1, n):
                self.wait(1)
                with self.voiceover(text=f"Now comparing {arr[j]} with our current minimum {arr[min_idx]}."):
                    # Highlight comparison
                    self.play(squares[j].animate.set_color(RED), run_time=0.3)
                    self.play(squares[min_idx].animate.set_color(YELLOW), run_time=0.3)
                    
                    # Create comparison and answer text
                    comparison_text = Text(f"Is {arr[j]} < {arr[min_idx]}?", font_size=36).to_edge(LEFT)
                    is_smaller = arr[j] < arr[min_idx]
                    answer_text = Text(
                        "Yes" if is_smaller else "No",
                        font_size=36,
                        color=GREEN if is_smaller else RED
                    ).next_to(comparison_text, RIGHT, buff=0.5)
                    
                    self.play(Write(comparison_text), run_time=0.5)
                    self.wait(0.2)
                    self.play(Write(answer_text), run_time=0.3)
                self.wait(1)
                if arr[j] < arr[min_idx]:
                    self.play(squares[min_idx].animate.set_color(WHITE), run_time=0.3)
                    min_idx = j
                    with self.voiceover(text=f"We found a new minimum: {arr[min_idx]}. Let's mark it and continue searching."):
                        new_min_text = Text("New minimum found!", font_size=36).next_to(answer_text, DOWN)
                        self.play(Write(new_min_text), run_time=0.5)
                        self.play(squares[min_idx].animate.set_color(YELLOW), run_time=0.3)
                        self.wait(0.5)
                        self.remove(new_min_text)

                # Reset previous comparisons
                self.play(squares[j].animate.set_color(WHITE), run_time=0.3)
                self.remove(comparison_text, answer_text)  # Remove both question and answer
                self.wait(0.2)

            # Swap if needed
            if min_idx != i:
                with self.voiceover(text=f"We've found the minimum value {arr[min_idx]}. Let's swap it with the current position's value {arr[i]}."):
                    self.play(
                        squares[i].animate.move_to(squares[min_idx].get_center()),
                        squares[min_idx].animate.move_to(squares[i].get_center()),
                        labels[i].animate.move_to(squares[min_idx].get_center()),
                        labels[min_idx].animate.move_to(squares[i].get_center()),
                        run_time=0.8
                    )
                    arr[i], arr[min_idx] = arr[min_idx], arr[i]
                    squares[i], squares[min_idx] = squares[min_idx], squares[i]
                    labels[i], labels[min_idx] = labels[min_idx], labels[i]
                    self.wait(0.3)
            
            # Mark sorted element
            with self.voiceover(text=f"Position {i+1} is now sorted with the correct value {arr[i]}."):
                self.play(squares[i].animate.set_color(GREEN), run_time=0.5)
                self.remove(pass_text)
                self.wait(0.3)

        # Mark the last element as sorted
        with self.voiceover(text="The last element is automatically in its correct position."):
            self.play(squares[-1].animate.set_color(GREEN), run_time=0.5)
            self.remove(arrow)
        
        self.wait(0.5)
        
        # Final sorted list text
        sorted_text = Text("Array Sorted!", font_size=48).next_to(title, DOWN)
        with self.voiceover(text="And there we have it! Our array is now fully sorted in ascending order."):
            self.play(Transform(pass_text, sorted_text), run_time=1)
        
        self.wait(0.5)
        
        # Display Selection Sort Algorithm
        code_text = '''def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
'''
        code = Code(
            code_string=code_text,
            language="Python",
            background="window",
            background_config={"stroke_color": "maroon"},
        ).to_edge(DOWN)
        
        with self.voiceover(text="Here is the Python implementation of Merge Sort. You can find the complete source code in the link provided in the video description below."):
            self.play(Write(code), run_time=2)
        
        self.wait(1)
        with self.voiceover(text="Thank you for watching!"):
            pass
        
        self.wait(1)