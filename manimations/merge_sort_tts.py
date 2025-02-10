from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.openai import OpenAIService


class MergeSortVisualization(VoiceoverScene):
    def construct(self):
        # self.set_speech_service(GTTSService(lang="en"))
        self.set_speech_service(
            OpenAIService(
                voice="echo",
                model="tts-1-hd",
            )
        )
        
        title = Text("Merge Sort Visualization").to_edge(UP)
        self.play(Write(title))
        
        elements = [38, 27, 43, 3,21,74,82,11]

        original_position = ORIGIN + UP * 2.5
        initial_position = ORIGIN + UP * 1
        sorted_position = ORIGIN + DOWN * 2
        
        self.original_mobs = self.create_array_squares(elements, original_position)
        array_mobs = self.create_array_squares(elements, initial_position)
        
        with self.voiceover(text="Let’s talk about Merge Sort—an efficient way to sort numbers by dividing and merging them back in order."):
            pass
        
        self.play(*[FadeIn(mob) for mob in self.original_mobs])
        self.wait(0.5)
        self.play(*[FadeIn(mob) for mob in array_mobs])
        
        with self.voiceover(text="Here’s an unsorted list. Our goal is to sort it in ascending order using Merge Sort."):
            self.wait(1)
        
        with self.voiceover("Starting Merge Sort on the list."):
            self.wait(1)
        
        self.merge_sort(elements, 0, len(elements) - 1, 0, initial_position, array_mobs)
        
        with self.voiceover("Merge Sort completed. The list is now sorted."):
            self.wait(2)
        # Display code block with Python implementation at the end
        with self.voiceover(text="Here is the Python implementation of Merge Sort. You may check the source code in the link below this video."):
            code_text = """
            def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]
            
            merge_sort(left_half)
            merge_sort(right_half)
            
            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1
            
            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1
            
            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
    """
            # Create the code block using 'Code' class
        code = Code(
            code_string=code_text,  # Correct argument: 'code_string'
            language="Python",
            background="window",
            background_config={"stroke_color": "maroon"},
        ).scale(0.6).to_edge(DOWN)

        self.play(Create(code))  # Show the code at the end
        self.wait(3)
        
        with self.voiceover(text="Thank you for watching!"):
            pass


    def merge_sort(self, arr, left, right, depth, position, parent_mobs=None):
        if left < right:
            mid = (left + right) // 2
            spacing = (right - left + 1) * 0.4
            left_position = position + LEFT * spacing + DOWN * 0.8
            right_position = position + RIGHT * spacing + DOWN * 0.8
            
            with self.voiceover(f"Dividing list from index {left} to {mid} and {mid+1} to {right}."):
                self.wait(0.5)
            
            left_mobs = self.create_array_squares(arr[left:mid + 1], left_position)
            right_mobs = self.create_array_squares(arr[mid + 1:right + 1], right_position)
            
            self.play(*[FadeIn(mob) for mob in left_mobs + right_mobs])
            
            left_result = self.merge_sort(arr, left, mid, depth + 1, left_position, left_mobs)
            right_result = self.merge_sort(arr, mid + 1, right, depth + 1, right_position, right_mobs)
            
            if parent_mobs and parent_mobs != self.original_mobs:
                with self.voiceover("We are now ready to merge."):
                    self.play(*[FadeOut(mob) for mob in parent_mobs])
            
            self.merge(arr, left, mid, right, position)
            
            return left_mobs + right_mobs

    def merge(self, arr, left, mid, right, position):
        left_subarray = arr[left:mid + 1]
        right_subarray = arr[mid + 1:right + 1]
        
        left_mobs = self.create_array_squares(left_subarray, position + LEFT * 0.8)
        right_mobs = self.create_array_squares(right_subarray, position + RIGHT * 0.8)
        
        with self.voiceover("Merging sublists."):
            self.wait(0.5)
        
        merged_array = []
        i = j = 0
        while i < len(left_subarray) and j < len(right_subarray):
            if left_subarray[i] < right_subarray[j]:
                merged_array.append(left_subarray[i])
                i += 1
            else:
                merged_array.append(right_subarray[j])
                j += 1
        
        merged_array.extend(left_subarray[i:])
        merged_array.extend(right_subarray[j:])
        
        merged_mobs = self.create_array_squares(merged_array, position)
        
        self.play(*[ReplacementTransform(left_mobs[i], merged_mobs[i]) for i in range(len(left_mobs))],
                *[ReplacementTransform(right_mobs[j], merged_mobs[i + len(left_mobs)]) for j, i in enumerate(range(len(right_mobs)))])
        
        self.play(*[mob.animate.set_color(GREEN) for mob in merged_mobs])
        self.wait(0.5)
        
        arr[left:right + 1] = merged_array
    
    def create_array_squares(self, array, position):
        return [VGroup(Square(side_length=0.6).move_to(position + RIGHT * i * 0.6),
                    Text(str(num), font_size=24).move_to(position + RIGHT * i * 0.6))
            for i, num in enumerate(array)]