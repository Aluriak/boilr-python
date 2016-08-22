"""{{PackageName}} entry point.

{{ if UseDocopt }}
usage: {{PackageName}} [options]

options:
    --help, -h      print this message
    --version, -v   print the version

{{ end }}
"""


from {{PackageName}} import info

{{ if UseDocopt }}
import docopt

{{ end }}
{{ if UseStdlib }}
import itertools
import functools
import collections

{{ end }}

if __name__ == "__main__":
{{ if UseDocopt }}
    args = docopt.docopt(__doc__, version=info.__version__)
    print(args)
{{ else }}
    pass
{{ end }}
