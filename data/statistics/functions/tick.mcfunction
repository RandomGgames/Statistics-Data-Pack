execute as @a if predicate statistics:something_triggered run function statistics:triggers/triggered/check_what_triggered

function statistics:triggers/enable/single
function statistics:triggers/enable/custom
function statistics:triggers/enable/used
function statistics:triggers/enable/mined
function statistics:triggers/enable/crafted
function statistics:triggers/enable/broken
function statistics:triggers/enable/picked_up
function statistics:triggers/enable/dropped
function statistics:triggers/enable/killed
function statistics:triggers/enable/killed_by

scoreboard players enable @a ClearSidebar
execute as @a[scores={ClearSidebar=1..}] run scoreboard objectives setdisplay sidebar
execute as @a[scores={ClearSidebar=..-1}] run scoreboard objectives setdisplay sidebar
scoreboard players set @a[scores={ClearSidebar=1..}] ClearSidebar 0
scoreboard players set @a[scores={ClearSidebar=..-1}] ClearSidebar 0