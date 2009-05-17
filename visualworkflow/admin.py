# Copyright (C) 2009 Mat Booth <mat@matbooth.co.uk>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from trac.admin import IAdminPanelProvider
from trac.core import *
from trac.ticket.default_workflow import get_workflow_config
from trac.web.chrome import ITemplateProvider, add_script

__all__ = ['WorkflowAdminPanel']


class WorkflowAdminPanel(Component):
    """Provides the workflow editor as an admin panel."""

    implements(IAdminPanelProvider, ITemplateProvider)

    # IAdminPanelProvider methods

    def get_admin_panels(self, req):
        if 'TICKET_ADMIN' in req.perm:
            yield ('ticket', 'Ticket System', 'workflow', 'Workflow')

    def render_admin_panel(self, req, cat, page, info):
        req.perm.require('TICKET_ADMIN')
        add_script(req, 'visualworkflow/js/graph_options.js')

        actions = get_workflow_config(self.config)
        self.log.debug("Workflow from config: %s" % str(actions))
        data = {'workflow' : actions}
        return 'admin_workflow.html', data

    # ITemplateProvider methods

    def get_htdocs_dirs(self):
        from pkg_resources import resource_filename
        return [('visualworkflow', resource_filename(__name__, 'htdocs'))]

    def get_templates_dirs(self):
        from pkg_resources import resource_filename
        return [resource_filename(__name__, 'templates')]

