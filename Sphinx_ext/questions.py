# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 The University of Sydney
# This file is part of the Reauthoring toolkit

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor
# Boston, MA  02110-1301, USA.
#
# Author: Abelardo Pardo (abelardo.pardo@sydney.edu.au)
#

from __future__ import division

import os, re, sys
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.compat import Directive

from Sphinx_ext import html_form, common

class question(nodes.General, nodes.Element): pass

def skip_visit(self, node):
    # Function to skip the processing of the entire directive
    pass

def visit_question_node(self, node):

    print
    print 'VISITING!!!'
    print
    print node["name"]
    print node["args"]
    print

    # Get the question ID from the given label
    if len(node["args"]) == 1:
        question_id = node["args"][0]
    else:
        print 'Error in file', node.source, 'line', node.line
        print 'Directive', node["name"], 'must have an id as argument.'
        sys.exit(1)

    self.body.append('<div class="reauthoring_form">\n')
    self.body.append('<form>\n')

    # Subject and Verb values and element id
    # self.body.append('<input type="hidden" name="question-id" value="%s"/>' %
    #                  question_id)

def depart_question_node(self, node):

    print
    print 'Departing!!!'
    print

    question_id = node["args"][0]
    rows = node["rows"]
    columns = node["columns"]
    other_params = node["other_params"]

    # Add the right answer type depeding on the node type
    if node["name"] == 'question':
        self.body.append('<textarea name="%s" rows="%s" cols="%s" %s>' % \
                         (question_id, rows, columns, other_params))
        self.body.append('</textarea>')
    elif node["name"] == 'question-o':
        options = node["options"]
        if options != []:
            self.body.append('<select name="options-%s" %s>' % \
                             (question_id, other_params))
            for txt in options:
                self.body.append('<option value="%s">%s</option>' % (txt, txt))
            self.body.append('</select>')
    else: # node["name"] == 'question-s'
        self.body.append('<input type="text" name="%s" %s></input>' % \
                         (question_id, other_params))
        pass
    
    self.body.append('\n<button class="reauthoring_submit">Ok</button>\n')
    self.body.append('</form>\n')
    self.body.append('<img class="submit_ok_icon" style="display: none;" src="%s"></img>\n' \
                     % os.path.join(node["p_to_static"], 
                                    'Correct_20x20.png'))
    self.body.append('</div>\n')

class Question(Directive):
    """Directive to insert a question and catch the answer as an HTML form. The
    direcive has three systax forms:

    .. question-s: (for short versions)

       QUESTION TEXT

    .. question: (for large versions)
       :rows: n
       :columns: m

       QUESTION TEXT

    .. question-o: (for a list of options)
       :options: a, b, c, d, e, f, g

       QUESTION TEXT

    The "other_params" option can be used in any of them and is copied literally
    to the HTML element (input, select, or textarea)

    """

    has_content = True
    required_arguments = 1
    optional_arguments = 3
    final_argument_whitespace = False
    option_spec = {
        "rows": directives.positive_int,
        "columns" : directives.positive_int,
        "options": directives.unchanged,
        "other_params": directives.unchanged
    }

    def run(self):
        rows =    self.options.get('rows', 25)
        columns = self.options.get('columns', 80)
        options = self.options.get('options', '')
        other_params = self.options.get('other_params', '')

        print
        print 'Running!!!'
        print
        print self.name
        print

        # Get the path to the static directory containing the images
        p_to_static = common.get_relative_path_to_static(self.state.document)

        result = question(args = self.arguments,
                          name = self.name,
                          rows = rows,
                          columns = columns,
                          options = [x for x in options.split(',') if x != ''],
                          other_params = other_params,
                          p_to_static = p_to_static)
 
        # Parse the nested content
        self.state.nested_parse(self.content, self.content_offset, result)

        return [result]

def setup(app):
    app.add_node(question, 
                 html = (visit_question_node, 
                         depart_question_node),
                 latex = (skip_visit, skip_visit),
                 text = (skip_visit, skip_visit),
                 man = (skip_visit, skip_visit),
                 texinfo = (skip_visit, skip_visit))

    # Declaring the directive
    # app.add_directive("question",   Question)
    # app.add_directive("question-s", Question)
    # app.add_directive("question-o", Question)


    
