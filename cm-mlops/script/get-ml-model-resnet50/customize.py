from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    automation = i['automation']

    cm = automation.cmind

    path = os.getcwd()

    url = env['CM_PACKAGE_URL']
    if 'CM_ML_MODEL_STARTING_WEIGHTS_FILENAME' not in env:
        env['CM_ML_MODEL_STARTING_WEIGHTS_FILENAME'] = url

    print ('Downloading from {}'.format(url))

    r = cm.access({'action':'download_file',
                'automation':'utils,dc2743f8450541e3',
                'url':url})
    if r['return']>0: return r

    filename = r['filename']

    if env.get('CM_UNZIP') == "yes":
        os.system("gzip -d "+filename)
        filename = env['CM_ML_MODEL_FILE']
        env['CM_ML_MODEL_FILE_WITH_PATH']=os.path.join(path, filename)
    else:
        env['CM_ML_MODEL_FILE'] = filename
        env['CM_ML_MODEL_FILE_WITH_PATH']=r['path']

    # Add to path
    env['CM_ML_MODEL_PATH']=path

    return {'return':0}
