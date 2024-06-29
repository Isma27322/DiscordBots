fixed = []
with open('redpandafacts.txt', 'r') as file:
    lines = file.readlines()
    i = 1
    for line in lines:
        remove1 = line.strip()
        remove2 = remove1.strip("\\")
        remove3 = remove2.strip(f"{i}.")
        remove4 = remove3.replace("**", "")
        remove5 = remove4.strip(" ")
        fixed.append(remove5)
        i += 1
        
with open('redpandafacts_fixed.txt', 'w') as fixed_facts:
    for facts in fixed:
        fixed_facts.write(f"{facts}\n")