import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': ['atexit', 'os'],
        'packages': ['openpyxl', 'os'],
        'path': sys.path + ['src'],
        'include_files': 'src\\cullen3logo.png'
    }
}

executables = [Executable('Cullen-DMU.py',
                          base=base,
                          icon="icon.ico")]

setup(name='Cullen DMU',
      version='0.1',
      description="Cullen DMU",
      url='jfitzpatrick.me',
      author='Jim Fitzpatrick',
      author_email='jimfity@gmail.com',
      options=options,
      executables=executables)
