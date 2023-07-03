from pydantic import BaseModel, validator
from typing import Optional, List

class Contents(BaseModel):
    key: str
    value: str

class ProductSpecs(BaseModel):
    product_specification: Optional[List[Contents]]

    @validator('product_specification', pre=True)
    def specs_check(cls, v):
        """
        pop out and ensure all dictionary going inside the function has the content attribute
        otherwise we discard them to reduce unwanted errors.
        """
        specs_attr = [i for i in Contents.__fields__.keys()]
        specs_attr_count = 0

        for i, x in enumerate(v):
            for k in dict(x).keys():
                if k in specs_attr:
                    specs_attr_count += 1
            if specs_attr_count != len(specs_attr):
                v.pop(i)
            specs_attr_count = 0
        return v

class Environment(BaseModel):
    log_level: str
    master: str
    source_file: str
    app_name: str

