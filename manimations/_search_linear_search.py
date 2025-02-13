from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.openai import OpenAIService

class LinearSearchTTS(VoiceoverScene): 
    def construct(self): 
        self.set_speech_service(OpenAIService(voice="echo",model="tts-1-hd"))
        # self.set_speech_service(GTTSService(lang="en"))


        elements  = [12,33,11,99,22,55,90]
        n = len(elements)
        target = 99
        # Create visual elements (boxes and numbers)
        squares = VGroup(*[Square(side_length=1).shift(RIGHT*i) for i in range(n)]).move_to(ORIGIN)
        labels = VGroup(*[Text(str(elements[i]), font_size=36).move_to(squares[i]) for i in range(n)])
        arrow = Triangle().scale(0.5).rotate(PI).next_to(squares[0],UP)
        target_square = Square(side_length=1).next_to(squares[n//2]).shift(UP*2)
        target_label = Text(str(target),font_size=36).move_to(target_square)

        #Title: 
        title = Text("Visualizing Linear Search: A Step-by-Step Guide",font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        with self.voiceover(text="Let's talk about Linear Search today. One of the simplest strategies for searching data which simply loop through each element looking for the target."): 
            pass

        with self.voiceover(text="Consider the following list of elements"):
            self.play(Write(squares),Write(labels))
            self.wait(1)

        with self.voiceover(text=f"Suppose we want to search for number {target} within our list. How does the Linear Search Go about this?"):
            self.play(Write(target_square),Write(target_label))
            self.play(target_square.animate.set_color(YELLOW))
            self.wait(1)



        with self.voiceover(text=f"So, we will first, define a flag 'found', which will help us track wheather our item of interest has been found or not."):
            # pass
            found_flag_text = Text("Found",font_size=36).next_to(squares[n-1]).shift(RIGHT*0.2)
            self.play(Write(found_flag_text))
            self.wait(1)

        with self.voiceover(text=f"Since we are just starting our search, this flag will be set to false."):
            self.remove(found_flag_text)
            found_flag_text = Text("Found = False",font_size=36).next_to(squares[n-1]).shift(RIGHT*0.2)
            self.play(Write(found_flag_text))
            self.wait(1)

        with self.voiceover(text="We are going to iteratively compare each element with our target, and if we find a match we will stop there and return the value found!"): 
            pass
        self.wait(1)
        found = False 
        for _idx,el in enumerate(elements):
            if _idx == 0:
                self.play(Create(arrow))
            self.play(arrow.animate.next_to(squares[_idx], UP))

            comparison_text = Text(f"Is {el} == {target}?",font_size=36).to_edge(LEFT)

            with self.voiceover(f"Is {el} equals to our target {target}?"):
                self.play(Write(comparison_text))
                self.wait(1)
                # self.play(squares[_idx].animate.set_color(RED), squares[j+1].animate.set_color(RED))
                self.play(squares[_idx].animate.set_color(RED))
                self.play(target_square.animate.set_color(RED))


            if el == target: 
                with self.voiceover("Yes, we have found our target! We are going to stop here."): 
                    self.remove(found_flag_text)
                    found_flag_text = Text("Found = True",font_size=36).next_to(squares[n-1]).shift(RIGHT*0.2)
                    self.play(Write(found_flag_text))
                found = True
                break
            else: 
                with self.voiceover("No, continue searching"):
                    self.wait(1)


            self.remove(comparison_text,arrow)
        self.wait(2)
        with self.voiceover("That's it!As simple as it sounds, we have successfuly found our target value within the list with the help of a linear search"): 
                    self.wait(2)
        
        self.remove(squares,labels,found_flag_text,arrow,comparison_text,target_square,target_label)

             # Display Bubble Sort Algorithm
        code_text = '''
        def linear_search(elements, item):
            found = False
            for el in elements: 
                if el == item: 
                    found = True
                    break
            return found
        '''

        code = Code(
            code_string=code_text,
            language="Python",
            background="window",
            background_config={"stroke_color": "maroon"},
        ).to_edge(DOWN).move_to(ORIGIN).shift(DOWN*0.2)

        with self.voiceover(text="Here’s the Python implementation of linear search. You can find the link to the full source code in the video description below.") as tracker:
            self.remove(squares,labels)
            self.play(Write(code))
            self.wait(2)

        with self.voiceover(text="Thank you for watching!"):
            pass

        self.wait(2)