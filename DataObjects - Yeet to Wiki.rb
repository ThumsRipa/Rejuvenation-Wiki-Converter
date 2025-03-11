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
