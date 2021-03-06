import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup

setup(
  name='anti-rsi',
  version='0.0.1dev',
  url="https://github.com/hasantayyar/anti-rsi",
  entry_points={
  'console_scripts': [
      'antirsi = rsi.mainmodule:main'
    ]
  },
  extras_require = {'notification':  ["pynotify"]},
  test_suite='rsi.test',
  packages=['rsi'],
  package_data={
    'icons': [
        'static/img/warning.png'
    ]
  },
  license='Creative Commons Attribution-Noncommercial-Share Alike license',
  long_description=open('README.md').read(),
)
