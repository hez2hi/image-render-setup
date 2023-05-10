#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: \install.py
# Created Date: Wednesday, April 27th 2022, 2:18:33 pm
# Author: Christian Perwass (CR/AEC5)
# <LICENSE id="Apache-2.0">
#
#   Image-Render Setup module
#   Copyright 2022 Robert Bosch GmbH and its subsidiaries
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# </LICENSE>
###


g_sCmdDesc = "Builds Catharsys setup"


####################################################################
def AddArgParseArguments(_parseArgs):
    _parseArgs.add_argument("-p", "--path", dest="path", nargs=1, default=None)


# enddef


####################################################################
def RunCmd(_argsCmd, _lArgs):
    from anybase import path
    from .build_modules_impl import RunBuildSetup
    from catharsys.setup import args

    argsSubCmd = args.ParseCmdArgs(_argsCmd=_argsCmd, _lArgs=_lArgs, _funcAddArgs=AddArgParseArguments)

    if argsSubCmd.path is None:
        pathSetup = None
    else:
        pathSetup = path.MakeNormPath(argsSubCmd.path)
        if not pathSetup.is_absolute():
            pathSetup = pathSetup.absolute()
        # endif
    # endif

    RunBuildSetup(pathSetup=pathSetup)


# enddef

