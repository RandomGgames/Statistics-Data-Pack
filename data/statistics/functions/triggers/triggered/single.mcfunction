execute as @s[scores={tAir=1..}] run scoreboard objectives setdisplay sidebar Air
execute as @s[scores={tAir=..-1}] run scoreboard objectives setdisplay sidebar Air
scoreboard players set @s[scores={tAir=1..}] tAir 0
scoreboard players set @s[scores={tAir=..-1}] tAir 0

execute as @s[scores={tArmor=1..}] run scoreboard objectives setdisplay sidebar Armor
execute as @s[scores={tArmor=..-1}] run scoreboard objectives setdisplay sidebar Armor
scoreboard players set @s[scores={tArmor=1..}] tArmor 0
scoreboard players set @s[scores={tArmor=..-1}] tArmor 0

execute as @s[scores={tDeathCount=1..}] run scoreboard objectives setdisplay sidebar DeathCount
execute as @s[scores={tDeathCount=..-1}] run scoreboard objectives setdisplay sidebar DeathCount
scoreboard players set @s[scores={tDeathCount=1..}] tDeathCount 0
scoreboard players set @s[scores={tDeathCount=..-1}] tDeathCount 0

execute as @s[scores={tFood=1..}] run scoreboard objectives setdisplay sidebar Food
execute as @s[scores={tFood=..-1}] run scoreboard objectives setdisplay sidebar Food
scoreboard players set @s[scores={tFood=1..}] tFood 0
scoreboard players set @s[scores={tFood=..-1}] tFood 0

execute as @s[scores={tHealth=1..}] run scoreboard objectives setdisplay sidebar Health
execute as @s[scores={tHealth=..-1}] run scoreboard objectives setdisplay sidebar Health
scoreboard players set @s[scores={tHealth=1..}] tHealth 0
scoreboard players set @s[scores={tHealth=..-1}] tHealth 0

execute as @s[scores={tLevel=1..}] run scoreboard objectives setdisplay sidebar Level
execute as @s[scores={tLevel=..-1}] run scoreboard objectives setdisplay sidebar Level
scoreboard players set @s[scores={tLevel=1..}] tLevel 0
scoreboard players set @s[scores={tLevel=..-1}] tLevel 0

execute as @s[scores={tPlayerKillCount=1..}] run scoreboard objectives setdisplay sidebar PlayerKillCount
execute as @s[scores={tPlayerKillCount=..-1}] run scoreboard objectives setdisplay sidebar PlayerKillCount
scoreboard players set @s[scores={tPlayerKillCount=1..}] tPlayerKillCount 0
scoreboard players set @s[scores={tPlayerKillCount=..-1}] tPlayerKillCount 0

execute as @s[scores={tTotalKillCount=1..}] run scoreboard objectives setdisplay sidebar TotalKillCount
execute as @s[scores={tTotalKillCount=..-1}] run scoreboard objectives setdisplay sidebar TotalKillCount
scoreboard players set @s[scores={tTotalKillCount=1..}] tTotalKillCount 0
scoreboard players set @s[scores={tTotalKillCount=..-1}] tTotalKillCount 0

execute as @s[scores={tXp=1..}] run scoreboard objectives setdisplay sidebar Xp
execute as @s[scores={tXp=..-1}] run scoreboard objectives setdisplay sidebar Xp
scoreboard players set @s[scores={tXp=1..}] tXp 0
scoreboard players set @s[scores={tXp=..-1}] tXp 0

