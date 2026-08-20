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
]

private_build_requires = [
    "visual_studio",
]

variants = [
    # ["maya-2025"],
    ["maya-2026"],
]

def commands():
    env.REZ_CVWRAP_ROOT = '{root}'
    env.PATH.prepend('{root}/plug-ins')
    env.PYTHONPATH.prepend('{root}/scripts')
    env.MAYA_MODULE_PATH.prepend('{root}')


uuid = 'repository.cvwrap'
