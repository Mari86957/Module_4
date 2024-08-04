from pathlib import Path

def get_cats_info(cats):
    cats_info = []
    try:
        with open(cats, "r", encoding='utf-8') as fh:
            for line in fh:
                data = line.strip().split(',')
                if len(data) == 3:
                    my_dict = {
                        "id": data[0], 
                        "name": data[1], 
                        "age": data[2]
                        }
                    cats_info.append(my_dict)
                else:
                    print("buu")
        return cats_info
    except ValueError:
        return []
    except FileNotFoundError:
        return []
cats_info = get_cats_info("./Module_4/cats.txt")
print(cats_info)
