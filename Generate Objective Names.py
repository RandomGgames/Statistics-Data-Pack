import json

input_data_ids_file = "IDs.txt"
file_to_export_data_to = "Names.txt"
abbreviations = [
		["Absorbed", "Abs"],
		["Amethyst", "Amthst"],
		["Attached", "Atchd"],
		["Azalea", "Azla"],
		["BannerPattern", "BnrPatn"],
		["Blackstone", "Blst"],
		["Blocked", "Bkd"],
		["Blue", "Blu"],
		["Brain", "Brn"],
		["Brick", "Brk"],
		["Bricks", "Brks"],
		["Brown", "Brn"],
		["Bubble", "Bbl"],
		["Bucket", "Bkt"],
		["Bush", "Bsh"],
		["Candle", "Cndl"],
		["Cartography", "Ctgrphy"],
		["Cauldron", "Cldron"],
		["Chainmail", "Chnml"],
		["Chestplate", "Chstplte"],
		["Chiseled", "Czd"],
		["Cobbled", "Cbld"],
		["Cobblestone", "Cblstn"],
		["CommandBlock", "Cmd"],
		["Concrete", "Ccrt"],
		["Copper", "Cpr"],
		["Coral", "Crl"],
		["Cracked", "Ckd"],
		["Creeper", "Crpr"],
		["Crimson", "Crms"],
		["Cut", "Ct"],
		["Damage", "Dmg"],
		["DarkOak", "DkOak"],
		["Dead", "Ded"],
		["Deepslate", "Dpsl"],
		["Detector", "Dtctr"],
		["Diamond", "Dmnd"],
		["Dripstone", "Drpstn"],
		["Enchanted", "Ench"],
		["Experience", "Exp"],
		["Exposed", "Ex"],
		["Fan", "Fn"],
		["Fermented", "Frmtd"],
		["Flowering", "Flwr"],
		["Froglight", "FrgLte"],
		["Fruit", "Frt"],
		["Glass", "Gls"],
		["Glistering", "Glstn"],
		["Golden", "Gldn"],
		["Gray", "Gry"],
		["Heavy", "Hvy"],
		["Infested", "Insd"],
		["Inspect", "Open"],
		["InteractWith", "Opn"],
		["Leather", "Lthr"],
		["Light", "Lte"],
		["LilyOfTheValley", "LlyOfTheVly"],
		["Magenta", "Mgt"],
		["Mangrove", "Mgrv"],
		["Melon", "Mln"],
		["Minecart", "Mcrt"],
		["Mossy", "Msy"],
		["Mushroom", "Mush"],
		["MusicDisc", "MscDsc"],
		["Netherite", "Ntrite"],
		["OnAStick", "OnStik"],
		["One", "1"],
		["Oxidized", "Ox"],
		["Pane", "Pne"],
		["Pearlescent", "Prlcnt"],
		["Plate", "Plt"],
		["Polished", "Psd"],
		["Popped", "Ppd"],
		["Potted", "Ptd"],
		["Powder", "Pwdr"],
		["Pressure", "Psr"],
		["Prismarine", "Prsmrn"],
		["Pumpkin", "Pmpkn"],
		["Redstone", "Rdst"],
		["Resisted", "Res"],
		["Sandstone", "SStn"],
		["Sapling", "Splng"],
		["ShulkerBox", "ShlkrBx"],
		["Skeleton", "Sklt"],
		["Skull", "Skl"],
		["Slab", "Slb"],
		["Smooth", "Smth"],
		["SpawnEgg", "SE"],
		["Spider", "Spdr"],
		["Stained", "St"],
		["Stairs", "Str"],
		["Stone", "Stn"],
		["Stripped", "Stpd"],
		["Table", "Tbl"],
		["Terracotta", "Tca"],
		["Trapped", "Trapd"],
		["Trigger", "Trigr"],
		["Twisting", "Twstg"],
		["Under", "Undr"],
		["Villager", "Vlgr"],
		["Wall", "Wal"],
		["Wandering", "Wndrng"],
		["Warped", "Wpd"],
		["Water", "Watr"],
		["Waxed", "Wxd"],
		["Weathered", "Wrd"],
		["Weeping", "Weep"],
		["Weighted", "Wgtd"],
		["Wither", "Wthr"],
		["Yellow", "Ylw"],
		["Zombified", "Zmbif"],
	]


with open(input_data_ids_file, "r") as f: Names = f.read()
Names = Names.split("\n")

for i, name in enumerate(Names):
	"""
	Turn IDs to Names
	"""
	name = name.replace("_", " ")
	name = name.title()
	name = name.replace(" ", "")
	for abbreviation in abbreviations:
		name = name.replace(abbreviation[0], abbreviation[1])
	Names[i] = name

if any(name for name in Names if len(name) > 15):
	"""
	Warn about names being too long
	"""
	print("[WARN] Found errors with the following values")
	for name in Names:
		if len(name) > 15:
			print(name)

else:
	"""
	Print to file
	"""
	print(f"[INFO] Exported data to {file_to_export_data_to}")
	with open(file_to_export_data_to, 'w') as f: f.write('\n'.join(Names))
