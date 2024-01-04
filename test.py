def min_bags(N):
    for five_kg_bags in range(N // 5, -1, -1):
        remaining_weight = N - (five_kg_bags * 5)

        if remaining_weight % 3 == 0:
            three_kg_bags = remaining_weight // 3
            
            return five_kg_bags + three_kg_bags
        
    return -1

print(min_bags(int(input())))