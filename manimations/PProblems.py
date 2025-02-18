from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.openai import OpenAIService

import random

class EnhancedPProblems(VoiceoverScene):
    def construct(self):
        # self.set_speech_service(GTTSService(lang="en"))
        self.set_speech_service(OpenAIService(voice="echo",model="tts-1-hd"))


        # Title Scene
        title = Text("Taming the Complexity: Understanding P Problems").scale(0.8).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction
        with self.voiceover("Ever wondered how your computer sorts a massive list of files so quickly, or finds the fastest route to your friend's house? It's all thanks to a special group of problems called 'P problems'. Today, we'll explore what makes these problems so manageable."):
            # Add animated icons for sorting and routing
            file_icons = VGroup(*[
                Rectangle(height=0.5, width=0.4, fill_opacity=0.8, fill_color=color)
                for color in [BLUE, RED, GREEN, YELLOW, PURPLE]
            ]).arrange(RIGHT, buff=0.1)
            route_icon = SVGMobject("map-pin").scale(0.5).next_to(file_icons, RIGHT, buff=2)

            self.play(Create(file_icons), Create(route_icon))
            self.wait(2)
            self.play(FadeOut(file_icons), FadeOut(route_icon))

        # Party Analogy
        with self.voiceover("Imagine you're organizing a huge party. Some tasks are easy: making a guest list, ordering pizza. Others are a nightmare: figuring out the seating arrangement for hundreds of guests! P problems are like those easy tasks. They're solvable by a computer in a reasonable amount of time, even if the party (or the problem) gets really big."):
            # Create party planning visualization
            party_tasks = VGroup(
                Text("Easy Tasks:", color=GREEN).scale(0.6),
                Text("- Guest List", color=GREEN).scale(0.5),
                Text("- Order Pizza", color=GREEN).scale(0.5),
                Text("Hard Tasks:", color=RED).scale(0.6),
                Text("- Seating Arrangement", color=RED).scale(0.5)
            ).arrange(DOWN, aligned_edge=LEFT).shift(UP * 1.5)
            
            # Add simple party icons
            guest_icon = Square(side_length=0.3).set_fill(BLUE, opacity=0.8)
            table = Circle(radius=0.5).set_stroke(WHITE)
            party_scene = VGroup(guest_icon, table).arrange(RIGHT)
            
            self.play(FadeIn(party_tasks))
            self.wait(1)
            self.play(Create(party_scene))
            self.wait(1)
            self.play(FadeOut(party_tasks), FadeOut(party_scene))
            self.wait(1)


        # Polynomial Time Explanation with Real Objects
        with self.voiceover("Computer scientists call this 'polynomial time'. Think of it like this: If you double the size of the problem (say, twice as many guests), the time it takes to solve it only increases a little bit – not exponentially, like that seating chart nightmare! Polynomial time is like a gentle slope, while exponential time is like a sheer cliff."):
            # Create axes and plots
            axes = Axes(
                x_range=[0, 5],
                y_range=[0, 5],
                axis_config={"include_tip": True}
            )
            
            poly = axes.plot(lambda x: x**2/5, color=GREEN)
            exp = axes.plot(lambda x: 2**x/4, color=RED)
            
            poly_label = Text("Polynomial (Gentle)", color=GREEN).scale(0.4)
            exp_label = Text("Exponential (Scary!)", color=RED).scale(0.4)
            
            poly_label.next_to(poly, LEFT)
            exp_label.next_to(exp, RIGHT)
            
            self.play(Create(axes))
            self.wait(1)

            self.play(Create(poly), Write(poly_label))
            self.wait(1)

            self.play(Create(exp), Write(exp_label))
            self.wait(2)
            self.play(FadeOut(axes), FadeOut(poly), FadeOut(exp),
                     FadeOut(poly_label), FadeOut(exp_label))

            self.wait(1)


        # Sorting Example with Library Books
        with self.voiceover("Let's say you have a bunch of unsorted song titles on your playlist. Your computer can quickly alphabetize them using a 'sorting algorithm'. One such algorithm, called 'Merge Sort', works in polynomial time. Even if your playlist has thousands of songs, the computer can sort it relatively quickly."):
            # Create library book visualization
            books = VGroup(*[
                Rectangle(height=1.5, width=0.3, fill_opacity=0.8, fill_color=color)
                for color in [RED, BLUE, GREEN, YELLOW, PURPLE]
            ]).arrange(RIGHT, buff=0.1)
            
            book_labels = VGroup(*[
                Text(title, font_size=20).next_to(book, DOWN)
                for book, title in zip(books, ["E", "B", "D", "A", "C"])
            ])
            
            shelf = Line(LEFT*3, RIGHT*3, color=BLUE)
            books.next_to(shelf, UP, buff=0)
            
            self.play(Create(shelf))
            self.play(Create(books), Write(book_labels))
            
            # Sorting animation
            sorted_books = books.copy()
            sorted_labels = VGroup(*sorted(book_labels, key=lambda x: x.text))
            sorted_books.arrange(RIGHT, buff=0.1).next_to(shelf, UP, buff=0)
            
            self.play(
                Transform(books, sorted_books),
                Transform(book_labels, sorted_labels),
                run_time=2
            )
            self.wait(1)
            self.play(FadeOut(books), FadeOut(book_labels), FadeOut(shelf))

        # GPS/Shortest Path Example
        with self.voiceover("Think about your GPS app. It figures out the quickest way to your destination, even with traffic and multiple routes. This is another P problem! Algorithms like 'Dijkstra's Algorithm' can find the shortest path in polynomial time. Even if the map has many roads and cities, the app can find the best route without taking forever."):
            # Create city map with buildings
            buildings = VGroup(*[
                Rectangle(height=random.uniform(0.5, 1.5), width=0.8, fill_color=GRAY, 
                         fill_opacity=0.7) for _ in range(6)
            ]).arrange_in_grid(2, 3, buff=1)
            
            roads = VGroup()
            for i in range(len(buildings)):
                for j in range(i + 1, len(buildings)):
                    if random.random() < 0.6:
                        road = Line(
                            buildings[i].get_center(),
                            buildings[j].get_center(),
                            color=WHITE
                        )
                        roads.add(road)
            
            self.play(Create(buildings))
            self.play(Create(roads))

            # Highlight shortest path
            path = [roads[0], roads[2], roads[4]]
            for road in path:
                self.play(road.animate.set_color(GREEN), run_time=0.5)
            
            self.wait(1)
            self.play(FadeOut(buildings), FadeOut(roads))

        # Final Recap with Visual Elements
        with self.voiceover("P problems are the problems computers can handle efficiently. Sorting, finding shortest routes, searching databases – these are all examples of P problems. They're the reason we can use computers for so many useful tasks. They're the manageable problems in a world of complex challenges."):
            recap_text = VGroup(
                Text("P Problems:", color=BLUE).scale(0.6),
                Text("- Solvable in Polynomial Time", color=GREEN).scale(0.5),
                Text("- Easily Verifiable", color=GREEN).scale(0.5),
                Text("Examples:", color=BLUE).scale(0.6),
                Text("- Sorting", color=GREEN).scale(0.5),
                Text("- Shortest Path", color=GREEN).scale(0.5)
            ).arrange(DOWN, aligned_edge=LEFT).shift(UP * 1.5)
            self.play(FadeIn(recap_text))
            self.wait(2)

        # Closing Message
        with self.voiceover("So, next time you use your phone to find directions or sort your photos, remember the power of P problems! They're making our digital world faster and more efficient."):
            closing_text = Text("Thank you for watching!", color=BLUE).scale(0.8)
            self.play(FadeOut(recap_text))
            self.play(Write(closing_text))
            self.wait(2)
            self.play(FadeOut(closing_text), FadeOut(title))
