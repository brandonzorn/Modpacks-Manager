import os.path


def save_version(mod, version, content):
    if not os.path.exists(f'ModrinthManagerData/{mod.get_name()}'):
        os.makedirs(f'ModrinthManagerData/{mod.get_name()}')
    with open(f'ModrinthManagerData/{mod.get_name()}/{version.name}.jar', 'wb') as ver:
        ver.write(content)
