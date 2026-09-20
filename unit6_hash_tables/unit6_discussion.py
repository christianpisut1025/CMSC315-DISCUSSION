"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    # A Python dictionary behaves like a hash table: each device ID is hashed
    # to an internal location that stores the device's associated information.
    # Unique device IDs are keys, and each value is a nested dictionary that
    # records the device type, location, and operational status.
    network_devices = {}


    print("\n=== INSERT OPERATIONS ===")
    network_devices["RTR-101"] = {
        "type": "Router", "location": "Headquarters", "status": "Online"
    }
    network_devices["SW-205"] = {
        "type": "Switch", "location": "Operations", "status": "Online"
    }
    network_devices["AP-310"] = {
        "type": "Wireless AP", "location": "Barracks", "status": "Online"
    }
    network_devices["FW-115"] = {
        "type": "Firewall", "location": "Server Room", "status": "Online"
    }
    network_devices["SAT-420"] = {
        "type": "SATCOM Terminal", "location": "Field Site", "status": "Standby"
    }

    print("Added five network devices by unique device ID:")
    for device_id, details in network_devices.items():
        print(f"  {device_id}: {details}")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    # Dictionary lookup uses the hashed key to find a value in average O(1)
    # time instead of scanning every device record one by one.
    router = network_devices["RTR-101"]
    terminal = network_devices["SAT-420"]
    print(f"RTR-101 lookup result: {router}")
    print(f"SAT-420 lookup result: {terminal}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print(f"Before update - SAT-420: {network_devices['SAT-420']}")
    # Assigning a new value to an existing key updates that record rather than
    # creating a duplicate device ID.
    network_devices["SAT-420"] = {
        "type": "SATCOM Terminal", "location": "Field Site", "status": "Online"
    }
    print(f"After update  - SAT-420: {network_devices['SAT-420']}")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print(f"Before deletion: {list(network_devices.keys())}")
    # pop() removes the key and its associated value from the dictionary.
    removed_device = network_devices.pop("AP-310")
    print(f"Removed AP-310 record: {removed_device}")
    print(f"After deletion:  {list(network_devices.keys())}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    # Edge case 1: get() safely returns a default value for a missing key.
    missing_lookup = network_devices.get("RTR-999", "Device not found")
    print(f"Missing lookup for RTR-999: {missing_lookup}")

    # Edge case 2: pop() with a default value avoids a KeyError when deleting
    # a device ID that is not present.
    missing_delete = network_devices.pop("SW-999", None)
    if missing_delete is None:
        print("Safe deletion for SW-999: no device removed; inventory unchanged.")

    # Edge case 3: assigning a missing key inserts a new record. The explicit
    # membership check makes this behavior clear before the insertion occurs.
    new_device_id = "UPS-510"
    if new_device_id not in network_devices:
        print(f"{new_device_id} was missing, so a new device record will be created.")
        network_devices[new_device_id] = {
            "type": "UPS", "location": "Server Room", "status": "Online"
        }
    print(f"New record for {new_device_id}: {network_devices[new_device_id]}")

    # Edge case 4: an empty dictionary contains no keys, so get() returns the
    # supplied default rather than raising an exception.
    empty_inventory = {}
    print(
        "Empty inventory lookup: "
        + empty_inventory.get("ANY-001", "No devices are currently stored")
    )

    print("\n=== FINAL NETWORK DEVICE INVENTORY ===")
    for device_id, details in network_devices.items():
        print(f"  {device_id}: {details}")



if __name__ == "__main__":
    main()
