import os
from setuptools   import setup, find_packages
from pip.req      import parse_requirements
from pip.download import PipSession


# import the data inside {{PackageName}}/info.py file, without trigger the
#  importing of the whole package.
#  equivalent to the python2 execfile routine.
INFO_FILE = '{{PackageName}}/info.py'
with open(INFO_FILE) as fd:
    code = compile(fd.read(), INFO_FILE, 'exec')
    local_vars = {}
    exec(code, {}, local_vars)
    __pkg_name__ = local_vars['__pkg_name__']
    __version__ = local_vars['__version__']


def path_to(filename):
    """access to the file at the package top level (like README)"""
    return os.path.join(os.path.dirname(__file__), filename)


# collect requirements needed by setup in dedicated files
reqs = [str(ir.req) for ir in parse_requirements(path_to('requirements.txt'),
                                                 session=PipSession())]


#########################
# SETUP                 #
#########################
setup(
    name = __pkg_name__,
    version = __version__,
    packages = find_packages(),
    include_package_data = True,  # read the MANIFEST.in file
    install_requires = reqs,

    author = "{{AuthorName}}",
    author_email = "{{AuthorMail}}",
    description = "{{Description}}",
    long_description = open(path_to('README.mkd')).read(),
    keywords = "{{Keywords}}",
    url = "https://github.com/{{AuthorGithubName}}/{{GithubRepository}}",

    classifiers = [
{{ if eq License "GNU GPL v3" }}
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
{{ else if eq License "MIT" }}
        "License :: OSI Approved :: MIT License",
{{ else if eq License "Apache Software License 2.0" }}
        "License :: OSI Approved :: Apache Software License",
{{ else if eq License "Public Domain" }}
        "License :: Public Domain",
{{ else if eq License "WTFPL" }}
        "License :: Public Domain",
{{end}}
{{ if eq PythonVersion "3.x" }}
        "Programming Language :: Python :: 3 :: Only",
{{ else if eq PythonVersion "2.x" }}
        "Programming Language :: Python :: 2 :: Only",
{{ else if eq PythonVersion "both" }}
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
{{ end }}
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Natural Language :: English",
        "Intended Audience :: Science/Research",
    ],
)
