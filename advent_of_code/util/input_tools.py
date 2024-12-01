AOC_TOKEN = '53616c7465645f5f68a7ad38ddc91ce363d0c8107a5ceb9c543568bb03cffd622f17f14f8adb170b38cc6cf57be6decb00ab5ec1c81fbd491fe295b8e0affad9'

def get_input_rows(filename = "input.txt"):
    with open('input.txt') as input:
        rows = [x for x in input.read().strip().split("\n")]
        input.close()
        
    return rows
