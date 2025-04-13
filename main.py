import graphviz
import os

# Optional: Define the path to the Graphviz executables if not in system PATH
# Example for Windows if installed in a custom location:
# os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'

# Create a new directed graph
# Specify engine='neato' to respect 'pos' attributes
dot = graphviz.Digraph('DripOMatic', 
                       comment='The Drip-O-Matic Process Flow', 
                       engine='neato')

# Set graph attributes (equivalent to the ones in the DOT file)
dot.graph_attr['overlap'] = 'false' 
dot.graph_attr['splines'] = 'true'
# Note: layout=neato is handled by setting engine='neato' during Digraph creation

# --- Node Definitions with Explicit Positions ---
# Use keyword arguments for node attributes
# The 'pos' attribute ends with '!' to pin the node

# Row 1: Left to Right (y=0)
dot.node('Start',              label='Start',                        shape='ellipse', fillcolor='lightblue',  style='filled', pos='0,0!')
dot.node('Brainstorm',         label='Brainstorming\n(Feb 3)',       shape='box',     fillcolor='lightgrey', style='filled', pos='2,0!')
dot.node('MarketResearch',     label='Market Research',              shape='box',     fillcolor='lightblue', style='filled', pos='4,0!')
dot.node('CustomerValidation', label='Customer Validation',          shape='box',     fillcolor='lightblue', style='filled', pos='6,0!')
dot.node('ChooseProduct',      label='Choosing Product\n(Feb 5)',    shape='box',     fillcolor='lightgrey', style='filled', pos='8,0!')
dot.node('CD',                 label='Concept Development',          shape='box',     fillcolor='lightgrey', style='filled', pos='10,0!')

# Row 2: Right to Left (y=-2)
dot.node('Proposal',           label='Product Proposal\n(Feb 6-10)',   shape='box',     fillcolor='lightgrey', style='filled', pos='10,-2!')
dot.node('Approval',           label='Product Approval\n(Feb 10)',     shape='box',     fillcolor='lightgrey', style='filled', pos='8,-2!')
dot.node('RRL',                label='Gathering RRLs & RRS\n(Feb 13)', shape='box',     fillcolor='lightgrey', style='filled', pos='6,-2!')
dot.node('DP',                 label='Design & Planning',              shape='box',     fillcolor='lightgrey', style='filled', pos='4,-2!')

# Row 3: Left to Right (y=-4)
dot.node('Sketch',             label='Draft Sketch\n(Feb 21)',         shape='box',     fillcolor='lightgrey', style='filled', pos='4,-4!')
dot.node('Materials',          label='Materials & Costing\n(Feb 24-35)', shape='box',     fillcolor='lightgrey', style='filled', pos='6,-4!') # Date typo kept
dot.node('MP',                 label='Material Procurement',           shape='box',     fillcolor='lightgrey', style='filled', pos='8,-4!')
dot.node('PD',                 label='Prototype Development\n(Mar 6-36)', shape='box',     fillcolor='lightgrey', style='filled', pos='10,-4!') # Date typo kept
dot.node('TC',                 label='Testing & Calibration\n(Mar 28)',  shape='box',     fillcolor='lightgrey', style='filled', pos='12,-4!')

# Row 4: Decision and Loop (y=-6)
dot.node('AN',                 label='Adjustments Needed?',            shape='diamond', fillcolor='lightyellow', style='filled', pos='12,-6!')
dot.node('FA',                 label='Final Adjustments',              shape='box',     fillcolor='lightgrey', style='filled', pos='10,-6!')

# Row 5: Right to Left (y=-8)
dot.node('Marketing',          label='Marketing Strategy',             shape='box',     fillcolor='lightgreen', style='filled', pos='12,-8!')
dot.node('Production',         label='Production',                     shape='box',     fillcolor='lightgreen', style='filled', pos='10,-8!')
dot.node('Distribution',       label='Distribution',                   shape='box',     fillcolor='lightgreen', style='filled', pos='8,-8!')
dot.node('DD',                 label='Deployment & Demo\n(Apr 3)',      shape='box',     fillcolor='lightgreen', style='filled', pos='6,-8!')
dot.node('End',                label='End',                          shape='ellipse', fillcolor='lightcoral', style='filled', pos='4,-8!')

# --- Edge Definitions ---
# Use the node names defined above

# Row 1 connections
dot.edge('Start', 'Brainstorm')
dot.edge('Brainstorm', 'MarketResearch')
dot.edge('MarketResearch', 'CustomerValidation')
dot.edge('CustomerValidation', 'ChooseProduct')
dot.edge('ChooseProduct', 'CD')

# Row 1 to Row 2
dot.edge('CD', 'Proposal') 

# Row 2 connections
dot.edge('Proposal', 'Approval')
dot.edge('Approval', 'RRL')
dot.edge('RRL', 'DP')

# Row 2 to Row 3
dot.edge('DP', 'Sketch') 

# Row 3 connections
dot.edge('Sketch', 'Materials')
dot.edge('Materials', 'MP')
dot.edge('MP', 'PD')
dot.edge('PD', 'TC')

# Row 3 to Row 4
dot.edge('TC', 'AN')

# Row 4 Decision and Loop
dot.edge('AN', 'FA', label=' Yes') # Edge with label
dot.edge('FA', 'TC')              # Loop back

# Row 4 to Row 5 (No branch)
dot.edge('AN', 'Marketing', label=' No') # Edge with label

# Row 5 connections
dot.edge('Marketing', 'Production')
dot.edge('Production', 'Distribution')
dot.edge('Distribution', 'DD')
dot.edge('DD', 'End')

# --- Rendering ---
# Define the output filename (without extension)
output_filename = 'dripomatic_graph'
output_format = 'png' # You can change this to 'pdf', 'svg', etc.

try:
    # Render the graph to a file (e.g., dripomatic_graph.png)
    # The '.gv' source file will also be created.
    # view=True automatically opens the generated file.
    dot.render(output_filename, format=output_format, view=True)
    print(f"Graph successfully generated and saved as '{output_filename}.{output_format}' and '{output_filename}.gv'")
    print(f"Attempting to open '{output_filename}.{output_format}'...")
except graphviz.exceptions.ExecutableNotFound:
    print("Error: Graphviz executables not found. Make sure Graphviz is installed and in your system's PATH.")
    print("You can check the generated DOT source file:", f"'{output_filename}.gv'")
except Exception as e:
    print(f"An error occurred during rendering: {e}")
    print("You can check the generated DOT source file:", f"'{output_filename}.gv'")

# Optional: Print the generated DOT source code
# print("\nGenerated DOT source:\n")
# print(dot.source)