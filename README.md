# Rejuvenation-Wiki-Converter
 
This is used to convert Ruby files to Module:Database files for Rejuvenation.wiki.gg

There are a total of 7 Module:Database files that are currently being used. Of those, 6 are being converted here. The Module:Database/Types file is one that can probably be updated manually (it simply lists out all the types and their resistances/weaknesses)

Module:Database/Moves<br />
    - A list of all the moves that are in the game (both official and custom), along with the power, accuracy, pp, and other tags<br />
    - Uses movetext.rb as the sole input<br />
    - Converts to DatabaseMoves.txt through moveTextConverter.py

Module:Database/TMs<br />
    - A list of compatible moves. It lists out the TM/Move Tutor move, then all the Pokemon that can learn that specific move in their base forms<br />
    - Compatible moves for alternate forms is listed in the individual forms (in Module:Database/Forms)<br />
    - Uses montext.rb, itemtext.rb, and RejuvTutors.csv as inputs<br />
    - montext.rb is used to see if a Pokemon can learn a specific move<br />
    - itemtext.rb is used to get a list of all the TMs/RMs/HMs<br />
    - RejuvTutors.csv is used to get a list of all the Move Tutor moves available<br />
    - Converts to DatabaseTMs.txt through compatibleMovesConverter.py

Module:Database/Names<br />
    - A list of all the names of Pokemon, Items, and Abilities<br />
    - Pokemon names are used to convert between Database names (MRMIME) and normal names (Mr. Mime)<br />
    - Some of them need to be manually updated after (NidoranF, NidoranM, Flabebe, maybe some more I'm forgetting)<br />
    - Uses montext.rb, itemtext.rb, and abiltext.rb as inputs<br />
    - Converts to DatabaseNames.txt through namesConverter.py

Module:Database/Encounters<br />
    - WIP<br />
    - The old version is a list of maps and the possible encounters on that map. That is what is currently on Rejuvenation.wiki.gg<br />
    - The new, proposed version (which is in here) lists out the Pokemon and the maps that it can be found in<br />
    - Uses montext.rb, enctext.rb, and EventEncounters.csv as inputs<br />
    - EventEncounters.csv to get the event encounters, which is not available through Ruby files<br />
    - Converts to DatabaseEncounters.txt

Module:Database/Species<br />
    - A list of Pokemon's base forms<br />
    - Uses montext.rb as the sole input<br />
    - Converts to DatabaseSpecies.txt

Module:Database/Forms<br />
    - A list of Pokemon's alternate forms<br />
    - Uses montext.rb and RejuvTutors.csv as inputs<br />
    - RejuvTutors.csv is needed because Module:Database/TMs only gives compatible moves for the base forms<br />
    - Converts to DatabaseForms.txt from monTextConverter-Forms.py

Feel free to reach out on Discord if you have questions. I'm not always available, but I'll usually check in on Discord at least two or three times a week

ThumsRipa