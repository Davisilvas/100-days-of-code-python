"""
    Nested Dictionaries and Lists.
"""

users_log = {
    "Maria": {
        "Name": "Maria Eduarda Loyola Xavier",
        "Age": 25,
    },
    "Davi": {
        "Name": "Davi Silva Santos",
        "Age": 22
    }
}

users_log =[
    {
        "Maria": {
                "Name": "Maria Eduarda Loyola Xavier",
                "Age": 25,
        }
    },
    {
        "Davi": {
            "Name": "Davi Silva Santos",
            "Age": 22
        }
    },
]
"""
    -> The advantage of having a list of dictionay is that this way is easier to iterate through it,
    and easier to add items.
"""