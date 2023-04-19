import xml.etree.ElementTree as ET

# Loads the rekordbox_settings_12apr.xml file
tree = ET.parse('rekordbox_settings_18apr.xml')
root = tree.getroot()

# Loops through all of the playlist names in the XML file and updates the name
for playlist in root.iter('PLAYLISTS'):
    for node in playlist.iter('NODE'):
        name_node = node.get('Name')
        if name_node is not None:
            new_name = name_node.lower().replace(' ', '_').replace("'", '').replace('-', '')
            new_name = new_name.rstrip(' _')
            node.set('Name', new_name)
            print(new_name)

# Writes to new xml 
tree.write('new_playlists_18apr.xml', encoding='utf-8', xml_declaration=True)