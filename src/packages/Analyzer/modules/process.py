from packages.Analyzer.modules.id import id_list

# Returns the corresponding name for the iD given
def id(id: int) -> str:
    for item in id_list:
        if id == item[0]:
            return item[1]
        else:
            return 'Invalid ID'
        
# Converts binary values into 'Yes' and 'No"
def binary(num: int) -> str:
    if num == 0:
        return 'No'
    if num == 1:
        return 'Yes'

# Process defense data into strictly numbers
def defense(defense):
    match defense:
        case '1 (Terrible)':
            return 1
        case '5 (Amazing)':
            return 5
        case 'N/A':
            return defense
        case _:
            return int(defense)