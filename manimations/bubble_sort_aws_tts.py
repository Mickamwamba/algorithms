from manim import *
import boto3
import os

def generate_audio(text, filename):
    polly = boto3.client('polly', region_name='us-east-1')
    response = polly.synthesize_speech(Text=text, OutputFormat='mp3', VoiceId='Joanna')
    with open(filename, 'wb') as f:
        f.write(response['AudioStream'].read())

def cleanup():
    for file in os.listdir():
        if file.endswith('.mp3'):
            os.remove(file)

class BubbleSortAnimation(Scene):
    def construct(self):
        numbers = [5, 3, 8, 1, 4]
        n = len(numbers)
        squares = VGroup(*[Square(side_length=1).shift(RIGHT * i) for i in range(n)])
        labels = VGroup(*[Text(str(numbers[i]), font_size=36).move_to(squares[i].get_center()) for i in range(n)])
        
        title = Text("Bubble Sort: Simple and Clear Explanation", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        intro_audio = "intro.mp3"
        generate_audio("Let’s talk about Bubble Sort—one of the simplest sorting algorithms out there!", intro_audio)
        self.add_sound(intro_audio)
        self.wait(5)
        
        self.play(Create(squares), Write(labels))
        self.wait(1)
        
        for i in range(n - 1):
            self.wait(2)
            swapped = False
            pass_audio = f"pass_{i+1}.mp3"
            generate_audio(f"Pass {i+1} begins", pass_audio)
            self.add_sound(pass_audio)
            
            for j in range(n - 1 - i):
                compare_audio = f"compare_{i}_{j}.mp3"
                generate_audio(f"Comparing {numbers[j]} and {numbers[j+1]}", compare_audio)
                self.add_sound(compare_audio)
                
                self.play(squares[j].animate.set_color(RED), squares[j+1].animate.set_color(RED))
                self.wait(0.5)
                
                if numbers[j] > numbers[j + 1]:
                    swap_audio = f"swap_{i}_{j}.mp3"
                    generate_audio("Swapping the two numbers", swap_audio)
                    self.add_sound(swap_audio)
                    
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
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
                
                self.play(squares[j].animate.set_color(WHITE), squares[j+1].animate.set_color(WHITE))
            
            self.play(squares[n-1-i].animate.set_color(GREEN))
            if not swapped:
                break  
        
        self.wait(1)
        sorted_audio = "sorted.mp3"
        generate_audio("The list is now sorted!", sorted_audio)
        self.add_sound(sorted_audio)
        self.wait(2)
        cleanup()

    
