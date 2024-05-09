from pydantic import BaseModel
from typing import List


class ReggressionInput(BaseModel):
    x_values: List[int]
