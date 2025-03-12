def speciesDump
  species_file = "Scripts/#{GAMEFOLDER}/montext.rb"

  require_relative species_file.gsub('.rb', '')

  exporttext = """--[[
WARNING: Page may freeze up!
Copy the following link in a new tab to go into edit mode:
https://rejuvenation.wiki.gg/wiki/Module:Database/Species?action=edit
--]]
--List of information about each Pokemon, used to construct a variety of templates.\n\n"""
  exporttext += "local Database = {\n"

  MONHASH.each do |key, value|
    unique_subkeys = []

    #get names of each form
    value.each_key do |subkey|
      unique_subkeys << subkey unless unique_subkeys.include?(subkey)  #no dupes
    end

    #puts "#{key}"

    #Get first form
    first_form_key, first_form_data = value.find { |key, value| value.is_a?(Hash) }

    exporttext += "[\"#{key}\"]={\n" #key

    exporttext += "\t\tID=#{first_form_data[:dexnum]},\n" #ID/DexNum
    exporttext += "\t\tType1=\"#{first_form_data[:Type1]}\",\n" #Type1
    if first_form_data.key?(:Type2) #type2 if exists
      exporttext += "\t\tType2=\"#{first_form_data[:Type2]}\",\n"
    end

    if first_form_data.key?(:Abilities) #abilities
      abilities = first_form_data[:Abilities].map { |ability| "\"#{ability}\"" }.join(",")
      exporttext += "\t\tAbilities={#{abilities}},\n"
    end
    if first_form_data.key?(:HiddenAbilities) #hidden ability
      exporttext += "\t\tHiddenAbility=\"#{first_form_data[:HiddenAbilities]}\",\n"
    end

    if first_form_data.key?(:Moveset) && !first_form_data[:Moveset].empty? #moves
      moveset = first_form_data[:Moveset].map { |pair| "#{pair[0]},\"#{pair[1]}\"" }.join(",")
      exporttext += "\t\tMoves={#{moveset}},\n"
    end

    if first_form_data.key?(:BaseStats) #base stats
      baseStats = first_form_data[:BaseStats].map { |baseStat| "#{baseStat}" }.join(",")
      exporttext += "\t\tBaseStats={#{baseStats}},\n"
    end
    if first_form_data.key?(:EVs) #evs
      evs = first_form_data[:EVs].map { |ev| "#{ev}" }.join(",")
      exporttext += "\t\tEffortPoints={#{evs}},\n"
    end
    if first_form_data.key?(:BaseEXP) #base exp
      exporttext += "\t\tBaseEXP=#{first_form_data[:BaseEXP]},\n"
    end
    if first_form_data.key?(:GrowthRate) #type2 if exists
      exporttext += "\t\tGrowthRate=\"#{first_form_data[:GrowthRate]}\",\n"
    end

    if first_form_data.key?(:Happiness) #happiness
      exporttext += "\t\tHappiness=#{first_form_data[:Happiness]},\n"
    end
    if first_form_data.key?(:CatchRate) #catchrate/rareness
      exporttext += "\t\tRareness=#{first_form_data[:CatchRate]},\n"
    end

    genderConversions = [["FemZero", "AlwaysMale"], ["FemEighth", "FemaleOneEighth"],
                         ["FemQuarter", "Female25Percent"], ["FemHalf", "Female50Percent"],
                         ["MaleQuarter", "Female75Percent"], ["MaleEighth", "MaleOneEighth"],
                         ["MaleZero", "AlwaysFemale"]]
    if first_form_data.key?(:GenderRatio)
      gender_symbol = first_form_data[:GenderRatio].to_s
      gender_match = genderConversions.find { |pair| pair[0] == gender_symbol }
      if gender_match
        exporttext += "\t\tGenderRate=\"#{gender_match[1]}\",\n"
      end
    end

    if first_form_data.key?(:Height)
      height = format("%.1f", first_form_data[:Height] / 10.0)
      exporttext += "\t\tHeight=\"#{height}\",\n"
    end
    if first_form_data.key?(:Weight)
      weight = format("%.1f", first_form_data[:Weight] / 10.0)
      exporttext += "\t\tWeight=\"#{weight}\",\n"
    end
    if first_form_data.key?(:Color)
      exporttext += "\t\tColor=\"#{first_form_data[:Color]}\",\n"
    end
    if first_form_data.key?(:EggSteps)
      exporttext += "\t\tStepsToHatch=#{first_form_data[:EggSteps]},\n"
    end
    
    if first_form_data.key?(:EggMoves) #egg moves
      eggmoves = first_form_data[:EggMoves].map { |eggmove| "\"#{eggmove}\"" }.join(",")
      exporttext += "\t\tEggMoves={#{eggmoves}},\n"
    end
    if first_form_data.key?(:EggGroups) #egg groups
      egggroups = first_form_data[:EggGroups].map { |egggroup| "\"#{egggroup}\"" }.join(",")
      exporttext += "\t\tCompatibility={#{egggroups}},\n"
    end
    if first_form_data.key?(:kind) #kind
      exporttext += "\t\tKind=\"#{first_form_data[:kind]}\",\n"
    end
    if first_form_data.key?(:dexentry) #dex
      exporttext += "\t\tPokedex=\"#{first_form_data[:dexentry]}\",\n"
    end

    #wild items
    if first_form_data.key?(:WildItemCommon) #hidden ability
      exporttext += "\t\tWildItemCommon=\"#{first_form_data[:WildItemCommon]}\",\n"
    end
    if first_form_data.key?(:WildItemUncommon) #hidden ability
      exporttext += "\t\tWildItemUncommon=\"#{first_form_data[:WildItemUncommon]}\",\n"
    end
    if first_form_data.key?(:WildItemRare) #hidden ability
      exporttext += "\t\tWildItemRare=\"#{first_form_data[:WildItemRare]}\",\n"
    end

    #evolutions
    if first_form_data.key?(:preevo) #preevolution
      species = "\"#{first_form_data[:preevo][:species]}\""
      form = first_form_data[:preevo][:form]
      exporttext += "\t\tPreEvolutions={#{species},#{form}},\n"
    end
    ### Need to manually change any evolutions with "Location" manually after the export
    ### Leafeon, Glaceon, Magneton, Nosepass, Hisuian Bergmite, Charjabug, Crabrawler
    if first_form_data.key?(:evolutions) && !first_form_data[:evolutions].empty? #evolutions
      allevos = first_form_data[:evolutions].map { |pair| "\"#{pair[0]}\",\"#{pair[1]}\",\"#{pair[2]}\"" }.join(",")
      exporttext += "\t\tEvolutions={#{allevos}},\n"
    else
      exporttext += "\t\tEvolutions={},\n"
    end

    #form amounts and names
    formsList = unique_subkeys
    whiteList = [ " Form", " Flower", " Drive", " Cloak", " Sea", " Rotom", "-Striped",
                  " Mode", " Kyurem", "Male", "Female", "Small", "Hoopa ", " Style", " Core",
                  "Dusk Mane", "Dawn Wings", "Necrozma", " Face", "Crowned ", "Eternamax", " Rider"] #probably need to check and add more exceptions
    finalList = [formsList.shift]  #pop first item
    
    #whitelist check loop
    if !formsList.empty?
      finalList += formsList.select do |form|
        form = form.to_s  #make it a string
        whiteList.any? { |phrase| form.include?(phrase) }
      end
    end
    
    formAmounts = finalList.length  # Get array length
    exporttext += "\t\tFormAmount=#{formAmounts},\n"
    allFormNames = finalList.map { |formName| "\"#{formName}\"" }.join(",")
    exporttext += "\t\tFormNames=#{allFormNames},\n"

    #if formAmounts >= 4
      #puts "4+ Forms: #{key}"
    #end
    #if formAmounts == 0
      #puts "No Forms: #{key}"
    #end

    exporttext += "},\n"
  end

  exporttext += "}"

  # Write to new file
  File.open("Scripts/#{GAMEFOLDER}/exportedSpecies.txt", "w") do |f|
    f.write(exporttext)
  end
end


def namesDump
  # Load the ability data file
  abil_file = "Scripts/#{GAMEFOLDER}/abiltext.rb"
  item_file = "Scripts/#{GAMEFOLDER}/itemtext.rb"
  species_file = "Scripts/#{GAMEFOLDER}/montext.rb"

  require_relative abil_file.gsub('.rb', '')
  require_relative item_file.gsub('.rb', '')
  require_relative species_file.gsub('.rb', '')

  #file header
  exporttext = "local p = {\n[\"none\"] = nil,\n"

  #abilities section
  exporttext += "---------------------------------Abilities\n"
  ABILHASH.sort_by { |key, _| key.to_s }.each do |key, value|
    cleaned_name = value[:name].gsub("\\", "")  #specifically for Stop \\PN
    exporttext += "[\"#{key}\"] = \"#{cleaned_name}\",\n"
  end

  #items section
  exporttext += "---------------------------------Items\n"
  ITEMHASH.sort_by { |key, _| key.to_s }.each do |key, value|
    cleaned_name = value[:name].gsub("\\", "")  #just in case idk
    exporttext += "[\"#{key}\"] = \"#{cleaned_name}\",\n"
  end

  #species section
  exporttext += "---------------------------------Species\n"
  exporttext2 = "---------------------------------Species (Reversed)\n" #for the reversed
  MONHASH.sort_by { |key, _| key.to_s }.each do |species_key, forms_hash|
    #Get first form
    first_form_key, first_form_data = forms_hash.find { |key, value| value.is_a?(Hash) }
    
    # Ensure the form data has a name
    if first_form_data && first_form_data[:name]
      cleaned_name = first_form_data[:name].gsub("\\", "")  #just in case
      exporttext += "[\"#{species_key}\"] = \"#{cleaned_name}\",\n"
      exporttext2 += "[\"#{cleaned_name}\"] = \"#{species_key}\",\n"
    end
  end

  exporttext += exporttext2
  exporttext += "}"

  # Write to new file
  File.open("Scripts/#{GAMEFOLDER}/exportedNames.txt", "w") do |f|
    f.write(exporttext)
  end
end

def moveEffectsListDump #to check for new flags
  move_file = "Scripts/#{GAMEFOLDER}/movetext.rb"

  require_relative move_file.gsub('.rb', '')

  unique_subkeys = []

  MOVEHASH.each do |key, value|
    value.each_key do |subkey|
      unique_subkeys << subkey unless unique_subkeys.include?(subkey)  #no dupes
    end
  end

  # Write to exportEffects.txt
  File.open("Scripts/#{GAMEFOLDER}/exportEffects.txt", "w") do |f|
    f.puts unique_subkeys.join("\n")
  end
end

def movesDump
  move_file = "Scripts/#{GAMEFOLDER}/movetext.rb"

  require_relative move_file.gsub('.rb', '')

  dataFlags = ["contact", "soundmove", "sharpmove", "beammove", "healingmove", "punchmove", "windmove", "heavymove", "zmove", "intercept", "highcrit", "recoil", "defrost"]
  moveFlags = ["kingrock", "snatchable", "nonmirror", "magiccoat", "gravityblocked", "bypassprotect"]

  #file header
  exporttext = "--Database of all moves in Rejuvenation\n"
  exporttext += "--DataFlags are things that categorize the move (Punch move, sound move, z-move, etc)\n"
  exporttext += "--MoveFlags are how other moves (or items) can affect it (King's Rock, Protect, Snatch)\n\n"

  exporttext += "local Moves = {\n"
  MOVEHASH.each do |key, value|
    if key == :AURAWHEELMINUS
      break
    end
    exporttext += "[\"#{key}\"]={\n" #key
    if value.key?(:longname) #chance of effect, doesn't exist for all moves
      cleanText = value[:longname].gsub("\\", "")  #just in case?
    else
      cleanText = value[:name].gsub("\\", "")  #just in case?
    end
    exporttext += "\t\tMoveName=\"#{cleanText}\",\n" #name
    cleanText = format("%03X", value[:function])  #remove 0x
    exporttext += "\t\tEffect=\"#{cleanText}\",\n" #effect
    cleanText = value[:type].to_s.gsub(":", "") #remove the : in front
    exporttext += "\t\tType=\"#{cleanText}\",\n" #type
    cleanText = value[:category].to_s.gsub(":", "").capitalize #remove the : in front of the type
    exporttext += "\t\tCategory=\"#{cleanText}\",\n" #category
    exporttext += "\t\tStrength=\"#{value[:basedamage]}\",\n" #strength/BP
    exporttext += "\t\tAccuracy=\"#{value[:accuracy]}\",\n" #accuracy
    exporttext += "\t\tPP=\"#{value[:maxpp]}\",\n" #maxpp

    if value.key?(:effect) #chance of effect, doesn't exist for all moves
      exporttext += "\t\tChance=\"#{value[:effect]}\",\n"
    end
    if value.key?(:moreeffect) #chance of second effect, doesn't exist for all moves
      exporttext += "\t\tSecondChance=\"#{value[:moreeffect]}\",\n"
    end

  
    cleanText = value[:target].to_s.gsub(":", "") #remove the : in front
    exporttext += "\t\tTarget=\"#{cleanText}\",\n" #target

    if value.key?(:priority) #priority, doesn't exist for all moves
      exporttext += "\t\tPriority=\"#{value[:priority]}\",\n"
    end

    exporttext += "\t\tDescription=\"#{value[:desc]}\",\n" #description

    #data and move flags
    present_data_flags = dataFlags.select { |flag| value.key?(flag.to_sym) }
    present_move_flags = moveFlags.select { |flag| value.key?(flag.to_sym) }
    formatted_data_flags = present_data_flags.map(&:capitalize)
    formatted_move_flags = present_move_flags.map(&:capitalize)

    # Only add to output if flags exist
    unless formatted_data_flags.empty?
      exporttext += "\t\tDataFlags={#{formatted_data_flags.map { |f| "\"#{f}\"" }.join(",")}},\n"
    end

    unless formatted_move_flags.empty?
      exporttext += "\t\tMoveFlags={#{formatted_move_flags.map { |f| "\"#{f}\"" }.join(",")}},\n"
    end

    exporttext += "},\n"
  end
  exporttext += "}"

  # Write to new file
  File.open("Scripts/#{GAMEFOLDER}/exportedMoves.txt", "w") do |f|
    f.write(exporttext)
  end
end
