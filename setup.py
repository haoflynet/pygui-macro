import platform

from setuptools import setup, find_packages

VERSION = '0.1.1'

requires = ['six', 'pynput']

system = platform.system()
if system == 'Darwin':
    requires.append('pyobjc-framework-Quartz')

setup(
    name='pygui-macro',
    version=VERSION,
    description='Cross-platform gui macro command tool with python, automate your keyboard and mouse.',
    long_description='Cross-platform gui macro command tool with python, automate your keyboard and mouse. You can use it to record keyboard and mouse action, and rerun it as a script.',
    keywords='gui macro automate keyboard mouse',
    author='haoflynet',
    author_email='haoflynet@gmail.com',
    maintainer='haoflynet',
    maintainer_email='haoflynet',
    url='https://github.com/haoflynet/pygui-macro',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=requires,
    entry_points={
        'console_script': [
            'pygui-macro=pygui_macro.pygui_macro:main'
        ]
    }
)