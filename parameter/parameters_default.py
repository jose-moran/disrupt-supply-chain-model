# Indicate the subfolder of the input folder that contains the input files
input_folder = "Tanzania"

# Save a log file in the output folder, called "exp.log"
export_log = True

# Save the main result in a "criticality.csv" file in the output folder
# Each line is a simulation, it saves what is disrupted and for how long, and aggregate observables
export_criticality = True

# Save the amount of good flowing on each transport segment
# It saves a flows.json file in the output folder
# The structure is a dic {"timestep = {"transport_link_id = {"sector_id = flow_quantity}}
# Can be True or False
export_flows = False

# Save firm-level impact results
# It creates an "extra_spending.csv" file and an "extra_consumption.csv" file in the output folder
# Each line is a simulation, it saves what was disrupted and the corresponding impact for each firm
export_per_firm = False

# Save aggregated time series
# It creates an "aggregate_ts.csv" file in the output folder
# Each columns is a time series
# Exports:
# - aggregate production
# - total profit, 
# - household consumption, 
# - household expenditure, 
# - total transport costs, 
# - average inventories.
export_time_series = False

# Save the firm table
# It creates a "firm_table.xlsx" file in the output folder
# It gives the properties of each firm, along with production, sales to households, to other firms, exports
export_firm_table = True


# Save the OD point table
# It creates a "odpoint_table.xlsx" file in the output folder
# It gives the properties of each OD point, along with production, sales to households, to other firms, exports
export_odpoint_table = True

# Save the country table
# It creates a "country_table.xlsx" file in the output folder
# It gives the trade profile of each country
export_country_table = True

# Save the edgelist table
# It creates a "edgelist_table.xlsx" file in the output folder
# It gives, for each supplier-buyer link, the distance and amounts of good that flows
export_edgelist_table = True

# Save inventories per sector
# It creates an "inventories.xlsx" file in the output folder
export_inventories = False

# Save the combination of district and sector that are over the cutoffs value
# It creates an "filtered_district_sector.xlsx" file in the output folder
export_district_sector_table = False

# Duration of the disruption
# Should be an integer
disruption_duration = 1

# Whether the criticality should loop on the tranport edges or nodes
# Admit 2 values: 'edges' or 'nodes'
disrupt_nodes_or_edges = "edges"

# Whether or not to model congestion
congestion = True

# Whether or not firms should readjust their price to changes in input prices
propagate_input_price_change = True

# Any sector in a district that have an importance lower than this value is discarded
# 2 exceptions apply:
# - for each sector, the most important district is kept, even if its importance is lower.
# It avoids having no firm at all from a sector
# - for agriculture, the cutoff value is twice lower. If we apply the same cutoff value as the other sector
# all districts are filtered out. This is because, agriculture is generally spread over 
# the country, such that importance values are low and rather uniformly distributed.
district_sector_cutoff = 0.003

# For each sector, how many of the most important districts will be kept, whatever the 'district_sector_cutoff' value
nb_top_district_per_sector = 1

# Duration target for the firm inventory
# When firm holds the inventories meeting this target, then the firms can keep meeting their pre-disruption
# production targets without ordering more inputs for the specified number of time steps.
# Two types of value are possible:
# - an integer value: all firms have the same inventory duration target for all inputs
# - 'inputed': values are provided in an external file, which a specific duration target to each input-sector, buying-firm-sector combination 
inventory_duration_target = 2

# Extend the inventory duration targets of all firms, uniformly
# Admit an integer value, which represents the number of time steps to add
# The type of inputs for which the inventory is to be extended is determined by the inputs_with_extra_inventories parameter
extra_inventory_target = 0

# List of input, identified by their producing sector, for which an extra inventory duration target is given
# Possible values:
# - 'all': all types of inputs
# - list of sector id, e.g., [1,13,15,'import']. Can be an empty list
inputs_with_extra_inventories = "all"

# Determines the speed at which firms try to reach their inventory duration target
# See Henriet, Hallegatte, and Tabourier 2011 for the formulas
# A too large value leads to dynamic instabilities, called Bullwhip effect
reactivity_rate = 0.1

# Determines the initial utilization rate of firms
# It is used to determine, based on the production of the input-output equilibrium, the production capacity of the firms
# E.g., if a firm produces 80 and has a 0.8 utilization rate, then its production capacity is set to 100.
# It applies uniformly to all firms.
utilization_rate = 0.8

# Determines which inputs will be kept in the firms' Leontief production function
# It sets to 0 the elements of the technical coefficient IO matrix that are below this cutoff
# E.g., if sector A uses 0.3 input of sector B and 0.005 input of sector C to produce 1 unit of output (data from
# the technical coefficient matrix), then, with a io_cutoff of 0.01, firms for sector A will only source inputs from 
# sector B firms.
io_cutoff = 0.01

# Determines the way firms ration their clients if they cannot meet all demand
# Possible values are:
# - 'equal': all clients are equally rationned in proportion of their order
# - 'household_first': if the firm sells to both households and other firms, then households are served first 
rationing_mode = "household_first"

# Set the number of supplier that firms have for each input
# Possible values are:
# - 1: each firms select one supplier per input
# - 2: each firms select two suppliers per input
# - a decimal number between 1 and 2: firms choose either one or two suppliers per input, such that, in average
# the average number of supplier per sector is equal to the specified number.
nb_suppliers_per_sector = 1

# Determines how important it is for firms to choose suppliers close to them
# The chance of choosing a firm as a supplier for an input, depends on its importance score and on its distance
# It is (importance) / (distance)^w where w is the weight_localization parameter
weight_localization = 1

# Determines the list of node or edge to disrupt in the criticality loop
# Possible values are:
# - "all = test all nodes or edges, ordered by their ID
# - other values are user defined in the main code, depending on the list of nodes/edges they have generated
nodeedge_tested = "all"

# Number of nodeedge to test
# It will take only the first N in the list of nodes or edges of the criticality loop
# Possible values are:
# - None: all elements are tested
# - an integer N: the N first are tested
nodeedge_tested_topn = None

# Skip the first elements in the list of nodes or edges to disrupt in the criticality loop
# Possible values are None or integer values. It should be lower than nodeedge_tested_topn, if such value is given.
# If nodeedge_tested_topn is N and nodeedge_tested_skipn is M, the we test list[M,N]
nodeedge_tested_skipn = None

# Run the model in the "Aggregate IO mode"
# Instead of disrupting the transport network, we evaluate how much production would be blocked if all the firms 
# located in the disrupted nodes were unable to produce. Then we uniformly distribute this drop of production on
# all the firm of the corresponding sector.
model_IO = False

# Provides default simulation duration Tfinal for different disruption duration
duration_dic = {
    0:2,
    1:5, 
    2:9, 
    3:12, 
    4:15
}

# The duration of the simulation, in time steps
Tfinal = duration_dic[disruption_duration]

# Whether or not to load extra roads in the model
new_roads = False