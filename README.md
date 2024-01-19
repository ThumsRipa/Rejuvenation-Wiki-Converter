# Rejuvenation-Wiki-Converter
 
This is used to convert Ruby files to Module:Database files for Rejuvenation.wiki.gg

There are a total of 7 Module:Database files that are currently being used. Of those, 6 are being converted here. The Module:Database/Types file is one that can probably be updated manually (it simply lists out all the types and their resistances/weaknesses)

Module:Database/Moves
    - A list of all the moves that are in the game (both official and custom), along with the power, accuracy, pp, and other tags
    - Uses movetext.rb as the sole input
    - Converts to DatabaseMoves.txt through moveTextConverter.py

Module:Database/TMs
    - A list of compatible moves. It lists out the TM/Move Tutor move, then all the Pokemon that can learn that specific move in their base forms
    - Compatible moves for alternate forms is listed in the individual forms (in Module:Database/Forms)
    - Uses montext.rb, itemtext.rb, and RejuvTutors.csv as inputs
    - montext.rb is used to see if a Pokemon can learn a specific move
    - itemtext.rb is used to get a list of all the TMs/RMs/HMs
    - RejuvTutors.csv is used to get a list of all the Move Tutor moves available
    - Converts to DatabaseTMs.txt through compatibleMovesConverter.py

Module:Database/Names
    - A list of all the names of Pokemon, Items, and Abilities
    - Pokemon names are used to convert between Database names (MRMIME) and normal names (Mr. Mime)
    - Some of them need to be manually updated after (NidoranF, NidoranM, Flabebe, maybe some more I'm forgetting)
    - Uses montext.rb, itemtext.rb, and abiltext.rb as inputs
    - Converts to DatabaseNames.txt through namesConverter.py

Module:Database/Encounters
    - WIP
    - The old version is a list of maps and the possible encounters on that map. That is what is currently on Rejuvenation.wiki.gg
    - The new, proposed version (which is in here) lists out the Pokemon and the maps that it can be found in
    - Uses montext.rb, enctext.rb, and EventEncounters.csv as inputs
    - EventEncounters.csv to get the event encounters, which is not available through Ruby files
    - Converts to DatabaseEncounters.txt

Module:Database/Species
    - A list of Pokemon's base forms
    - Uses montext.rb as the sole input
    - Converts to DatabaseSpecies.txt

Module:Database/Forms
    - A list of Pokemon's alternate forms
    - Uses montext.rb and RejuvTutors.csv as inputs
    - RejuvTutors.csv is needed because Module:Database/TMs only gives compatible moves for the base forms
    - Converts to DatabaseForms.txt from monTextConverter-Forms.py

Feel free to reach out on Discord if you have questions. I'm not always available, but I'll usually check in on Discord at least two or three times a week

ThumsRipa