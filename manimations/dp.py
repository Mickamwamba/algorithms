from manim import *
import numpy as np
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
from manim_voiceover.services.openai import OpenAIService

# Define colors for different item types
FOOD_COLOR = "#e74c3c"  # Red
TOOL_COLOR = "#3498db"  # Blue
CAMPING_COLOR = "#2ecc71"  # Green
TECH_COLOR = "#9b59b6"  # Purple
CLOTHING_COLOR = "#f1c40f"  # Yellow

class KnapsackAdventureScene(VoiceoverScene):
    def construct(self):

        # Set up the voiceover
        self.set_speech_service(OpenAIService(voice="echo", model="tts-1-hd"))
        
        # Define class-level variables to avoid scope issues
        self.items = [
            {"name": "Food Supplies", "weight": 4, "value": 10, "color": FOOD_COLOR, "icon": "🍗"},
            {"name": "Multi-tool", "weight": 1, "value": 7, "color": TOOL_COLOR, "icon": "🔧"},
            {"name": "Sleeping Bag", "weight": 3, "value": 8, "color": CAMPING_COLOR, "icon": "🛌"},
            {"name": "Camera", "weight": 2, "value": 9, "color": TECH_COLOR, "icon": "📷"},
            {"name": "Jacket", "weight": 2, "value": 6, "color": CLOTHING_COLOR, "icon": "🧥"},
        ]
        self.max_capacity = 7
        self.cells = {}
        self.dp_table = None
        self.dp_values = None
        
        # Scene 1: Adventure Introduction
        with self.voiceover(
            """
            Imagine you're planning a weekend hiking trip through the beautiful
            trails of Yosemite National Park. You've got a variety of items you'd like
            to bring along.
            """
        ) as tracker:
            # Create title
            title = Text("The Backpacking Problem", font_size=48)
            title.to_edge(UP)
            self.play(Write(title))
            
            # Create mountain background silhouette with polygons instead of SVG
            mountains = VGroup()
            
            # Back mountains (darker)
            back_mountain_points = [
                [-6, -3, 0],  # Bottom left
                [-6, 0, 0],  # Left edge
                [-4, 2, 0],  # First peak
                [-2, 0.5, 0],  # Valley
                [0, 3, 0],  # Second peak
                [2, 1, 0],  # Valley
                [4, 2.5, 0],  # Third peak
                [6, -1, 0],  # Right edge
                [6, -3, 0],  # Bottom right
            ]
            back_mountains = Polygon(*back_mountain_points, color="#2c3e50", fill_opacity=1)
            
            # Front mountains (lighter)
            front_mountain_points = [
                [-6, -3, 0],  # Bottom left
                [-6, -1, 0],  # Left edge
                [-3, 1, 0],  # First peak
                [-1, -0.5, 0],  # Valley
                [1, 1.5, 0],  # Second peak
                [3, 0, 0],  # Valley
                [5, 0.5, 0],  # Third peak
                [6, -0.5, 0],  # Right edge
                [6, -3, 0],  # Bottom right
            ]
            front_mountains = Polygon(*front_mountain_points, color="#34495e", fill_opacity=1)
            
            mountains.add(back_mountains, front_mountains)
            mountains.scale(1.5)
            mountains.to_edge(DOWN)
            mountains.set_z_index(-1)
            
            self.play(FadeIn(mountains))
            
            # Create items to choose from
            items_title = Text("Available Items", font_size=32)
            items_title.next_to(title, DOWN, buff=0.5)
            
            self.play(Write(items_title))
            self.wait(0.5)  # Added pause
            
            # Create item cards - rearranged to have Camera and Jacket in a second row
            item_cards = VGroup()
            
            # Position first three items in top row
            for i in range(3):
                card = self.create_item_card(self.items[i])
                x_pos = (i - 1) * 3.0  # More spacing between cards
                y_pos = 0
                card.move_to(ORIGIN + np.array([x_pos, y_pos, 0]))
                item_cards.add(card)
            
            # Position last two items (Camera and Jacket) in bottom row
            for i in range(3, 5):
                card = self.create_item_card(self.items[i])
                x_pos = ((i-3) - 0.5) * 3.0  # Center the two cards
                y_pos = -2.5  # Move down to create second row with more space
                card.move_to(ORIGIN + np.array([x_pos, y_pos, 0]))
                item_cards.add(card)
            
            self.play(FadeIn(item_cards, lag_ratio=0.2))
            self.wait(1)  # Added pause
            
            # Keep references for later use
            self.item_cards = item_cards
            self.mountains = mountains
            self.title = title
            self.items_title = items_title
            
        # Continue with backpack introduction
        with self.voiceover(
            """
            But there's just one problem: your backpack can only
            hold a limited amount of weight.
            """
        ) as tracker:
            # Create a backpack image - now shown only when mentioned
            backpack = self.create_backpack()
            backpack.scale(1.5)
            backpack.to_edge(RIGHT, buff=1.5)
            backpack.to_edge(UP, buff=3.5)  # Moved up to avoid interference with item cards
            
            self.play(Create(backpack))
            
            # Show backpack capacity
            capacity_label = Text("Capacity: 7 kg", font_size=28, color=YELLOW)
            capacity_label.next_to(backpack, UP, buff=0.3)
            
            self.play(Write(capacity_label))
            self.wait(0.5)  # Added pause
            
            # Keep references for later use
            self.backpack = backpack
            self.capacity_label = capacity_label
            
        # Scene 2: Defining the Knapsack Problem
        with self.voiceover(
            """
            This situation perfectly illustrates the zero-one knapsack problem. For each item,
            you have a binary choice: either pack it entirely (one) or leave it behind (zero).
            You can't just pack half a sleeping bag or a quarter of your camera!
            """
        ) as tracker:
            # Wait for the voiceover to mention binary choice before showing 0/1 demonstration
            # Highlight one item
            highlighted_item = self.item_cards[2]  # Sleeping bag
            highlight_box = SurroundingRectangle(highlighted_item, color=YELLOW, stroke_width=3, buff=0.1)
            self.play(Create(highlight_box))
            
            self.wait(1)  # Added pause before the choice demonstration
            
            # Create visualization for 0/1 choice
            choice_group = VGroup()
            
            # Pack Option (1)
            pack_text = Text("Pack it (1)", font_size=24, color=GREEN)
            pack_arrow = Arrow(highlighted_item.get_right(), self.backpack.get_left(), color=GREEN, buff=0.2)
            pack_group = VGroup(pack_text, pack_arrow)
            pack_text.next_to(pack_arrow, UP, buff=0.2)
            
            # Leave Option (0)
            leave_text = Text("Leave it (0)", font_size=24, color=RED)
            leave_cross = Cross(highlighted_item.copy(), stroke_width=3, color=RED)
            leave_group = VGroup(leave_text, leave_cross)
            leave_text.next_to(leave_cross, DOWN, buff=0.2)
            
            choice_group.add(pack_group, leave_group)
            
            # Show pack option
            self.play(
                Create(pack_arrow),
                Write(pack_text)
            )
            self.wait(1)
            
            # Show leave option
            self.play(
                FadeOut(pack_arrow),
                FadeOut(pack_text)
            )
            self.play(
                Create(leave_cross),
                Write(leave_text)
            )
            self.wait(1)
        
        with self.voiceover(
            """
            Each item has both a weight and a value - which represents how useful or
            important it would be on your trip. Your challenge is to pack your backpack
            with the most valuable combination of items without exceeding its weight capacity.
            """
        ) as tracker:
            # Remove choice visualization to clean up
            self.play(
                FadeOut(leave_cross),
                FadeOut(leave_text),
                FadeOut(highlight_box)
            )
            
            # Move items into a cleaner layout for the next scenes
            self.play(
                self.items_title.animate.to_edge(LEFT, buff=1).to_edge(UP, buff=1),
                # Rearrange all items in a vertical list on the left
                self.item_cards.animate.arrange(DOWN, buff=0.4).next_to(self.items_title, DOWN, buff=0.5).to_edge(LEFT, buff=1)
            )
            self.wait(0.5)  # Added pause

        # Scene 3: Naive Approach - Try All Combinations
        with self.voiceover(
            """
            One approach would be to try every possible combination of items.
            With five items, you'd need to evaluate 2 to the power of 5, or 32 different combinations.
            """
        ) as tracker:
            # Create title for this section - positioned to not interfere with other elements
            approach_title = Text("Approach 1: Try All Combinations", font_size=36)
            approach_title.to_edge(RIGHT, buff=1)  # Moved to the right
            approach_title.to_edge(UP, buff=1)    # Moved down from top
            
            self.play(
                FadeOut(self.backpack),
                FadeOut(self.capacity_label),
                Write(approach_title)
            )
            self.wait(0.5)  # Added pause
        
        with self.voiceover(
            """
            Let's look at a few examples.
            """
        ) as tracker:
            # Create a visualization area for combinations
            combo_area = Rectangle(height=4, width=8, color=WHITE, fill_opacity=0.1)
            combo_area.move_to(ORIGIN + RIGHT * 2)  # Moved right to avoid overlap with item list
            
            combo_title = Text("Possible Combinations", font_size=28)
            combo_title.next_to(combo_area, UP, buff=0.2)
            
            self.play(
                Create(combo_area),
                Write(combo_title)
            )
            
            # Show several different combinations
            combinations = [
                [0, 1, 3],  # Food, Multi-tool, Camera
                [1, 2, 4],  # Multi-tool, Sleeping Bag, Jacket
                [0, 2, 3, 4],  # Food, Sleeping Bag, Camera, Jacket
            ]
            
            for i, combo_indices in enumerate(combinations):
                # Create the combination display
                combo_cards = VGroup()
                for idx in combo_indices:
                    card = self.create_item_card(self.items[idx], scale=0.7)
                    combo_cards.add(card)
                
                # Arrange cards horizontally with more space
                combo_cards.arrange(RIGHT, buff=0.6)
                combo_cards.move_to(combo_area.get_center())
                
                # Calculate total weight and value
                total_weight = sum(self.items[idx]["weight"] for idx in combo_indices)
                total_value = sum(self.items[idx]["value"] for idx in combo_indices)
                
                # Create weight and value display - with more spacing
                weight_text = Text(f"Total Weight: {total_weight} kg", font_size=24)
                value_text = Text(f"Total Value: {total_value} points", font_size=24)
                
                weight_text.next_to(combo_cards, DOWN, buff=0.5)  # Increased buffer
                value_text.next_to(weight_text, DOWN, buff=0.3)   # Increased buffer
                
                # Show if it fits in the backpack
                if total_weight <= self.max_capacity:
                    valid_text = Text("✓ Fits in Backpack", font_size=28, color=GREEN)
                else:
                    valid_text = Text("✗ Too Heavy!", font_size=28, color=RED)
                
                valid_text.next_to(value_text, DOWN, buff=0.4)  # Increased buffer
                
                # Group everything
                combo_group = VGroup(combo_cards, weight_text, value_text, valid_text)
                
                # Show the combination
                self.play(FadeIn(combo_group))
                self.wait(1.5)  # Longer pause to review each combination
                self.play(FadeOut(combo_group))
            
            # Explain the problem with this approach
            complexity_text = Text("For n items: 2ⁿ combinations to check!", font_size=28, color=YELLOW)
            complexity_text.move_to(combo_area.get_center())
            
            self.play(Write(complexity_text))
            self.wait(1.5)  # Added longer pause
            
            # Clean up for the next scene
            self.play(
                FadeOut(complexity_text),
                FadeOut(combo_area),
                FadeOut(combo_title),
                FadeOut(approach_title)
            )
            self.wait(0.5)  # Added pause

        # Scene 4: Dynamic Programming Approach
        with self.voiceover(
            """
            But trying every combination becomes impractical as the number of items grows.
            Instead, we can use dynamic programming to solve this efficiently.
            """
        ) as tracker:
            # Create title for DP approach
            dp_title = Text("Dynamic Programming Solution", font_size=36)
            # dp_title.next_to(self.title, DOWN, buff=0.5)
            
            self.play(Write(dp_title))
            self.wait(0.5)  # Added pause
            self.clear()
        
        with self.voiceover(
            """
            We'll build a table where rows represent the items we're considering,
            and columns represent the different possible weight capacities of our backpack,
            from zero up to its maximum capacity.
            """
        ) as tracker:
            # Create the DP table
            table = VGroup()
            
            # Define dimensions
            num_items = len(self.items)
            
            # Create table cells
            cell_height = 0.7  # Cell height
            cell_width = 0.9   # Cell width
            
            # Define the dp_values matrix to use throughout the animation
            self.dp_values = np.zeros((num_items + 1, self.max_capacity + 1), dtype=int)
            
            # Build the base table and empty cells
            for i in range(num_items + 1):
                for w in range(self.max_capacity + 1):
                    cell = Rectangle(height=cell_height, width=cell_width)
                    cell.set_stroke(WHITE, 1)
                    
                    # Position the cell
                    if i == 0 and w == 0:
                        cell.to_edge(UP, buff=3.0)
                        cell.to_edge(LEFT, buff=4.0)  # Moved left to ensure full table is visible
                    elif i == 0:
                        cell.next_to(self.cells.get((0, w-1)), RIGHT, buff=0)
                    elif w == 0:
                        cell.next_to(self.cells.get((i-1, 0)), DOWN, buff=0)
                    else:
                        cell.next_to(self.cells.get((i, w-1)), RIGHT, buff=0)
                    
                    # Add text for the cell
                    if i == 0 and w == 0:
                        text = Text("Items", font_size=16)
                    elif i == 0:
                        text = Text(f"{w}kg", font_size=18)
                    elif w == 0:
                        text = Text(f"Item {i}", font_size=18)
                    else:
                        # Initially empty cell
                        text = Text("", font_size=20)  # Larger font for cell values
                    
                    text.move_to(cell)
                    self.cells[(i, w)] = VGroup(cell, text)
                    table.add(self.cells[(i, w)])
            
            # Add item descriptions next to the row headers
            descriptions = VGroup()
            for i, item in enumerate(self.items):
                desc = Text(
                    f"({i+1}) {item['icon']} {item['name']} ({item['weight']}kg, {item['value']}pts)",
                    font_size=16
                )
                desc.next_to(self.cells[(i+1, 0)], LEFT, buff=1.0)
                descriptions.add(desc)
            
            # Show the table
            self.play(
                Create(table),
                run_time=2
            )
            
            self.play(Write(descriptions))
            self.wait(0.5)
            
            # Keep references for later
            self.dp_title = dp_title
            self.table = table
            self.descriptions = descriptions
        
        # UPDATED PART: Fill the table cell by cell using the pattern from KnapsackDPCellFiller
        with self.voiceover(
            """
            Now, let's fill this table one cell at a time.
            """
        ) as tracker:
            # First fill in the base cases (zeros in row 0 and column 0)
            for i in range(num_items + 1):
                for w in range(self.max_capacity + 1):
                    if i == 0 or w == 0:
                        if not (i == 0 and w == 0):  # Skip the "Items" cell
                            # Update the cell value
                            cell_rect, cell_text = self.cells[(i, w)]
                            value_text = Text("0", font_size=20, color=WHITE)
                            value_text.move_to(cell_rect.get_center())
                            self.play(Transform(cell_text, value_text), run_time=0.15)
                            
                            # Save to dp table
                            self.dp_values[i, w] = 0
            
            # Now fill the table cell by cell
            for i in range(1, num_items + 1):
                item = self.items[i-1]
                for w in range(1, self.max_capacity + 1):
                    # Get the current cell
                    cell_rect, cell_text = self.cells[(i, w)]
                    highlight = SurroundingRectangle(cell_rect, color=YELLOW)
                    self.play(Create(highlight))
                    
                    if item["weight"] > w:
                        # Item doesn't fit, take value from above
                        self.dp_values[i, w] = self.dp_values[i-1, w]
                        
                        with self.voiceover(f"At capacity {w}kg, the {item['icon']} can't fit since it weighs {item['weight']}kg. We keep the previous value: {self.dp_values[i, w]}."):
                            explanation = Text(
                                f"Can't fit {item['icon']} ({item['weight']}kg) → {self.dp_values[i, w]}",
                                font_size=20
                            ).to_edge(DOWN)
                            value_text = Text(str(self.dp_values[i, w]), font_size=24, color=RED)
                            value_text.move_to(cell_rect.get_center())
                            
                            self.play(Write(explanation))
                            self.play(Transform(cell_text, value_text))
                            self.play(FadeOut(explanation))
                    else:
                        # Item fits, choose max of (skip item) or (take item + best with remaining weight)
                        option1 = self.dp_values[i-1, w]  # Value if we skip this item
                        remaining_capacity = w - item["weight"]
                        option2 = item["value"] + self.dp_values[i-1, remaining_capacity]  # Value if we take this item
                        
                        self.dp_values[i, w] = max(option1, option2)
                        color = GREEN if option2 > option1 else BLUE
                        
                        with self.voiceover(f"At capacity {w}kg, we choose the best between skipping the {item['icon']} worth {option1} and taking it for {option2}. We pick {self.dp_values[i, w]}."):
                            explanation = Text(
                                f"Max({option1}, {item['value']} + {self.dp_values[i-1, remaining_capacity]}) → {self.dp_values[i, w]}",
                                font_size=20
                            ).to_edge(DOWN)
                            
                            value_text = Text(str(self.dp_values[i, w]), font_size=24, color=color)
                            value_text.move_to(cell_rect.get_center())
                            
                            self.play(Write(explanation))
                            self.play(Transform(cell_text, value_text))
                            self.play(FadeOut(explanation))
                    
                    # Move to next cell
                    self.play(FadeOut(highlight))
                    self.wait(0.2)
        
        # Highlight the final solution
        with self.voiceover(
            f"""
            We've filled our entire dynamic programming table.
            The bottom-right cell shows our final answer: the maximum possible value
            of {self.dp_values[num_items, self.max_capacity]} points that can fit in our {self.max_capacity} kilogram backpack.
            """
        ) as tracker:
            # Highlight the final cell
            final_cell = self.cells[(num_items, self.max_capacity)][0]  # The Rectangle part of the cell
            final_highlight = SurroundingRectangle(final_cell, color=YELLOW, stroke_width=3)
            
            optimal_text = Text(f"Optimal Value: {self.dp_values[num_items, self.max_capacity]} points", font_size=28, color=YELLOW)
            optimal_text.to_edge(DOWN, buff=1.5)
            
            self.play(
                Create(final_highlight),
                Write(optimal_text)
            )
            
            self.wait(1.5)
            
            # Save for later reference
            self.final_highlight = final_highlight
            self.optimal_text = optimal_text




        # Scene 6: Backtracking to Find the Solution
        with self.voiceover(
        """
        Now that we've filled our table, the bottom-right cell shows the maximum possible value
        we can pack: 26 points. But which items should we actually take?

        To figure this out, we'll backtrack through our table. Starting from the final cell,
        we'll trace our path back to determine which items to include.
        """
        ) as tracker:
        # Bring back the backpack for the final solution - positioned to avoid interference
            backpack = self.create_backpack()
            backpack.scale(1.5)
            backpack.to_edge(RIGHT, buff=2.5)  # Moved further right
            backpack.to_edge(DOWN, buff=2.5)   # Moved further down

            capacity_label = Text(f"Capacity: {self.max_capacity} kg", font_size=24, color=YELLOW)
            capacity_label.next_to(backpack, UP, buff=0.3)

            self.play(
                Create(backpack),
                Write(capacity_label)
            )
            self.wait(0.5)  # Added pause

            # Backtrack to determine which items to include
            i, j = num_items, self.max_capacity
            selected_items = []
            total_weight = 0

            backtrack_title = Text("Backtracking to Find Selected Items", font_size=28)
            # Position to avoid overlapping with the table
            backtrack_title.to_edge(UP, buff=3.5)

            self.play(
                FadeOut(self.optimal_text),
                # Write(backtrack_title)
            )
            self.wait(0.5)  # Added pause

            backpack_items = VGroup()

            while i > 0 and j > 0:
                # Check if this item was included
                current_item = self.items[i-1]
                
                if self.dp_values[i, j] != self.dp_values[i-1, j]:
                    # This item was included
                    selected_items.append(i-1)
                    total_weight += current_item["weight"]
                    
                    # Highlight the current cell and the item
                    curr_cell = self.cells[(i, j)]
                    curr_highlight = SurroundingRectangle(curr_cell, color=GREEN, stroke_width=2)
                    
                    item_highlight = SurroundingRectangle(
                        self.descriptions[i-1], 
                        color=GREEN, 
                        stroke_width=2
                    )
                    
                    # Position text to avoid overlap
                    selection_text = Text(
                        f"Include {current_item['icon']} {current_item['name']} ({current_item['weight']}kg, {current_item['value']}pts)",
                        font_size=20,
                        color=GREEN
                    )
                    selection_text.next_to(backtrack_title, DOWN, buff=0.5)
                    
                    self.play(
                        Create(curr_highlight),
                        Create(item_highlight),
                        Write(selection_text)
                    )
                    self.wait(0.5)  # Added pause
                    
                    # Add the item to the backpack
                    item_card = self.create_item_card(current_item, scale=0.5)  # Smaller cards
                    item_card.move_to(ORIGIN + RIGHT * 2)  # Start position
                    
                    # Calculate position in backpack with better spacing
                    offset_y = (len(backpack_items) - 1) * 0.6
                    target_pos = backpack.get_center() + UP * (0.5 - offset_y)
                    
                    self.play(FadeIn(item_card))
                    self.play(item_card.animate.move_to(target_pos))
                    
                    backpack_items.add(item_card)
                    
                    # Update weight status
                    weight_update = Text(f"Current Weight: {total_weight}/{self.max_capacity}kg", font_size=22)
                    weight_update.next_to(selection_text, DOWN, buff=0.4)  # Increased buffer
                    
                    self.play(Write(weight_update))
                    self.wait(0.5)  # Added pause
                    
                    # Update j (reduce by the weight of the included item)
                    j_new = j - current_item["weight"]
                    
                    # Highlight next cell to check
                    next_cell = self.cells[(i-1, j_new)]
                    next_highlight = SurroundingRectangle(next_cell, color=BLUE, stroke_width=2)
                    
                    self.play(Create(next_highlight))
                    self.wait(0.5)  # Added pause
                    
                    # Move to next position
                    j = j_new
                    
                    # Clean up before moving to next item
                    self.play(
                        FadeOut(curr_highlight),
                        FadeOut(item_highlight),
                        FadeOut(selection_text),
                        FadeOut(weight_update),
                        FadeOut(next_highlight)
                    )
                else:
                    # This item wasn't included
                    skip_text = Text(
                        f"Skip {current_item['icon']} {current_item['name']}",
                        font_size=20,
                        color=RED
                    )
                    skip_text.next_to(backtrack_title, DOWN, buff=0.5)
                    
                    curr_cell = self.cells[(i, j)]
                    curr_highlight = SurroundingRectangle(curr_cell, color=RED, stroke_width=2)
                    
                    item_highlight = SurroundingRectangle(
                        self.descriptions[i-1], 
                        color=RED, 
                        stroke_width=2
                    )
                    
                    self.play(
                        Create(curr_highlight),
                        Create(item_highlight),
                        Write(skip_text)
                    )
                    self.wait(0.5)  # Added pause
                    
                    # Highlight next cell to check
                    next_cell = self.cells[(i-1, j)]
                    next_highlight = SurroundingRectangle(next_cell, color=BLUE, stroke_width=2)
                    
                    self.play(Create(next_highlight))
                    self.wait(0.5)  # Added pause
                    
                    # Clean up before moving to next item
                    self.play(
                        FadeOut(curr_highlight),
                        FadeOut(item_highlight),
                        FadeOut(skip_text),
                        FadeOut(next_highlight)
                    )
                
                i -= 1

            # Reverse selected_items to show them in original order
            selected_items.reverse()

        # Scene 7: Final Solution
        with self.voiceover(
            """
            And there we have it! Our optimal solution is to pack these specific items
            for our hiking trip, giving us the maximum value while staying within our
            backpack's weight limit.
            
            Dynamic Programming has helped us solve a complex decision problem by breaking it down
            into simpler subproblems and building up the solution step by step. This approach is
            much more efficient than checking all possible combinations.
            
            Whether you're packing for a hiking trip or making important investment decisions,
            the 0/1 Knapsack algorithm can help you make optimal choices when faced with
            constraints.
            """
        ) as tracker:
            # Clear previous elements to make space
            self.play(
                FadeOut(self.final_highlight),
                FadeOut(self.table),
                FadeOut(self.descriptions),
                FadeOut(backtrack_title),
                FadeOut(self.dp_title)
            )
            self.wait(0.5)  # Added pause
            
            # Final overview
            final_title = Text("Optimal Backpack Solution", font_size=36, color=YELLOW)
            final_title.to_edge(UP, buff=0.7)
            
            self.play(
                FadeOut(self.title),
                Write(final_title)
            )
            self.wait(0.5)  # Added pause
            
            # Calculate total value
            total_value = sum(self.items[idx]["value"] for idx in selected_items)
            
            # Create a breakdown of the selected items
            item_breakdown = VGroup()
            for idx in selected_items:
                item = self.items[idx]
                item_text = Text(
                    f"{item['icon']} {item['name']}: {item['weight']}kg, {item['value']} points",
                    font_size=20, color=item['color']
                )
                item_breakdown.add(item_text)
            
            item_breakdown.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            item_breakdown.to_edge(LEFT, buff=1.0)
            item_breakdown.to_edge(UP, buff=3.0)
            
            self.play(Write(item_breakdown))
            self.wait(0.5)
            
            # Final solution summary - positioned to avoid overlap with backpack
            summary = VGroup(
                Text(f"Total Weight: {total_weight}/{self.max_capacity}kg", font_size=24),
                Text(f"Total Value: {total_value} points", font_size=24),
                Text(f"Number of Items: {len(selected_items)}/{len(self.items)}", font_size=24)
            )
            summary.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            summary.next_to(backpack, LEFT, buff=3.0)  # Increased buffer
            
            self.play(Write(summary))
            self.wait(0.7)  # Added pause
            
            # Show a happy hiker - positioned to avoid overlaps
            hiker = self.create_hiker()
            hiker.scale(0.8)
            hiker.next_to(backpack, UP, buff=2.0)  # Increased buffer
            
            self.play(FadeIn(hiker))
            self.wait(0.5)  # Added pause
            
            # Final message
            success = Text("Ready for Adventure!", font_size=32, color=GREEN)
            success.next_to(hiker, UP, buff=0.7)  # Increased buffer
            
            self.play(Write(success))
            self.wait(2)  # Added longer final pause

    def create_item_card(self, item, scale=1.0):
        """Create a card for an item with icon and details"""
        name = item["name"]
        weight = item["weight"]
        value = item["value"]
        color = item["color"]
        icon = item["icon"]
        
        # Create card background
        card = RoundedRectangle(height=1.5, width=2.2, corner_radius=0.1)
        card.set_stroke(WHITE, 1)
        card.set_fill(color, opacity=0.3)
        
        # Group for all text elements
        text_group = VGroup()
        
        # Create icon text
        icon_text = Text(icon, font_size=28)
        
        # Create item details
        name_text = Text(name, font_size=16)
        weight_text = Text(f"Weight: {weight}kg", font_size=14)
        value_text = Text(f"Value: {value} pts", font_size=14)
        
        # Arrange details vertically and center-aligned
        details = VGroup(name_text, weight_text, value_text)
        details.arrange(DOWN, center=True, buff=0.15)  # Center alignment
        
        # Add icon and details to text group
        text_group.add(icon_text, details)
        
        # Center-align all text elements horizontally
        text_group.arrange(RIGHT, buff=0.3, center=True)
        
        # Position the text group in the center of the card
        text_group.move_to(card.get_center())
        
        # Group everything
        card_group = VGroup(card, text_group)
        card_group.scale(scale)
        
        return card_group
    
    def create_hiker(self):
        """Create a simple happy hiker figure"""
        hiker = VGroup()
        
        # Head
        head = Circle(radius=0.3, color=WHITE)
        head.set_fill("#F8D5AC", opacity=1)
        
        # Face
        smile = ArcBetweenPoints(
            head.get_bottom() + LEFT * 0.15,
            head.get_bottom() + RIGHT * 0.15,
            angle=-PI/2
        )
        
        left_eye = Dot(point=head.get_center() + UP * 0.1 + LEFT * 0.1, radius=0.03)
        right_eye = Dot(point=head.get_center() + UP * 0.1 + RIGHT * 0.1, radius=0.03)
        
        face = VGroup(smile, left_eye, right_eye)
        face.set_color(BLACK)
        
        # Body
        body = Rectangle(height=0.8, width=0.5, color=GREEN_E)
        body.set_fill(GREEN_D, opacity=1)
        body.next_to(head, DOWN, buff=0.05)
        
        # Arms
        left_arm = Line(
            body.get_left() + UP * 0.2,
            body.get_left() + UP * 0.2 + LEFT * 0.4 + UP * 0.2,
            color=GREEN_E
        )
        
        right_arm = Line(
            body.get_right() + UP * 0.2,
            body.get_right() + UP * 0.2 + RIGHT * 0.4 + UP * 0.2,
            color=GREEN_E
        )
        
        # Legs
        left_leg = Line(
            body.get_bottom() + LEFT * 0.15,
            body.get_bottom() + LEFT * 0.15 + DOWN * 0.4,
            color="#5D4037"
        )
        
        right_leg = Line(
            body.get_bottom() + RIGHT * 0.15,
            body.get_bottom() + RIGHT * 0.15 + DOWN * 0.4,
            color="#5D4037"
        )
        
        # Hat
        hat = ArcBetweenPoints(
            head.get_top() + LEFT * 0.4,
            head.get_top() + RIGHT * 0.4,
            angle=PI/2
        )
        hat.set_stroke(BLUE, 4)
        
        hiker.add(body, left_arm, right_arm, left_leg, right_leg, head, face, hat)
        
        return hiker
    def create_backpack(self):
        """Create a simple backpack icon"""
        backpack_shape = VGroup()
        
        # Main bag
        bag = RoundedRectangle(height=2, width=1.5, corner_radius=0.2)
        
        # Top flap
        flap = ArcBetweenPoints(
            bag.get_top() + LEFT * 0.75,
            bag.get_top() + RIGHT * 0.75,
            angle=-PI
        )
        
        # Straps
        left_strap = ArcBetweenPoints(
            bag.get_top() + LEFT * 0.5,
            bag.get_corner(DL) + UP * 0.5,
            angle=-1
        )
        
        right_strap = ArcBetweenPoints(
            bag.get_top() + RIGHT * 0.5,
            bag.get_corner(DR) + UP * 0.5,
            angle=1
        )
        
        # Small pocket
        pocket = RoundedRectangle(height=0.5, width=1, corner_radius=0.1)
        pocket.move_to(bag.get_center() + DOWN * 0.5)
        
        backpack_shape.add(bag, flap, left_strap, right_strap, pocket)
        backpack_shape.set_color(BLUE_D)
        backpack_shape.set_fill(BLUE_E, opacity=0.8)
        
        return backpack_shape


# Add this main block to run the animation
if __name__ == "__main__":
    scene = KnapsackAdventureScene()
    scene.render()