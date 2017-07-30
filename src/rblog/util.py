import sys
import settings
import os

sys.path.append(settings.WEB_PY_PATH);


import web


renderV = None

### Templates
t_globals = {
    'datestr': web.datestr
}


def render():
    global  renderV
    if renderV is None:
        renderV = web.template.render(os.path.dirname(__file__) + '/../templates', base='base', globals=t_globals)
    return renderV

