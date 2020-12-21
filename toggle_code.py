#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.core.display import display, HTML


toggle_code_str = '''
<form action="javascript:code_toggle()"><input type="submit" id="toggleButton" value="Hide/Show Code"></form>
'''

toggle_code_prepare_str = '''
    <script>
    function code_toggle() {
        if ($('div.cell.code_cell.rendered.selected div.input').css('display') !='none'){
            $('div.cell.code_cell.rendered.selected div.input').hide('500');
        } else {
            $('div.cell.code_cell.rendered.selected div.input').show('500');
            
        }
        
    }
    </script>

'''

display(HTML(toggle_code_prepare_str + toggle_code_str))

def toggle_code():
    display(HTML(toggle_code_str))

run_code_str = '''
<form action="javascript:Jupyter.notebook.execute_cell()"><input type ="submit" id="runButton" value="Run Cell"></form>
'''

display(HTML(run_code_str))


def run_code():
    display(HTML(run_code_str))

