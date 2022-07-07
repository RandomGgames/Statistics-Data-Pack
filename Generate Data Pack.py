import json
import os
import shutil

input_stats_file = "Statistics.txt"

if os.path.exists("Statistics"): shutil.rmtree("Statistics")
folders = [
	"Statistics/data/minecraft/tags/functions",
	"Statistics/data/statistics/functions",
	"Statistics/data/disable/functions",
	]
for folder in folders:
	if not os.path.exists(folder):
		os.makedirs(folder)

with open("Statistics/pack.mcmeta", "w") as f: json.dump({"pack": {"pack_format": 10,"description": "RandomGgames' Statistics Data Pack"}}, f, indent = "\t")
with open("Statistics/data/minecraft/tags/functions/load.json", "w") as f: json.dump({"values": ["statistics:load"]}, f, indent = "\t")
with open("Statistics/data/statistics/functions/load.mcfunction", "w") as f: f.write(f"function statistics:create_objectives")
add_objective = open("Statistics/data/statistics/functions/create_objectives.mcfunction", "a")
remove_objective = open("Statistics/data/statistics/functions/remove_objectives.mcfunction", "a")
with open("Statistics/data/disable/functions/statistics.mcfunction", "w") as f: f.write(f"function statistics:remove_objectives\n\ndatapack disable \"file/Statistics\"\ndatapack disable \"file/Statistics.zip\"")

with open(input_stats_file, "r") as f: data = f.read()
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
		"name": object[1],
		"single": object[2],
		"custom": object[3],
		"mined": object[4],
		"broken": object[5],
		"crafted": object[6],
		"used": object[7],
		"picked_up": object[8],
		"dropped": object[9],
		"killed": object[10],
		"killed_by": object[11],
	}

	if object["single"]:
		add_objective.write(f"scoreboard objectives add {object['name']} {object['id']}\n")
		remove_objective.write(f"scoreboard objectives remove {object['name']}\n")

	if object["custom"]:
		add_objective.write(f"scoreboard objectives add {object['name']} minecraft.custom:minecraft.{object['id']}\n")
		remove_objective.write(f"scoreboard objectives remove {object['name']}\n")

	if object["mined"]:
		add_objective.write(f"scoreboard objectives add m{object['name']} minecraft.mined:minecraft.{object['id']}\n")
		remove_objective.write(f"scoreboard objectives remove m{object['name']}\n")

	if object["used"]:
		add_objective.write(f"scoreboard objectives add u{object['name']} minecraft.used:minecraft.{object['id']}\n")
		remove_objective.write(f"scoreboard objectives remove u{object['name']}\n")
	
	if object["crafted"]:
		add_objective.write(f"scoreboard objectives add c{object['name']} minecraft.crafted:minecraft.{object['id']}\n")
		remove_objective.write(f"scoreboard objectives remove c{object['name']}\n")
	
	if object["broken"]:
		add_objective.write(f"scoreboard objectives add b{object['name']} minecraft.broken:minecraft.{object['id']}\n")
		remove_objective.write(f"scoreboard objectives remove b{object['name']}\n")
	
	if object["picked_up"]:
		add_objective.write(f"scoreboard objectives add p{object['name']} minecraft.picked_up:minecraft.{object['id']}\n")
		remove_objective.write(f"scoreboard objectives remove p{object['name']}\n")
	
	if object["dropped"]:
		add_objective.write(f"scoreboard objectives add d{object['name']} minecraft.dropped:minecraft.{object['id']}\n")
		remove_objective.write(f"scoreboard objectives remove d{object['name']}\n")

	if object["killed"]:
		add_objective.write(f"scoreboard objectives add k{object['name']} minecraft.killed:minecraft.{object['id']}\n")
		remove_objective.write(f"scoreboard objectives remove k{object['name']}\n")
		
	if object["killed_by"]:
		add_objective.write(f"scoreboard objectives add x{object['name']} minecraft.killed_by:minecraft.{object['id']}\n")
		remove_objective.write(f"scoreboard objectives remove x{object['name']}\n")
