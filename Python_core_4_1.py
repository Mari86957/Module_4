from pathlib import Path

fh = open('path.txt', 'w', encoding='utf-8')
fh.write("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000")
fh.close()

def total_salary(path):
    try:
        total = 0
        count = 0
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                name, salary = line.strip().split(',')
                total += float(salary)
                count += 1
        average = total / count 
        return total, average
    except ValueError:  
        return ()
    except FileNotFoundError:
        return ()

total, average = total_salary("path.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
