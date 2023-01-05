import json
import re

json_data = input()

json_data_dict = json.loads(json_data)

errors_count = {"bus_id": 0, "stop_id": 0, "stop_name": 0, "next_stop": 0, "stop_type": 0, "a_time": 0}

for item in json_data_dict:
    for key, value in item.items():
        if key == "bus_id":
            if not isinstance(value, int) or not value:
                errors_count["bus_id"] += 1
        if key == "stop_id":
            if not isinstance(value, int) or not value:
                errors_count["stop_id"] += 1
        if key == "stop_name":
            if not isinstance(value, str) or not value:
                errors_count["stop_name"] += 1
                continue
            if not re.fullmatch(r"([A-Z]\w+ )+(Avenue|Road|Boulevard|Street)", value):
                errors_count["stop_name"] += 1
        if key == "next_stop":
            if not isinstance(value, int):
                errors_count["next_stop"] += 1
        if key == "stop_type":
            if value:
                if len(str(value)) > 1:
                    errors_count["stop_type"] += 1
                    continue
                if not isinstance(value, str):
                    errors_count["stop_type"] += 1
                    continue
                if value not in ["S", "O", "F"]:
                    errors_count["stop_type"] += 1
        if key == "a_time":
            if not isinstance(value, str) or not value:
                errors_count["a_time"] += 1
                continue
            if not re.fullmatch(r"[0-2]\d:[0-6]\d", value):
                errors_count["a_time"] += 1


print("Type and required field validation:", sum(errors_count.values()), "errors")
for key, value in errors_count.items():
    if key == "a_time" or key == "stop_name" or key == "stop_type":
        print(f"{key}: {value}")
