from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.openai import OpenAIService

import random

class EnhancedPProblems(VoiceoverScene):
    def construct(self):
        # Using OpenAI's high-definition voice for better clarity
        self.set_speech_service(OpenAIService(voice="echo", model="tts-1-hd"))
        # Title Scene
        title = Text("Taming the Complexity: Understanding P Problems").scale(0.8).to_edge(UP)
        subtitle = Text("Efficient solutions to everyday computational problems", color=BLUE).scale(0.5).next_to(title, DOWN)
        
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(1)  # Added pause for viewers to read the title

        # Introduction
        with self.voiceover("Ever wondered how your computer sorts a massive list of files so quickly?"):
            # Improved animation for sorting with sequential highlighting
            file_icons = VGroup(*[
                Rectangle(height=0.5, width=0.4, fill_opacity=0.8, fill_color=color)
                for color in [BLUE, RED, GREEN, YELLOW, PURPLE]
            ]).arrange(RIGHT, buff=0.2)  # Increased buffer to avoid visual crowding
            
            file_labels = VGroup(*[
                Text(label, font_size=20).next_to(icon, DOWN, buff=0.1)
                for icon, label in zip(file_icons, ["E", "B", "D", "A", "C"])
            ])
            
            computer = SVGMobject("desktop-computer").scale(0.6).to_edge(LEFT, buff=1)
        
            # Route visualization with improved spacing
            map_bg = Rectangle(height=3, width=3, fill_color=GREY_E, fill_opacity=0.3)
            start_point = Dot(color=GREEN).move_to(map_bg.get_corner(UL) + [0.5, -0.5, 0])
            end_point = Dot(color=RED).move_to(map_bg.get_corner(DR) + [-0.5, 0.5, 0])
            route = DashedLine(start_point.get_center(), end_point.get_center(), color=YELLOW)
            map_group = VGroup(map_bg, start_point, end_point, route).scale(0.6).to_edge(RIGHT, buff=1)
            
            # Animation sequence with better timing
            file_group = VGroup(file_icons, file_labels).move_to(ORIGIN)
            
            # First show the computer
            self.play(Create(computer), run_time=0.7)
            self.wait(0.3)
            
            # Then show files with sequential appearance
            self.play(FadeIn(file_icons, lag_ratio=0.2))
            self.play(FadeIn(file_labels, lag_ratio=0.2))
            
            # Sorting animation
            sorted_indices = [3, 1, 4, 2, 0]  # A, B, C, D, E
            sorted_icons = file_icons.copy()
            sorted_labels = file_labels.copy()
            
            # Highlight each element as it's being "processed"
            for i in range(len(sorted_indices)):
                self.play(
                    file_icons[sorted_indices[i]].animate.set_color(YELLOW),
                    run_time=0.3
                )
                self.play(
                    file_icons[sorted_indices[i]].animate.set_color(file_icons[sorted_indices[i]].get_color()),
                    run_time=0.2
                )
            
            # Show sorting result
            sorted_group = VGroup(*[file_icons[i] for i in sorted_indices])
            sorted_group.arrange(RIGHT, buff=0.2)
            sorted_text = VGroup(*[file_labels[i] for i in sorted_indices])
            for i, text in enumerate(sorted_text):
                text.next_to(sorted_group[i], DOWN, buff=0.1)
            
            sorted_full = VGroup(sorted_group, sorted_text).move_to(ORIGIN)
            
            self.play(Transform(VGroup(file_icons, file_labels), sorted_full), run_time=1.5)
            self.wait(1)
            
            # Hide sorting and show map
            self.play(
                # FadeOut(VGroup(file_icons, file_labels), shift=LEFT),
                FadeIn(map_group, shift=RIGHT)
            )
        # self.wait(1)    
        with self.voiceover("Or, lets say, how does it find the fastest route to your friend's house?"):
        
            # Animate the route finding with pulsing effect for clarity
            self.play(route.animate.set_color(BLUE), run_time=0.5)
            self.play(Flash(start_point, color=GREEN, line_length=0.2, flash_radius=0.3))
            self.play(Flash(end_point, color=RED, line_length=0.2, flash_radius=0.3))
            
            # Draw alternative routes that get discarded
            alt_route1 = ArcBetweenPoints(start_point.get_center(), end_point.get_center(), angle=PI/4, color=GREY)
            alt_route2 = ArcBetweenPoints(start_point.get_center(), end_point.get_center(), angle=-PI/4, color=GREY)
            
            self.play(Create(alt_route1), Create(alt_route2), run_time=0.7)
            self.play(
                alt_route1.animate.set_stroke(opacity=0.3), 
                alt_route2.animate.set_stroke(opacity=0.3),
                route.animate.set_stroke(width=4, color=GREEN)
            )
            
            self.wait(0.5)
            self.play(FadeOut(computer), FadeOut(map_group), FadeOut(alt_route1), FadeOut(alt_route2), FadeOut(VGroup(file_icons, file_labels))) 
                
        with self.voiceover("It's all thanks to a special group of problems called 'Polynomial Problems' or 'P problems' in short."):
            # Create a copy of the title to highlight the "P Problems" part
            # First, find where "P Problems" is in the title
            original_title_text = "Taming the Complexity: Understanding P Problems"
            p_problems_index = original_title_text.find("P Problems")
            
            # Create a new text object for highlighting just the "P Problems" part
            highlighted_text = Text("P Problems", color=WHITE).scale(0.8)
            
            # Position it correctly over the same text in the title
            # Get the position of "P Problems" in the original title
            p_problems_start = p_problems_index / len(original_title_text)  # Fraction of the way through
            p_problems_width = len("P Problems") / len(original_title_text)  # Width as a fraction
            
            # Calculate the position - this is an approximation and may need adjustment
            title_width = title.width
            title_left = title.get_left()[0]
            highlight_pos_x = title_left + (title_width * p_problems_start) + (title_width * p_problems_width / 2)
            
            # Move the highlight to position
            highlighted_text.move_to([highlight_pos_x, title.get_center()[1], 0])
            self.wait(1)
            # Animate highlighting
            self.play(
                Flash(highlighted_text, color=YELLOW, line_length=0.2, flash_radius=0.5, run_time=3.0),
                # FadeIn(highlighted_text)
            )
            
            # Keep it highlighted while continuing the narration
            self.wait(1)
            
            # Optional: fade it back to normal at the end of the voiceover
            # self.play(FadeOut(highlighted_text))
        self.wait(1)
        with self.voiceover("Today, we'll explore what makes these problems so manageable."):
            pass;
        self.wait(2)
        
        # Party Analogy with properly separated and timed easy and hard tasks
        with self.voiceover("Imagine you're organizing a huge party."):
            pass
        self.wait(1)
        # First part: Easy tasks
        with self.voiceover("Some tasks are easy: making a guest list and ordering pizza."):
            # Create party planning visualization with better vertical spacing
            easy_tasks_header = Text("Easy Tasks (P Problems):", color=GREEN).scale(0.6)
            
            # Create tasks but don't show them yet
            easy_task1 = Text("- Guest List", color=GREEN).scale(0.5)
            easy_task2 = Text("- Order Pizza", color=GREEN).scale(0.5)
            
            # Position the header
            easy_tasks_header.to_edge(LEFT, buff=1.5).shift(UP*2)
            
            # Position tasks with more vertical spacing
            easy_task1.next_to(easy_tasks_header, DOWN, buff=0.5).align_to(easy_tasks_header, LEFT)
            easy_task2.next_to(easy_task1, DOWN, buff=0.5).align_to(easy_task1, LEFT)
            
            # Add visual representations for tasks
            guest_list = VGroup(*[
                Dot(radius=0.05, color=BLUE) for _ in range(10)
            ]).arrange_in_grid(2, 5, buff=0.1).scale(1.2).next_to(easy_task1, RIGHT, buff=0.8)
            
            pizza_icon = Circle(radius=0.3, color=YELLOW, fill_opacity=0.8)
            pizza_slices = VGroup(*[
                Line(ORIGIN, 0.3*UP).rotate(angle, about_point=ORIGIN)
                for angle in np.linspace(0, 2*PI, 9)[:-1]
            ])
            pizza = VGroup(pizza_icon, pizza_slices).next_to(easy_task2, RIGHT, buff=0.8)
            
            # Animation sequence with improved timing
            self.play(Write(easy_tasks_header), run_time=0.7)
            
            # Wait for the voiceover to mention "guest list"
            self.wait(1.2)  # Adjust timing based on your voiceover speed
            
            # Guest list animation - show when mentioned in voiceover
            self.play(Write(easy_task1), run_time=0.5)
            self.play(FadeIn(guest_list, lag_ratio=0.1), run_time=0.8)
            
            # Wait for the voiceover to mention "ordering pizza"
            self.wait(0.8)  # Adjust timing based on your voiceover speed
            
            # Pizza order animation - show when mentioned in voiceover
            self.play(Write(easy_task2), run_time=0.5)
            self.play(Create(pizza_icon), run_time=0.5)
            self.play(Create(pizza_slices), run_time=0.5)
            
            self.wait(1)
        with self.voiceover("These easy tasks are like P problems. They're solvable by a computer in a reasonable amount of time, even if the party gets really big."):
            pass
        # Add 2 seconds wait between easy task and hard task transition
        self.wait(2)

        # Second part: Hard tasks
        with self.voiceover("In contrast, some tasks are a nightmare: like figuring out the seating arrangement for hundreds of guests with all their preferences and conflicts!"):
            # Hard tasks on right side with careful positioning
            hard_tasks_header = Text("Hard Tasks (Not P Problems):", color=RED).scale(0.6)
            hard_task = Text("- Seating Arrangement", color=RED).scale(0.5)
            
            # Position headers and task
            hard_tasks_header.to_edge(RIGHT, buff=1.5).shift(UP*2)
            hard_task.next_to(hard_tasks_header, DOWN, buff=0.5).align_to(hard_tasks_header, LEFT)
            
            # Seating problem visualization (complex graph) - position it lower to avoid overlap
            seats = VGroup()
            num_seats = 8
            for i in range(num_seats):
                angle = i * TAU / num_seats
                seat = Circle(radius=0.1, color=WHITE, fill_opacity=0)
                seat.move_to([0.6 * np.cos(angle), 0.6 * np.sin(angle), 0])
                seats.add(seat)
            
            # Add complexity lines between all seats (indicating constraints)
            constraints = VGroup()
            for i in range(len(seats)):
                for j in range(i+1, len(seats)):
                    if random.random() < 0.7:  # 70% chance of a constraint
                        line = DashedLine(
                            seats[i].get_center(), 
                            seats[j].get_center(),
                            color=RED_A,
                            dash_length=0.05
                        )
                        constraints.add(line)
            
            # Position the seating problem lower to avoid overlaps
            seating_problem = VGroup(seats, constraints).scale(0.9).next_to(hard_task, DOWN, buff=0.7)
            
            # Hard task animation
            self.play(Write(hard_tasks_header), run_time=0.7)
            self.wait(0.5)
            self.play(Write(hard_task), run_time=0.5)
            
            # Complex seating problem animation
            self.play(Create(seats), run_time=0.8)
            self.play(Create(constraints, lag_ratio=0.05), run_time=1)
            
            # Highlight the complexity - with delay to avoid overlap with text
            self.wait(0.5)
            self.play(
                constraints.animate.set_color(RED),
                Flash(seating_problem, color=RED_A, line_length=0.1, flash_radius=0.8),
                run_time=0.7
            )
            
            # Add a computer trying to solve the seating problem
            computer_icon = SVGMobject("desktop-computer").scale(0.4).next_to(seating_problem, DOWN, buff=0.5)  # Changed to below to avoid overlap
            thinking_bubble = SVGMobject("thought-bubble").scale(0.5).next_to(computer_icon, UP, buff=0.1).shift(RIGHT*1.5)
            question_mark = Text("?", color=RED).scale(0.8).move_to(thinking_bubble)
            computer_group = VGroup(computer_icon, thinking_bubble, question_mark)
            
            self.play(FadeIn(computer_group))
            self.play(
                Wiggle(question_mark),
                Flash(computer_icon, color=YELLOW, flash_radius=0.3),
                run_time=1
            )
            
        self.wait(2)
        with self.voiceover("These hard problems grow exponentially more difficult as they get bigger, unlike the manageable P problems."):
            # Show comparison between easy and hard sides
            # Move comparison to the left to avoid overlapping with seating arrangement
            comparison_arrow = Arrow(LEFT*3, RIGHT*3, color=YELLOW).move_to(DOWN*2.5)  # Moved lower
            comparison_text = Text("Polynomial vs. Exponential Growth", color=YELLOW).scale(0.5).next_to(comparison_arrow, DOWN)
            
            self.play(
                Create(comparison_arrow),
                Write(comparison_text),
                run_time=0.8
            )
            
            # Wait more time before transition
            self.wait(2)

        # Wait 1 more second after fadeout
        self.wait(2)

         # Clean transition
        self.play(
            FadeOut(VGroup(
                easy_tasks_header, easy_task1, easy_task2,
                guest_list, pizza_icon, pizza_slices,
                hard_tasks_header, hard_task, 
                seating_problem, computer_group,
                comparison_arrow, comparison_text
            ))
        )
        
        # Polynomial Time Explanation with improved visuals and positioning
        
        with self.voiceover("Computer scientists call this 'polynomial time'. Think of it like this: If you double the size of the problem (say, twice as many guests), the time it takes to solve it only increases a little bit – not exponentially, like that seating chart nightmare!"):
            # Temporarily hide the main title to avoid overlap
            self.play(FadeOut(title), FadeOut(subtitle))
            
            # Create a section title 
            section_title = Text("Understanding Polynomial Time", color=BLUE).scale(0.7).to_edge(UP)
            self.play(FadeIn(section_title))
            
            # Create axes with better labels and scale
            axes = Axes(
                x_range=[0, 5, 1],
                y_range=[0, 5, 1],
                axis_config={"include_tip": True, "numbers_to_include": range(0, 6)},
                x_axis_config={"label_direction": DOWN},
                y_axis_config={"label_direction": LEFT}
            ).scale(0.8)
            
            # Add axis labels for clarity
            x_label = Text("Problem Size", font_size=24).next_to(axes.x_axis, DOWN, buff=0.5)
            y_label = Text("Time to Solve", font_size=24).rotate(PI/2).next_to(axes.y_axis, LEFT, buff=0.5)
            
            # Create value trackers for smooth transitions
            t_growth = ValueTracker(0.1)  # For growing the graphs gradually
            t_points = ValueTracker(0.1)  # For showing points and timing
            
            def poly_func(x):
                return x**2/5
            
            def exp_func(x):
                return 2**x/4
            
            # Create graphs that will grow smoothly
            poly = always_redraw(lambda: axes.plot(
                lambda x: poly_func(x) if x <= t_growth.get_value() else poly_func(t_growth.get_value()), 
                color=GREEN, 
                x_range=[0, 5]
            ))
            
            exp = always_redraw(lambda: axes.plot(
                lambda x: exp_func(x) if x <= t_growth.get_value() else exp_func(t_growth.get_value()),
                color=RED,
                x_range=[0, 5]
            ))
            
            # Emphasize the cliff metaphor with little climber icons
            poly_climber = SVGMobject("person-hiking").scale(0.2).move_to(axes.c2p(4.5, poly_func(4.5)))
            exp_climber = SVGMobject("person-falling").scale(0.2).move_to(axes.c2p(4.5, exp_func(4.5)))
            
            # Add small labels for climbers if needed
            poly_climber_label = Text("Easy!", font_size=12, color=GREEN).next_to(poly_climber, UP, buff=0.1)
            exp_climber_label = Text("Impossible!", font_size=12, color=RED).next_to(exp_climber, UP, buff=0.1)

            # Add better labels with examples - positioned to avoid overlap
            poly_label = Text("Polynomial (n²): Gentle growth", font_size=33, color=GREEN).scale(0.4)
            exp_label = Text("Exponential (2ⁿ): Explosive growth!", font_size=33, color=RED).scale(0.4)
            
            # Position labels to avoid overlap
            poly_label.next_to(poly_climber, RIGHT, buff=0.2)
            exp_label.next_to(exp_climber, RIGHT, buff=0.2)
            
            # Double problem size indicators
            problem_size_1 = Dot(axes.c2p(1, 0), color=BLUE)
            problem_size_2 = Dot(axes.c2p(2, 0), color=BLUE)
            
            dashed_line_1 = DashedLine(
                axes.c2p(1, 0), 
                axes.c2p(1, 5), 
                color=BLUE_A,
                dash_length=0.05
            )
            
            dashed_line_2 = DashedLine(
                axes.c2p(2, 0), 
                axes.c2p(2, 5), 
                color=BLUE_A,
                dash_length=0.05
            )
            
            size_label_1 = Text("Size n", color=BLUE, font_size=13).next_to(problem_size_1, DOWN, buff=0.2)
            size_label_2 = Text("Size 2n", color=BLUE, font_size=13).next_to(problem_size_2, DOWN, buff=0.2)
            
            # Animation sequence
            self.play(
                Create(axes),
                Write(x_label),
                Write(y_label),
                run_time=1.5
            )
            
            # Add the graphs to the scene but they're initially almost empty (t_growth is small)
            self.add(poly, exp)
            
            # Show problem size doubling
            self.play(
                Create(problem_size_1),
                Create(dashed_line_1),
                Write(size_label_1)
            )
            
            # Add horizontal lines showing time increase for polynomial
            poly_time_1 = Dot(axes.c2p(1, poly_func(1)), color=GREEN)
            poly_time_1_label = Text("Time for size n", font_size=16, color=GREEN).next_to(poly_time_1, RIGHT, buff=0.2)
            
            self.play(
                Create(poly_time_1),
                Write(poly_time_1_label)
            )
            
            # Show doubling the problem size
            self.play(
                Create(problem_size_2),
                Create(dashed_line_2),
                Write(size_label_2)
            )
            
            # Show resulting polynomial time increase
            poly_time_2 = Dot(axes.c2p(2, poly_func(2)), color=GREEN)
            poly_time_2_label = Text("Time for size 2n", font_size=16, color=GREEN).next_to(poly_time_2, RIGHT, buff=0.2)
            
            poly_line = DashedLine(
                poly_time_1.get_center(),
                poly_time_2.get_center(),
                color=GREEN_A
            )
            
            self.play(
                Create(poly_time_2),
                Create(poly_line),
                Write(poly_time_2_label),
                run_time=1
            )
            
            # Now introduce exponential growth
            
            # Add exponential time points
            exp_time_1 = Dot(axes.c2p(1, exp_func(1)), color=RED)
            exp_time_2 = Dot(axes.c2p(2, exp_func(2)), color=RED)
            
            # Position labels to avoid overlap
            exp_time_1_label = Text("Exponential time for size n", font_size=16, color=RED).next_to(exp_time_1, LEFT, buff=0.2)
            exp_time_2_label = Text("Exponential time for size 2n", font_size=16, color=RED).next_to(exp_time_2, RIGHT, buff=0.2)
            
            exp_line = DashedLine(
                exp_time_1.get_center(),
                exp_time_2.get_center(),
                color=RED_A
            )
            
            self.play(
                Create(exp_time_1),
                Write(exp_time_1_label),
                run_time=0.8
            )
            
            self.play(
                Create(exp_time_2),
                Create(exp_line),
                Write(exp_time_2_label),
                run_time=0.8
            )
            
            # SMOOTH TRANSITION: Animate both graphs growing simultaneously
            # First to show the comparison of growth rates from 0 to 2
            self.play(t_growth.animate.set_value(2), run_time=1.5)
            
            # Add labels after initial growth
            self.play(Write(poly_label), Write(exp_label), run_time=0.8)
            
            # Now continue the growth to the full range to emphasize the difference
            self.play(t_growth.animate.set_value(5), run_time=2)
            
            # Keep the graph on screen for 2 seconds as requested
            self.wait(2)
        
        self.wait(1)
        with self.voiceover("Polynomial time is like a gentle slope, while exponential time is like a sheer cliff."):
               # Add the climbers
            self.play(FadeIn(poly_climber), FadeIn(poly_climber_label), run_time=0.5)
            self.play(FadeIn(exp_climber), FadeIn(exp_climber_label), run_time=0.5)

          # Clean transition
        self.play(
            FadeOut(VGroup(
                section_title, axes, poly, exp, poly_label, exp_label,
                problem_size_1, problem_size_2, dashed_line_1, dashed_line_2,
                size_label_1, size_label_2,
                poly_time_1, poly_time_1_label, poly_time_2, poly_time_2_label,
                exp_time_1, exp_time_1_label, exp_time_2, exp_time_2_label,
                poly_line, exp_line, x_label, y_label,
                poly_climber, exp_climber,poly_climber_label,exp_climber_label
            )),
            # FadeIn(title), FadeIn(subtitle)  # Restore the main title
        )

        self.wait(1)

        with self.voiceover("Let's say you have a bunch of unsorted song titles on your playlist. Your computer can quickly alphabetize them using a 'sorting algorithm'. One such algorithm, called 'Merge Sort', works in polynomial time."):
            # Hide main title to avoid overlap
            
            # Create playlist visualization with proper positioning
            playlist_title = Text("My Playlist", color=BLUE).scale(0.7).to_edge(UP)
            
            songs = VGroup(*[
                Rectangle(height=0.6, width=3.5, fill_opacity=0.8, fill_color=color)  # Increased width for longer text
                for color in [RED_D, BLUE_D, GREEN_D, YELLOW_D, PURPLE_D]
            ]).arrange(DOWN, buff=0.2).scale(0.8)
            
            songs.next_to(playlist_title, DOWN, buff=0.5)

            # Create text labels and ensure they're properly centered in each rectangle
            song_titles = []
            song_names = ["Echoes of Tomorrow", "Beyond the Horizon", "Dream Walker", "Astral Journey", "Cosmic Waves"]

            for i, (song, name) in enumerate(zip(songs, song_names)):
                # Create text with appropriate size that fits inside the rectangle
                text = Text(name, font_size=18, color=WHITE)
                # Ensure text is properly centered in the rectangle
                text.move_to(song.get_center())
                song_titles.append(text)

            song_titles = VGroup(*song_titles)

            
            # Add sorting visualization
            computer_icon = SVGMobject("desktop-computer").scale(0.6).to_edge(LEFT, buff=1.5)
            
            # FIXED MERGE SORT VISUALIZATION WITH LETTERS INSIDE BOXES
            # Use original unsorted letters
            unsorted_letters = ["E", "B", "D", "A", "C"]
            
            # Helper function to create a box with a letter inside
            def create_letter_box(letter, color=BLUE_D):
                box = Rectangle(height=0.4, width=0.8, fill_opacity=0.8, fill_color=color)
                text = Text(letter, font_size=16, color=WHITE)
                text.move_to(box.get_center())
                return VGroup(box, text)
            
            # Level 1: Split into individual elements - original unsorted state
            level1_boxes = []
            for letter, color in zip(unsorted_letters, [RED_D, BLUE_D, GREEN_D, YELLOW_D, PURPLE_D]):
                level1_boxes.append(create_letter_box(letter, color))
            
            level1 = VGroup(*level1_boxes).arrange(RIGHT, buff=0.4).scale(0.7)
            
            # Level 2: First merge step - create boxes with letters
            # Group 1: B, E sorted
            level2_1_boxes = [
                create_letter_box("B", BLUE_D),
                create_letter_box("E", RED_D)
            ]
            level2_1 = VGroup(*level2_1_boxes).arrange(RIGHT, buff=0.3).scale(0.7)
            
            # Group 2: A, D sorted
            level2_2_boxes = [
                create_letter_box("A", YELLOW_D),
                create_letter_box("D", GREEN_D)
            ]
            level2_2 = VGroup(*level2_2_boxes).arrange(RIGHT, buff=0.3).scale(0.7)
            
            # Group 3: C alone
            level2_3 = create_letter_box("C", PURPLE_D).scale(0.7)
            
            # Arrange level 2 groups
            level2 = VGroup(level2_1, level2_2, level2_3).arrange(RIGHT, buff=0.8)
            
            # Level 3: Second merge step
            # Group 1: A, B, E merged correctly
            level3_1_boxes = [
                create_letter_box("A", YELLOW_D),
                create_letter_box("B", BLUE_D),
                create_letter_box("E", RED_D)
            ]
            level3_1 = VGroup(*level3_1_boxes).arrange(RIGHT, buff=0.3).scale(0.7)
            
            # Group 2: C, D merged correctly
            level3_2_boxes = [
                create_letter_box("C", PURPLE_D),
                create_letter_box("D", GREEN_D)
            ]
            level3_2 = VGroup(*level3_2_boxes).arrange(RIGHT, buff=0.3).scale(0.7)
            
            # Arrange level 3 groups
            level3 = VGroup(level3_1, level3_2).arrange(RIGHT, buff=1.0)
            
            # Final level: Fully sorted in alphabetical order A, B, C, D, E
            level4_boxes = [
                create_letter_box("A", YELLOW_D),
                create_letter_box("B", BLUE_D),
                create_letter_box("C", PURPLE_D),
                create_letter_box("D", GREEN_D),
                create_letter_box("E", RED_D)
            ]
            level4 = VGroup(*level4_boxes).arrange(RIGHT, buff=0.3).scale(0.7)
            
            # Position levels with vertical spacing
            merge_sort_y_positions = [2, 0.8, -0.4, -1.6]
            
            level1.move_to([0, merge_sort_y_positions[0], 0])
            level2.move_to([0, merge_sort_y_positions[1], 0])
            level3.move_to([0, merge_sort_y_positions[2], 0])
            level4.move_to([0, merge_sort_y_positions[3], 0])
            
            # Create arrows with clear positioning
            def create_arrow(source, target):
                return Arrow(
                    start=source.get_bottom() + DOWN*0.05, 
                    end=target.get_top() + UP*0.05, 
                    buff=0.1,
                    color=WHITE,
                    max_tip_length_to_length_ratio=0.15
                )
            
            # Create arrows for level transitions
            # Level 1 to Level 2
            split_arrows = VGroup(
                create_arrow(level1[0], level2_1[1]),  # E → second position in BE
                create_arrow(level1[1], level2_1[0]),  # B → first position in BE
                create_arrow(level1[2], level2_2[1]),  # D → second position in AD
                create_arrow(level1[3], level2_2[0]),  # A → first position in AD
                create_arrow(level1[4], level2_3)      # C → C
            )
            
            # Level 2 to Level 3
            merge_arrows_l2_to_l3 = VGroup(
                Arrow(level2_1.get_bottom() + DOWN*0.05, level3_1.get_top() + UP*0.05, buff=0.1, color=WHITE),
                Arrow(level2_2.get_bottom() + DOWN*0.05, level3_1.get_top() + UP*0.05, buff=0.1, color=WHITE),
                Arrow(level2_3.get_bottom() + DOWN*0.05, level3_2.get_top() + UP*0.05, buff=0.1, color=WHITE)
            )
            
            # Level 3 to Level 4
            merge_arrows_l3_to_l4 = VGroup(
                Arrow(level3_1.get_bottom() + DOWN*0.05, level4.get_top() + UP*0.05, buff=0.1, color=WHITE),
                Arrow(level3_2.get_bottom() + DOWN*0.05, level4.get_top() + UP*0.05, buff=0.1, color=WHITE)
            )
            
            # Animation sequence
            self.play(Write(playlist_title), run_time=0.7)
            
            # Position songs below the title with enough space
            songs.next_to(playlist_title, DOWN, buff=0.5)
            
            self.play(
                Create(songs, lag_ratio=0.2),
                Write(song_titles, lag_ratio=0.2),
                run_time=1.5
            )
            
            # Show computer processing
            self.play(Create(computer_icon), run_time=0.7)
            processing_text = Text("Sorting...", color=YELLOW).scale(0.5).next_to(computer_icon, UP)
            self.play(Write(processing_text))
            
            # Hide playlist, transition to merge sort visualization
            self.play(
                FadeOut(songs), 
                FadeOut(song_titles),
                FadeOut(processing_text),
                FadeIn(level1),
                run_time=1
            )
            
            # Merge sort animation - Step 1: Split
            merge_sort_text = Text("Merge Sort", color=BLUE).scale(0.7).to_edge(UP)
            step1_text = Text("Step 1: Split into individual elements", color=WHITE).scale(0.5).next_to(merge_sort_text, DOWN)
            
            self.play(
                ReplacementTransform(playlist_title, merge_sort_text),
                Write(step1_text),
                run_time=0.8
            )
            
            # Step 2: First merge - initial sorting into pairs
            step2_text = Text("Step 2: Merge into sorted pairs", color=WHITE).scale(0.5).next_to(merge_sort_text, DOWN)
            
            self.play(
                ReplacementTransform(step1_text, step2_text),
                FadeIn(level2),
                Create(split_arrows, lag_ratio=0.2),
                run_time=1.5
            )
            
            # Step 3: Second merge - merge sorted groups
            step3_text = Text("Step 3: Merge sorted groups", color=WHITE).scale(0.5).next_to(merge_sort_text, DOWN)
            
            self.play(
                ReplacementTransform(step2_text, step3_text),
                FadeIn(level3),
                Create(merge_arrows_l2_to_l3, lag_ratio=0.2),
                run_time=1.5
            )
            
            # Step 4: Final merge - final correctly sorted result
            step4_text = Text("Step 4: Final sorted result (A-E)", color=WHITE).scale(0.5).next_to(merge_sort_text, DOWN)
            
            self.play(
                ReplacementTransform(step3_text, step4_text),
                FadeIn(level4),
                Create(merge_arrows_l3_to_l4, lag_ratio=0.2),
                run_time=1.5
            )
            
            # Highlight polynomial time complexity
            time_complexity = Text("Time Complexity: O(n log n)", color=GREEN).scale(0.5).next_to(step4_text, RIGHT, buff=0.3)
            self.play(Write(time_complexity), run_time=0.7)
            

        self.wait(1)
        with self.voiceover(" Even if your playlist has thousands of songs, the computer can sort it relatively quickly."):
          
            # thousands_text = Text("Even with thousands of songs...", color=YELLOW).scale(0.6).to_edge(UP)
            checkmark = Text("✓", color=GREEN).scale(1.5).next_to(computer_icon).shift(LEFT*0.5)

            # Create many songs block with proper positioning to avoid overlap with merge sort
            many_songs = VGroup(*[
                Rectangle(height=0.1, width=2.5, fill_opacity=0.8, fill_color=interpolate_color(BLUE, RED, i/20))
                for i in range(20)
            ]).arrange(DOWN, buff=0.02)

            # Position many_songs further to the left to avoid overlap with merge sort
            many_songs.next_to(computer_icon, RIGHT, buff=0.3).shift(LEFT*1.5)
            # self.play(FadeIn(many_songs, lag_ratio=0.05), run_time=1)
            self.play(Write(many_songs),Write(checkmark), run_time=0.5)
            
            # Wait a bit before transition
            self.wait(1)
            
            
            # Add extra wait before next section
        
        self.wait(2)
        self.clear()
        
        # GPS/Shortest Path Example with improved visualizations and better spacing
        with self.voiceover("Think about your GPS app. It figures out the quickest way to your destination, even with traffic and multiple routes. This is another P problem! Algorithms like 'Dijkstra's Algorithm' can find the shortest path in polynomial time. Even if the map has many roads and cities, the app can find the best route without taking forever."):

            # Clean transition
            # self.play(
            #     FadeOut(VGroup(
            #         level1, level1_labels, level2, level2_labels, level3, level3_labels, 
            #         level4, level4_labels, split_arrows, merge_arrows_l2_to_l3, merge_arrows_l3_to_l4,
            #         computer_icon, checkmark, many_songs
            #     )),
            # )

            
            # Create a more detailed navigation scene
            section_title = Text("GPS Navigation: Finding Shortest Path", color=BLUE).scale(0.7).to_edge(UP)
            
            # Create a more structured city map
            city_bg = Rectangle(height=5, width=7, fill_color=GREY_E, fill_opacity=0.3).scale(0.8)
            
            # Position city map on the left side for better balance - do this BEFORE creating buildings
            city_bg.move_to(LEFT * 2.5 + DOWN * 0.8)  # Move further left and down to avoid overlap with text
            
            # Create buildings with better visual structure
            buildings = VGroup()
            building_positions = [
                [-2, 1.5, 0], [0, 2, 0], [2, 1.5, 0],  # Top row
                [-2.5, 0, 0], [0, 0, 0], [2.5, 0, 0],  # Middle row
                [-2, -1.5, 0], [0, -2, 0], [2, -1.5, 0]  # Bottom row
            ]
            
            # Apply the LEFT shift and DOWN shift to all building positions directly
            shifted_positions = []
            for pos in building_positions:
                shifted_positions.append([pos[0] - 2.5, pos[1] - 0.8, pos[2]])  # Apply the LEFT * 2.5 and DOWN * 0.8 shift
            
            for i, pos in enumerate(shifted_positions):
                height = random.uniform(0.5, 0.8)
                width = random.uniform(0.3, 0.5)
                building = Rectangle(
                    height=height, 
                    width=width, 
                    fill_color=interpolate_color(BLUE_E, PURPLE_E, random.random()),
                    fill_opacity=0.8,
                    stroke_color=WHITE,
                    stroke_width=1
                ).move_to(pos)
                buildings.add(building)
            
            # Add city landmarks for context - use shifted positions
            start_point = Dot(color=GREEN).move_to(shifted_positions[0])
            end_point = Dot(color=RED).move_to(shifted_positions[8])
            
            start_label = Text("Start", color=GREEN).scale(0.4).next_to(start_point, UP)
            end_label = Text("End", color=RED).scale(0.4).next_to(end_point, UP)
            
            # Create road network between buildings
            roads = VGroup()
            road_graph = [
                (0, 1), (0, 3), (1, 2), (1, 4), (2, 5),
                (3, 4), (3, 6), (4, 5), (4, 7), (5, 8),
                (6, 7), (7, 8)
            ]
            
            for start_idx, end_idx in road_graph:
                road = Line(
                    buildings[start_idx].get_center(),
                    buildings[end_idx].get_center(),
                    color=WHITE,
                    stroke_width=2
                )
                roads.add(road)
            
            # Add traffic congestion to some roads
            traffic_roads = [1, 4, 7]  # Indices of roads with traffic
            for idx in traffic_roads:
                traffic_indicator = DashedLine(
                    roads[idx].get_start(),
                    roads[idx].get_end(),
                    color=RED_E,
                    dash_length=0.1,
                    stroke_width=4
                )
                roads[idx].become(traffic_indicator)
            
            # Create a smartphone frame - position on right side
            phone_frame = RoundedRectangle(
                height=4.5, 
                width=2.5, 
                corner_radius=0.2,
                stroke_color=GREY_A,
                stroke_width=3,
                fill_color=BLACK,
                fill_opacity=0.8
            ).to_edge(RIGHT, buff=1)
            
            phone_screen = Rectangle(
                height=4, 
                width=2.2,
                fill_color=GREY_E,
                fill_opacity=1,
                stroke_width=0
            ).move_to(phone_frame)
            
            # Animation sequence
            self.play(Write(section_title), run_time=0.8)
            
            # Create the city
            self.play(
                FadeIn(city_bg),
                FadeIn(buildings, lag_ratio=0.1),
                run_time=1.2
            )
            
            # Add roads with traffic indicators
            self.play(Create(roads, lag_ratio=0.1), run_time=1.5)
            
            # Show starting and ending points
            self.play(
                Create(start_point),
                Create(end_point),
                Write(start_label),
                Write(end_label),
                run_time=0.8
            )
            
            # Show smartphone with navigation app
            self.play(
                Create(phone_frame),
                FadeIn(phone_screen),
                run_time=0.8
            )
            
            # Create mini map on phone
            mini_map = city_bg.copy().scale(0.35).move_to(phone_screen)
            mini_buildings = buildings.copy().scale(0.35).move_to(phone_screen)
            mini_roads = roads.copy().scale(0.35).move_to(phone_screen)
            mini_start = start_point.copy().scale(0.35).move_to(mini_buildings[0].get_center())
            mini_end = end_point.copy().scale(0.35).move_to(mini_buildings[8].get_center())
            
            nav_header = Text("Navigation", color=WHITE).scale(0.3).move_to(phone_screen.get_top() + DOWN*0.3)
            
            self.play(
                FadeIn(mini_map),
                FadeIn(mini_buildings),
                FadeIn(mini_roads),
                FadeIn(mini_start),
                FadeIn(mini_end),
                Write(nav_header),
                run_time=1
            )
            
            # Show algorithm analyzing all paths
            searching_text = Text("Searching all paths...", color=YELLOW).scale(0.25).next_to(nav_header, DOWN, buff=0.1)
            self.play(Write(searching_text), run_time=0.5)
            
            # Highlight possible paths with different colors
            possible_paths = [
                [0, 1, 2, 5, 8],  # Indices of roads for path 1
                [0, 3, 6, 7, 8],  # Indices of roads for path 2
                [0, 3, 4, 5, 8],  # Indices of roads for path 3
            ]
            
            path_colors = [BLUE_A, PURPLE_A, YELLOW_A]
            path_lines = VGroup()
            mini_path_lines = VGroup()
            
            # Show algorithm considering multiple paths
            for i, path_indices in enumerate(possible_paths):
                path_segments = VGroup()
                mini_path_segments = VGroup()
                
                for j in range(len(path_indices) - 1):
                    idx1, idx2 = path_indices[j], path_indices[j+1]
                    for road_idx, (s, e) in enumerate(road_graph):
                        if (s == idx1 and e == idx2) or (s == idx2 and e == idx1):
                            road_copy = roads[road_idx].copy().set_stroke(path_colors[i], opacity=0.5)
                            mini_road_copy = mini_roads[road_idx].copy().set_stroke(path_colors[i], opacity=0.5)
                            path_segments.add(road_copy)
                            mini_path_segments.add(mini_road_copy)
                
                path_lines.add(path_segments)
                mini_path_lines.add(mini_path_segments)
                
                self.play(
                    FadeIn(path_segments, lag_ratio=0.3),
                    FadeIn(mini_path_segments, lag_ratio=0.3),
                    run_time=0.8
                )
            
            # Show algorithm selecting optimal path
            found_text = Text("Route found!", color=GREEN).scale(0.25).next_to(nav_header, DOWN, buff=0.1)
            
            # Define the optimal path (shortest and avoiding traffic)
            optimal_path_indices = [0, 3, 6, 7, 8]  # Bottom route avoiding traffic
            optimal_path = VGroup()
            mini_optimal_path = VGroup()
            
            for j in range(len(optimal_path_indices) - 1):
                idx1, idx2 = optimal_path_indices[j], optimal_path_indices[j+1]
                for road_idx, (s, e) in enumerate(road_graph):
                    if (s == idx1 and e == idx2) or (s == idx2 and e == idx1):
                        road_copy = roads[road_idx].copy().set_stroke(GREEN, width=4)
                        mini_road_copy = mini_roads[road_idx].copy().set_stroke(GREEN, width=4)
                        optimal_path.add(road_copy)
                        mini_optimal_path.add(mini_road_copy)
            
            self.play(
                ReplacementTransform(searching_text, found_text),
                FadeOut(path_lines),
                FadeOut(mini_path_lines),
                run_time=0.8
            )
            
            self.play(
                FadeIn(optimal_path, lag_ratio=0.2),
                FadeIn(mini_optimal_path, lag_ratio=0.2),
                run_time=1
            )
            
            # Show time estimation
            eta_text = Text("ETA: 12 minutes", color=GREEN).scale(0.25).next_to(found_text, DOWN, buff=0.1)
            distance_text = Text("Distance: 3.2 miles", color=WHITE).scale(0.25).next_to(eta_text, DOWN, buff=0.1)
            
            self.play(
                Write(eta_text),
                Write(distance_text),
                run_time=0.8
            )
            
            # Highlight algorithm name and complexity
            algo_text = Text("Dijkstra's Algorithm: O(E log V)", color=BLUE).scale(0.5).next_to(section_title, DOWN, buff=0.3)
            self.play(Write(algo_text), run_time=0.8)
            
            self.wait(0.5)
            
            # Demonstrate that it scales well with larger maps
            scaling_text = Text("Scales well with larger maps!", color=GREEN).scale(0.5).next_to(algo_text, DOWN, buff=0.3).to_edge(UP, buff=1.5).shift(DOWN*0.5)
            
            # Make the map more complex (add more nodes and edges)
            extra_dots = VGroup(*[
                Dot(color=GREY).move_to([
                    random.uniform(-3, 3),
                    random.uniform(-2, 2),
                    0
                ]) for _ in range(10)
            ])
            
            # Adjust positions to match city group position - update to use the same shift as buildings
            for dot in extra_dots:
                dot.shift(LEFT * 2.5 + DOWN * 0.8)  # Match the shift we applied to buildings
            
            extra_roads = VGroup()
            for dot in extra_dots:
                # Connect to 2 random buildings
                for _ in range(2):
                    building = random.choice(buildings)
                    new_road = DashedLine(
                        dot.get_center(),
                        building.get_center(),
                        color=GREY_A,
                        dash_length=0.05
                    )
                    extra_roads.add(new_road)
            
            self.play(Write(scaling_text), run_time=0.7)
            self.play(
                FadeIn(extra_dots, lag_ratio=0.1),
                Create(extra_roads, lag_ratio=0.1),
                run_time=1
            )
            
            # Show that it still finds path quickly
            fast_checkmark = Text("✓", color=GREEN).scale(1.0).next_to(scaling_text)
            self.play(Write(fast_checkmark), run_time=0.5)
            
            self.wait(1)
            
            # Add wait time before next section
        self.wait(2)
         # Clean transition
        self.play(
            FadeOut(VGroup(
                section_title, city_bg, buildings, roads, start_point, end_point,
                start_label, end_label, phone_frame, phone_screen, mini_map,
                mini_buildings, mini_roads, mini_start, mini_end, nav_header,
                found_text, optimal_path, mini_optimal_path, eta_text, distance_text,
                algo_text, scaling_text, extra_dots, extra_roads, fast_checkmark
            ))
        )

        # Final Recap with more engaging Visual Elements and better spacing
        with self.voiceover("P problems are the problems computers can handle efficiently. Sorting, finding shortest routes, searching databases – these are all examples of P problems. They're the reason we can use computers for so many useful tasks. They're the manageable problems in a world of complex challenges."):
            # Hide main title to avoid overlap
            
            # Create a dedicated recap title that doesn't overlap
            recap_title = Text("P Problems: Making Computing Possible", color=BLUE).scale(0.7).to_edge(UP)
            
            recap_text = VGroup(
                Text("P Problems:", color=BLUE).scale(0.6),
                Text("- Solvable in Polynomial Time", color=GREEN).scale(0.5),
                Text("- Efficiently Computed", color=GREEN).scale(0.5),
                Text("- Scales Well with Input Size", color=GREEN).scale(0.5),
                Text("Examples:", color=BLUE).scale(0.6),
                Text("- Sorting", color=GREEN).scale(0.5),
                Text("- Shortest Path", color=GREEN).scale(0.5),
                Text("- Database Search", color=GREEN).scale(0.5)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)  # Added more space between lines
            
            # Position text on left side with enough margin
            recap_text.to_edge(LEFT, buff=1.5).shift(UP * 0.5)
            
            # Add visual icons next to examples - aligned properly
            sort_icon = VGroup(*[
                Rectangle(height=0.2, width=0.4, fill_opacity=0.8, fill_color=color)
                for color in [YELLOW_D, BLUE_D, RED_D, GREEN_D, PURPLE_D]
            ]).arrange(RIGHT, buff=0.05).scale(0.8).next_to(recap_text[5], RIGHT, buff=0.4)
            
            path_icon = VGroup(
                Circle(radius=0.1, color=GREEN, fill_opacity=1),
                Line(LEFT*0.3, RIGHT*0.3, color=BLUE),
                Circle(radius=0.1, color=RED, fill_opacity=1)
            ).scale(0.8).next_to(recap_text[6], RIGHT, buff=0.4)
            
            db_icon = VGroup(
                Rectangle(height=0.4, width=0.6, fill_color=BLUE_E, fill_opacity=0.8, stroke_color=WHITE),
                Line(LEFT*0.2 + UP*0.05, RIGHT*0.2 + UP*0.05, color=WHITE).scale(0.6),
                Line(LEFT*0.2, RIGHT*0.2, color=WHITE).scale(0.6),
                Line(LEFT*0.2 - UP*0.05, RIGHT*0.2 - UP*0.05, color=WHITE).scale(0.6),
                Dot(color=YELLOW).scale(0.8)
            ).scale(0.8).next_to(recap_text[7], RIGHT, buff=0.4)
            
            # Add a visual illustration of polynomial vs exponential growth
            # Position on right side with enough margin
            axes = Axes(
                x_range=[0, 5],
                y_range=[0, 5],
                axis_config={"include_tip": True}
            ).scale(0.5).to_edge(RIGHT, buff=1.5)
            
            poly = axes.plot(lambda x: x**2/5, color=GREEN)
            exp = axes.plot(lambda x: 2**x/4, color=RED)
            
            growth_title = Text("Time vs Problem Size", color=BLUE).scale(0.4).next_to(axes, UP, buff=0.2)
            
            # Position labels carefully to avoid overlap
            poly_label = Text("P Problems (n²)", color=GREEN).scale(0.3).next_to(poly, RIGHT, buff=0.1).shift(LEFT*1.5)
            exp_label = Text("Hard Problems (2ⁿ)", color=RED).scale(0.3).next_to(exp, RIGHT, buff=0.2).shift(UP*1.5).shift(LEFT*0.4)
            
            # Animation sequence
            self.play(Write(recap_title), run_time=0.8)
            
            # Show P problem characteristics
            self.play(
                Write(recap_text[0]),  # "P Problems:" header
                run_time=0.5
            )
            
            # Show each characteristic with sequential timing
            for i in range(1, 4):
                self.play(Write(recap_text[i]), run_time=0.5)
            
            # Show examples header
            self.play(Write(recap_text[4]), run_time=0.5)  # "Examples:" header
            
            # Show sorting example with icon
            self.play(
                Write(recap_text[5]),
                Create(sort_icon),
                run_time=0.7
            )
            
            # Show shortest path example with icon
            self.play(
                Write(recap_text[6]),
                Create(path_icon),
                run_time=0.7
            )
            
            # Show database search example with icon
            self.play(
                Write(recap_text[7]),
                Create(db_icon),
                run_time=0.7
            )
            
            # Add growth comparison graph
            self.play(
                Create(axes),
                Write(growth_title),
                run_time=0.8
            )
            
            self.play(
                Create(poly),
                Write(poly_label),
                run_time=0.7
            )
            
            self.play(
                Create(exp),
                Write(exp_label),
                run_time=0.7
            )
            
            # Add a computer icon processing efficiently - position at bottom center
            computer_icon = SVGMobject("desktop-computer").scale(0.3).move_to([0, -2, 0])
            success_indicator = Text("✓", color=GREEN).scale(1).next_to(computer_icon, RIGHT)
            
            self.play(
                Create(computer_icon),
                run_time=0.7
            )
            
            self.play(
                Write(success_indicator),
                Flash(computer_icon, color=GREEN, line_length=0.2, flash_radius=0.5),
                run_time=0.8
            )
            
            self.wait(1)
            
        # Group all elements for clean fadeout
        all_elements = VGroup(
            recap_title, recap_text, sort_icon, path_icon, db_icon,
            axes, poly, exp, growth_title, poly_label, exp_label,
            computer_icon, success_indicator
        )
        
        # Clean transition
        self.play(FadeOut(all_elements))
            
        # Enhanced Closing Message with visuals of everyday technologies and better spacing
        # with self.voiceover("So, next time you use your phone to find directions or sort your photos, remember the power of P problems! They're making our digital world faster and more efficient."):
            
        #     # Create closing title with proper positioning
        #     closing_title = Text("P Problems All Around Us", color=BLUE).scale(0.8).to_edge(UP)
            
        #     # Create devices showing P problem examples
        #     smartphone = RoundedRectangle(
        #         height=2, width=1, corner_radius=0.1,
        #         stroke_color=GREY_A, stroke_width=2,
        #         fill_color=BLACK, fill_opacity=0.8
        #     ).shift(LEFT*2)
            
        #     laptop = VGroup(
        #         Rectangle(height=1.2, width=1.8, fill_color=GREY_D, fill_opacity=0.8),
        #         Rectangle(height=0.1, width=1.8, fill_color=GREY, fill_opacity=0.8).next_to(ORIGIN, DOWN, buff=0)
        #     ).shift(RIGHT*2)
            
        #     # Add app icons on phone
        #     map_app = Square(side_length=0.2, fill_color=BLUE, fill_opacity=0.8).move_to(smartphone.get_center() + UP*0.3)
        #     photo_app = Square(side_length=0.2, fill_color=RED, fill_opacity=0.8).move_to(smartphone.get_center())
        #     music_app = Square(side_length=0.2, fill_color=GREEN, fill_opacity=0.8).move_to(smartphone.get_center() + DOWN*0.3)
            
        #     # Position labels with space to avoid overlap
        #     map_label = Text("Maps", font_size=16).next_to(map_app, RIGHT, buff=0.2)
        #     photo_label = Text("Photos", font_size=16).next_to(photo_app, RIGHT, buff=0.2)
        #     music_label = Text("Music", font_size=16).next_to(music_app, RIGHT, buff=0.2)
            
        #     # Add code on laptop screen
        #     code_text = """
        #     def merge_sort(arr):
        #         if len(arr) <= 1:
        #             return arr
        #         mid = len(arr) // 2
        #         left = merge_sort(arr[:mid])
        #         right = merge_sort(arr[mid:])
        #         return merge(left, right)
        #     """
        #     code = Text(code_text, font="Monospace", font_size=10).move_to(laptop)
            
        #     # Animation sequence
        #     self.play(Write(closing_title), run_time=0.8)
            
        #     # Show devices with sequential timing
        #     self.play(
        #         Create(smartphone),
        #         Create(laptop),
        #         run_time=1
        #     )
            
        #     # Show phone apps with sequential timing for clarity
        #     self.play(
        #         FadeIn(map_app), 
        #         Write(map_label),
        #         run_time=0.6
        #     )
            
        #     self.play(
        #         FadeIn(photo_app),
        #         Write(photo_label),
        #         run_time=0.6
        #     )
            
        #     self.play(
        #         FadeIn(music_app),
        #         Write(music_label),
        #         run_time=0.6
        #     )
            
        #     # Show code on laptop
        #     self.play(Write(code), run_time=0.8)
            
        #     # Highlight key points with animations
        #     self.play(
        #         Flash(map_app, color=BLUE, line_length=0.1, flash_radius=0.2),
        #         Flash(photo_app, color=RED, line_length=0.1, flash_radius=0.2),
        #         Flash(music_app, color=GREEN, line_length=0.1, flash_radius=0.2),
        #         run_time=1
        #     )
            
        # Enhanced section with only smartphone visualization
        with self.voiceover("So, next time you use your phone to find directions or sort your photos, remember the power of P problems! They're making our digital world faster and more efficient."):
            
            # Create closing title with proper positioning
            closing_title = Text("P Problems All Around Us", color=BLUE).scale(0.8).to_edge(UP)
            
            # Create smartphone only
            smartphone = RoundedRectangle(
                height=2.5, width=1.3, corner_radius=0.1,
                stroke_color=GREY_A, stroke_width=2,
                fill_color=BLACK, fill_opacity=0.8
            ).move_to(ORIGIN)
            
            # Add app icons on phone with more space between them
            map_app = Square(side_length=0.25, fill_color=BLUE, fill_opacity=0.8).move_to(smartphone.get_center() + UP*0.6)
            photo_app = Square(side_length=0.25, fill_color=RED, fill_opacity=0.8).move_to(smartphone.get_center())
            music_app = Square(side_length=0.25, fill_color=GREEN, fill_opacity=0.8).move_to(smartphone.get_center() + DOWN*0.6)
            
            # Position labels with improved spacing
            map_label = Text("Maps", font_size=20).next_to(map_app, RIGHT, buff=0.3)
            photo_label = Text("Photos", font_size=20).next_to(photo_app, RIGHT, buff=0.3)
            music_label = Text("Music", font_size=20).next_to(music_app, RIGHT, buff=0.3)
            
            # Add algorithm labels next to the app icons to explain what P problems they solve
            map_algo = Text("Shortest Path", font_size=16, color=YELLOW).next_to(map_label, RIGHT, buff=0.3)
            photo_algo = Text("Pattern Recognition", font_size=16, color=YELLOW).next_to(photo_label, RIGHT, buff=0.3)
            music_algo = Text("Recommendation", font_size=16, color=YELLOW).next_to(music_label, RIGHT, buff=0.3)
            
            # Animation sequence
            self.play(Write(closing_title), run_time=0.8)
            
            # Show smartphone
            self.play(Create(smartphone), run_time=1)
            
            # Show phone apps with sequential timing for clarity
            self.play(
                FadeIn(map_app), 
                Write(map_label),
                run_time=0.6
            )
            
            self.play(
                Write(map_algo),
                run_time=0.6
            )
            
            self.play(
                FadeIn(photo_app),
                Write(photo_label),
                run_time=0.6
            )
            
            self.play(
                Write(photo_algo),
                run_time=0.6
            )
            
            self.play(
                FadeIn(music_app),
                Write(music_label),
                run_time=0.6
            )
            
            self.play(
                Write(music_algo),
                run_time=0.6
            )
            
            # Highlight key points with animations
            self.play(
                Flash(map_app, color=BLUE, line_length=0.1, flash_radius=0.3),
                Flash(photo_app, color=RED, line_length=0.1, flash_radius=0.3),
                Flash(music_app, color=GREEN, line_length=0.1, flash_radius=0.3),
                run_time=1.5
            )
        self.wait(2)
        # self.clear()
        # Add final "thank you" message with proper spacing
        # thank_you = Text("Thank you for watching!", color=YELLOW).scale(0.8).move_to(ORIGIN)
        with self.voiceover("Thank you for watching!"): 
            # self.play(Write(thank_you), run_time=1)
            pass
        self.wait(2.0)