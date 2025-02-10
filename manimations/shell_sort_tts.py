from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.openai import OpenAIService

class ShellSortVisualization(VoiceoverScene):
    def construct(self):
        # Initialize text-to-speech service
        # self.set_speech_service(GTTSService(lang="en"))
        self.set_speech_service(
            OpenAIService(
                voice="echo",
                model="tts-1-hd",
            )
        )

        # Define the array to be sorted
        # arr = [5, 3, 8, 1, 4]
        arr = [9, 8, 3, 7, 5, 6, 4, 1]
        n = len(arr)

        # Create square representations for each number in the array, now centered
        squares = [Square(side_length=1).shift(RIGHT * (i - n / 2)) for i in range(n)]  # Center the list
        labels = [Text(str(num), font_size=36).move_to(square) for num, square in zip(arr, squares)]
        squares_vg = VGroup(*squares)
        labels_vg = VGroup(*labels)

        # Create Python code block to display on the right side of the screen
        code_text = '''def shell_sort(arr):
    distance = len(arr)//2
    while distance > 0: 
        for i in range(distance, len(arr)): 
            temp = arr[i]
            j = i 
            while (j>=distance and 
                   arr[j-distance] > temp): 
                arr[j] = arr[j-distance] 
                j = j - distance
            arr[j] = temp 
        distance = distance // 2 
    return arr
'''
        # Create the code block
        code = Code(
            code_string=code_text,
            language="Python",
            background="window",
            background_config={"stroke_color": "maroon"},
        ).to_edge(DOWN)

        # Display the title
        title = Text("Shell Sort: Step-by-Step", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Voiceover introduction
        with self.voiceover(text="Let's explore Shell Sort, an advanced sorting algorithm that improves upon insertion sort by first sorting elements far apart."):
            pass

        # Show the unsorted array and Python code block
        with self.voiceover(text="Here's our unsorted list. Shell Sort will sort it efficiently."):
            self.play(Create(squares_vg), Write(labels_vg))
            self.wait(1)

        # Shell Sort visualization
        distance = n // 2
        pass_count = 1

        while distance > 0:
            # Display the current distance
            distance_text = Text(f"Current Distance: {distance}", font_size=36).next_to(title, DOWN)
            self.play(Write(distance_text))

            with self.voiceover(f"In pass {pass_count}, we'll compare and swap elements {distance} positions apart."):
                pass

            # Iterate through the array with current distance
            for i in range(distance, n):
                temp = arr[i]
                temp_square = squares[i]
                temp_label = labels[i]

                # Highlight the current element
                with self.voiceover(f"Looking at element {temp}"):
                    self.play(
                        temp_square.animate.set_color(YELLOW),
                        temp_label.animate.set_color(YELLOW)
                    )

                j = i
                # Compare and swap elements
                # while j >= distance and arr[j - distance] > temp:
                #     # Comparison text
                #     comp_text = Text(f"Is {arr[j-distance]} > {temp}?", font_size=30).to_edge(LEFT)
                #     self.play(Write(comp_text))

                #     swap_text = Text("Yes, Swapping!", font_size=30).next_to(squares[n//2], DOWN)
                    
                #     with self.voiceover(f"Comparing {arr[j-distance]} with {temp}"):
                #         # Highlight comparison elements
                #         self.play(
                #             squares[j - distance].animate.set_color(RED),
                #             labels[j - distance].animate.set_color(RED),
                #             Write(swap_text)
                #         )

                #         # Add a bent arrow pointing to the two elements being compared
                #         arrow = CurvedArrow(
                #             start_point=squares[j - distance].get_center(),
                #             end_point=squares[j].get_center(),
                #             angle=PI / 2,  # Adjust the angle of the arrow as needed
                #             color=WHITE,
                #             # buff=0.1,
                #         )
                #         self.play(Create(arrow))
                #         self.wait(2)

                #     # Swap elements
                #     arr[j] = arr[j - distance]
                    
                #     self.play(
                #         squares[j - distance].animate.move_to(squares[j].get_center()),
                #         labels[j - distance].animate.move_to(squares[j].get_center()),
                #         squares[j].animate.move_to(squares[j - distance].get_center()),
                #         labels[j].animate.move_to(squares[j - distance].get_center())
                #     )

                #     # Swap squares and labels in the visualization
                #     squares[j], squares[j - distance] = squares[j - distance], squares[j]
                #     labels[j], labels[j - distance] = labels[j - distance], labels[j]

                #     j -= distance
                    
                #     # Remove comparison text and arrow
                #     self.remove(comp_text, swap_text, arrow)

                # # If no swap occurs
                # if j >= distance and arr[j - distance] <= temp:
                #     swap_text = Text("No, Don't Swap", font_size=30).next_to(squares[n//2], DOWN)
                #     self.play(Write(swap_text))
                #     self.wait(1)
                #     self.remove(swap_text)
                # Compare and swap elements
                while j >= distance and arr[j - distance] > temp:
                    # Comparison text (always show it)
                    comp_text = Text(f"Is {arr[j-distance]} > {temp}?", font_size=30).to_edge(LEFT)
                    self.play(Write(comp_text))
                    
                    with self.voiceover(f"Comparing {arr[j-distance]} with {temp}"):
                        # Highlight comparison elements
                        self.play(
                            squares[j - distance].animate.set_color(RED),
                            labels[j - distance].animate.set_color(RED),
                        )

                        # Add a bent arrow pointing to the two elements being compared
                        arrow = CurvedArrow(
                            start_point=squares[j - distance].get_center(),
                            end_point=squares[j].get_center(),
                            angle=PI,  # Adjust the angle of the arrow as needed
                            color=WHITE,
                            # buff=0.1,
                        )
                        self.play(Create(arrow))
                        self.wait(1)
                        swap_text = Text("Yes, Swapping!", font_size=30).next_to(squares[n//2], DOWN)
                        self.play(Write(swap_text))
                        self.wait(1)

                    # Swap elements
                    arr[j] = arr[j - distance]
                    
                    self.play(
                        squares[j - distance].animate.move_to(squares[j].get_center()),
                        labels[j - distance].animate.move_to(squares[j].get_center()),
                        squares[j].animate.move_to(squares[j - distance].get_center()),
                        labels[j].animate.move_to(squares[j - distance].get_center())
                    )

                    # Swap squares and labels in the visualization
                    squares[j], squares[j - distance] = squares[j - distance], squares[j]
                    labels[j], labels[j - distance] = labels[j - distance], labels[j]

                    j -= distance

                    # Remove comparison text and arrow
                    self.remove(comp_text, swap_text, arrow)

                # If no swap occurs (this now shows the comparison as well)
                if j >= distance and arr[j - distance] <= temp:
                    comp_text = Text(f"Is {arr[j-distance]} > {temp}?", font_size=30).to_edge(LEFT)
                    self.play(Write(comp_text))

                    # Add a bent arrow pointing to the two elements being compared
                    arrow = CurvedArrow(
                            start_point=squares[j - distance].get_center(),
                            end_point=squares[j].get_center(),
                            angle=PI,  # Adjust the angle of the arrow as needed
                            color=WHITE,
                            # buff=0.1,
                        )
                    self.play(Create(arrow))
                    self.wait(1)
                    swap_text = Text("No, Don't Swap", font_size=30).next_to(squares[n//2], DOWN)
                    self.play(Write(swap_text))
                    self.wait(1)

                    with self.voiceover(f"Comparing {arr[j-distance]} with {temp}"):
                        self.play(
                            squares[j - distance].animate.set_color(RED),
                            labels[j - distance].animate.set_color(RED),
                            Write(swap_text)
                        )

                    self.remove(comp_text,swap_text, swap_text,)  # Clean up the texts


                # Place the temp element
                arr[j] = temp
                self.play(
                    temp_square.animate.move_to(squares[j].get_center()),
                    temp_label.animate.move_to(squares[j].get_center())
                )

                # Reset colors
                self.play(
                    temp_square.animate.set_color(WHITE),
                    temp_label.animate.set_color(WHITE)
                )

            # Reduce distance
            distance //= 2
            pass_count += 1
            self.remove(distance_text)

        # Final message indicating sorting is complete
        sorted_text = Text("Sorted!", font_size=48).next_to(title, DOWN)
        self.play(Write(sorted_text))

        # Color the entire array green to show it's sorted
        self.play(
            *[square.animate.set_color(GREEN) for square in squares],
            *[label.animate.set_color(GREEN) for label in labels]
        )
        self.wait(2)

        # Clean up
        self.play(
            FadeOut(squares_vg), 
            FadeOut(labels_vg), 
            FadeOut(sorted_text)
        )

        # Display code block
        with self.voiceover(text="Here's the Python implementation of Shell Sort."):
            self.play(Create(code))
            self.wait(3)

        with self.voiceover(text="Thank you for watching!"):
            pass
        self.wait(1)

