import json

def check(res):
    """Check a result from `requests` for error information."""
    if res and res['meta']['code'] == 200:  # 200 OK
        return True

    print('ERROR in request:')
    err = res['meta']
    for key in err:
        print('\t{}: {}'.format(key, err[key]))
    return False

def pprint(json_):
    """Pretty print a JSON object."""
    print(json.dumps(json_, indent=4))
