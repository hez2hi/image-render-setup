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

g_sCmdDesc = "Installs Catharsys workspaces"


####################################################################
def AddArgParseArguments(_xArgParser):
    _xArgParser.add_argument("workspace_name", nargs="?", default=None)
    _xArgParser.add_argument("--path", nargs=1, default=None)
    _xArgParser.add_argument("--force", dest="force", action="store_true", default=False)
    _xArgParser.add_argument("--list", dest="do_list", action="store_true", default=False)


# enddef


####################################################################
def RunCmd(_argsCmd, _lArgs):
    from . import install_workspace_impl as impl
    from catharsys.setup import args

    argsSubCmd = args.ParseCmdArgs(_argsCmd=_argsCmd, _lArgs=_lArgs, _funcAddArgs=AddArgParseArguments)

    if argsSubCmd.path is not None:
        sPathTrg = argsSubCmd.path[0]
    else:
        sPathTrg = None
    # endif

    impl.Run(
        sWsName=argsSubCmd.workspace_name,
        sPathTrg=sPathTrg,
        bForce=argsSubCmd.force,
        bDoList=argsSubCmd.do_list,
    )


# enddef
