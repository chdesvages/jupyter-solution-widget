# Module to create widgets revealing exercise solutions.
# Example use in a notebook:
#
# from show_solutions import show
# show('Exercise 1')


import re
import ipywidgets as widgets
from IPython.display import display, Markdown

def show(tag, path='solutions.md'):
    '''
    Displays solution to a particular exercise.
    
    Input:
    tag (str): string corresponding to the exercise tag in the solutions file
    path (str, default 'solutions.md'): path to the Markdown file containing solutions
    '''

    # Create output area for the solution
    sol_area = widgets.Output(layout={'border': '1px solid green'})

    # Create accordion
    acc = widgets.Accordion(children=[sol_area], selected_index=None)
    acc.set_title(0, 'Solution')

    # Read solutions from file
    try:
        # Retrieve solution code from script, as a string
        with open(path) as f:
            sol = ''
            write_line = False

            # Read line-by-line
            for l in f:
                if re.match(r'#+ ?' + tag, l):
                    # Found a header with the exercise tag,
                    # start writing at the next line
                    write_line = True
                    continue

                # Continue writing lines until end tag
                if write_line:
                    if l.startswith('---'):
                        # Reached the end tag, stop reading file
                        write_line = False
                        break
                    else:
                        # Append current line to the solution to display
                        sol += l

        # Finally, add full solution to the display area, and display the accordion widget
        sol_area.append_display_data(Markdown(data=sol))
        display(acc)

    except FileNotFoundError:
        # If the file is not found, assume that solutions have not been released yet
        print('Solutions not available!')
