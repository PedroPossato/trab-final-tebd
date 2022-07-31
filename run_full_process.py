from json_to_turle import json_to_turtle
from final_transformation import final_transformation

try:
    print("Starting JSON to Turtle conversion...")
    success = json_to_turtle()

    if success:
        print("Turtle file generated!")
        print("Starting final transformation...")
        final_transformation()

        print("Done!")

    else:
        raise "JSON to Turtle conversion failed"

except Exception as e:
    raise e