from bson import ObjectId
from pydantic_core import core_schema


class PyObjectId(str):
    """
    Custom type jo MongoDB ke ObjectId ko Pydantic v2 ke saath
    compatible banata hai — validation aur JSON serialization dono ke liye.
    """

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type, handler):
        return core_schema.union_schema([
            core_schema.is_instance_schema(ObjectId),
            core_schema.chain_schema([
                core_schema.str_schema(),
                core_schema.no_info_plain_validator_function(cls.validate),
            ]),
        ], serialization=core_schema.to_string_ser_schema())

    @classmethod
    def validate(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid ObjectId")
        return ObjectId(value)