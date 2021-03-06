from django.conf import settings

from core.external.utils import get_third_party_js, get_third_party_css


def _get_sql_queries():
    if settings.SQL_DEBUG:
        from django.db import connections
        sql_queries = connections['default'].queries + connections['pdns'].queries
    else:
        sql_queries = []

    return sql_queries


def _get_debug_settings():
    return {
        'debug': settings.DEBUG,
        'template': settings.TEMPLATE_DEBUG,
        'javascript': settings.JAVASCRIPT_DEBUG,
        'sql': settings.SQL_DEBUG,
        'sql_queries': _get_sql_queries(),
    }


def print_sql_debug():
    sql_queries = _get_sql_queries()

    if sql_queries:
        print('---------- SQLDEBUG ----------')
        for i, q in enumerate(sql_queries, start=1):
            print('%02d. [%s] %s\n' % (i, q['time'], q['sql']))
        print('---------- SQLDEBUG ----------')


# noinspection PyUnusedLocal
def common_stuff(request):
    """
    Make common settings and variables available in templates.
    """
    from core.version import __version__, __edition__
    from gui.node.utils import get_dc1_settings
    from api.system.update.api_views import UpdateView

    return {
        'settings': settings,
        'dc_settings': request.dc.settings,
        'dc1_settings': get_dc1_settings(request),
        'ANALYTICS': None if request.user.is_authenticated() else settings.ANALYTICS,
        'DEBUG': _get_debug_settings(),
        'SOCKETIO_URL': settings.SOCKETIO_URL,
        'THIRD_PARTY_JS': get_third_party_js(),
        'THIRD_PARTY_CSS': get_third_party_css(),
        'SYSTEM_UPDATE_RUNNING': UpdateView.is_task_running(),
        'SYSTEM_VERSION': __version__,
        'SYSTEM_EDITION': __edition__
    }
