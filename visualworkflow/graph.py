# Copyright (C) 2009 Mat Booth <mat@matbooth.co.uk>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from pydot import Dot, Edge

from trac.core import *
from trac.ticket.default_workflow import get_workflow_config
from trac.web import IRequestHandler

__all__ = ['GraphRenderer']


class GraphRenderer(Component):
    """Request handler for rendering the graph of a workflow as an image."""

    implements(IRequestHandler)

    # IRequestHandler methods

    def match_request(self, req):
        return req.path_info == '/render-graph'

    def process_request(self, req):
        cp = ColourPicker()
        graph = Dot(size='6,10')

        """TODO - get workflow from request or database """

        actions = get_workflow_config(self.config)
        for action, attributes in actions.items():
            label = [attributes['name'], ]
            if req.args.get('show_ops'):
                label += attributes['operations']
            if req.args.get('show_perms'):
                label += attributes['permissions']
            for oldstate in attributes['oldstates']:
                colour = cp.get_colour(attributes['name'])
                edge = Edge(oldstate, attributes['newstate'], label='\\n'.join(label), color=colour, fontcolor=colour)
                graph.add_edge(edge)

        req.send(graph.create_png(prog='dot'), 'image/png')
        return None

class ColourPicker(object):
    """This colour picker is mostly stolen from workflow_parser.py in the Trac
    contrib directory."""

    # cyan, yellow are too light in colour
    colours = ['black', 'blue', 'red', 'green', 'purple', 'orange', 'darkgreen']

    def __init__(self):
        self.mapping = {}
        self.colouruse = [0,] * len(self.colours)

    def get_colour(self, name):
        """Choose a colour for the specified name. Names and their colours are
        stored in a dict so subsequent calls for the same name will yield the
        same colour."""
        try:
            colour_num = self.mapping[name]
        except(KeyError):
            self.mapping[name] = colour_num = self._pick_colour(name)

        self.colouruse[colour_num] += 1
        return self.colours[colour_num]

    def _pick_colour(self, name):
        """Pick the least used colour."""
        return self.colouruse.index(min(self.colouruse))
