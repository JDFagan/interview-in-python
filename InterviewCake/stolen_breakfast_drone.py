# O(n) time and O(u) space where u is max amount of unique deliveries in progress
def find_missing_drones(delivery_id_confirmations: []):
    unique_delivery_ids = set()
    for id in delivery_id_confirmations:
        if id in unique_delivery_ids:
            unique_delivery_ids.remove(id)
        else:
            unique_delivery_ids.add(id)

    return unique_delivery_ids


# O(n) time and O(1) space but it assumes you'd only have one missing drone, whereas my solution is more generic
# and can find one or more missing drones
def find_missing_drone(delivery_id_confirmations: []):
    unique_delivery_id = 0
    for id in delivery_id_confirmations:
        unique_delivery_id ^= id

    return unique_delivery_id
