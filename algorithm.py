#!/usr/bin/python3
import itertools
import random, json

def create_package(items, budget):
   
    items.sort(key=lambda x: x['price'])
    
    package = []
    total_price = 0

    for item in items:
        if total_price + item['price'] <= budget:
            package.append(item)
            total_price += item['price']
    
    
    if len(package) == 0:
        return {
            "total_price": 0,
            "package": [],
            "message": "Can't create package!"
        }
    
    if len(package) == 1:
        return {
            "total_price": 0,
            "package": [],
            "message": "Can't create package!"
        }
    
    remaining_budget = budget - total_price
    return {
        "total_price": total_price,
        "package": package,
        "remaining_budget": remaining_budget
    }

def add_additional_items(package, items, remaining_budget):
   
    for item in sorted(items, key=lambda x: x['price']):
        if item not in package and item['price'] <= remaining_budget:
            package.append(item)
            remaining_budget -= item['price']
            if remaining_budget <= 0:
                break
    return package, remaining_budget

def create_multiple_packages(item_collection, budget, priorities, num_packages=3):
    
    prioritized_items = [item for item in item_collection if any(priority.lower() in item['name'].lower() for priority in priorities)]
    
    
    not_affordable = [priority for priority in priorities if all(item['price'] > budget for item in prioritized_items)]
    
    packages = []
    
    
    initial_package = create_package(prioritized_items, budget)
    
    if initial_package["total_price"] > 0:
        
        updated_package, remaining_budget = add_additional_items(initial_package["package"], item_collection, initial_package["remaining_budget"])
        
        packages.append({
            "total_price": sum(item['price'] for item in updated_package),
            "package": updated_package,
            "remaining_budget": remaining_budget,
            "message": f"Remaining budget: ${remaining_budget:.2f}" if remaining_budget > 0 else "No remaining budget."
        })
    else:
        packages.append({
            "total_price": 0,
            "package": [],
            "message": f"Can't afford prioritized items: {', '.join(not_affordable)} or Cant create a package with your prefered items"
        })
    
    all_combinations = []
    
    
    for r in range(2, len(item_collection) + 1):
        all_combinations.extend(itertools.combinations(item_collection, r))
    
    
    selected_combinations = random.sample(all_combinations, min(num_packages - 1, len(all_combinations)))

    for combination in selected_combinations:
        initial_package = create_package(list(combination), budget)
        
        if initial_package["total_price"] > 0:
            
            updated_package, remaining_budget = add_additional_items(initial_package["package"], item_collection, initial_package["remaining_budget"])
            packages.append({
                "total_price": sum(item['price'] for item in updated_package),
                "package": updated_package,
                "remaining_budget": remaining_budget,
                "message": f"Remaining budget: ${remaining_budget:.2f}" if remaining_budget > 0 else "No remaining budget."
            })
        else:
            packages.append({
                "total_price": 0,
                "package": [],
                "message": "Can't create package!"
            })

    return packages


item_collection = [
    {"name": "Luxury Bed", "price": 999.99},
    {"name": "Sofa Bed", "price": 599.99},
    {"name": "Mirror", "price": 59.99},
    {"name": "Desk", "price": 149.99},
    {"name": "Rug", "price": 199.99},
    {"name": "Dining Table", "price": 299.99},
    {"name": "Dining Chairs", "price": 79.99},
    {"name": "Armchair", "price": 199.99},
    {"name": "Lamp", "price": 49.99},
    {"name": "Picture Frame", "price": 19.99},
]


budget = float(input("Enter your budget: "))
priorities = input("Enter your priority items (comma-separated): ").split(",")


result_packages = create_multiple_packages(item_collection, budget, priorities)
for idx, package in enumerate(result_packages, start=1):
    print(f"Package {idx}:")
    print(json.dumps(package, indent=4))
    print()
