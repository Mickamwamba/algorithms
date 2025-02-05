# from manim import *
# from manim_voiceover import VoiceoverScene
# from manim_voiceover.services.gtts import GTTSService

# class InsertionSortTTS(VoiceoverScene):
#     def construct(self):
#         self.set_speech_service(GTTSService(lang="en"))

#         arr = [5, 3, 8, 1, 4]
#         n = len(arr)

#         squares = [Square(side_length=1).shift(RIGHT * i) for i in range(n)]
#         labels = [Text(str(num), font_size=36).move_to(square) for num, square in zip(arr, squares)]
#         squares_vg = VGroup(*squares)
#         labels_vg = VGroup(*labels)

#         title = Text("Insertion Sort: Step-by-Step", font_size=48).to_edge(UP)
#         self.play(Write(title))
#         self.wait(1)

#         with self.voiceover(text="Let’s talk about Insertion Sort—an efficient way to sort numbers by building a sorted list one element at a time.") as tracker:
#             pass

#         with self.voiceover(text="Here’s an unsorted list. Our goal is to Sort it in ascending order using Insertion Sort.") as tracker:
#             self.play(Create(squares_vg), Write(labels_vg))
#             self.wait(1)

#         for i in range(1, n):
#             key = arr[i]
#             j = i - 1
#             key_square = squares[i]
#             key_label = labels[i]

#             pass_text = Text(f"Pass {i}", font_size=36).next_to(title, DOWN)
#             self.play(Write(pass_text))

#             # with self.voiceover(text=f"Pass {i} begins. We take {key} and place it in the correct position."):
#             #     self.play(
#             #         key_square.animate.set_color(YELLOW),
#             #         key_label.animate.set_color(YELLOW),
#             #         key_square.animate.shift(UP * 1.2),
#             #         key_label.animate.shift(UP * 1.2),
#             #         run_time=1
#             #     )

#             with self.voiceover(text=f"Pass {i} begins."):
#                 pass
            
#             with self.voiceover(text=f"We take {key} and place it in the correct position."):

#                 for _ in range(3):  # Adjust the number of blinks
#                     self.play(
#                         key_square.animate.set_color(RED),
#                         key_label.animate.set_color(RED),
#                         run_time=0.3
#                     )
#                     self.play(
#                         key_square.animate.set_color(WHITE),
#                         key_label.animate.set_color(WHITE),
#                         run_time=0.3
#                     )
#                     self.play(
#                         key_square.animate.set_color(RED),
#                         key_label.animate.set_color(RED),
#                         run_time=0.3
#                     )

#             self.play(
#                 key_square.animate.shift(UP * 1.2),
#                 key_label.animate.shift(UP * 1.2),
#                 run_time=0.5  # Then shift
#             )

#             squares.pop(i)
#             labels.pop(i)

#             shift_squares = squares.copy()
#             shift_labels = labels.copy()
#             empty_index = i

#             while j >= 0 and arr[j] > key:
#                 comp_text = f"Is {arr[j]} > {key}?"
#                 comparison_text = Text(comp_text, font_size=36).to_edge(LEFT)
#                 self.play(Write(comparison_text))
#                 with self.voiceover(text=f"Is {arr[j]} greater than {key}?"):
#                     # pass
#                     # key_square.animate.set_color(RED),
#                     self.play(squares[j].animate.set_color(RED))


#                 decision_text = Text("Yes, shift to the right!", font_size=36).next_to(squares[0], DOWN).shift(DOWN * 0.2)
#                 self.play(Write(decision_text))
#                 self.wait(1)

#                 arr[j + 1] = arr[j]
#                 self.play(
#                     shift_squares[j].animate.shift(RIGHT * 1),
#                     shift_labels[j].animate.shift(RIGHT * 1),
#                     run_time=0.5
#                 )

#                 if j + 1 < len(squares): 
#                     shift_squares[j + 1] = shift_squares[j]
#                     shift_labels[j + 1] = shift_labels[j]
#                     empty_index = j

#                 if j==1: 
#                     with self.voiceover(text=f"This is the correct position, insert {key} here!"):
#                         pass
#                 j -= 1
                

#                 self.remove(comparison_text, decision_text)
#                 self.wait(1)

#             arr[empty_index] = key
#             squares.insert(empty_index, key_square)
#             labels.insert(empty_index, key_label)
#             self.add(key_square, key_label)
#             self.play(
#                 key_square.animate.move_to(RIGHT * empty_index),
#                 key_label.animate.move_to(RIGHT * empty_index),
#                 run_time=0.5
#             )

#             self.play(
#                 key_square.animate.set_color(WHITE),
#                 key_label.animate.set_color(WHITE),
#                 run_time=0.5
#             )
#             for k in range(i + 1):
#                 self.play(
#                     squares[k].animate.set_color(GREEN),
#                     labels[k].animate.set_color(GREEN),
#                     run_time=0.2
#                 )
#             self.remove(pass_text)
#         sorted_text = Text("Sorted!", font_size=48).next_to(title, DOWN)
#         self.play(Write(sorted_text))
#         self.wait(2)


from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class InsertionSortTTS(VoiceoverScene):
    def construct(self):
        # Initialize text-to-speech service
        self.set_speech_service(GTTSService(lang="en"))

        # Define the array to be sorted
        arr = [5, 3, 8, 1, 4]
        n = len(arr)

        # Create square representations for each number in the array
        squares = [Square(side_length=1).shift(RIGHT * i) for i in range(n)]
        labels = [Text(str(num), font_size=36).move_to(square) for num, square in zip(arr, squares)]
        squares_vg = VGroup(*squares)
        labels_vg = VGroup(*labels)

        # Display the title
        title = Text("Insertion Sort: Step-by-Step", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Voiceover introduction
        with self.voiceover(text="Let’s talk about Insertion Sort—an efficient way to sort numbers by building a sorted list one element at a time."):
            pass

        # Show the unsorted array
        with self.voiceover(text="Here’s an unsorted list. Our goal is to sort it in ascending order using Insertion Sort."):
            self.play(Create(squares_vg), Write(labels_vg))
            self.wait(1)

        # Start the insertion sort visualization
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            key_square = squares[i]
            key_label = labels[i]

            # Display the pass number
            pass_text = Text(f"Pass {i}", font_size=36).next_to(title, DOWN)
            self.play(Write(pass_text))

            # Highlight the key element for insertion
            with self.voiceover(text=f"Pass {i} begins."):
                pass
            
            with self.voiceover(text=f"We take {key} and place it in the correct position."):
                for _ in range(3):  # Blinking effect to highlight the key element
                    self.play(
                        key_square.animate.set_color(RED),
                        key_label.animate.set_color(RED),
                        run_time=0.3
                    )
                    self.play(
                        key_square.animate.set_color(WHITE),
                        key_label.animate.set_color(WHITE),
                        run_time=0.3
                    )
                self.play(
                        key_square.animate.set_color(YELLOW),
                        key_label.animate.set_color(YELLOW),
                        run_time=0.3
                    )
            # Move the key element upwards to indicate selection
            self.play(
                key_square.animate.shift(UP * 1.2),
                key_label.animate.shift(UP * 1.2),
                run_time=0.5
            )

            # Remove key from current position
            squares.pop(i)
            labels.pop(i)

            # Copy references to shift elements later
            shift_squares = squares.copy()
            shift_labels = labels.copy()
            empty_index = i

            in_correct_position = True
            # Perform shifting of elements if necessary
            while j >= 0 and arr[j] > key:
                in_correct_position = False
                comp_text = Text(f"Is {arr[j]} > {key}?", font_size=36).to_edge(LEFT)
                self.play(Write(comp_text))
                
                with self.voiceover(text=f"Is {arr[j]} greater than {key}?"):
                    self.play(squares[j].animate.set_color(RED))
                
                decision_text = Text("Yes, shift to the right!", font_size=36).next_to(squares[0], DOWN).shift(DOWN * 0.2)
                self.play(Write(decision_text))
                self.wait(1)
                
                # Shift the element to the right
                arr[j + 1] = arr[j]
                self.play(
                    shift_squares[j].animate.shift(RIGHT * 1),
                    shift_labels[j].animate.shift(RIGHT * 1),
                    run_time=0.5
                )

                if j + 1 < len(squares): 
                    shift_squares[j + 1] = shift_squares[j]
                    shift_labels[j + 1] = shift_labels[j]
                    empty_index = j
                
                j -= 1
                self.remove(comp_text, decision_text)
                self.wait(1)

            # Insert the key in the correct position
            with self.voiceover(text=f"Insert {key} in the sorted section." if not in_correct_position else f"{key} is already correctly placed. Moving on."):
                pass
            
            arr[empty_index] = key
            squares.insert(empty_index, key_square)
            labels.insert(empty_index, key_label)
            self.add(key_square, key_label)
            
            self.play(
                key_square.animate.move_to(RIGHT * empty_index),
                key_label.animate.move_to(RIGHT * empty_index),
                run_time=0.5
            )

            # Reset color of inserted element
            self.play(
                key_square.animate.set_color(WHITE),
                key_label.animate.set_color(WHITE),
                run_time=0.5
            )
            
            # Mark sorted portion in green
            for k in range(i + 1):
                self.play(
                    squares[k].animate.set_color(GREEN),
                    labels[k].animate.set_color(GREEN),
                    run_time=0.2
                )
            
            self.remove(pass_text)

        # Final message indicating sorting is complete
        sorted_text = Text("Sorted!", font_size=48).next_to(title, DOWN)
        self.play(Write(sorted_text))
        self.wait(2)
