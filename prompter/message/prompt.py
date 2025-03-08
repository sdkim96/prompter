import string
from typing import List
from pydantic import BaseModel

from prompter._types import FormattedPrompt
from prompter.utils.annotations import dev_log

import logging
logging.basicConfig(level=logging.INFO)


class RawPrompt(BaseModel):
    system: str
    user: str

    def placeholders(self) -> dict[str, List[str]]:
        """ Returns the placeholders in the system and user prompts """
        
        seen_vars = set()
        system_var_it = (
            string.
            Formatter()
            .parse(self.system)
        )
        system_placholders = []
        for _, var, _, _ in system_var_it:
            if var:
                if var in seen_vars:
                    raise ValueError(f"Placeholder **{var}** is duplicated")
                system_placholders.append(var)
                seen_vars.add(var)

        user_var_it = (
            string.
            Formatter()
            .parse(self.user)
        )
        user_placholders = []
        for _, var, _, _ in user_var_it:
            if var:
                if var in seen_vars:
                    raise ValueError(f"Placeholder **{var}** is duplicated")
                user_placholders.append(var)
                seen_vars.add(var)

        return {
            "system": system_placholders,
            "user": user_placholders
        }
    
    def format_placeholders(self, **kwargs) -> FormattedPrompt:

        formatted_system= self.system
        formatted_user = self.user
        
        placeholders = self.placeholders()
        for key, value in placeholders.items():
            for var in value:
                try:
                    if key == "system":
                        formatted_system = self.system.format(**kwargs)
                    elif key == "user":
                        formatted_user = self.user.format(**kwargs)
                except KeyError as e:
                    logging.error(f"KeyError: {e}")
                    raise KeyError(f"Placeholder **{e}** is unparameterized")
        
        return FormattedPrompt(system=formatted_system, user=formatted_user)
