from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']
    state = i['state']
    pm = env.get('CM_HOST_OS_PACKAGE_MANAGER')
    if not pm:
        return {'return': 1, 'error': 'Package manager not detected for the given OS'}
    util = env.get('CM_SYS_UTIL_NAME')
    if not util:
        return {'return': 1, 'error': 'Please select a variation specifying the sys util name'}
    package = state.get(util)
    if not package:
        return {'return': 1, 'error': 'No package name specified for {} and util name {}'.format(pm, util)}
    package_name = package.get(pm)
    if not package_name:
        return {'return': 1, 'error': 'No package name specified for {} and util name {}'.format(pm, util)}
    install_cmd = env.get('CM_HOST_OS_PACKAGE_MANAGER_INSTALL_CMD')
    if not install_cmd:
        return {'return': 1, 'error': 'Package manager installation command not detected for the given OS'}
    env['CM_SYS_UTIL_INSTALL_CMD'] = env.get('CM_SUDO', '') + ' ' +install_cmd + ' ' + package_name


    return {'return':0}
