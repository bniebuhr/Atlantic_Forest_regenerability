#---------------------------------------------------------------------------
#
# Modeling Atlantic Forest regenerability
# 
# 2. Rasterizing shapefiles (all with the same extent and resolution = 30m)
#
# Bernardo BS Niebuhr - bernardo_brandaum@yahoo.com.br
# Mauricio Humberto Vancine
#
# 02/06/2017
# Feel free to modify and share this code
#---------------------------------------------------------------------------

###--------------------------------------------------------------------###
## Import python modules
import os # operational system commands
import grass.script as grass # GRASS GIS commands
###--------------------------------------------------------------------###

###--------------------------------------------------------------------###
## Rasterize shapefiles

# Define the region of study

#grass.run_command('g.region', vector = 'limite_ma_extendido_albers_sad69_shp', res = 30, flags = 'p')
#grass.run_command('g.region', vector = 'limite_leima_ribeiroetal2009_albers_sad69_dissolve_shp', flags = 'p') 
# The above command does not set the exact resolution of 30m - we are going to add some meters to the extent to get an exact resolution of 30m

grass.run_command('g.region', n=3207580, s=-215690, w=207880, e=2738800, res = 30, flags = 'p')

# 1. Forest fragmentos of AF - SOSMA 2014 (considering forest, mangroove, humid areas, and restinga)
grass.run_command('v.to.rast', input = 'atlas_ma_sos_ma_2014_mata_restinga_mangue_albers_sad69_shp',
                  output = 'atlas_ma_sos_ma_2014_mata_restinga_mangue_albers_sad69_rast', use='val', value=1, overwrite = True)

# 2. Urban areas (SOSMA 2014 + IBGE)
grass.run_command('v.to.rast', input = 'mancha_urbana_composicao_ibge_SOS_limiteMAestendido_albers_sad69_shp',
                  output = 'mancha_urbana_composicao_ibge_SOS_limiteMAestendido_albers_sad69_rast', use='val', value=1, overwrite = True)

# 3. Water bodies of Brazil (ANA)
grass.run_command('v.to.rast', input = 'geoft_bho_massa_dagua_albers_sad69_shp',
                  output = 'geoft_bho_massa_dagua_albers_sad69_rast', use='val', value=1, overwrite = True)

# 4. Roads of Brazil DNIT
grass.run_command('v.to.rast', input = 'dnit_pavimentada_albers_sad69_shp',
                  output = 'dnit_pavimentada_albers_sad69_rast', use='val', value=1, overwrite = True)

# 5. Tree plantations - Global Forest Watch 2013-2014
grass.run_command('v.to.rast', input = 'gfw_tree_plantations_albers_sad69_shp',
                  output = 'gfw_tree_plantations_albers_sad69_rast', use='val', value=1, overwrite = True)

# 6. Forest fragments of AF in Rio de Janeiro State - SOS Mata Atlantica 30m resolution, 2015 (considering forest, mangroove, humid areas, and restinga)
grass.run_command('v.to.rast', input = 'atlas_sosma_rj_2014_2015_albers_sad69_shp',
                  output = 'atlas_sosma_rj_2014_2015_albers_sad69_rast', use='attr', attribute_column='code_hab2', overwrite = True)

# 6. Forest fragments of AF - SOS Mata Atlantica 30m resolution, 2005
grass.run_command('v.to.rast', input = 'mata_atlantica_remanescentes_sad69_albers_2005_shp',
                  output = 'mata_atlantica_remanescentes_sad69_albers_2005_rast', use='val', value = 1, overwrite = True)
