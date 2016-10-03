# Written by Sergey Melykov
# Copyright (c) 2016 Sergey Melykov
# License: MIT
# Ported to CudaText: Alexey T.

from cuda_lint import Linter, util


class CssTree(Linter):
    """Provides an interface to csstree validator."""

    syntax = 'CSS'
    cmd = 'csstree-validator @ --reporter checkstyle'    
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.0'
    regex = r'''(?mix)
        line="(?P<line>\d+)".+column="(?P<col>\d+)".+message="(?P<message>[\s\S]+?)(?<!\\)"
    '''
    multiline = True
    error_stream = util.STREAM_BOTH
    tempfile_suffix = 'css'
