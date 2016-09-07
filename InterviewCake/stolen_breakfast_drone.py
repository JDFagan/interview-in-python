# O(n) time and O(u) space where u is max amount of unique deliveries in progress
def find_missing_drones(delivery_id_confirmations: []):
    unique_delivery_ids = set()
    for id in delivery_id_confirmations:
        if id in unique_delivery_ids:
            unique_delivery_ids.remove(id)
        else:
            unique_delivery_ids.add(id)

    return unique_delivery_ids
