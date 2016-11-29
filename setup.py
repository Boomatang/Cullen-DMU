import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': 'atexit',
        'path': sys.path + ['src']
    }
}

executables = [Executable('runner.py', base=base)]

setup(name='Cullen DMU',
      version='0.1',
      description="Cullen DMU",
      options=options,
      executables=executables)
