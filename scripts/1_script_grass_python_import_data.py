#---------------------------------------------------------------------------
#
# Modeling Atlantic Forest regenerability
# 
# 1. Importing data into GRASS GIS
#
# Bernardo BS Niebuhr - bernardo_brandaum@yahoo.com.br
# Mauricio Humberto Vancine - mauricio.vancine@gmail.com#
# 02/06/2017
# Feel free to modify and share this code
#---------------------------------------------------------------------------

###--------------------------------------------------------------------##### Import python modulesimport os # operational system commandsimport grass.script as grass # GRASS GIS commands
###--------------------------------------------------------------------###
###--------------------------------------------------------------------###
## Import data
# 1. Mapbiomasfolder_path = r'G:/regenerabilidade_MA/01_bases/raster/mapbiomas'os.chdir(folder_path) # Change to this folder
files = os.listdir(folder_path) # List files in the folder
for i in files:    if '2016_albers' in i and i[-3:] == 'tif': # Select tif files with this pattern in the name        print i        name = i.replace('.tif', '_tif')          grass.run_command('r.in.gdal', input=i, output=name, overwrite = True) # Import maps

# 2. Limits of AF and Brazil (states, municipalities)folder_path = r'G:/regenerabilidade_MA/01_bases/vetor/limites'os.chdir(folder_path) # Change to this folder
files = os.listdir(folder_path) # List files in the folderlist_maps = [] # List of maps
for i in files:    if ('sad69.shp' in i) and (not 'lock' in i) and (i[-3:] == 'shp'):        print i        name = i.replace('.shp', '_shp')          grass.run_command('v.in.ogr', input=i, output=name, overwrite = True) # Import maps        list_maps.append(name)
 
# 3. Pastures of Brazil - LAPIG 30m resolution, 2015folder_path = r'G:/regenerabilidade_MA/01_bases/raster/pastagens'os.chdir(folder_path) # Change to this foldergrass.run_command('r.in.gdal', input="pastagens_br_2015_albers_sad69.tif", output="pastagens_br_2015_albers_sad69_tif", overwrite = True) # Import map

# 4. Forest fragments from Sao Paulo State - FBDS 5m resolution, 2014
folder_path = r'G:\regenerabilidade_MA\01_bases\raster\vegetacao_FBDS_SP_5m'
os.chdir(folder_path) # Change to this folder
grass.run_command('r.in.gdal', input="floresta_FBDS_albers_final1_HABMAT.tif", output="floresta_FBDS_albers_final1_HABMAT_tif", overwrite = True) # Import map

# 5. Forest fragments of AF in Rio de Janeiro State - SOS Mata Atlantica 30m resolution, 2015 (considering forest, mangroove, humid areas, and restinga)
folder_path = r'G:\regenerabilidade_MA\01_bases\vetor\SOSMA_2014_2015_RJ'
os.chdir(folder_path) # Change to this folder
grass.run_command('v.in.ogr', input="rj_2014_2015_albers_sad69.shp", output="atlas_sosma_rj_2014_2015_albers_sad69_shp", overwrite = True) # Import map

# 6. Forest fragments of AF - SOS Mata Atlantica 30m resolution, 2014 (considering forest, mangroove, humid areas, and restinga)folder_path = r'G:/regenerabilidade_MA/01_bases/vetor/sosma'os.chdir(folder_path) # Change to this foldergrass.run_command('v.in.ogr', input="atlas_ma_sos_ma_2014_mata_restinga_mangue_albers_sad69.shp", output="atlas_ma_sos_ma_2014_mata_restinga_mangue_albers_sad69_shp", snap='1', overwrite = True) # Import map
# 7. Urban areas (SOSMA 2014 + IBGE)folder_path = r'G:\regenerabilidade_MA\01_bases\vetor\urbano'os.chdir(folder_path) # Change to this foldergrass.run_command('v.in.ogr', input="mancha_urbana_composicao_ibge_SOS_limiteMAestendido_albers_sad69.shp", output="mancha_urbana_composicao_ibge_SOS_limiteMAestendido_albers_sad69_shp", overwrite = True) # Import map
# 8. Water bodies of Brazil (ANA)
folder_path = r'G:\regenerabilidade_MA\01_bases\vetor\massa_dagua\ana'
os.chdir(folder_path) # Change to this folder
grass.run_command('v.in.ogr', input="geoft_bho_massa_dagua_albers_sad69.shp", output="geoft_bho_massa_dagua_albers_sad69_shp", snap='1', overwrite = True)

# 9. Roads of Brazil DNITfolder_path = r'G:\regenerabilidade_MA\01_bases\vetor\rodovias'os.chdir(folder_path) # Change to this foldergrass.run_command('v.in.ogr', input="dnit_pavimentada_albers_sad69.shp", output="dnit_pavimentada_albers_sad69_shp", overwrite = True)# 10. Tree plantations - Global Forest Watch 2013-2014folder_path = r'G:\regenerabilidade_MA\01_bases\vetor\tree_plantations'os.chdir(folder_path) # Change to this foldergrass.run_command('v.in.ogr', input="gfw_tree_plantations_albers_sad69.shp", output="gfw_tree_plantations_albers_sad69_shp", overwrite = True)

# 11. AF patches - SOSMA 2005 - from Ribeiro et al 2009
folder_path = r'G:\regenerabilidade_MA\01_bases\vetor\remanescentes_ribeiro_etal_2009'
os.chdir(folder_path) # Change to this folder
grass.run_command('v.in.ogr', input="mata_atlantica_remanescentes_sad69_albers_2005.shp", output="mata_atlantica_remanescentes_sad69_albers_2005_shp", snap = 1, overwrite = True)

###--------------------------------------------------------------------###
