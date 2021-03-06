from flask_sqlalchemy import get_debug_queries

from src.app import log


def sql_debug(response):
    queries = list(get_debug_queries())
    query_str = ''
    total_duration = 0.0
    for q in queries:
        total_duration += q.duration
        stmt = str(q.statement % q.parameters).replace('\n', '\n       ')
        query_str += 'Query: {0}\nDuration: {1}ms\n\n'.format(stmt, round(q.duration * 1000, 2))

    log.debug('=' * 80 + '\n')
    log.debug(' SQL Queries - {0} Queries Executed in {1}ms'.format(len(queries), round(total_duration * 1000, 2)))
    log.debug('=' * 80)
    log.debug(query_str.rstrip('\n'))
    log.debug('=' * 80 + '\n')

    return response
