#---------------------------------------------------------------------------
#
# Modeling Atlantic Forest regenerability
# 
# 1. Importing data into GRASS GIS
#
# Bernardo BS Niebuhr - bernardo_brandaum@yahoo.com.br
# Mauricio Humberto Vancine - mauricio.vancine@gmail.com
# 02/06/2017
# Feel free to modify and share this code
#---------------------------------------------------------------------------

###--------------------------------------------------------------------###
###--------------------------------------------------------------------###
###--------------------------------------------------------------------###
## Import data

files = os.listdir(folder_path) # List files in the folder
for i in files:

# 2. Limits of AF and Brazil (states, municipalities)
files = os.listdir(folder_path) # List files in the folder
for i in files:
 
# 3. Pastures of Brazil - LAPIG 30m resolution, 2015

# 4. Forest fragments from Sao Paulo State - FBDS 5m resolution, 2014
folder_path = r'G:\regenerabilidade_MA\01_bases\raster\vegetacao_FBDS_SP_5m'
os.chdir(folder_path) # Change to this folder
grass.run_command('r.in.gdal', input="floresta_FBDS_albers_final1_HABMAT.tif", output="floresta_FBDS_albers_final1_HABMAT_tif", overwrite = True) # Import map

# 5. Forest fragments of AF in Rio de Janeiro State - SOS Mata Atlantica 30m resolution, 2015 (considering forest, mangroove, humid areas, and restinga)
folder_path = r'G:\regenerabilidade_MA\01_bases\vetor\SOSMA_2014_2015_RJ'
os.chdir(folder_path) # Change to this folder
grass.run_command('v.in.ogr', input="rj_2014_2015_albers_sad69.shp", output="atlas_sosma_rj_2014_2015_albers_sad69_shp", overwrite = True) # Import map

# 6. Forest fragments of AF - SOS Mata Atlantica 30m resolution, 2014 (considering forest, mangroove, humid areas, and restinga)

# 8. Water bodies of Brazil (ANA)
folder_path = r'G:\regenerabilidade_MA\01_bases\vetor\massa_dagua\ana'
os.chdir(folder_path) # Change to this folder
grass.run_command('v.in.ogr', input="geoft_bho_massa_dagua_albers_sad69.shp", output="geoft_bho_massa_dagua_albers_sad69_shp", snap='1', overwrite = True)

# 9. Roads of Brazil DNIT

# 11. AF patches - SOSMA 2005 - from Ribeiro et al 2009
folder_path = r'G:\regenerabilidade_MA\01_bases\vetor\remanescentes_ribeiro_etal_2009'
os.chdir(folder_path) # Change to this folder
grass.run_command('v.in.ogr', input="mata_atlantica_remanescentes_sad69_albers_2005.shp", output="mata_atlantica_remanescentes_sad69_albers_2005_shp", snap = 1, overwrite = True)

###--------------------------------------------------------------------###