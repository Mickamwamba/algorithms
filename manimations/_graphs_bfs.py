from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService
import networkx as nx
import numpy as np

class BFSExplanation(VoiceoverScene):
    def construct(self):
        # Set up the voice service
        self.set_speech_service(OpenAIService(voice="echo", model="tts-1-hd"))
        
        # Title - positioned higher to avoid overlap
        title = Text("Breadth-First Search (BFS) Algorithm", font_size=40)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)
        
        # Introduction
        with self.voiceover(
            "Welcome to this exploration of the Breadth-First Search algorithm, or BFS for short. "
            "BFS is a fundamental graph traversal algorithm that explores all neighbors at the present "
            "depth level before moving on to nodes at the next depth level."
        ):
            pass
        
        # Define our graph
        with self.voiceover(
            "Let's consider this graph, which represents connections between people."
        ):
            # Create a hierarchical layout manually
            # Define positions for each level - adjusted to avoid overlaps with title
            positions = {
                'Mike': [0, 2, 0],  # Top level - moved down to avoid title overlap
                'Mohamed': [-3, 0.5, 0], 'Diego': [0, 0.5, 0], 'John': [3, 0.5, 0],  # Second level
                'Naomi': [-3, -1, 0],  # Third level
                'Trevor': [-3, -2.5, 0]  # Fourth level
            }
            
            # Create the graph with these edges
            connections = [
                ('Mike', 'Mohamed'), ('Mike', 'Diego'), ('Mike', 'John'),
                ('Mohamed', 'Naomi'), ('Naomi', 'Trevor')
            ]
            
            # Create Manim graph
            vertices = {}
            edges = []
            
            # Create vertices
            for node, position in positions.items():
                vertices[node] = Dot(point=position, radius=0.3, color=BLUE)
                vertices[node].add(Text(node, font_size=20).next_to(vertices[node], DOWN))
            
            # Create edges
            for u, v in connections:
                edge = Line(
                    vertices[u].get_center(),
                    vertices[v].get_center(),
                    color=GRAY
                )
                edges.append(edge)
            
            # Group all elements
            graph_verts = VGroup(*vertices.values())
            graph_edges = VGroup(*edges)
            graph = VGroup(graph_edges, graph_verts)
            
            # Center the graph
            graph.center()
            
            # Create graph
            self.play(Create(graph_edges), run_time=1.5)
            self.play(Create(graph_verts), run_time=1.5)
        
        # Create queue and visited trackers - moved more to the left
        queue_title = Text("Queue:", font_size=24).to_corner(DR).shift(LEFT * 6 + UP * 2)
        visited_title = Text("Visited:", font_size=24).to_corner(DR).shift(LEFT * 6 + UP * 0.5)
        
        queue_content = Text("[]", font_size=24).next_to(queue_title, RIGHT)
        visited_content = Text("[]", font_size=24).next_to(visited_title, RIGHT)
        
        with self.voiceover(
            "To keep track of our graph traversal, we'll use two data structures: "
            "a Queue and a Visited list. The Queue will keep track of nodes we need to visit next, "
            "while the Visited list will store nodes we've already processed."
        ):
            self.play(
                Write(queue_title), 
                Write(visited_title),
                Write(queue_content),
                Write(visited_content)
            )
            
        with self.voiceover(
            "Since we're starting with 'Mike' as our root node, we'll add it to the queue."
        ):
            self.play(queue_content.animate.become(Text("['Mike']", font_size=20).next_to(queue_title, RIGHT)))
        
        # BFS algorithm step by step - slowed down with clearer highlighting
        with self.voiceover(
            "Now, let's start our BFS traversal. We take 'Mike' out of the queue and visit it. "
            "Then we mark it as visited and look at all its unvisited neighbors."
        ):
            # Focus on processing the current node
            self.play(Indicate(vertices['Mike'], color=RED, scale_factor=1.5), run_time=1.5)
            
            # Update queue - remove Mike
            self.play(queue_content.animate.become(Text("[]", font_size=20).next_to(queue_title, RIGHT)), run_time=1)
            
            # Mark Mike as visited
            self.play(visited_content.animate.become(Text("['Mike']", font_size=20).next_to(visited_title, RIGHT)), run_time=1)
            self.wait(0.5)
            
            # Highlight each neighbor individually with a pause
            for neighbor in ['Mohamed', 'Diego', 'John']:
                # Highlight edge to neighbor
                # Find the edge connecting Mike and the current neighbor
                for edge in edges:
                    start_point = edge.get_start()
                    end_point = edge.get_end()
                    
                    # Check if this edge connects Mike and the neighbor
                    if ((np.allclose(start_point, vertices['Mike'].get_center()) and 
                         np.allclose(end_point, vertices[neighbor].get_center())) or
                        (np.allclose(end_point, vertices['Mike'].get_center()) and 
                         np.allclose(start_point, vertices[neighbor].get_center()))):
                        neighbor_edge = edge
                        break
                
                self.play(
                    neighbor_edge.animate.set_color(YELLOW).set_stroke(width=6),
                    run_time=0.8
                )
                
                # Create a pulsing effect around the neighbor
                self.play(Indicate(vertices[neighbor], color=YELLOW, scale_factor=1.2), run_time=1)
                
                # Check if neighbor is visited (none are at this point)
                unvisited_text = Text("Unvisited", font_size=16, color=GREEN).next_to(vertices[neighbor], RIGHT)
                self.play(Write(unvisited_text), run_time=0.6)
                self.wait(0.3)
                self.play(FadeOut(unvisited_text), run_time=0.5)
                
                # Reset edge color
                self.play(neighbor_edge.animate.set_color(GRAY).set_stroke(width=4), run_time=0.5)
            
            # Highlight all neighbors together
            self.play(
                vertices['Mohamed'].animate.set_color(YELLOW),
                vertices['Diego'].animate.set_color(YELLOW),
                vertices['John'].animate.set_color(YELLOW),
                run_time=1.5
            )
            
            # Add neighbors to queue one by one with animation
            self.play(queue_content.animate.become(Text("['Mohamed']", font_size=20).next_to(queue_title, RIGHT)), run_time=0.8)
            self.wait(0.3)
            self.play(queue_content.animate.become(Text("['Mohamed', 'Diego']", font_size=20).next_to(queue_title, RIGHT)), run_time=0.8)
            self.wait(0.3)
            self.play(queue_content.animate.become(Text("['Mohamed', 'Diego', 'John']", font_size=20).next_to(queue_title, RIGHT)), run_time=0.8)
            self.wait(0.5)
        
        with self.voiceover(
            "Now we visit 'Mohamed' by taking it out of the queue. We mark it as visited and check its neighbors."
        ):
            # Focus on processing the current node
            self.play(Indicate(vertices['Mohamed'], color=RED, scale_factor=1.5), run_time=1.5)
            
            # Update queue - remove Mohamed
            self.play(queue_content.animate.become(Text("['Diego', 'John']", font_size=20).next_to(queue_title, RIGHT)), run_time=1)
            
            # Mark Mohamed as visited
            self.play(vertices['Mohamed'].animate.set_color(RED), run_time=1)
            self.play(visited_content.animate.become(Text("['Mike', 'Mohamed']", font_size=20).next_to(visited_title, RIGHT)), run_time=1)
            self.wait(0.5)
            
            # Check neighboring connections - emphasize we're looking at Mohamed's neighbors
            # First check Mike (already visited)
            # Find the edge connecting Mohamed and Mike
            for edge in edges:
                start_point = edge.get_start()
                end_point = edge.get_end()
                
                # Check if this edge connects Mohamed and Mike
                if ((np.allclose(start_point, vertices['Mohamed'].get_center()) and 
                     np.allclose(end_point, vertices['Mike'].get_center())) or
                    (np.allclose(end_point, vertices['Mohamed'].get_center()) and 
                     np.allclose(start_point, vertices['Mike'].get_center()))):
                    mike_edge = edge
                    break
            
            self.play(
                mike_edge.animate.set_color(YELLOW).set_stroke(width=6),
                run_time=0.8
            )
            
            # Indicate Mike is already visited
            mike_visited = Text("Already visited", font_size=16, color=RED).next_to(vertices['Mike'], RIGHT)
            self.play(Write(mike_visited), run_time=0.8)
            self.wait(0.5)
            self.play(FadeOut(mike_visited), run_time=0.5)
            
            # Reset edge color
            self.play(mike_edge.animate.set_color(GRAY).set_stroke(width=4), run_time=0.5)
            
            # Now check Naomi (unvisited)
            # Find the edge connecting Mohamed and Naomi
            for edge in edges:
                start_point = edge.get_start()
                end_point = edge.get_end()
                
                # Check if this edge connects Mohamed and Naomi
                if ((np.allclose(start_point, vertices['Mohamed'].get_center()) and 
                     np.allclose(end_point, vertices['Naomi'].get_center())) or
                    (np.allclose(end_point, vertices['Mohamed'].get_center()) and 
                     np.allclose(start_point, vertices['Naomi'].get_center()))):
                    naomi_edge = edge
                    break
            
            self.play(
                naomi_edge.animate.set_color(YELLOW).set_stroke(width=6),
                run_time=0.8
            )
            
            # Highlight Naomi as unvisited
            self.play(Indicate(vertices['Naomi'], color=YELLOW, scale_factor=1.2), run_time=1)
            
            # Show Naomi is unvisited
            naomi_unvisited = Text("Unvisited", font_size=16, color=GREEN).next_to(vertices['Naomi'], RIGHT)
            self.play(Write(naomi_unvisited), run_time=0.8)
            self.wait(0.5)
            self.play(FadeOut(naomi_unvisited), run_time=0.5)
            
            # Reset edge color but keep Naomi yellow for queue
            self.play(
                naomi_edge.animate.set_color(GRAY).set_stroke(width=4),
                vertices['Naomi'].animate.set_color(YELLOW),
                run_time=0.8
            )
            
            # Add Naomi to queue
            self.play(queue_content.animate.become(Text("['Diego', 'John', 'Naomi']", font_size=20).next_to(queue_title, RIGHT)), run_time=1)
            self.wait(0.5)
        
        with self.voiceover(
            "Now we visit 'Diego' by taking it from the queue. We mark it as visited and check its neighbors."
        ):
            # Focus on processing the current node
            self.play(Indicate(vertices['Diego'], color=RED, scale_factor=1.5), run_time=1.5)
            
            # Update queue - remove Diego
            self.play(queue_content.animate.become(Text("['John', 'Naomi']", font_size=20).next_to(queue_title, RIGHT)), run_time=1)
            
            # Mark Diego as visited
            self.play(vertices['Diego'].animate.set_color(RED), run_time=1)
            self.play(visited_content.animate.become(Text("['Mike', 'Mohamed', 'Diego']", font_size=20).next_to(visited_title, RIGHT)), run_time=1)
            self.wait(0.5)
            
            # Check Diego's only neighbor - Mike (already visited)
            # Find the edge connecting Diego and Mike
            for edge in edges:
                start_point = edge.get_start()
                end_point = edge.get_end()
                
                # Check if this edge connects Diego and Mike
                if ((np.allclose(start_point, vertices['Diego'].get_center()) and 
                     np.allclose(end_point, vertices['Mike'].get_center())) or
                    (np.allclose(end_point, vertices['Diego'].get_center()) and 
                     np.allclose(start_point, vertices['Mike'].get_center()))):
                    mike_edge = edge
                    break
            
            self.play(
                mike_edge.animate.set_color(YELLOW).set_stroke(width=6),
                run_time=0.8
            )
            
            # Indicate Mike is already visited
            mike_visited = Text("Already visited", font_size=16, color=RED).next_to(vertices['Mike'], UP)
            self.play(Write(mike_visited), run_time=0.8)
            self.wait(0.5)
            self.play(FadeOut(mike_visited), run_time=0.5)
            
            # Reset edge color
            self.play(mike_edge.animate.set_color(GRAY).set_stroke(width=4), run_time=0.5)
            
            # Visual indicator that no nodes are added to queue
            no_additions = Text("No new nodes to add", font_size=20, color=YELLOW).next_to(queue_content, DOWN)
            self.play(Write(no_additions), run_time=1)
            self.wait(1)
            self.play(FadeOut(no_additions), run_time=0.5)
        
        with self.voiceover(
            "Next, we visit 'John' by taking it from the queue. We mark it as visited and check its neighbors."
        ):
            # Focus on processing the current node
            self.play(Indicate(vertices['John'], color=RED, scale_factor=1.5), run_time=1.5)
            
            # Update queue - remove John
            self.play(queue_content.animate.become(Text("['Naomi']", font_size=20).next_to(queue_title, RIGHT)), run_time=1)
            
            # Mark John as visited
            self.play(vertices['John'].animate.set_color(RED), run_time=1)
            self.play(visited_content.animate.become(Text("['Mike', 'Mohamed', 'Diego', 'John']", font_size=20).next_to(visited_title, RIGHT)), run_time=1)
            self.wait(0.5)
            
            # Check John's only neighbor - Mike (already visited)
            # Find the edge connecting John and Mike
            for edge in edges:
                start_point = edge.get_start()
                end_point = edge.get_end()
                
                # Check if this edge connects John and Mike
                if ((np.allclose(start_point, vertices['John'].get_center()) and 
                     np.allclose(end_point, vertices['Mike'].get_center())) or
                    (np.allclose(end_point, vertices['John'].get_center()) and 
                     np.allclose(start_point, vertices['Mike'].get_center()))):
                    mike_edge = edge
                    break
            
            self.play(
                mike_edge.animate.set_color(YELLOW).set_stroke(width=6),
                run_time=0.8
            )
            
            # Indicate Mike is already visited
            mike_visited = Text("Already visited", font_size=16, color=RED).next_to(vertices['Mike'], UP)
            self.play(Write(mike_visited), run_time=0.8)
            self.wait(0.5)
            self.play(FadeOut(mike_visited), run_time=0.5)
            
            # Reset edge color
            self.play(mike_edge.animate.set_color(GRAY).set_stroke(width=4), run_time=0.5)
            
            # Visual indicator that no nodes are added to queue
            no_additions = Text("No new nodes to add", font_size=20, color=YELLOW).next_to(queue_content, DOWN)
            self.play(Write(no_additions), run_time=1)
            self.wait(1)
            self.play(FadeOut(no_additions), run_time=0.5)
        
        with self.voiceover(
            "Now we visit 'Naomi' by taking it from the queue. We mark it as visited and check its neighbors."
        ):
            # Focus on processing the current node
            self.play(Indicate(vertices['Naomi'], color=RED, scale_factor=1.5), run_time=1.5)
            
            # Update queue - remove Naomi
            self.play(queue_content.animate.become(Text("[]", font_size=20).next_to(queue_title, RIGHT)), run_time=1)
            
            # Mark Naomi as visited
            self.play(vertices['Naomi'].animate.set_color(RED), run_time=1)
            self.play(visited_content.animate.become(Text("['Mike', 'Mohamed', 'Diego', 'John', 'Naomi']", font_size=20).next_to(visited_title, RIGHT)), run_time=1)
            self.wait(0.5)
            
            # Check neighboring connections - check Mohamed first (already visited)
            # Find the edge connecting Naomi and Mohamed
            for edge in edges:
                start_point = edge.get_start()
                end_point = edge.get_end()
                
                # Check if this edge connects Naomi and Mohamed
                if ((np.allclose(start_point, vertices['Naomi'].get_center()) and 
                     np.allclose(end_point, vertices['Mohamed'].get_center())) or
                    (np.allclose(end_point, vertices['Naomi'].get_center()) and 
                     np.allclose(start_point, vertices['Mohamed'].get_center()))):
                    mohamed_edge = edge
                    break
            
            self.play(
                mohamed_edge.animate.set_color(YELLOW).set_stroke(width=6),
                run_time=0.8
            )
            
            # Show Mohamed is already visited
            mohamed_visited = Text("Already visited", font_size=16, color=RED).next_to(vertices['Mohamed'], RIGHT)
            self.play(Write(mohamed_visited), run_time=0.8)
            self.wait(0.5)
            self.play(FadeOut(mohamed_visited), run_time=0.5)
            
            # Reset edge color
            self.play(mohamed_edge.animate.set_color(GRAY).set_stroke(width=4), run_time=0.5)
            
            # Now check Trevor (unvisited)
            # Find the edge connecting Naomi and Trevor
            for edge in edges:
                start_point = edge.get_start()
                end_point = edge.get_end()
                
                # Check if this edge connects Naomi and Trevor
                if ((np.allclose(start_point, vertices['Naomi'].get_center()) and 
                     np.allclose(end_point, vertices['Trevor'].get_center())) or
                    (np.allclose(end_point, vertices['Naomi'].get_center()) and 
                     np.allclose(start_point, vertices['Trevor'].get_center()))):
                    trevor_edge = edge
                    break
            
            self.play(
                trevor_edge.animate.set_color(YELLOW).set_stroke(width=6),
                run_time=0.8
            )
            
            # Highlight Trevor as unvisited
            self.play(Indicate(vertices['Trevor'], color=YELLOW, scale_factor=1.2), run_time=1)
            
            # Show Trevor is unvisited
            trevor_unvisited = Text("Unvisited", font_size=16, color=GREEN).next_to(vertices['Trevor'], RIGHT)
            self.play(Write(trevor_unvisited), run_time=0.8)
            self.wait(0.5)
            self.play(FadeOut(trevor_unvisited), run_time=0.5)
            
            # Reset edge color but keep Trevor yellow for queue
            self.play(
                trevor_edge.animate.set_color(GRAY).set_stroke(width=4),
                vertices['Trevor'].animate.set_color(YELLOW),
                run_time=0.8
            )
            
            # Add Trevor to queue
            self.play(queue_content.animate.become(Text("['Trevor']", font_size=20).next_to(queue_title, RIGHT)), run_time=1)
            self.wait(0.5)
        
        with self.voiceover(
            "Finally, we visit 'Trevor' by taking it from the queue. We mark it as visited and check its neighbors."
        ):
            # Focus on processing the current node
            self.play(Indicate(vertices['Trevor'], color=RED, scale_factor=1.5), run_time=1.5)
            
            # Update queue - remove Trevor
            self.play(queue_content.animate.become(Text("[]", font_size=20).next_to(queue_title, RIGHT)), run_time=1)
            
            # Mark Trevor as visited
            self.play(vertices['Trevor'].animate.set_color(RED), run_time=1)
            self.play(visited_content.animate.become(Text("['Mike', 'Mohamed', 'Diego', 'John', 'Naomi', 'Trevor']", font_size=20).next_to(visited_title, RIGHT)), run_time=1)
            self.wait(0.5)
            
            # Check neighboring connection - examine Naomi (already visited)
            # Find the edge connecting Trevor and Naomi
            for edge in edges:
                start_point = edge.get_start()
                end_point = edge.get_end()
                
                # Check if this edge connects Trevor and Naomi
                if ((np.allclose(start_point, vertices['Trevor'].get_center()) and 
                     np.allclose(end_point, vertices['Naomi'].get_center())) or
                    (np.allclose(end_point, vertices['Trevor'].get_center()) and 
                     np.allclose(start_point, vertices['Naomi'].get_center()))):
                    naomi_edge = edge
                    break
            
            self.play(
                naomi_edge.animate.set_color(YELLOW).set_stroke(width=6),
                run_time=0.8
            )
            
            # Indicate Naomi is already visited
            naomi_visited = Text("Already visited", font_size=16, color=RED).next_to(vertices['Naomi'], RIGHT)
            self.play(Write(naomi_visited), run_time=0.8)
            self.wait(0.5)
            self.play(FadeOut(naomi_visited), run_time=0.5)
            
            # Reset edge color
            self.play(naomi_edge.animate.set_color(GRAY).set_stroke(width=4), run_time=0.5)
            
            # Empty queue indicator
            empty_queue = Text("Queue is empty - BFS complete", font_size=20, color=GREEN).next_to(queue_content, DOWN)
            self.play(Write(empty_queue), run_time=1)
            self.wait(1)
            self.play(FadeOut(empty_queue), run_time=0.5)
        
        # Remove queue and visited before showing the traversal order
        self.play(
            FadeOut(queue_title),
            FadeOut(queue_content),
            FadeOut(visited_title),
            FadeOut(visited_content)
        )
        
        # Show the traversal order with animation for each node
        final_order = Text("BFS Traversal Order:", font_size=28).to_edge(DOWN, buff=1)
        
        with self.voiceover(
            "And that's our final BFS traversal order. Let's review it step by step."
        ):
            self.play(Write(final_order))
            self.wait(0.5)
        
        # List of nodes in traversal order
        node_order = ['Mike', 'Mohamed', 'Diego', 'John', 'Naomi', 'Trevor']
        traversal_text = VGroup()
        
        # Animate highlighting each node in the traversal order
        for i, node in enumerate(node_order):
            if i == 0:
                text = Text(node, font_size=24, color=WHITE).next_to(final_order, RIGHT)
            else:
                text = Text(f" → {node}", font_size=24, color=WHITE).next_to(traversal_text[-1], RIGHT)
            
            traversal_text.add(text)
            
            # Highlight the corresponding node in the graph
            with self.voiceover(f"{node}"):
                self.play(
                    Write(text),
                    Indicate(vertices[node], color=YELLOW, scale_factor=1.5),
                    run_time=1
                )
                self.wait(0.3)
        
        # Group all traversal text
        all_traversal = VGroup(final_order, *traversal_text)
        
        with self.voiceover(
            "Notice how BFS explored all nodes at the current depth level before moving to the next level."
        ):
            self.wait(2)
            
        # Clear everything including edges before showing key insights
        self.play(
            FadeOut(graph_edges),
            FadeOut(graph_verts),
            FadeOut(all_traversal),
            FadeOut(title)
        )
        
        # Key insights centered on screen
        insights_title = Text("Key BFS Insights", font_size=36).to_edge(UP, buff=0.5)
        
        insights = VGroup(
            Text("• BFS explores nodes level by level", font_size=28),
            Text("• Uses a queue data structure (FIFO)", font_size=28),
            Text("• Guarantees shortest path in unweighted graphs", font_size=28),
            Text("• Time complexity: O(V + E)", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).center()
        
        with self.voiceover(
            "Let's highlight some key insights about BFS. First, BFS explores nodes level by level, "
            "using a queue data structure that follows First-In-First-Out or FIFO principle. "
            "BFS guarantees the shortest path in unweighted graphs, which makes it ideal for finding "
            "the closest connections. The time complexity is O(V plus E), where V is the number of vertices "
            "and E is the number of edges."
        ):
            self.play(Write(insights_title), run_time=1)
            self.play(Write(insights), run_time=8)
        
        # Conclusion
        self.play(FadeOut(insights), FadeOut(insights_title))
        
        self.wait(2)
        # conclusion = Text("Breadth-First Search is particularly useful for finding shortest paths,\n"
        #                  "connected components, and analyzing social networks.",
        #                  font_size=32).center()
        
        # with self.voiceover(
        #     "In conclusion, Breadth-First Search is particularly useful for finding shortest paths, "
        #     "connected components, and analyzing social networks like the one we just demonstrated. "
        #     "Thanks for watching this explanation of the BFS algorithm!"
        # ) as _:
        #     pass
        
           # Now create a simple example python code box
        code_text = '''
            def bfs(graph, start):
                visited = []
                queue = [start]

                while queue:
                    node = queue.pop(0)
                    if node not in visited: 
                        visited.append(node)
                        neighbours = graph[node]
                        for neighbour in neighbours: 
                            queue.append(neighbour)
                return visited
            '''

        code = Code(
            code_string=code_text,
            language="Python",
            background="window",
            background_config={"stroke_color": "maroon"},
        ).to_edge(DOWN).move_to(ORIGIN).shift(DOWN * 0.2)

        with self.voiceover("Here’s the Python implementation of breadth first search. You can find the link to the full source code in the video description below.") as _:
            self.play(Write(code))
            self.wait(2)

        with self.voiceover("Thank you for watching!"):
            pass
            # self.play(Write(conclusion))
            # self.wait(2)
            # self.play(FadeOut(conclusion))