# Copyright (c) 2023 kk
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

# https://regex101.com/
# https://docs.opsdroid.dev/en/v0.16.0/matchers/regex/

from opsdroid.skill import Skill
from opsdroid.matchers import match_regex  # , match_parse
from .lib.ChatOpsJenkinsLib import ChatOpsJenkinsLib
import time


class ChatOpsJenkinsSkill(Skill):
    @match_regex(r"jenkins help")
    async def jenkins_help(self, message):
        res_str = """
            # Example
            jenkins xxxx main test xxx deploy 
        """
        await message.respond(res_str)

    @match_regex(
        "^jenkins (?P<job_name>\w+\.\w+\.\w+) (?P<app_git_tag>\w+) (?P<app_env>\w+) (?P<app_name>\w+) deploy$"
    )
    async def jenkins_deploy(self, message):
        val = "jenkinsDeploy"

        await message.respond(val)
