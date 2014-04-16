def file_to_string(file_name):
    f = open(file_name)
    groups = []
    temp_group = []
    for line in f:
        new_item = line.strip()
        if len(new_item)>0:
            temp_group.append(new_item)
        else:
            groups.append(temp_group)
            temp_group = []
    return groups
            
