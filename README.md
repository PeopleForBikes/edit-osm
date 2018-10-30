# edit-osm
Tools for editing OSM files for BNA scenario planning

The BNA can be used as a scenario planning tool by running the analysis on proposed/hypothetical infrastructure and comparing the results to BNA scores for the existing/actual network. Generating data for hypothetical infrastructure requires modifying OpenStreetMap (OSM) data and saving the modified file without uploading the modifications back to OSM. JOSM is the easiest tool to make modifications, providing a GUI and the ability to make edits to OSM data offline. Instructions for modifying OSM data to run the BNA for scenario planning follow. 


## How to Create Hypothetical OSM Data for the BNA
1. Download OSM data for the target area using JOSM. You can download JOSM here: https://josm.openstreetmap.de/. Keep in mind that the BNA uses a buffer of <0.5 * bikeshed distance> around the area boundary, so the data downloaded via JOSM should include the region with the buffer area.
2. Modify OSM data using JOSM to include proposed infrastructure (with JOSM, editing can be done offline). For guidance on using JOSM, visit the Learn OSM website: https://learnosm.org/en/josm/start-josm/
NOTE: IT IS CRITICALLY IMPORTANT NOT TO UPLOAD THE HYPOTHETICAL DATA BACK TO OPENSTREETMAP, AS THIS WILL CONTRIBUTE ERRONEOUS DATA TO THE WORLD MAP. When you exit JOSM, be sure you save the file locally but do not select the "Upload" option.
Note: For a large area like an entire city this process may be difficult without significant computing resources, due to large file sizes.
3. If new features were added to OSM (i.e. new lines or polygons drawn on the map), run the OSM file through the number.py script first. When new features are added but not uploaded to OSM, they are assigned negative ID numbers. Those numbers need to be rearranged in increasing order, as the standard positive ID numbers are.

Once you've created the file with hypothetical data, run it through the BNA to obtain scenario planning results. 

Keep in mind that changes to the overall scores will depend on the extent and significance of proposed infrastructure changes and the size of the measured region. For instance, adding a protected bike lane on a dangerous street that connects a residential neighborhood to a business district could produce significant score improvements at the neighborhood scale. However, that single improvement might not affect the overall BNA score on the city scale, because it is a small part of a big region.

Also keep in mind that in some cases intersections or crossings of busy streets are major barriers to connectivity. Road improvement may not make a significant difference unless they include safe intersection treatments.
