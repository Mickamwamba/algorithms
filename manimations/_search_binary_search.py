from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService

class BinarySearchTTS(VoiceoverScene):
    def construct(self):
        self.set_speech_service(OpenAIService(voice="echo", model="tts-1-hd"))  # AI voice

        # Define initial unsorted elements
        elements = [12, 33, 11, 99, 22, 55, 90,4,20,28,10]  # Unsorted array
        sorted_elements = sorted(elements)  # Sorted array for binary search
        n = len(elements)
        target = 90

       # Move initial list up
        initial_position = ORIGIN + UP * 2
        new_position = initial_position + DOWN * 1.5  # Position for new search range

        squares = VGroup(*[Square(side_length=1).shift(RIGHT * i) for i in range(n)]).move_to(initial_position)
        labels = VGroup(*[Text(str(num), font_size=36).move_to(squares[i]) for i, num in enumerate(elements)])

        target_square = Square(side_length=1).next_to(squares[-1]).shift(RIGHT*0.1)
        target_label = Text(str(target), font_size=36).move_to(target_square)

        sorted_squares = VGroup(*[Square(side_length=1).shift(RIGHT * i) for i, num in enumerate(sorted_elements)]).move_to(initial_position)
        sorted_labels = VGroup(*[Text(str(num), font_size=36).move_to(sorted_squares[i]) for i, num in enumerate(sorted_elements)])

         #Title: 
        title = Text("Visualizing Binary Search: A Step-by-Step Guide", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        with self.voiceover("We are going to visualize Binary Search, an efficient search algorithm that keeps on dividing a list into two parts until the target value is found") as _:
            pass
        with self.voiceover("We will start with unsorted list") as _:
            self.play(Write(squares), Write(labels))
            self.wait(2)

        with self.voiceover(f"Our goal is to search for number {target}.") as _:
            self.play(Write(target_square), Write(target_label))
            self.wait(2)
        
        with self.voiceover("However, one pre-condition for Binary Search is that the list needs to be sorted first before searching starts. So we sort the elements first.") as _:
            self.play(FadeOut(squares), FadeOut(labels))
            self.wait(1)

        self.play(Write(sorted_squares), Write(sorted_labels))
        self.wait(2)
        
        
        with self.voiceover(f"Now that our array is sorted, we can begin our search for the target number {target}.") as _:
            self.wait(1)

        first, last = 0, len(sorted_elements) - 1
        found = False
        current_squares = squares  # Track the current visual squares
        search_range = sorted_elements

        while first <= last and not found:
            midpoint_index = (len(search_range) - 1) // 2
            mid_value = search_range[midpoint_index]

            with self.voiceover(f"Now, we check the middle element {mid_value} and compare that to our target search value") as _:
                self.play(current_squares[midpoint_index].animate.set_color(YELLOW), run_time=0.5)
                self.wait(1)

            comparison_text = Text(f"Is {mid_value} == {target}?", font_size=36).to_edge(LEFT)
            self.play(Write(comparison_text))
            self.wait(1)

            if mid_value == target:
                with self.voiceover("Great! We found the target.") as _:
                    self.play(current_squares[midpoint_index].animate.set_color(GREEN))
                    self.wait(1)
                found = True
            else:
                if target < mid_value:
                    last = first + midpoint_index - 1
                else:
                    first = first + midpoint_index + 1

                search_range = sorted_elements[first:last + 1]
                with self.voiceover("No, We update the search range.") as _:
                    new_squares = self.create_array_squares(search_range, new_position)
                    self.play(FadeIn(new_squares))
                    self.wait(1)
                    self.remove(comparison_text)
                
                current_squares = new_squares  # Update to new squares for visualization
                new_position += DOWN * 1.5  # Move the next search range lower

        if not found:
            with self.voiceover("The target was not found in the array.") as _:
                self.wait(1)

                
        # Display Binary Search Algorithm Code
        code_text = '''
        def binary_search(arr, target):
            first, last = 0, len(arr) - 1
            while first <= last:
                mid = (first + last) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    first = mid + 1
                else:
                    last = mid - 1
            return False
        '''

        code = Code(
            code_string=code_text,
            language="Python",
            background="window",
            background_config={"stroke_color": "maroon"},
        ).to_edge(DOWN).move_to(ORIGIN).shift(DOWN * 0.2)

        with self.voiceover("Here’s the Python implementation of binary search. You can find the link to the full source code in the video description below.") as _:
            self.play(Write(code))
            self.wait(2)

        with self.voiceover("Thank you for watching!"):
            pass

        self.wait(2)

    def create_array_squares(self, array, position):
        """Creates a new row of squares for the updated search range."""
        return VGroup(*[
            VGroup(Square(side_length=1).move_to(position + RIGHT * i),
                   Text(str(num), font_size=36).move_to(position + RIGHT * i))
            for i, num in enumerate(array)
        ])