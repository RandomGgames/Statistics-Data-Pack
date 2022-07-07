import json
import os
import shutil

if os.path.exists("Statistics"): shutil.rmtree("Statistics")

directories = [
	"Statistics/data/minecraft/tags/functions",
	"Statistics/data/statistics/functions",
	"Statistics/data/disable/functions",
	]
for folder in directories:
	if not os.path.exists(folder):
		os.makedirs(folder)

with open("Statistics/pack.mcmeta", "w") as f: json.dump({"pack": {"pack_format": 10,"description": "RandomGgames' Statistics Data Pack"}}, f, indent = "\t")
with open("Statistics/data/minecraft/tags/functions/load.json", "w") as f: json.dump({"values": ["statistics:load"]}, f, indent = "\t")
with open("Statistics/data/statistics/functions/load.mcfunction", "w") as f: f.write(f"function statistics:create_objectives")
add_objective = open("Statistics/data/statistics/functions/create_objectives.mcfunction", "a")
remove_objective = open("Statistics/data/statistics/functions/remove_objectives.mcfunction", "a")
with open("Statistics/data/disable/functions/statistics.mcfunction", "w") as f: f.write(f"function statistics:remove_objectives\n\ndatapack disable \"file/Statistics\"\ndatapack disable \"file/Statistics.zip\"")

with open("Statistics.txt", "r") as f: data = f.read()
data = data.split("\n")
if data[-1] == "": data = data[:-1]

for i, object in enumerate(data):
	object = object.split("\t")
	for y, each in enumerate(object):
		if each == "TRUE":
			object[y] = True
		if each == "FALSE":
			object[y] = False
	
	object = {
		"id": object[0],
		"single": object[1],
		"custom": object[2],
		"mined": object[3],
		"broken": object[4],
		"crafted": object[5],
		"used": object[6],
		"picked_up": object[7],
		"dropped": object[8],
		"killed": object[9],
		"killed_by": object[10],
	}

	if object["single"]:
		add_objective.write(f"scoreboard objectives add {object['id']} {object['id']}\n")
		remove_objective.write(f"scoreboard objectives remove {object['id']}\n")

	if object["custom"]:
		add_objective.write(f"scoreboard objectives add {object['id']} minecraft.custom:minecraft.{object['id']}\n")
		remove_objective.write(f"scoreboard objectives remove {object['id']}\n")

	if object["mined"]:
		add_objective.write(f"scoreboard objectives add mined_minecraft.{object['id']} minecraft.mined:minecraft.{object['id']}\n")
		remove_objective.write(f"scoreboard objectives remove mined_minecraft.{object['id']}\n")

	if object["used"]:
		add_objective.write(f"scoreboard objectives add used_minecraft.{object['id']} minecraft.used:minecraft.{object['id']}\n")
		remove_objective.write(f"scoreboard objectives remove used_minecraft.{object['id']}\n")
	
	if object["crafted"]:
		add_objective.write(f"scoreboard objectives add crafted_minecraft.{object['id']} minecraft.crafted:minecraft.{object['id']}\n")
		remove_objective.write(f"scoreboard objectives remove crafted_minecraft.{object['id']}\n")
	
	if object["broken"]:
		add_objective.write(f"scoreboard objectives add broken_minecraft.{object['id']} minecraft.broken:minecraft.{object['id']}\n")
		remove_objective.write(f"scoreboard objectives remove broken_minecraft.{object['id']}\n")
	
	if object["picked_up"]:
		add_objective.write(f"scoreboard objectives add picked_up_minecraft.{object['id']} minecraft.picked_up:minecraft.{object['id']}\n")
		remove_objective.write(f"scoreboard objectives remove picked_up_minecraft.{object['id']}\n")
	
	if object["dropped"]:
		add_objective.write(f"scoreboard objectives add dropped_minecraft.{object['id']} minecraft.dropped:minecraft.{object['id']}\n")
		remove_objective.write(f"scoreboard objectives remove dropped_minecraft.{object['id']}\n")

	if object["killed"]:
		add_objective.write(f"scoreboard objectives add killed_minecraft.{object['id']} minecraft.killed:minecraft.{object['id']}\n")
		remove_objective.write(f"scoreboard objectives remove killed_minecraft.{object['id']}\n")
		
	if object["killed_by"]:
		add_objective.write(f"scoreboard objectives add killed_by_minecraft.{object['id']} minecraft.killed_by:minecraft.{object['id']}\n")
		remove_objective.write(f"scoreboard objectives remove killed_by_minecraft.{object['id']}\n")
