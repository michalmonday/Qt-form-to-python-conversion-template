''' Converts .ui file (outputted by Qt Designer) to .py file (for PyQt6) 
and imports from the bottom to the top of the file, because promoted 
classes happen to be imported at the bottom for some reason which was 
causing an error. '''

import os
import re
out_fname = 'MainWindow.py'
form_name = 'mainwindow.ui'

print( os.popen(f'pyuic6 {form_name} -o {out_fname}').read() )

with open(out_fname) as f:
    lines = [line.rstrip() for line in f.readlines()]

lines_to_move = []
for line in reversed(lines):
    # if re.search(r'^from.+import', line):
    if line.startswith('from'):
        lines_to_move.append(line)
    else:
        break
for line in lines_to_move:
    lines.remove(line)

lines = lines_to_move + lines

with open(out_fname, 'w') as f:
    f.write('\n'.join(lines))

