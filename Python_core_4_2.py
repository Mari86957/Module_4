from pathlib import Path

def get_cats_info(path):
    cats_info = []
    try:
        with open("path.txt", "r", encoding='utf-8') as fh:
            for line in fh:
                data = line.strip().split(',')
                my_dict = {
                    "id": data[0], 
                    "name": data[1], 
                    "age": data[2]}
                cats_info.append(my_dict)
        return cats_info
    except ValueError:
        return []
    except FileNotFoundError:
        return []
cats_info = get_cats_info("path.txt")
print(cats_info)
