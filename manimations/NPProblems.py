from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService
import random

class EnhancedNPProblems(VoiceoverScene):
    def construct(self):
        self.set_speech_service(OpenAIService(voice="echo", model="tts-1-hd"))

        # Title Scene
        title = Text("Unraveling the Mystery: Understanding NP Problems").scale(0.8).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction to NP
        with self.voiceover("We've talked about P problems, the easy ones for computers. But what about the really tough challenges?  That's where NP problems come in.  NP doesn't stand for 'Not Possible', but rather 'Nondeterministic Polynomial'.  It's a class of problems where, if you're given a *potential* solution, you can quickly *check* if it's correct.  Finding the solution itself, however, might be incredibly difficult."):
            self.wait(2)

        # The Subset Sum Problem
        with self.voiceover("Let's take an example: the Subset Sum problem. Imagine you have a set of numbers, like 5, 12, 17, and 23.  The question is: can you find a subset of these numbers that adds up to a specific target, say, 30?"):
            numbers = [5, 12, 17, 23]
            target = 30
            number_mobs = VGroup(*[Integer(num) for num in numbers]).arrange(RIGHT, buff=0.5)
            target_mob = Integer(target).next_to(number_mobs, DOWN, buff=1)
            self.play(Create(number_mobs), Write(target_mob))
            self.wait(1)

        with self.voiceover("If I give you a possible solution, say 5, 12, and 13, you can quickly add them up and check if it equals 30.  But *finding* that subset in the first place?  That could take a long time, especially if you have a lot of numbers."):
            solution = [5, 12, 13]  # Note: 13 is not in the original set, for demonstration
            solution_sum = sum(solution)  # Calculate the sum numerically
            solution_mobs = VGroup(*[Integer(num) for num in solution]).arrange(RIGHT, buff=0.5).next_to(number_mobs, DOWN).set_color(GREEN)

            # self.play(Transform(number_mobs.copy(), solution_mobs))
            self.play(Write(solution_mobs))

            self.remove(target_mob)
            sum_mob = MathTex(r"\sum = ", str(solution_sum)).next_to(solution_mobs, DOWN) # Use the calculated sum
            self.play(Write(sum_mob))
            self.wait(1)


        with self.voiceover("This highlights a key point about NP problems: verifying a solution is easy, but finding one can be hard.  It's like checking a completed puzzle versus assembling it from scratch."):
            self.play(FadeOut(number_mobs), FadeOut(target_mob), FadeOut(solution_mobs), FadeOut(sum_mob))
            self.wait(1)

        # The Traveling Salesperson Problem (TSP)
        with self.voiceover("Another classic NP problem is the Traveling Salesperson Problem, or TSP.") as _:
            self.wait(1)
                            
        with self.voiceover("You have a list of cities, and you want to find the shortest route that visits every city exactly once and returns to the starting city."):
            # self.remove(solution_mobs,number_mobs)
            # cities = VGroup(*[Dot() for _ in range(6)]).arrange_in_grid(2, 3)
            # self.play(Create(cities))
            # self.wait(1)
             # Create cities and connections
            cities = VGroup(*[Dot(color=BLUE) for _ in range(6)])
            cities.arrange_in_grid(3, 2, buff=1.5)
            
            # Add city labels
            labels = VGroup(*[
                Text(f"City {i+1}", font_size=24).next_to(city, DOWN)
                for i, city in enumerate(cities)
            ])
            
            self.play(Create(cities), Write(labels))



        with self.voiceover("Given a proposed route, you can easily calculate its total distance.  But finding the absolute shortest route?  That becomes incredibly difficult as the number of cities increases.  Even a small increase in cities can dramatically increase the number of possible routes."):
            # # Show some possible routes (just lines connecting the dots)
            # routes = VGroup()
            # for _ in range(3):  # Show 3 random routes
            #     route_cities = random.sample(list(cities), len(cities))
            #     route = VGroup(*[Line(route_cities[i].get_center(), route_cities[(i+1)%len(route_cities)].get_center()) for i in range(len(route_cities))]).set_color(BLUE)
            #     routes.add(route)
            # self.play(Create(routes[0]))
            # self.wait(0.5)
            # self.play(Transform(routes[0],routes[1]))
            # self.wait(0.5)
            # self.play(Transform(routes[1],routes[2]))
            # self.wait(1)
            # self.play(FadeOut(routes))


            # Show all possible connections
            connections = VGroup()
            for i in range(len(cities)):
                for j in range(i + 1, len(cities)):
                    line = Line(cities[i].get_center(), cities[j].get_center(), color=GRAY, stroke_opacity=0.3)
                    connections.add(line)
            
            self.play(Create(connections))
            
            # Highlight one possible route
            route = VGroup(*[
                Line(cities[i].get_center(), cities[(i+1)%6].get_center(), color=RED)
                for i in range(6)
            ])
            
            self.play(Create(route))
            self.wait(1)
            self.play(FadeOut(cities), FadeOut(labels), FadeOut(connections), FadeOut(route))



        # NP-Complete
        with self.voiceover("Now, within NP, there's a special subset called NP-Complete.  These are the *hardest* problems in NP.  If you could solve any NP-Complete problem quickly, you could solve *all* NP problems quickly.  Think of them as the 'universal translators' for NP problems.  The Subset Sum and TSP we just discussed are both NP-Complete."):
            np_circle = Circle(radius=2, color=BLUE).shift(LEFT*2)
            np_complete_circle = Circle(radius=1, color=RED).move_to(np_circle.get_center())
            np_label = Text("NP", color=BLUE).next_to(np_circle, UP)
            np_complete_label = Text("NP-Complete", color=RED).next_to(np_complete_circle, UP)
            self.play(Create(np_circle), Create(np_complete_circle), Write(np_label), Write(np_complete_label))
            self.wait(2)

        # NP-Hard
        with self.voiceover("Finally, there are NP-Hard problems. These are at least as hard as *any* problem in NP, but they don't necessarily have to be in NP themselves.  This means that a solution to an NP-hard problem might not even be quickly verifiable.  A classic example is the Halting Problem: can you determine if a given computer program will eventually stop running, or will it run forever? This is undecidable, and therefore NP-hard."):
            np_hard_text = Text("NP-Hard", color=YELLOW).next_to(np_circle, RIGHT)
            self.play(Write(np_hard_text))
            self.wait(2)

        # Recap
        with self.voiceover("Let's recap: NP problems are those where solutions are easy to check. NP-Complete problems are the hardest problems in NP. And NP-Hard problems are at least as hard as any problem in NP, but solutions might not be verifiable.  These concepts are crucial for understanding the limits of computation and the challenges of solving complex problems."):
            self.wait(2)

        # Closing
        with self.voiceover("Understanding these classifications helps us appreciate the complexity of computation and the challenges of solving certain problems, like optimizing routes or finding specific data within large datasets. Thank you for watching!"):
            self.play(FadeOut(np_circle), FadeOut(np_complete_circle), FadeOut(np_label), FadeOut(np_complete_label), FadeOut(np_hard_text), FadeOut(title))
            self.wait(2)

