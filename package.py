name = 'cvwrap'

version = '1.0.0.hh.1.0.0'

authors = [
    'Chad V.',
]

description = '''Maya plugin for rigging'''

with scope('config') as c:
    import os
    c.release_packages_path = os.environ['HH_REZ_REPO_RELEASE_EXT']
    c.plugins.release_hook.hh_emailer.recipients = []

requires = [
    "maya",
]

private_build_requires = [
]

variants = [
]

def commands():
    env.REZ_CVWRAP_ROOT = '{root}'
    env.LD_LIBRARY_PATH.prepend('{root}/plug-ins')
    env.PYTHONPATH.prepend('{root}/scripts')


uuid = 'repository.cvwrap'
