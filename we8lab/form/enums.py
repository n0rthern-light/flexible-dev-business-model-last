from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        choices = list()

        # Loop thru defined enums
        for item in cls:
            choices.append((item.value, item.name))

        # return as tuple
        return tuple(choices)

    def __str__(self):
        return self.name

    def __int__(self):
        return self.value


class EnumFormInstanceState(ChoiceEnum):
    FORM_STATE_PENDING_ADMIN = 1
    FORM_STATE_PENDING_CLIENT = 2
    FORM_STATE_PENDING_INITIAL_PAYMENT = 3
    FORM_STATE_IN_PROGRESS = 4
    FORM_STATE_DONE = 5


class EnumFormRecordState(ChoiceEnum):
    FORM_RECORD_ACCEPTED_ONLY_CLIENT = 1
    FORM_RECORD_ACCEPTED_ONLY_ADMIN = 2
    FORM_RECORD_ACCEPTED_BOTH = 3


class EnumFormRecordInitUser(ChoiceEnum):
    FORM_CLIENT = 1
    FORM_ADMIN = 2


class EnumInputTypes(ChoiceEnum):
    Text = 1
    Number = 2
    Money = 3
    Email = 4
    Phone = 5
    Date = 6
    Check = 7
    Textarea = 8
    Select = 9
    List = 10