# Copyright (c) 2023 kk
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from opsdroid.skill import Skill
from opsdroid.matchers import match_regex


class ChatOpsHelperSkill(Skill):
    @match_regex(r"help")
    async def chatops_help(self, message):
        res_str = f"""
          chatops_help information about
        """
        await message.respond(res_str)
