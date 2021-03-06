# pylint: disable=C0111,R0903

"""Displays the number of todo items in ~/Documents/todo.txt"""

import platform

import bumblebee.input
import bumblebee.output
import bumblebee.engine


class Module(bumblebee.engine.Module):

    
    def __init__(self, engine, config):
        super(Module, self).__init__(engine, config,
            bumblebee.output.Widget(full_text=self.output)
        )
        self._todos = self.count_items() 


    def output(self, widget):
       self._todos = self.count_items()
       return self._todos 

    
    def state(self, widgets):
        if self._todos == 0 :
            return "empty"
        return "items"
        

    def count_items(filename):
        try:
            i=-1
            with open('~/Documents/todo.txt') as f:
                for i, l in enumerate(f):
                    pass
            return i+1 
        except Exception:
            return 0

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
