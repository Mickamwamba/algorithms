from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.openai import OpenAIService


class MergeSortVisualization(VoiceoverScene):
    def construct(self):
        # Using OpenAI's Echo voice for high-quality narration
        self.set_speech_service(
            OpenAIService(
                voice="echo",
                model="tts-1-hd",
            )
        )
        
        # Title and introduction
        title = Text("Merge Sort Visualization").to_edge(UP)
        self.play(Write(title))
        
        elements = [38, 27, 43, 3, 21, 74, 82, 11]

        # Positioning for different stages
        original_position = ORIGIN + UP * 2.5
        initial_position = ORIGIN + UP * 1
        
        # Create visual elements
        self.original_mobs = self.create_array_squares(elements, original_position)
        array_mobs = self.create_array_squares(elements, initial_position)
        
        # Introduction
        with self.voiceover(text="Today we will explore Merge Sort — an efficient, divide-and-conquer algorithm for sorting elements."):
            pass
        self.wait(0.5)
        
        # Show original array
        with self.voiceover(text="Here's our unsorted list of numbers:"):
            self.play(*[FadeIn(mob) for mob in self.original_mobs])
            self.wait(1)
        
        # Explain the goal
        with self.voiceover(text="Our goal is to sort these numbers in ascending order using the Merge Sort algorithm."):
            # Highlight the original array
            self.play(*[mob.animate.set_color(YELLOW) for mob in self.original_mobs])
            self.play(*[mob.animate.set_color(WHITE) for mob in self.original_mobs])
            self.wait(0.5)
        
        # Start the sorting process
        with self.voiceover("Let's begin the Merge Sort process."):
            self.play(*[FadeIn(mob) for mob in array_mobs])
            self.wait(0.5)
        
        # Explain the approach
        with self.voiceover(text="Merge Sort works through a two-step process: first, we recursively divide the list in half until we have single elements. Then, we merge these elements back together in sorted order."):
            # Add visual indication of the division process
            division_arrow = Arrow(start=UP * 0.5, end=DOWN * 0.5, color=BLUE).next_to(array_mobs[len(array_mobs)//2 - 1], DOWN)
            self.play(Create(division_arrow))
            self.wait(0.5)
            self.play(FadeOut(division_arrow))
        
        # Begin the recursive sorting
        self.merge_sort(elements, 0, len(elements) - 1, 0, initial_position, array_mobs)
        
        # Conclusion
        with self.voiceover("Merge Sort is now complete. The list has been successfully sorted in ascending order."):
            # Highlight the sorted result
            # self.play(*[mob.animate.set_color(GREEN) for mob in array_mobs])
            # self.wait(2)
            # self.play(*[mob.animate.set_color(WHITE) for mob in array_mobs])
            pass

        self.wait(2)
        
        # Display the Python implementation
        with self.voiceover(text="Here is the Python implementation of Merge Sort. You can find the complete source code in the link provided in the video description below."):
            code_text = """
            def merge_sort(arr):
                if len(arr) > 1:
                    mid = len(arr) // 2
                    left_half = arr[:mid]
                    right_half = arr[mid:]
                    
                    # Recursively sort both halves
                    merge_sort(left_half)
                    merge_sort(right_half)
                    
                    # Merge the sorted halves
                    i = j = k = 0
                    while i < len(left_half) and j < len(right_half):
                        if left_half[i] < right_half[j]:
                            arr[k] = left_half[i]
                            i += 1
                        else:
                            arr[k] = right_half[j]
                            j += 1
                        k += 1
                    
                    # Check for remaining elements
                    while i < len(left_half):
                        arr[k] = left_half[i]
                        i += 1
                        k += 1
                    
                    while j < len(right_half):
                        arr[k] = right_half[j]
                        j += 1
                        k += 1"""

            code = Code(
                code_string=code_text, 
                language="Python",
                background="window",
                background_config={"stroke_color": "maroon"},
            ).scale(0.6).to_edge(DOWN)
            self.play(FadeOut(*self.mobjects))
            self.play(Create(code))  # Show the code at the end
            self.wait(3)
        # Final message
        with self.voiceover(text="Thank you for watching!"):
            # self.play(Indicate(title))
            self.wait(1)


    def merge_sort(self, arr, left, right, depth, position, parent_mobs=None):
        if left < right:
            mid = (left + right) // 2
            
            # Calculate appropriate spacing based on array size and depth
            spacing = (right - left + 1) * 0.4 * (0.9 ** depth)  # Reduce spacing for deeper recursion
            left_position = position + LEFT * spacing + DOWN * 0.8
            right_position = position + RIGHT * spacing + DOWN * 0.8
            
            with self.voiceover(f"Dividing the list at index {left} to {right} into two parts: indices {left} to {mid}, and indices {mid+1} to {right}."):
                # Highlight the current subarray being divided
                if parent_mobs and parent_mobs != self.original_mobs:
                    self.play(*[mob.animate.set_color(YELLOW) for mob in parent_mobs])
                    self.wait(0.3)
                    self.play(*[mob.animate.set_color(WHITE) for mob in parent_mobs])
            
            # Create and display the divided subarrays
            left_mobs = self.create_array_squares(arr[left:mid + 1], left_position)
            right_mobs = self.create_array_squares(arr[mid + 1:right + 1], right_position)
            
            self.play(*[FadeIn(mob) for mob in left_mobs + right_mobs])
            
            # Recursively sort both halves
            left_result = self.merge_sort(arr, left, mid, depth + 1, left_position, left_mobs)
            right_result = self.merge_sort(arr, mid + 1, right, depth + 1, right_position, right_mobs)
            
            # Remove parent mobs before merging
            if parent_mobs and parent_mobs != self.original_mobs:
                with self.voiceover(f"Both halves have been sorted. Now we'll merge them back together."):
                    self.play(*[FadeOut(mob) for mob in parent_mobs])
            
            # Merge the sorted subarrays
            self.merge(arr, left, mid, right, position, depth)
            
            return left_mobs + right_mobs

    def merge(self, arr, left, mid, right, position, depth):
        left_subarray = arr[left:mid + 1]
        right_subarray = arr[mid + 1:right + 1]
        
        # Adjust spacing for the final merge to prevent overlap
        if left == 0 and right == len(arr) - 1:  # This is the final merge of the entire array
            left_position = position + LEFT * 2.5  # Increased spacing for final merge
            right_position = position + RIGHT * 2.5
        else:
            left_position = position + LEFT * 0.8
            right_position = position + RIGHT * 0.8
        
        # Create visual elements for the subarrays to be merged
        left_mobs = self.create_array_squares(left_subarray, left_position)
        right_mobs = self.create_array_squares(right_subarray, right_position)
        
        # Set different colors for left and right subarrays
        self.play(*[mob.animate.set_color(BLUE_C) for mob in left_mobs])
        self.play(*[mob.animate.set_color(RED_C) for mob in right_mobs])
        self.wait(0.5)
        
        # Modified: Removed sublist sizes from voiceover
        with self.voiceover(f"Merging two sorted sublists."):
            self.wait(0.5)
        
        # Perform the merge operation
        merged_array = []
        i = j = 0
        
        # Compare elements from both subarrays
        while i < len(left_subarray) and j < len(right_subarray):
            if left_subarray[i] < right_subarray[j]:
                # Only provide detailed narration for small merges
                if len(left_subarray) + len(right_subarray) <= 4:
                    self.voiceover(f"Taking {left_subarray[i]} from the left sublist as it's smaller.")
                else:
                    self.wait(0.1)
                merged_array.append(left_subarray[i])
                i += 1
            else:
                if len(left_subarray) + len(right_subarray) <= 4:
                    self.voiceover(f"Taking {right_subarray[j]} from the right sublist as it's smaller.")
                else:
                    self.wait(0.1)
                merged_array.append(right_subarray[j])
                j += 1
        
        # Add remaining elements
        merged_array.extend(left_subarray[i:])
        merged_array.extend(right_subarray[j:])
        
        # Create and transform to the merged array
        merged_mobs = self.create_array_squares(merged_array, position)
        
        # Transform subarrays into merged array with animation
        self.play(
            *[ReplacementTransform(left_mobs[i], merged_mobs[i]) for i in range(len(left_mobs))],
            *[ReplacementTransform(right_mobs[j], merged_mobs[i + len(left_mobs)]) for j, i in enumerate(range(len(right_mobs)))]
        )
        
        # Indicate successful merging
        self.play(*[mob.animate.set_color(GREEN) for mob in merged_mobs])
        self.wait(0.4)
        
        # Update the original array
        arr[left:right + 1] = merged_array
    
    def create_array_squares(self, array, position):
        """Create visual representation of an array as squares with numbers"""
        return [VGroup(
                Square(side_length=0.6, fill_opacity=0.2, fill_color=DARK_GREY).move_to(position + RIGHT * i * 0.7),
                Text(str(num), font_size=24).move_to(position + RIGHT * i * 0.7)
            ) for i, num in enumerate(array)]