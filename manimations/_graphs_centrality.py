# from manim import *
# import networkx as nx
# from manim_voiceover import VoiceoverScene
# from manim_voiceover.services.gtts import GTTSService
# from manim_voiceover.services.openai import OpenAIService

# class GraphCentrality(VoiceoverScene):
#     def construct(self):
#         # Set up voice service
#         self.set_speech_service(OpenAIService(voice="echo", model="tts-1-hd"))  # AI voice

#         # Create a sample graph using NetworkX
#         g = nx.Graph()
#         g.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (4, 6), (5, 6), (3, 7)])
#         nodes = list(g.nodes())
#         edges = list(g.edges())

#         # Setup layout areas
#         left_side = 3 * LEFT
#         right_side = 3 * RIGHT
#         explanation_area = VGroup().to_edge(RIGHT, buff=0.5).to_edge(UP, buff=2)

#         # Create Manim graph object
#         layout = {
#             1: [-2, 1, 0],
#             2: [-2, -1, 0],
#             3: [0, 1, 0],
#             4: [0, -1, 0],
#             5: [2, 1, 0],
#             6: [2, -1, 0],
#             7: [0, 2.5, 0]
#         }
        
#         manim_graph = Graph(nodes, edges, layout=layout, layout_scale=2)
#         manim_graph.move_to(left_side)
        
#         # Node and edge styles
#         default_node_style = {"fill_color": WHITE, "stroke_color": DARK_GRAY, "stroke_width": 2}
#         highlighted_node_style = {"fill_color": YELLOW, "stroke_color": GOLD, "stroke_width": 3}
#         active_edge_style = {"stroke_color": YELLOW, "stroke_width": 4}
#         path_edge_style = {"stroke_color": GREEN, "stroke_width": 4}
        
#         # Label nodes
#         node_labels = VGroup()
#         for node in nodes:
#             label = Text(str(node), font_size=20).next_to(manim_graph.vertices[node], UP, buff=0.1)
#             node_labels.add(label)

#         # Title at the top
#         main_title = Text("Graph Centrality Measures", font_size=36).to_edge(UP)

#         with self.voiceover("Hello everyone! Today, we'll explore measures of centrality in graphs using Manim. These measures help us understand the importance of nodes within a network.") as tracker:
#             self.play(Write(main_title))
#             self.wait(0.5)
#             self.play(Create(manim_graph), run_time=2)
#             self.play(FadeIn(node_labels), run_time=1)
#             self.wait(0.5)

#         # Function to highlight a node and its connections
#         def highlight_node_and_connections(node):
#             neighbor_animations = []
#             edge_animations = []
            
#             # Get neighbors of the node
#             neighbors = list(g.neighbors(node))
            
#             # Highlight the edges connecting to neighbors
#             for neighbor in neighbors:
#                 if (node, neighbor) in edges:
#                     edge = (node, neighbor)
#                 elif (neighbor, node) in edges:
#                     edge = (neighbor, node)
#                 else:
#                     continue
                
#                 edge_animations.append(manim_graph.edges[edge].animate.set_stroke(color=YELLOW, width=4))
            
#             # Highlight the node itself
#             node_animation = manim_graph.vertices[node].animate.set_fill(YELLOW).set_stroke(color=GOLD, width=3)
            
#             return [node_animation] + edge_animations
        
#         # Function to reset node and edge highlights
#         def reset_highlights():
#             animations = []
#             for node in nodes:
#                 animations.append(manim_graph.vertices[node].animate.set_fill(WHITE).set_stroke(color=DARK_GRAY, width=2))
            
#             for edge in edges:
#                 animations.append(manim_graph.edges[edge].animate.set_stroke(color=WHITE, width=2))
                
#             return animations

#         # Function to show formula and explanation
#         def show_measure_title_and_formula(title_text, formula_tex, explanation_text=None, real_world_example=None):
#             title = Text(title_text, font_size=28).to_edge(RIGHT, buff=1).to_edge(UP, buff=1)
#             formula = MathTex(formula_tex, font_size=24).next_to(title, DOWN, buff=0.5)
            
#             animations = [Write(title), Write(formula)]
#             mobjects = [title, formula]
            
#             if explanation_text:
#                 explanation = Text(explanation_text, font_size=18, line_spacing=1.2).next_to(formula, DOWN, buff=0.5)
#                 explanation.set_width(config.frame_width/2 - 1)
#                 animations.append(Write(explanation))
#                 mobjects.append(explanation)
            
#             if real_world_example:
#                 # example_title = Text("Real-World Application:", font_size=20, color=BLUE).next_to(explanation if explanation else formula, DOWN, buff=0.5)
#                 # example_text = Text(real_world_example, font_size=16, line_spacing=1.2).next_to(example_title, DOWN, buff=0.2)
#                 # example_text.set_width(config.frame_width/2 - 1)
#                 # animations.append(Write(example_title))
#                 # animations.append(Write(example_text))
#                 # mobjects.extend([example_title, example_text])

#                 with self.voiceover(real_world_example) as _:
#                     pass
                
#             return animations, mobjects

#         # Clear previous measure info
#         def clear_measure_info(mobjects_to_clear):
#             return [FadeOut(mob) for mob in mobjects_to_clear]

#         # Function to show node calculation
#         def show_node_calculation(node, measure_name, value, calculation=None):
#             result_text = f"Node {node}: {measure_name} = {value:.3f}"
#             if calculation:
#                 result_text += f"\n{calculation}"
                
#             result = Text(result_text, font_size=18).next_to(manim_graph.vertices[node], buff=0.5)
#             result.move_to(RIGHT * 3 + DOWN * 2)
            
#             return Write(result), result

#         # Function to show summary of all node values
#         def show_summary_table(measure_values, measure_name):
#             table_title = Text(f"{measure_name} Summary", font_size=22)
#             table_title.move_to(RIGHT * 3 + DOWN * 0.5)
            
#             # Create table content
#             table_content = VGroup()
            
#             # Header
#             header = Text("Node   Value", font_size=18)
#             table_content.add(header)
            
#             # Sort nodes by centrality value (descending)
#             sorted_nodes = sorted(measure_values.items(), key=lambda x: x[1], reverse=True)
            
#             # Add each node's value
#             for node, value in sorted_nodes:
#                 row = Text(f" {node}      {value:.3f}", font_size=16)
#                 table_content.add(row)
            
#             # Arrange rows
#             table_content.arrange(DOWN, aligned_edge=LEFT)
#             table_content.next_to(table_title, DOWN, buff=0.3)
            
#             # Create background rectangle
#             background = SurroundingRectangle(
#                 VGroup(table_title, table_content), 
#                 buff=0.3, 
#                 stroke_color=BLUE_D, 
#                 stroke_width=2,
#                 fill_color=BLACK,
#                 fill_opacity=0.1
#             )
            
#             table_group = VGroup(background, table_title, table_content)
#             table_group.move_to(RIGHT * 3)
            
#             return [Create(background), Write(table_title), Write(table_content)], table_group

#         # Create a box for calculation results
#         calc_box = Rectangle(width=4, height=2.5, color=BLUE_D, fill_opacity=0.1)
#         calc_box.move_to(RIGHT * 3 + DOWN * 2)
#         calc_title = Text("Calculation", font_size=20).next_to(calc_box, UP, buff=0.1)
#         calc_group = VGroup(calc_box, calc_title)

#         # ======= DEGREE CENTRALITY =======
#         degree_title = "Degree Centrality"
#         degree_formula = r"C_D(v) = \frac{deg(v)}{|V| - 1}"
#         degree_explanation = "Measures how connected a node is based on the number of edges it has. Higher values indicate more connections."
#         degree_real_world = "In social networks, people with high degree centrality are 'connectors' who know many people directly. They're essential for information dissemination and can reach many people without intermediaries."
        
#         with self.voiceover("Let's start with Degree Centrality. The degree of a node is simply the number of edges connected to it. The formula normalizes this by dividing by the maximum possible connections, which is the total number of nodes minus one.") as tracker:
#             self.play(FadeOut(main_title))
#             self.wait(1)
#         degree_animations, degree_mobjects = show_measure_title_and_formula(degree_title, degree_formula, degree_explanation, degree_real_world)
#         self.play(*degree_animations)
#         self.wait(2)

#         with self.voiceover("Let's calculate the degree centrality for a couple of nodes in our graph.") as tracker:
#             self.play(FadeIn(calc_group))

#         # Calculate degree centrality for specific nodes (just 2 nodes as examples)
#         example_nodes = [1, 4]  # Chosen to show contrast
#         for node in example_nodes:
#             degree = g.degree(node)
#             degree_centrality = degree / (len(nodes) - 1)
#             calculation = f"deg({node}) = {degree}, |V| - 1 = {len(nodes) - 1}\n{degree} ÷ {len(nodes) - 1} = {degree_centrality:.3f}"
            
#             with self.voiceover(f"For node {node}, the degree is {degree}, meaning it has {degree} connections. Dividing by the number of nodes minus one, which is {len(nodes) - 1}, gives us a degree centrality of {degree_centrality:.3f}.") as tracker:
#                 # Highlight the node and its connections
#                 self.play(*highlight_node_and_connections(node))
                
#                 # Show calculation
#                 calc_anim, calc_text = show_node_calculation(node, "Degree Centrality", degree_centrality, calculation)
#                 self.play(calc_anim)
#                 self.wait(1)
                
#                 # Reset highlights and clear calculation
#                 self.play(*reset_highlights(), FadeOut(calc_text))

#         # Now calculate and display summary for all nodes
#         degree_centrality = {node: g.degree(node)/(len(nodes)-1) for node in nodes}
        
#         with self.voiceover("Let's now see the degree centrality values for all nodes in our network. Node 4 has the highest degree centrality, making it the most connected node.") as tracker:
#             summary_anims, summary_group = show_summary_table(degree_centrality, "Degree Centrality")
#             self.play(*summary_anims)
#             self.wait(2)
#             self.play(FadeOut(summary_group), FadeOut(calc_group))

#         # ======= BETWEENNESS CENTRALITY =======
#         betweenness_title = "Betweenness Centrality"
#         betweenness_formula = r"C_B(v) = \sum_{s \neq v \neq t} \frac{\sigma_{st}(v)}{\sigma_{st}}"
#         betweenness_explanation = "Measures how often a node lies on the shortest path between other nodes. Higher values indicate nodes that bridge different parts of the network."
#         betweenness_real_world = "In transportation networks, cities with high betweenness are major transit hubs. If removed, they disrupt the entire network. In communication networks, these are critical gatekeepers that control information flow between different groups."
        
#         with self.voiceover("Next, we'll look at Betweenness Centrality. This measures how often a node lies on the shortest path between other nodes. Nodes with high betweenness centrality act as bridges in the network.") as tracker:
#             self.play(*clear_measure_info(degree_mobjects))
#             self.wait(1)
        
#         betweenness_animations, betweenness_mobjects = show_measure_title_and_formula(betweenness_title, betweenness_formula, betweenness_explanation, betweenness_real_world)
#         self.play(*betweenness_animations)
#         self.wait(2)
        
#         # Function to show shortest paths through a node
#         def show_shortest_paths(node):
#             animations = []
#             path_edges = []
            
#             # For demonstration, we'll just show a few representative paths for key nodes
#             if node == 4:  # Node 4 is likely a central node in our graph
#                 paths = [
#                     [(1, 2), (2, 4)],  # Path from 1 to 5 through 4
#                     [(4, 5), (5, 6)]   # Path from 2 to 6 through 4
#                 ]
                
#                 for path in paths:
#                     for edge in path:
#                         if edge in manim_graph.edges:
#                             e = edge
#                         else:  # Check the reverse edge
#                             e = (edge[1], edge[0])
                            
#                         if e in manim_graph.edges:
#                             animations.append(manim_graph.edges[e].animate.set_stroke(color=GREEN, width=4))
#                             path_edges.append(e)
            
#             elif node == 3:  # Node 3 might be another important node
#                 paths = [
#                     [(1, 3)],  # Path from 1 to 7 through 3
#                     [(3, 7)]
#                 ]
                
#                 for path in paths:
#                     for edge in path:
#                         if edge in manim_graph.edges:
#                             e = edge
#                         else:  # Check the reverse edge
#                             e = (edge[1], edge[0])
                            
#                         if e in manim_graph.edges:
#                             animations.append(manim_graph.edges[e].animate.set_stroke(color=GREEN, width=4))
#                             path_edges.append(e)
            
#             return animations, path_edges

#         # Calculate betweenness centrality for each node
#         betweenness = nx.betweenness_centrality(g)
        
#         # Show only 2 nodes as examples
#         example_nodes = [3, 4]  # These should have interesting betweenness values
#         self.play(FadeIn(calc_group))
        
#         for node in example_nodes:
#             with self.voiceover(f"Node {node} has a betweenness centrality of {betweenness[node]:.3f}. This indicates how frequently this node appears on shortest paths between other nodes.") as tracker:
#                 # Highlight the node
#                 self.play(manim_graph.vertices[node].animate.set_fill(YELLOW).set_stroke(color=GOLD, width=3))
                
#                 # Show some shortest paths through this node
#                 path_animations, path_edges = show_shortest_paths(node)
#                 if path_animations:
#                     self.play(*path_animations)
                
#                 # Show calculation
#                 calc_anim, calc_text = show_node_calculation(node, "Betweenness Centrality", betweenness[node])
#                 self.play(calc_anim)
#                 self.wait(1)
                
#                 # Reset highlights and clear calculation
#                 reset_anims = [manim_graph.vertices[node].animate.set_fill(WHITE).set_stroke(color=DARK_GRAY, width=2)]
#                 for edge in edges:
#                     reset_anims.append(manim_graph.edges[edge].animate.set_stroke(color=WHITE, width=2))
                
#                 self.play(*reset_anims, FadeOut(calc_text))

#         # Show summary for all nodes
#         with self.voiceover("Here's a summary of betweenness centrality for all nodes. Nodes 3 and 4 have the highest values, as they connect different parts of the network.") as tracker:
#             summary_anims, summary_group = show_summary_table(betweenness, "Betweenness Centrality")
#             self.play(*summary_anims)
#             self.wait(2)
#             self.play(FadeOut(summary_group), FadeOut(calc_group))

#         # ======= CLOSENESS CENTRALITY =======
#         closeness_title = "Closeness Centrality"
#         closeness_formula = r"C_C(v) = \frac{n-1}{\sum_{u \neq v} d(v, u)}"
#         closeness_explanation = "Measures how close a node is to all other nodes. Higher values indicate nodes that can quickly reach or communicate with other nodes."
#         closeness_real_world = "In emergency response networks, facilities with high closeness centrality can reach all parts of the network quickly. In organizations, people with high closeness can efficiently distribute information to everyone, making them ideal coordinators."
        
#         with self.voiceover("Now, let's explore Closeness Centrality. This measures how close a node is to all other nodes in the graph. Nodes with high closeness can efficiently spread information to the entire network.") as tracker:
#             self.play(*clear_measure_info(betweenness_mobjects))
#             self.wait(1)
        
#         closeness_animations, closeness_mobjects = show_measure_title_and_formula(closeness_title, closeness_formula, closeness_explanation, closeness_real_world)
#         self.play(*closeness_animations)
#         self.wait(2) 

#         # Function to visualize distances from a node
#         def show_distances_from_node(node):
#             animations = []
#             distance_labels = []
            
#             # Calculate distances from this node to all others
#             distances = nx.single_source_shortest_path_length(g, node)
            
#             # Show distance animations (concentric circles)
#             max_distance = max(distances.values())
#             circles = []
#             for d in range(1, max_distance + 1):
#                 circle = Circle(radius=d*0.5, color=BLUE_E, fill_opacity=0.1)
#                 circle.move_to(manim_graph.vertices[node].get_center())
#                 circles.append(circle)
                
#             animations.append(AnimationGroup(*[Create(c) for c in circles], lag_ratio=0.3))
            
#             # Add distance labels to nodes
#             for other_node, distance in distances.items():
#                 if other_node != node:
#                     dist_label = Text(f"d={distance}", font_size=16)
#                     dist_label.next_to(manim_graph.vertices[other_node], DOWN, buff=0.1)
#                     distance_labels.append(dist_label)
            
#             animations.append(AnimationGroup(*[Write(label) for label in distance_labels], lag_ratio=0.1))
            
#             return animations, circles + distance_labels

#         # Calculate closeness centrality
#         closeness = nx.closeness_centrality(g)
        
#         # Show just 2 nodes as examples
#         example_nodes = [1, 4]  # Edge node vs central node
#         self.play(FadeIn(calc_group))
        
#         for node in example_nodes:
#             with self.voiceover(f"Node {node} has a closeness centrality of {closeness[node]:.3f}. This is based on the sum of shortest path lengths from this node to all others.") as tracker:
#                 # Highlight the node
#                 self.play(manim_graph.vertices[node].animate.set_fill(YELLOW).set_stroke(color=GOLD, width=3))
                
#                 # Show distances
#                 distance_animations, distance_objects = show_distances_from_node(node)
#                 if distance_animations:
#                     self.play(*distance_animations)
                
#                 # Show calculation
#                 distances_sum = sum(nx.single_source_shortest_path_length(g, node).values()) - 0  # Subtract distance to self (0)
#                 calculation = f"n-1 = {len(nodes)-1}, sum of distances = {distances_sum}\n{len(nodes)-1} ÷ {distances_sum} = {closeness[node]:.3f}"
#                 calc_anim, calc_text = show_node_calculation(node, "Closeness Centrality", closeness[node], calculation)
#                 self.play(calc_anim)
#                 self.wait(1.5)
                
#                 # Reset
#                 self.play(
#                     manim_graph.vertices[node].animate.set_fill(WHITE).set_stroke(color=DARK_GRAY, width=2),
#                     *[FadeOut(obj) for obj in distance_objects],
#                     FadeOut(calc_text)
#                 )

#         # Show summary for all nodes
#         with self.voiceover("Here's a summary of closeness centrality values for all nodes in our network. Nodes near the center of the graph have higher closeness, as they can reach other nodes more efficiently.") as tracker:
#             summary_anims, summary_group = show_summary_table(closeness, "Closeness Centrality")
#             self.play(*summary_anims)
#             self.wait(2)
#             self.play(FadeOut(summary_group), FadeOut(calc_group))

#         # ======= EIGENVECTOR CENTRALITY =======
#         eigenvector_title = "Eigenvector Centrality"
#         eigenvector_formula = r"C_E(v) = \frac{1}{\lambda} \sum_{u \in N(v)} C_E(u)"
#         eigenvector_explanation = "Measures node importance based on connections to other important nodes. A node is important if it's connected to other important nodes."
#         eigenvector_real_world = "In scientific citation networks, papers with high eigenvector centrality are foundational works in their field. In web search algorithms like Google's PageRank, websites with links from other important sites are ranked higher in search results."
        
#         with self.voiceover("Finally, we'll discuss Eigenvector Centrality. This measure considers a node important if it's connected to other important nodes. It's a recursive definition that converges to the principal eigenvector of the adjacency matrix.") as tracker:
#             self.play(*clear_measure_info(closeness_mobjects))
#             self.wait(1)
#         eigenvector_animations, eigenvector_mobjects = show_measure_title_and_formula(eigenvector_title, eigenvector_formula, eigenvector_explanation, eigenvector_real_world)
#         self.play(*eigenvector_animations)
#         self.wait(2)
#         # Calculate eigenvector centrality
#         eigenvector = nx.eigenvector_centrality(g)
        
#         # Function to visualize eigenvector centrality
#         def visualize_eigenvector_importance(centrality_values):
#             animations = []
#             node_sizes = []
            
#             # Scale node sizes based on centrality
#             max_centrality = max(centrality_values.values())
#             min_size, max_size = 0.2, 0.5
            
#             for node, value in centrality_values.items():
#                 # Calculate relative size
#                 relative_size = min_size + (value / max_centrality) * (max_size - min_size)
                
#                 # Change node size
#                 animations.append(manim_graph.vertices[node].animate.scale(relative_size * 3))
                
#                 # Also color nodes based on importance (red = high, blue = low)
#                 color = interpolate_color(BLUE_E, RED_E, value / max_centrality)
#                 animations.append(manim_graph.vertices[node].animate.set_fill(color))
                
#                 node_sizes.append((node, relative_size))
            
#             return animations, node_sizes

#         with self.voiceover("Let's visualize eigenvector centrality by adjusting the size and color of each node based on its importance. Larger, redder nodes are more central according to this measure.") as tracker:
#             eigenvector_animations, node_sizes = visualize_eigenvector_importance(eigenvector)
#             self.play(*eigenvector_animations)
#             self.wait(1)

#         # Just show the top 2 nodes by eigenvector centrality
#         top_nodes = sorted(eigenvector.items(), key=lambda x: x[1], reverse=True)[:2]
#         self.play(FadeIn(calc_group))
        
#         for node, value in top_nodes:
#             with self.voiceover(f"Node {node} has an eigenvector centrality of {value:.3f}. This reflects its connections to other important nodes in the network.") as tracker:
#                 # Highlight just this node
#                 self.play(Flash(manim_graph.vertices[node], color=WHITE, line_length=0.3))
                
#                 # Show calculation
#                 calc_anim, calc_text = show_node_calculation(node, "Eigenvector Centrality", value)
#                 self.play(calc_anim)
#                 self.wait(0.5)
                
#                 # Clear calculation
#                 self.play(FadeOut(calc_text))

#         # Show summary for all nodes
#         with self.voiceover("Here's a summary of eigenvector centrality for all nodes, showing which nodes are connected to other important nodes.") as tracker:
#             summary_anims, summary_group = show_summary_table(eigenvector, "Eigenvector Centrality")
#             self.play(*summary_anims)
#             self.wait(2)
#             self.play(FadeOut(summary_group), FadeOut(calc_group))

#         # Reset node sizes and colors
#         reset_animations = []
#         for node, size in node_sizes:
#             reset_animations.append(manim_graph.vertices[node].animate.scale(1/(size*3)).set_fill(WHITE))

#         with self.voiceover("Now that we've explored these centrality measures, we can better understand which nodes are most important in our network, depending on what kind of importance we care about.") as tracker:
#             self.play(*reset_animations)
#             self.play(*clear_measure_info(eigenvector_mobjects))
            
#             # Show final title
#             final_title = Text("Graph Centrality Measures", font_size=36).to_edge(UP)
#             self.play(Write(final_title))
            
#             # Create a summary table
#             table_data = [
#                 ["Node", "Degree", "Betweenness", "Closeness", "Eigenvector"],
#             ]
            
#             # Add data for all nodes
#             for node in nodes:
#                 table_data.append([
#                     str(node),
#                     f"{g.degree(node)/(len(nodes)-1):.3f}",
#                     f"{betweenness[node]:.3f}",
#                     f"{closeness[node]:.3f}",
#                     f"{eigenvector[node]:.3f}"
#                 ])
            
#             # Create a visual table since MobjectTable was commented out
#             table_title = Text("Centrality Measures Comparison", font_size=24).next_to(final_title,RIGHT, buff=0.5)
#             self.play(Write(table_title))
            
#             # Create visual table with rectangles
#             table_content = VGroup().next_to(manim_graph,RIGHT)
#             cell_width = 1.2
#             cell_height = 0.5
            
#             for i, row in enumerate(table_data):
#                 for j, cell in enumerate(row):
#                     cell_rect = Rectangle(width=cell_width, height=cell_height, 
#                                          fill_opacity=0.1, 
#                                          fill_color=BLUE if i == 0 else WHITE)
                    
#                     cell_rect.move_to(LEFT * 3 + RIGHT * j * cell_width + DOWN * (i * cell_height + 2))
#                     cell_text = Text(cell, font_size=16 if i == 0 else 14)
#                     cell_text.move_to(cell_rect.get_center())
                    
#                     table_content.add(VGroup(cell_rect, cell_text))
            
#             self.play(Create(table_content), run_time=2)
#             self.wait(1)

#         with self.voiceover("Finally, let's highlight an important real-world application: In social networks like Facebook, different centrality measures serve different purposes. Degree centrality identifies social hubs who can quickly spread information. Betweenness centrality finds users who connect different communities. Closeness centrality finds users who can efficiently reach the entire network. And eigenvector centrality, similar to PageRank, identifies the most influential users.") as tracker:
#             # Create a real-world example box
#             # example_title
#             pass


from manim import *
import networkx as nx
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.openai import OpenAIService

class GraphCentrality(VoiceoverScene):
    def construct(self):
        # Set up voice service
        self.set_speech_service(OpenAIService(voice="echo", model="tts-1-hd"))  # AI voice

        # Create a sample graph using NetworkX
        g = nx.Graph()
        g.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (4, 6), (5, 6), (3, 7)])
        nodes = list(g.nodes())
        edges = list(g.edges())

        # Setup layout areas
        left_side = 3 * LEFT
        right_side = 3 * RIGHT
        explanation_area = VGroup().to_edge(RIGHT, buff=0.5).to_edge(UP, buff=2)

        # Create Manim graph object
        layout = {
            1: [-2, 1, 0],
            2: [-2, -1, 0],
            3: [0, 1, 0],
            4: [0, -1, 0],
            5: [2, 1, 0],
            6: [2, -1, 0],
            7: [0, 2.5, 0]
        }
        
        manim_graph = Graph(nodes, edges, layout=layout, layout_scale=2)
        manim_graph.move_to(left_side)
        
        # Node and edge styles
        default_node_style = {"fill_color": WHITE, "stroke_color": DARK_GRAY, "stroke_width": 2}
        highlighted_node_style = {"fill_color": YELLOW, "stroke_color": GOLD, "stroke_width": 3}
        active_edge_style = {"stroke_color": YELLOW, "stroke_width": 4}
        path_edge_style = {"stroke_color": GREEN, "stroke_width": 4}
        
        # Label nodes
        node_labels = VGroup()
        for node in nodes:
            label = Text(str(node), font_size=20).next_to(manim_graph.vertices[node], UP, buff=0.1)
            node_labels.add(label)

        # Title at the top
        main_title = Text("Graph Centrality Measures", font_size=36).to_edge(UP)

        with self.voiceover("Hello everyone! Today, we'll explore measures of centrality in graphs using Manim. These measures help us understand the importance of nodes within a network.") as tracker:
            self.play(Write(main_title))
            self.wait(0.5)
            self.play(Create(manim_graph), run_time=2)
            self.play(FadeIn(node_labels), run_time=1)
            self.wait(0.5)

        # Function to highlight a node and its connections
        def highlight_node_and_connections(node):
            neighbor_animations = []
            edge_animations = []
            
            # Get neighbors of the node
            neighbors = list(g.neighbors(node))
            
            # Highlight the edges connecting to neighbors
            for neighbor in neighbors:
                if (node, neighbor) in edges:
                    edge = (node, neighbor)
                elif (neighbor, node) in edges:
                    edge = (neighbor, node)
                else:
                    continue
                
                edge_animations.append(manim_graph.edges[edge].animate.set_stroke(color=YELLOW, width=4))
            
            # Highlight the node itself
            node_animation = manim_graph.vertices[node].animate.set_fill(YELLOW).set_stroke(color=GOLD, width=3)
            
            return [node_animation] + edge_animations
        
        # Function to reset node and edge highlights
        def reset_highlights():
            animations = []
            for node in nodes:
                animations.append(manim_graph.vertices[node].animate.set_fill(WHITE).set_stroke(color=DARK_GRAY, width=2))
            
            for edge in edges:
                animations.append(manim_graph.edges[edge].animate.set_stroke(color=WHITE, width=2))
                
            return animations

        # Function to show formula and explanation
        def show_measure_title_and_formula(title_text, formula_tex, explanation_text=None, real_world_example=None):
            title = Text(title_text, font_size=28).to_edge(RIGHT, buff=1).to_edge(UP, buff=1)
            formula = MathTex(formula_tex, font_size=24).next_to(title, DOWN, buff=0.5)
            
            animations = [Write(title), Write(formula)]
            mobjects = [title, formula]
            
            if explanation_text:
                explanation = Text(explanation_text, font_size=18, line_spacing=1.2).next_to(formula, DOWN, buff=0.5)
                explanation.set_width(config.frame_width/2 - 1)
                animations.append(Write(explanation))
                mobjects.append(explanation)
            
            if real_world_example:
                example_title = Text("Real-World Application:", font_size=20, color=BLUE).next_to(explanation if explanation else formula, DOWN, buff=0.5)
                example_text = Text(real_world_example, font_size=16, line_spacing=1.2).next_to(example_title, DOWN, buff=0.2)
                example_text.set_width(config.frame_width/2 - 1.5)  # Make slightly narrower to avoid overlap
                animations.append(Write(example_title))
                animations.append(Write(example_text))
                mobjects.extend([example_title, example_text])
                
            return animations, mobjects

        # Clear previous measure info
        def clear_measure_info(mobjects_to_clear):
            return [FadeOut(mob) for mob in mobjects_to_clear]

        # Function to show node calculation
        def show_node_calculation(node, measure_name, value, calculation=None):
            result_text = f"Node {node}: {measure_name} = {value:.3f}"
            if calculation:
                result_text += f"\n{calculation}"
                
            result = Text(result_text, font_size=18).next_to(manim_graph.vertices[node], buff=0.5)
            result.move_to(RIGHT * 3 + DOWN * 2)
            
            return Write(result), result

        # Function to show summary of all node values - moved to right side
        def show_summary_table(measure_values, measure_name):
            table_title = Text(f"{measure_name} Summary", font_size=22)
            table_title.move_to(RIGHT * 4 + UP * 1)  # Moved more to the right and up
            
            # Create table content
            table_content = VGroup()
            
            # Header
            header = Text("Node   Value", font_size=18)
            table_content.add(header)
            
            # Sort nodes by centrality value (descending)
            sorted_nodes = sorted(measure_values.items(), key=lambda x: x[1], reverse=True)
            
            # Add each node's value
            for node, value in sorted_nodes:
                row = Text(f" {node}      {value:.3f}", font_size=16)
                table_content.add(row)
            
            # Arrange rows
            table_content.arrange(DOWN, aligned_edge=LEFT)
            table_content.next_to(table_title, DOWN, buff=0.3)
            
            # Create background rectangle
            background = SurroundingRectangle(
                VGroup(table_title, table_content), 
                buff=0.3, 
                stroke_color=BLUE_D, 
                stroke_width=2,
                fill_color=BLACK,
                fill_opacity=0.1
            )
            
            table_group = VGroup(background, table_title, table_content)
            table_group.move_to(RIGHT * 4)  # Moved more to the right
            
            return [Create(background), Write(table_title), Write(table_content)], table_group

        # Create a box for calculation results
        calc_box = Rectangle(width=4, height=2.5, color=BLUE_D, fill_opacity=0.1)
        calc_box.move_to(RIGHT * 3 + DOWN * 2)
        calc_title = Text("Calculation", font_size=20).next_to(calc_box, UP, buff=0.1)
        calc_group = VGroup(calc_box, calc_title)

        # ======= DEGREE CENTRALITY =======
        degree_title = "Degree Centrality"
        degree_formula = r"C_D(v) = \frac{deg(v)}{|V| - 1}"
        degree_explanation = "Measures how connected a node is based on the number of edges it has. Higher values indicate more connections."
        degree_real_world = "In social networks, people with high degree centrality are 'connectors' who know many people directly. They're essential for information dissemination and can reach many people without intermediaries."
        
        with self.voiceover("Let's start with Degree Centrality. The degree of a node is simply the number of edges connected to it. The formula normalizes this by dividing by the maximum possible connections, which is the total number of nodes minus one.") as tracker:
            self.play(FadeOut(main_title))
            self.wait(1)
        degree_animations, degree_mobjects = show_measure_title_and_formula(degree_title, degree_formula, degree_explanation)
        self.play(*degree_animations)
        self.wait(2)

        # Add real world example with proper timing
        with self.voiceover(degree_real_world) as tracker:
            # Let the voiceover finish before proceeding
            self.wait(1)

        with self.voiceover("Let's calculate the degree centrality for a couple of nodes in our graph.") as tracker:
            self.play(FadeIn(calc_group))

        # Calculate degree centrality for specific nodes (just 2 nodes as examples)
        example_nodes = [1, 4]  # Chosen to show contrast
        for node in example_nodes:
            degree = g.degree(node)
            degree_centrality = degree / (len(nodes) - 1)
            calculation = f"deg({node}) = {degree}, |V| - 1 = {len(nodes) - 1}\n{degree} ÷ {len(nodes) - 1} = {degree_centrality:.3f}"
            
            with self.voiceover(f"For node {node}, the degree is {degree}, meaning it has {degree} connections. Dividing by the number of nodes minus one, which is {len(nodes) - 1}, gives us a degree centrality of {degree_centrality:.3f}.") as tracker:
                # Highlight the node and its connections
                self.play(*highlight_node_and_connections(node))
                
                # Show calculation
                calc_anim, calc_text = show_node_calculation(node, "Degree Centrality", degree_centrality, calculation)
                self.play(calc_anim)
                self.wait(1)
                
                # Reset highlights and clear calculation
                self.play(*reset_highlights(), FadeOut(calc_text))

        # Now calculate and display summary for all nodes
        degree_centrality = {node: g.degree(node)/(len(nodes)-1) for node in nodes}
        
        with self.voiceover("Let's now see the degree centrality values for all nodes in our network. Node 4 has the highest degree centrality, making it the most connected node.") as tracker:
            summary_anims, summary_group = show_summary_table(degree_centrality, "Degree Centrality")
            self.play(*summary_anims)
            self.wait(2)
            self.play(FadeOut(summary_group), FadeOut(calc_group))

        # ======= BETWEENNESS CENTRALITY =======
        betweenness_title = "Betweenness Centrality"
        betweenness_formula = r"C_B(v) = \sum_{s \neq v \neq t} \frac{\sigma_{st}(v)}{\sigma_{st}}"
        betweenness_explanation = "Measures how often a node lies on the shortest path between other nodes. Higher values indicate nodes that bridge different parts of the network."
        betweenness_real_world = "In transportation networks, cities with high betweenness are major transit hubs. If removed, they disrupt the entire network. In communication networks, these are critical gatekeepers that control information flow between different groups."
        
        with self.voiceover("Next, we'll look at Betweenness Centrality. This measures how often a node lies on the shortest path between other nodes. Nodes with high betweenness centrality act as bridges in the network.") as tracker:
            self.play(*clear_measure_info(degree_mobjects))
            self.wait(1)
        
        betweenness_animations, betweenness_mobjects = show_measure_title_and_formula(betweenness_title, betweenness_formula, betweenness_explanation)
        self.play(*betweenness_animations)
        self.wait(2)
        
        # Add real world example with proper timing
        with self.voiceover(betweenness_real_world) as tracker:
            # Let the voiceover finish before proceeding
            self.wait(1)
        
        # Function to show shortest paths through a node
        def show_shortest_paths(node):
            animations = []
            path_edges = []
            
            # For demonstration, we'll just show a few representative paths for key nodes
            if node == 4:  # Node 4 is likely a central node in our graph
                paths = [
                    [(1, 2), (2, 4)],  # Path from 1 to 5 through 4
                    [(4, 5), (5, 6)]   # Path from 2 to 6 through 4
                ]
                
                for path in paths:
                    for edge in path:
                        if edge in manim_graph.edges:
                            e = edge
                        else:  # Check the reverse edge
                            e = (edge[1], edge[0])
                            
                        if e in manim_graph.edges:
                            animations.append(manim_graph.edges[e].animate.set_stroke(color=GREEN, width=4))
                            path_edges.append(e)
            
            elif node == 3:  # Node 3 might be another important node
                paths = [
                    [(1, 3)],  # Path from 1 to 7 through 3
                    [(3, 7)]
                ]
                
                for path in paths:
                    for edge in path:
                        if edge in manim_graph.edges:
                            e = edge
                        else:  # Check the reverse edge
                            e = (edge[1], edge[0])
                            
                        if e in manim_graph.edges:
                            animations.append(manim_graph.edges[e].animate.set_stroke(color=GREEN, width=4))
                            path_edges.append(e)
            
            return animations, path_edges

        # Calculate betweenness centrality for each node
        betweenness = nx.betweenness_centrality(g)
        
        # Show only 2 nodes as examples
        example_nodes = [3, 4]  # These should have interesting betweenness values
        self.play(FadeIn(calc_group))
        
        for node in example_nodes:
            with self.voiceover(f"Node {node} has a betweenness centrality of {betweenness[node]:.3f}. This indicates how frequently this node appears on shortest paths between other nodes.") as tracker:
                # Highlight the node
                self.play(manim_graph.vertices[node].animate.set_fill(YELLOW).set_stroke(color=GOLD, width=3))
                
                # Show some shortest paths through this node
                path_animations, path_edges = show_shortest_paths(node)
                if path_animations:
                    self.play(*path_animations)
                
                # Show calculation
                calc_anim, calc_text = show_node_calculation(node, "Betweenness Centrality", betweenness[node])
                self.play(calc_anim)
                self.wait(1)
                
                # Reset highlights and clear calculation
                reset_anims = [manim_graph.vertices[node].animate.set_fill(WHITE).set_stroke(color=DARK_GRAY, width=2)]
                for edge in edges:
                    reset_anims.append(manim_graph.edges[edge].animate.set_stroke(color=WHITE, width=2))
                
                self.play(*reset_anims, FadeOut(calc_text))

        # Show summary for all nodes
        with self.voiceover("Here's a summary of betweenness centrality for all nodes. Nodes 3 and 4 have the highest values, as they connect different parts of the network.") as tracker:
            summary_anims, summary_group = show_summary_table(betweenness, "Betweenness Centrality")
            self.play(*summary_anims)
            self.wait(2)
            self.play(FadeOut(summary_group), FadeOut(calc_group))

        # ======= CLOSENESS CENTRALITY =======
        closeness_title = "Closeness Centrality"
        closeness_formula = r"C_C(v) = \frac{n-1}{\sum_{u \neq v} d(v, u)}"
        closeness_explanation = "Measures how close a node is to all other nodes. Higher values indicate nodes that can quickly reach or communicate with other nodes."
        closeness_real_world = "In emergency response networks, facilities with high closeness centrality can reach all parts of the network quickly. In organizations, people with high closeness can efficiently distribute information to everyone, making them ideal coordinators."
        
        with self.voiceover("Now, let's explore Closeness Centrality. This measures how close a node is to all other nodes in the graph. Nodes with high closeness can efficiently spread information to the entire network.") as tracker:
            self.play(*clear_measure_info(betweenness_mobjects))
            self.wait(1)
        
        closeness_animations, closeness_mobjects = show_measure_title_and_formula(closeness_title, closeness_formula, closeness_explanation)
        self.play(*closeness_animations)
        self.wait(2)
        
        # Add real world example with proper timing
        with self.voiceover(closeness_real_world) as tracker:
            # Let the voiceover finish before proceeding
            self.wait(1)

        # Function to visualize distances from a node
        def show_distances_from_node(node):
            animations = []
            distance_labels = []
            
            # Calculate distances from this node to all others
            distances = nx.single_source_shortest_path_length(g, node)
            
            # Show distance animations (concentric circles)
            max_distance = max(distances.values())
            circles = []
            for d in range(1, max_distance + 1):
                circle = Circle(radius=d*0.5, color=BLUE_E, fill_opacity=0.1)
                circle.move_to(manim_graph.vertices[node].get_center())
                circles.append(circle)
                
            animations.append(AnimationGroup(*[Create(c) for c in circles], lag_ratio=0.3))
            
            # Add distance labels to nodes
            for other_node, distance in distances.items():
                if other_node != node:
                    dist_label = Text(f"d={distance}", font_size=16)
                    dist_label.next_to(manim_graph.vertices[other_node], DOWN, buff=0.1)
                    distance_labels.append(dist_label)
            
            animations.append(AnimationGroup(*[Write(label) for label in distance_labels], lag_ratio=0.1))
            
            return animations, circles + distance_labels

        # Calculate closeness centrality
        closeness = nx.closeness_centrality(g)
        
        # Show just 2 nodes as examples
        example_nodes = [1, 4]  # Edge node vs central node
        self.play(FadeIn(calc_group))
        
        for node in example_nodes:
            with self.voiceover(f"Node {node} has a closeness centrality of {closeness[node]:.3f}. This is based on the sum of shortest path lengths from this node to all others.") as tracker:
                # Highlight the node
                self.play(manim_graph.vertices[node].animate.set_fill(YELLOW).set_stroke(color=GOLD, width=3))
                
                # Show distances
                distance_animations, distance_objects = show_distances_from_node(node)
                if distance_animations:
                    self.play(*distance_animations)
                
                # Show calculation
                distances_sum = sum(nx.single_source_shortest_path_length(g, node).values()) - 0  # Subtract distance to self (0)
                calculation = f"n-1 = {len(nodes)-1}, sum of distances = {distances_sum}\n{len(nodes)-1} ÷ {distances_sum} = {closeness[node]:.3f}"
                calc_anim, calc_text = show_node_calculation(node, "Closeness Centrality", closeness[node], calculation)
                self.play(calc_anim)
                self.wait(1.5)
                
                # Reset
                self.play(
                    manim_graph.vertices[node].animate.set_fill(WHITE).set_stroke(color=DARK_GRAY, width=2),
                    *[FadeOut(obj) for obj in distance_objects],
                    FadeOut(calc_text)
                )

        # Show summary for all nodes
        with self.voiceover("Here's a summary of closeness centrality values for all nodes in our network. Nodes near the center of the graph have higher closeness, as they can reach other nodes more efficiently.") as tracker:
            summary_anims, summary_group = show_summary_table(closeness, "Closeness Centrality")
            self.play(*summary_anims)
            self.wait(2)
            self.play(FadeOut(summary_group), FadeOut(calc_group))

        # ======= EIGENVECTOR CENTRALITY =======
        eigenvector_title = "Eigenvector Centrality"
        eigenvector_formula = r"C_E(v) = \frac{1}{\lambda} \sum_{u \in N(v)} C_E(u)"
        eigenvector_explanation = "Measures node importance based on connections to other important nodes. A node is important if it's connected to other important nodes."
        eigenvector_real_world = "In scientific citation networks, papers with high eigenvector centrality are foundational works in their field. In web search algorithms like Google's PageRank, websites with links from other important sites are ranked higher in search results."
        
        with self.voiceover("Finally, we'll discuss Eigenvector Centrality. This measure considers a node important if it's connected to other important nodes. It's a recursive definition that converges to the principal eigenvector of the adjacency matrix.") as tracker:
            self.play(*clear_measure_info(closeness_mobjects))
            self.wait(1)
        eigenvector_animations, eigenvector_mobjects = show_measure_title_and_formula(eigenvector_title, eigenvector_formula, eigenvector_explanation)
        self.play(*eigenvector_animations)
        self.wait(2)
        
        # Add real world example with proper timing
        with self.voiceover(eigenvector_real_world) as tracker:
            # Let the voiceover finish before proceeding
            self.wait(1)
            
        # Calculate eigenvector centrality
        eigenvector = nx.eigenvector_centrality(g)
        
        # Function to visualize eigenvector centrality
        def visualize_eigenvector_importance(centrality_values):
            animations = []
            node_sizes = []
            
            # Scale node sizes based on centrality
            max_centrality = max(centrality_values.values())
            min_size, max_size = 0.2, 0.5
            
            for node, value in centrality_values.items():
                # Calculate relative size
                relative_size = min_size + (value / max_centrality) * (max_size - min_size)
                
                # Change node size
                animations.append(manim_graph.vertices[node].animate.scale(relative_size * 3))
                
                # Also color nodes based on importance (red = high, blue = low)
                color = interpolate_color(BLUE_E, RED_E, value / max_centrality)
                animations.append(manim_graph.vertices[node].animate.set_fill(color))
                
                node_sizes.append((node, relative_size))
            
            return animations, node_sizes

        with self.voiceover("Let's visualize eigenvector centrality by adjusting the size and color of each node based on its importance. Larger, redder nodes are more central according to this measure.") as tracker:
            eigenvector_animations, node_sizes = visualize_eigenvector_importance(eigenvector)
            self.play(*eigenvector_animations)
            self.wait(1)

        # Just show the top 2 nodes by eigenvector centrality
        top_nodes = sorted(eigenvector.items(), key=lambda x: x[1], reverse=True)[:2]
        self.play(FadeIn(calc_group))
        
        for node, value in top_nodes:
            with self.voiceover(f"Node {node} has an eigenvector centrality of {value:.3f}. This reflects its connections to other important nodes in the network.") as tracker:
                # Highlight just this node
                self.play(Flash(manim_graph.vertices[node], color=WHITE, line_length=0.3))
                
                # Show calculation
                calc_anim, calc_text = show_node_calculation(node, "Eigenvector Centrality", value)
                self.play(calc_anim)
                self.wait(0.5)
                
                # Clear calculation
                self.play(FadeOut(calc_text))

        # Show summary for all nodes
        with self.voiceover("Here's a summary of eigenvector centrality for all nodes, showing which nodes are connected to other important nodes.") as tracker:
            summary_anims, summary_group = show_summary_table(eigenvector, "Eigenvector Centrality")
            self.play(*summary_anims)
            self.wait(2)
            self.play(FadeOut(summary_group), FadeOut(calc_group))

        # Reset node sizes and colors
        reset_animations = []
        for node, size in node_sizes:
            reset_animations.append(manim_graph.vertices[node].animate.scale(1/(size*3)).set_fill(WHITE))

        with self.voiceover("Now that we've explored these centrality measures, we can better understand which nodes are most important in our network, depending on what kind of importance we care about.") as tracker:
            self.play(*reset_animations)
            self.play(*clear_measure_info(eigenvector_mobjects))
            
            # Show final title
            final_title = Text("Graph Centrality Measures", font_size=36).to_edge(UP)
            self.play(Write(final_title))
            
            # Create a summary table
            table_data = [
                ["Node", "Degree", "Betweenness", "Closeness", "Eigenvector"],
            ]
            
            # Add data for all nodes
            for node in nodes:
                table_data.append([
                    str(node),
                    f"{g.degree(node)/(len(nodes)-1):.3f}",
                    f"{betweenness[node]:.3f}",
                    f"{closeness[node]:.3f}",
                    f"{eigenvector[node]:.3f}"
                ])
            
            # Create a visual table since MobjectTable was commented out
            table_title = Text("Centrality Measures Comparison", font_size=24).next_to(manim_graph, RIGHT, buff=1).to_edge(UP, buff=2)
            self.play(Write(table_title))
            
            # Create visual table with rectangles - positioned to the RIGHT of the graph
            table_content = VGroup()
            cell_width = 1.2
            cell_height = 0.5
            
            for i, row in enumerate(table_data):
                for j, cell in enumerate(row):
                    cell_rect = Rectangle(width=cell_width, height=cell_height, 
                                         fill_opacity=0.1, 
                                         fill_color=BLUE if i == 0 else WHITE)
                    
                    # Position table to the right of the graph
                    cell_rect.move_to(RIGHT * (3 + j * cell_width) + DOWN * (i * cell_height - 1))
                    cell_text = Text(cell, font_size=16 if i == 0 else 14)
                    cell_text.move_to(cell_rect.get_center())
                    
                    table_content.add(VGroup(cell_rect, cell_text))
            
            self.play(Create(table_content), run_time=2)
            self.wait(1)

        with self.voiceover("Finally, let's highlight an important real-world application: In social networks like Facebook, different centrality measures serve different purposes. Degree centrality identifies social hubs who can quickly spread information. Betweenness centrality finds users who connect different communities. Closeness centrality finds users who can efficiently reach the entire network. And eigenvector centrality, similar to PageRank, identifies the most influential users.") as tracker:
            # Add a pause to ensure the voiceover completes fully
            self.wait(2)