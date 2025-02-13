from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class SelectionSortTTS(VoiceoverScene):
    def construct(self):
        # Set up voiceover service
        self.set_speech_service(GTTSService(lang="en"))

        # Data to be sorted
        arr = [25, 21, 22, 24, 23, 27, 26]
        n = len(arr)

        # Create visual elements (boxes and numbers)
        squares = VGroup(*[Square(side_length=1).shift(RIGHT * i) for i in range(n)])
        labels = VGroup(*[Text(str(arr[i]), font_size=36).move_to(squares[i]) for i in range(n)])
        arrow = Triangle().scale(0.5).rotate(PI)

        # Title
        title = Text("Selection Sort: Step-by-Step Visualization", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction voiceover
        with self.voiceover(text="Let's explore Selection Sort, another simple yet efficient sorting algorithm!"):
            pass

        with self.voiceover(text="At each iteration, we pick a starting index and loop through the list to find the minimum element. If a new minimum is found, we swap it with the current index."):
            self.play(Create(squares), Write(labels))
            self.wait(1)

        # Selection Sort Animation
        for i in range(n - 1):
            min_idx = i
            if i == 0:
                self.play(Create(arrow))
            self.play(arrow.animate.next_to(squares[i], UP))

            # Pass number text
            pass_text = Text(f"Pass {i+1}", font_size=36).next_to(title, DOWN)
            self.play(Write(pass_text))

            with self.voiceover(text=f"Pass {i+1} begins. We start by assuming {arr[i]} is the smallest."):
                self.play(squares[i].animate.set_color(YELLOW))
                self.play(squares[min_idx].animate.set_color(YELLOW))

            for j in range(i + 1, n):
                # Highlight comparison
                self.play(squares[j].animate.set_color(RED), squares[min_idx].animate.set_color(YELLOW))
                self.wait(0.2)
                self.play(squares[j].animate.set_color(WHITE), squares[min_idx].animate.set_color(YELLOW))
                
                comparison_text = Text(f"Is {arr[j]} < {arr[min_idx]}?", font_size=36).to_edge(LEFT)
                self.play(Write(comparison_text))
                
                with self.voiceover(text=f"Comparing {arr[j]} with the current minimum {arr[min_idx]}."):
                    pass
                
                if arr[j] < arr[min_idx]:
                    self.play(squares[min_idx].animate.set_color(WHITE))
                    min_idx = j
                    with self.voiceover(text=f"Yes, new minimum found: {arr[min_idx]}."):
                        new_min_text = Text("Yes, new minimum found", font_size=36).next_to(comparison_text, DOWN)
                        self.play(Write(new_min_text))
                        self.play(squares[min_idx].animate.set_color(YELLOW))
                        self.wait(0.5)
                        self.remove(new_min_text)
                
                # Reset previous comparisons
                self.play(squares[j].animate.set_color(WHITE))
                self.remove(comparison_text)

            # Swap if needed
            if min_idx != i:
                with self.voiceover(text=f"Swapping {arr[i]} with {arr[min_idx]}."):
                    self.play(
                        squares[i].animate.move_to(squares[min_idx].get_center()),
                        squares[min_idx].animate.move_to(squares[i].get_center()),
                        labels[i].animate.move_to(squares[min_idx].get_center()),
                        labels[min_idx].animate.move_to(squares[i].get_center()),
                        run_time=0.5
                    )
                    arr[i], arr[min_idx] = arr[min_idx], arr[i]
                    squares[i], squares[min_idx] = squares[min_idx], squares[i]
                    labels[i], labels[min_idx] = labels[min_idx], labels[i]
            
            # Mark sorted element
            self.play(squares[i].animate.set_color(GREEN))
            self.remove(pass_text)

        # Mark the last element as sorted
        self.play(squares[-1].animate.set_color(GREEN))
        self.remove(arrow)
        
        self.wait(1)
        
        # Final sorted list text
        sorted_text = Text("Sorted!", font_size=48).next_to(title, DOWN)
        self.play(Transform(pass_text, sorted_text))
        
        self.wait(2)
        
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
        self.play(Write(code))
        
        self.wait(2)
        with self.voiceover(text="Thank you for watching!"):
            pass
        
        self.wait(2)
