ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# len evaluates to number of key_value entries
print(len(ice_cream))

# add key_value entries using subscription notation
ice_cream["mint"] = 10

# access values by their key using subscription
mint_orders: int = ice_cream["mint"]
print(mint_orders)

# re-assign values by their key using assignment
ice_cream["mint"] += 1

# remove items by key using the pop method
ice_cream.pop("strawberry")

# test if a key is in the dictionary
print("strawberry" in ice_cream)

for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor}: {tally}")

print(ice_cream["strawberry"])
