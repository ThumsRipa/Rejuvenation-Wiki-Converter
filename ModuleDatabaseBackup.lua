--THIS IS AN INCOMPLETE, TESTING VERSION, PLEASE DO NOT USE ON ANY WIKIS AND ASK FOR A BETTER ONE
local p = {}
-- Here we call the databases to be able to use the data they store
local Moves = mw.loadData('Module:Database/Moves')
local Species = mw.loadData('Module:Database/Species')
local TMs = mw.loadData('Module:Database/TMs')
local Encounters = mw.loadData('Module:Database/Encounters')
local Types = mw.loadData('Module:Database/Types')
local Names = mw.loadData('Module:Database/Names')
local Forms = mw.loadData('Module:Database/Forms')

function firstToUpper(string)
	if string == nil then
		return nil
	elseif type(string) == "number" then
		return string
	else
		return (string.lower(string):gsub("^%l", string.upper))
	end
end

----------------------------------------------- POKEMON INFOBOX -----------------------------------------------
function p.Navbox(Frame)
	local Pokemon = Frame.args[1]
	if not Pokemon then
		Pokemon = mw.title.getCurrentTitle().text
	end
	Pokemon=Names[Pokemon]
	local wikitext = {}
	local prev = ""
	local next = ""
	for a, b in pairs(Species) do
		if b.ID == Species[Pokemon].ID - 1 then
			prev = Names[a] 
		end
		if b.ID == Species[Pokemon].ID + 1 then
			next = Names[a]
		end
	end
	-- adding the navbox at the top
	table.insert(wikitext, Frame:getParent():expandTemplate{title = "PokemonPrevNextHead", args = {
		type = firstToUpper(Species[Pokemon].Type1),
		type2 = firstToUpper(Species[Pokemon].Type2),
		prevnum = ("%03d"):format(tonumber(Species[Pokemon].ID - 1)),
		nextnum = ("%03d"):format(tonumber(Species[Pokemon].ID + 1)),
		prev = prev,
		next = next}
	} .. "\n")
 return table.concat(wikitext)
	
end

function p.PokemonInfobox(Frame)
	local Pokemon = Frame.args[1]
	Pokemon=Names[Pokemon]
	if not Pokemon then
		Pokemon = mw.title.getCurrentTitle().text
	end
	local wikitext = {}
	local ability1 = Species[Pokemon].Abilities[1]
	local ability2 = "none"
	local HA = "none"
	if Species[Pokemon].Abilities[2] then
		ability2 = Species[Pokemon].Abilities[2]
	end
	if Species[Pokemon].HiddenAbility then
		HA = Species[Pokemon].HiddenAbility
	end
-------------------------------------- Forms start --------------------------------------
	local caption = ""
	local body2 = ""
	local color2 = ""
	local type21 = ""
	local type22 = ""
	local megaability = ""
	local ability12 = ""
	local ability22 = ""
	local hiddenability2 = ""
	local height2 = ""
	local weight2 = ""
	local caption2 = ""
	local type31 = ""
	local type32 = ""
	local megaability2 = ""
	local ability13 = ""
	local ability23 = ""
	--Falirion start
	local hiddenability3 = ""
	--Falirion end
	local height3 = ""
	local weight3 = ""
	local caption3 = ""
	local type41 = ""
	local type42 = ""
	local ability14 = ""
	local ability24 = ""
	--Falirion start
	local hiddenability4 = ""
	--Falirion end
	local height4 = ""
	local weight4 = ""
	local caption4 = ""
	local type51 = ""
	local type52 = ""
	local caption5 = ""
	local type61 = ""
	local type62 = ""
	local caption6 = ""
	local formnumber=1
	local evhp2 = 0
	local evat2 = 0
	local evde2 = 0
	local evsp2 = 0
	local evsa2 = 0
	local evsd2 = 0
	local evhp3 = 0
	local evat3 = 0
	local evde3 = 0
	local evsp3 = 0
	local evsa3 = 0
	local evsd3 = 0
	local evhp4 = 0
	local evat4 = 0
	local evde4 = 0
	local evsp4 = 0
	local evsa4 = 0
	local evsd4 = 0
	if Forms[Pokemon] then
		caption = Species[Pokemon].Name
		for a,b in pairs(Forms[Pokemon]) do
		if formnumber == 1 then
			if Forms[Pokemon][a].Type1 then
				type21 = firstToUpper(Forms[Pokemon][a].Type1)
			elseif Forms[Pokemon][a].Type2 then
				type21 = firstToUpper(Species[Pokemon].Type1)
			end
			if Forms[Pokemon][a].Type2 then
				type22 = firstToUpper(Forms[Pokemon][a].Type2)
			end
			--if Forms[Pokemon][a].MegaStone then
			--	if Forms[Pokemon][a].Abilities then
			--		megaability = Forms[Pokemon][a].Abilities[1]
			--	end
			--else
				if Forms[Pokemon][a].Abilities then
					ability12 = Names[Forms[Pokemon][a].Abilities[1]]
					ability22 = Names[Forms[Pokemon][a].Abilities[2]] or nil
				end
				if Forms[Pokemon][a].HiddenAbility then
					hiddenability2 = Names[Forms[Pokemon][a].HiddenAbility]
				end
			--end
			if Forms[Pokemon][a].Height then
				height2 = Forms[Pokemon][a].Height
			end
			if Forms[Pokemon][a].Weight then
				weight2 = Forms[Pokemon][a].Weight
			end
			if Forms[Pokemon][a].Color then
				color2 = Forms[Pokemon][a].Color
			end
			if Forms[Pokemon][a].Shape then
				body2 = Forms[Pokemon][a].Shape
				if body2 < 10 then
					body2 = "0" .. body2
				end
			end
			if Forms[Pokemon][a].EffortPoints then
				evhp2 = Forms[Pokemon][a].EffortPoints[1]
				evat2 = Forms[Pokemon][a].EffortPoints[2]
				evde2 = Forms[Pokemon][a].EffortPoints[3]
				evsp2 = Forms[Pokemon][a].EffortPoints[6]
				evsa2 = Forms[Pokemon][a].EffortPoints[4]
				evsd2 = Forms[Pokemon][a].EffortPoints[5]
			end
			caption2 = Forms[Pokemon][a].FormName
		end
		if formnumber == 2 then
			if Forms[Pokemon][a].Type1 then
				type31 = firstToUpper(Forms[Pokemon][a].Type1)
			elseif Forms[Pokemon][a].Type2 then
				type31 = firstToUpper(Species[Pokemon].Type1)
			end
			if Forms[Pokemon][a].Type2 then
				type32 = firstToUpper(Forms[Pokemon][a].Type2)
			end
			--if Forms[Pokemon][a].MegaStone then
			--	if Forms[Pokemon][a].Abilities then
			--		megaability2 = Forms[Pokemon][a].Abilities[1]
			--	end
			--else
				if Forms[Pokemon][a].Abilities then
					ability13 = Names[Forms[Pokemon][a].Abilities[1]]
					ability23 = Names[Forms[Pokemon][a].Abilities[2]] or nil
				end
				--Falirion start
				if Forms[Pokemon][a].HiddenAbility then
					hiddenability3 = Names[Forms[Pokemon][a].HiddenAbility]
				end
				--Falirion end
			--end
			if Forms[Pokemon][a].Height then
				height3 = Forms[Pokemon][a].Height
			end
			if Forms[Pokemon][a].Weight then
				weight3 = Forms[Pokemon][a].Weight
			end
			if Forms[Pokemon][a].EffortPoints then
				evhp3 = Forms[Pokemon][a].EffortPoints[1]
				evat3 = Forms[Pokemon][a].EffortPoints[2]
				evde3 = Forms[Pokemon][a].EffortPoints[3]
				evsp3 = Forms[Pokemon][a].EffortPoints[6]
				evsa3 = Forms[Pokemon][a].EffortPoints[4]
				evsd3 = Forms[Pokemon][a].EffortPoints[5]
			end
			caption3 = Forms[Pokemon][a].FormName
		end
		if formnumber == 3 then
			if Forms[Pokemon][a].Type1 then
				type41 = firstToUpper(Forms[Pokemon][a].Type1)
			elseif Forms[Pokemon][a].Type2 then
				type41 = firstToUpper(Species[Pokemon].Type1)
			end
			if Forms[Pokemon][a].Type2 then
				type42 = firstToUpper(Forms[Pokemon][a].Type2)
			end
			if Forms[Pokemon][a].Abilities then
				ability14 = Names[Forms[Pokemon][a].Abilities[1]]
				ability24 = Names[Forms[Pokemon][a].Abilities[2]] or nil
			--Falirion start
			if Forms[Pokemon][a].HiddenAbility then
				hiddenability4 = Names[Forms[Pokemon][a].HiddenAbility]
			end
			--Falirion end
			end
			if Forms[Pokemon][a].Height then
				height4 = Forms[Pokemon][a].Height
				weight4 = Species[Pokemon].Weight
			end
			if Forms[Pokemon][a].EffortPoints then
				evhp4 = Forms[Pokemon][a].EffortPoints[1]
				evat4 = Forms[Pokemon][a].EffortPoints[2]
				evde4 = Forms[Pokemon][a].EffortPoints[3]
				evsp4 = Forms[Pokemon][a].EffortPoints[6]
				evsa4 = Forms[Pokemon][a].EffortPoints[4]
				evsd4 = Forms[Pokemon][a].EffortPoints[5]
			end
			caption4 = Forms[Pokemon][a].FormName
		end
		if formnumber == 4 then
			if Forms[Pokemon][a].Type1 then
				type51 = firstToUpper(Forms[Pokemon][a].Type1)
			elseif Forms[Pokemon][a].Type2 then
				type51 = firstToUpper(Species[Pokemon].Type1)
			end
			if Forms[Pokemon][a].Type2 then
				type52 = firstToUpper(Forms[Pokemon][a].Type2)
			end
			caption5 = Forms[Pokemon][a].FormName
			end
		if formnumber == 5 then
			if Forms[Pokemon][a].Type1 then
				type61 = firstToUpper(Forms[Pokemon][a].Type1)
			elseif Forms[Pokemon][a].Type2 then
				type61 = firstToUpper(Species[Pokemon].Type1)
			end
			if Forms[Pokemon][a].Type2 then
				type62 = firstToUpper(Forms[Pokemon][a].Type2)
			end
			caption6 = Forms[Pokemon][a].FormName
		end
		formnumber=formnumber+1
		end
	end

-------------------------------------- Forms end --------------------------------------

	table.insert(wikitext, Frame:getParent():expandTemplate{title = "Pokemon Infobox", args = {
		ndex = ("%03d"):format(tonumber(Species[Pokemon].ID)),
		name = Names[Pokemon],
		type1 = firstToUpper(Species[Pokemon].Type1),
		type2 = firstToUpper(Species[Pokemon].Type2),
		genderrate = Species[Pokemon].GenderRate,
		expgroup = Species[Pokemon].GrowthRate,
		expyield = Species[Pokemon].BaseEXP,
		evhp = Species[Pokemon].EffortPoints[1],
		evat = Species[Pokemon].EffortPoints[2],
		evde = Species[Pokemon].EffortPoints[3],
		evsa = Species[Pokemon].EffortPoints[4],
		evsd = Species[Pokemon].EffortPoints[5],
		evsp = Species[Pokemon].EffortPoints[6],
		catchrate = Species[Pokemon].Rareness,
		friendship = Species[Pokemon].Happiness,
		ability1 = Names[ability1],
		ability2 = Names[ability2],
		hidenability = Names[HA],
		egggroup1 = Species[Pokemon].Compatibility[1],
		egggroup2 = Species[Pokemon].Compatibility[2],
		eggsteps = Species[Pokemon].StepsToHatch,
		["height-m"] = Species[Pokemon].Height,
		["weight-kg"] = Species[Pokemon].Weight,
		color = Species[Pokemon].Color,
		body = Species[Pokemon].Shape,
		category = Species[Pokemon].Kind,
-------------------------------------- Forms start --------------------------------------
		caption = caption,
		color2 = color2,
		body2 = body2,
		["type1-2"] = type21,
		["type2-2"] = type22,
		--megaability = Names[megaability],
		ability12 = ability12,
		ability22 = ability22,
		hiddenability2 = hiddenability2,
		["height2-m"] = height2,
		["weight2-kg"] = weight2,
		caption2 = caption2,
		["type1-3"] = type31,
		["type2-3"] = type32,
		--megaability2 = Names[megaability2],
		ability13 = ability13,
		ability23 = ability23,
		--Falirion start
		hiddenability3 = hiddenability3,
		--Falirion end
		["height3-m"] = height3,
		["weight3-kg"] = weight3,
		caption3 = caption3,
		["type1-4"] = type41,
		["type2-4"] = type42,
		ability14 = ability14,
		ability24 = ability24,
		--Falirion start
		hiddenability4 = hiddenability4,
		--Falirion end
		["height4-m"] = height4,
		["weight4-kg"] = weight4,
		caption4 = caption4,
		["type1-5"] = type51,
		["type2-5"] = type52,
		caption5 = caption5,
		["type1-6"] = type61,
		["type2-6"] = type62,
		caption6 = caption6,
		evhp2 = evhp2,
		evat2 = evat2,
		evde2 = evde2,
		evsp2 = evsp2,
		evsa2 = evsa2,
		evsd2 = evsd2,
		evhp3 = evhp3,
		evat3 = evat3,
		evde3 = evde3,
		evsp3 = evsp3,
		evsa3 = evsa3,
		evsd3 = evsd3,
		evhp4 = evhp4,
		evat4 = evat4,
		evde4 = evde4,
		evsp4 = evsp4,
		evsa4 = evsa4,
		evsd4 = evsd4,
-------------------------------------- Forms end --------------------------------------
		}
	} .. "\n")
	-- a line of text about typing and evolutions, not neccessary but seen it on every wiki I've been at.
	table.insert(wikitext, Names[Pokemon] .. " is a [[" .. firstToUpper(Species[Pokemon].Type1) .. " (type)|" .. firstToUpper(Species[Pokemon].Type1))
	if Species[Pokemon].Type2 == nil then
		table.insert(wikitext, "]]-type Pokémon.")
	else
		table.insert(wikitext, "]]/[[" .. firstToUpper(Species[Pokemon].Type2) .. " (type)|" .. firstToUpper(Species[Pokemon].Type2) .. "]] dual type Pokémon.")
	end
	return table.concat(wikitext)
end

-------------------------------------------------- EVOLUTION DATA -------------------------------------------------------

local EvolutionMethods = {
	--[[
	A complete list of possible requirements of pokémon to evolve. Other = "Yes" means there is an additional part to the requirement (method uses 3 strings in the pokemon.PBS), for example, "by levelling up" needs a certain level to be reached. Other = "No" means there is no additional part, for example "by trade" will make it evolve all the time.
	--]]
	["Happiness"] = {Method = " with high friendship"},
	["HappinessDay"] = {Method = " with high friendship, during the day"},
	["HappinessNight"] = {Method = " with high friendship, at night"},
	["Level"] = {Method = " starting at level "},
	["Trade"] = {Method = " when exposed to a [[Link Heart]]"},
	["TradeItem"] = {Method = " when exposed to a [[Link Heart]] while holding a(n) "},
	["Item"] = {Method = " while exposed to a(n) "},
	["AttackGreater"] = {Method = " if its attack is greater than its defense, starting at level "},
	["AtkDefEqual"] = {Method = " if its attack is equal to its defense, starting at level "},
	["DefenseGreater"] = {Method = " if its attack is lower than its defense, starting at level "},
	["Silcoon"] = {Method = " at random, starting at level "},
	["Cascoon"] = {Method = " at random, starting at level "},
	["Ninjask"] = {Method = " starting at level "},
	["Shedinja"] = {Method = " alongside a Ninjask, if there is a Poké Ball in the bag and a free space in the party, starting at level "},
	["Beauty"] = {Method = " if its beauty stat is higher than "},
	["ItemMale"] = {Method = " if it is male and is exposed to a(n) "},
	["ItemFemale"] = {Method = " if it is female and is exposed to a(n) "},
	["DayHoldItem"] = {Method = " during the day, while holding a(n) "},
	["NightHoldItem"] = {Method = " at night, if holding a(n) "},
	["HasMove"] = {Method = " if its moveset contains the move "},
	["HasInParty"] = {Method = " if your party also has a(n) "},
	["LevelMale"] = {Method = " if male, starting at level "},
	["LevelFemale"] = {Method = " if female, starting at level "},
	["Location"] = {Method = " when leveled up in the area: "},
	["TradeSpecies"] = {Method = " when exposed to a [[Link Heart]] with the following species in the party: "},
	["LevelDay"] = {Method = " during the day, starting at level "},
	["LevelNight"] = {Method = " at night, starting at level "},
	["BadInfluence"] = {Method = " if there is a Dark-type Pokémon in the party, starting at level "},
	["LevelRain"] = {Method = " in rainy weather, starting at level "},
	["Affection"] = {Method = " with high friendship, if has a move with the type: "},
	--Falirion start
	["BattleCrits"] = {Method = " after landing 3 critical hits in a single battle "},
	["Runerigus"] = {Method = " while missing 49 or more HP and leveling up in the area: Wispy Ruins or Wispy Chasm"},
	["Dusk"] = {Method = " when it has the Ability Own Tempo and is leveled up between 5 PM and 5:59 PM, starting at level "},
	["ItemLoc"] = {Method = " when in [[Terajuma Jungle]] while exposed to a(n) "},
	["MoveLoc"] = {Method = " when on [[Evergreen Island]] while its moveset contains the move "},
}

local BranchingForms = {
	--A list of Pokemon that have a branching evolution to with a regional of the same evolved species (like Pikachu to Raichu or Alola Raichu)
	["PIKACHU"] = {0,1},
	["EXEGGCUTE"] = {0,1},
	["CUBONE"] = {0,1},
	["KOFFING"] = {0,1},
	["MIMEJR"] = {0,1},
	["ROCKRUFF"] = {0,1,2},
	["TOXEL"] = {0,2},
}

function getPreEvolution(Pokemon, Formnumber)
	local PreSpecies = Pokemon
	for a, b in pairs(Species) do
		-- Checks all the species in the database.
		if Species[a]["Evolutions"] ~= nil then
		for c, d in pairs(Species[a]["Evolutions"]) do
		-- Checks if any of these species evolves into the Pokémon whose article we are writing.
			if ((Species[a].Evolutions[c] == Pokemon) and (Formnumber==0)) then
				PreSpecies = a
				local Method = Species[a].Evolutions[(c+1)]
				local Methodextra = Species[a].Evolutions[(c+2)]
				return PreSpecies, Method, Methodextra
			elseif ((Species[a].Evolutions[c] == Pokemon) and (BranchingForms[a])) then
				for e,f in pairs(BranchingForms[a]) do
					if ((f==Formnumber) and (c>(3*e)-3)) then
						PreSpecies = a
						local Method = Species[a].Evolutions[(c+1)]
						local Methodextra = Species[a].Evolutions[(c+2)]
						return PreSpecies, Method, Methodextra
					end
				end
			end
		end
		end
	end
	for a, b in pairs(Forms) do
		-- Checks all the species with alternate Forms in the database.
		for c, d in pairs(Forms[a]) do
			-- Checks all different Forms of a given species
			if Forms[a][c]["Evolution"] ~= nil then
				for e, f in pairs(Forms[a][c]["Evolution"]) do
				-- Checks if any of these Forms evolves into the Pokémon whose article we are writing.
					if (Forms[a][c]["Evolution"][e] == Pokemon) and (Forms[a][c].Evolutions[e+1] == Formnumber) then
						PreSpecies = a
						local FormName = Forms[a][c]["FormName"]
						local Method = Forms[a][c].Evolutions[e+2]
						local Methodextra = Forms[a][c].Evolutions[e+3]
						return PreSpecies, Method, Methodextra, FormName
					end
				end
			end
		end
	end
	return PreSpecies
end
--Falirion end

function p.EvoData(Frame)
	local Pokemon = Frame.args[1]
	Pokemon = Names[Pokemon]
	local PriorEvo, Method, Methodextra, FormName = getPreEvolution(Pokemon,0)
	local wikitext = {}
	if (PriorEvo ~= Pokemon) then
		if (FormName == nil) then
			table.insert(wikitext, "It evolves from [[" .. Names[PriorEvo] .. "]]" .. EvolutionMethods[Method]["Method"])
		else
			table.insert(wikitext, "It evolves from [[" .. Names[PriorEvo] .. "|" .. FormName .. "]]" .. EvolutionMethods[Method]["Method"])
		end
		if Moves[Methodextra] then
			table.insert(wikitext, Moves[Methodextra]["MoveName"])
		elseif Encounters["Wild"][tostring(Methodextra)] then
			table.insert(wikitext, Encounters["Wild"][tostring(Methodextra)]["Name"])
		elseif Names[Methodextra] then
			table.insert(wikitext, Names[Methodextra])
		--Falirion start
		elseif Method=="Affection" then
			table.insert(wikitext, Types[Methodextra]["Name"])
		--Falirion end
		else
			if Methodextra == "0" then
				table.insert(wikitext, ". ")
			else
				table.insert(wikitext, firstToUpper(Methodextra) .. ". ")
			end
		end
		table.insert(wikitext, ". ")
	end
	
	local Evolutions = {}
	if Species[Pokemon]["Evolutions"] then
		for a, b in pairs(Species[Pokemon]["Evolutions"]) do
			table.insert(Evolutions, b)
		end
	end
	
	local count = 0
	for a, b in pairs(Evolutions) do
		if a~= nil then
			--Falirion start
			if count ~= 0 then
				table.insert(wikitext, "<br>")
			end
			count=count+1
			if BranchingForms[Pokemon] and ((BranchingForms[Pokemon][count])~=0) then
				table.insert(wikitext, "It evolves into [[" .. Names[(Evolutions[a])] .. "|" .. Forms[(Evolutions[a])][(BranchingForms[Pokemon][count])]["FormName"] .. "]]" .. EvolutionMethods[(Evolutions[a+1])]["Method"])
			else
				table.insert(wikitext, "It evolves into [[" .. Names[(Evolutions[a])] .. "]]" .. EvolutionMethods[(Evolutions[a+1])]["Method"])
			end
			--Falirion end
			if Moves[(Evolutions[a+2])] then
				table.insert(wikitext, Moves[(Evolutions[a+2])]["MoveName"] .. ". ")
			elseif Encounters["Wild"][tostring(Evolutions[a+2])] then
				table.insert(wikitext, Encounters["Wild"][tostring(Evolutions[a+2])]["Name"] .. ". ")
			elseif Names[(Evolutions[a+2])] then
				table.insert(wikitext, Names[(Evolutions[a+2])] .. ". ")
			--Falirion start
			elseif Evolutions[a+1]=="Affection" then
				table.insert(wikitext, Types[Evolutions[a+2]]["Name"] .. ". ")
			--Falirion end
			else
				if Evolutions[a+2] == "0" then
					table.insert(wikitext, ". ")
				else
					table.insert(wikitext, firstToUpper(Evolutions[a+2]) .. ". ")
				end
			end
			Evolutions[a+1] = nil
			Evolutions[a+2] = nil
		end
	end
	--Falirion start
	local FormEvolutions = {}
	local type1 = firstToUpper(Species[Pokemon].Type1)
	local type2 = nil
	if Forms[Pokemon] then
		for a,b in pairs (Forms[Pokemon]) do
			if Forms[Pokemon][a].Regional then
				table.insert(wikitext, "<br>")
				if Forms[Pokemon][a].Type1 then
					type1 = firstToUpper(Forms[Pokemon][a].Type1)
				end
				if Forms[Pokemon][a].Type2 then
					type2 = firstToUpper(Forms[Pokemon][a].Type2)
				elseif not Forms[Pokemon][a].Type1 then
					type2 = firstToUpper(Species[Pokemon].Type2)
				end
				table.insert(wikitext, Names[Pokemon] .. " has a [[" .. type1 .. " (type)|" .. type1)
				if type2 == nil then
					table.insert(wikitext, "]]-type ".. Forms[Pokemon][a].Regional .. " Form. ")
				else
					table.insert(wikitext, "]]/[[" .. type2 .. " (type)|" .. type2 .. "]] dual type " .. Forms[Pokemon][a].Regional .. " Form. ")
				end
				--Falirion start
				local PriorEvo, Method, Methodextra, FormName = getPreEvolution(Pokemon,a)
				if (PriorEvo ~= Pokemon) then
					if (FormName == nil) then
						table.insert(wikitext, "It evolves from [[" .. Names[PriorEvo] .. "]]" .. EvolutionMethods[Method]["Method"])
					else
						table.insert(wikitext, "It evolves from [[" .. Names[PriorEvo] .. "|" .. FormName .. "]]" .. EvolutionMethods[Method]["Method"])
					end
					if Moves[Methodextra] then
						table.insert(wikitext, Moves[Methodextra]["MoveName"])
					elseif Encounters["Wild"][tostring(Methodextra)] then
						table.insert(wikitext, Encounters["Wild"][tostring(Methodextra)]["Name"])
					elseif Names[Methodextra] then
						table.insert(wikitext, Names[Methodextra])
					elseif Method=="Affection" then
						table.insert(wikitext, Types[Methodextra]["Name"])
					else
						table.insert(wikitext, firstToUpper(Methodextra))
					end
					table.insert(wikitext, ". ")
				end
				--Falirion end
				if Forms[Pokemon][a].Evolutions then
					for e, f in pairs(Forms[Pokemon][a].Evolutions) do
						table.insert(FormEvolutions, f)
					end
					count = 0
					for c, d in pairs(FormEvolutions) do
						if c~= nil then
							if count ~= 0 then
								table.insert(wikitext, "<br>")
							end
							count=count+1
							if Forms[(FormEvolutions[c])] then
								table.insert(wikitext, "It evolves into [[" .. Names[(FormEvolutions[c])] .. "|" .. Forms[(FormEvolutions[c])][a]["FormName"] .. "]]" .. EvolutionMethods[(FormEvolutions[c+1])]["Method"])
							else
								table.insert(wikitext, "It evolves into [[" .. Names[(FormEvolutions[c])] .. "]]" .. EvolutionMethods[(FormEvolutions[c+1])]["Method"])
							end
							if Moves[(FormEvolutions[c+2])] then
								table.insert(wikitext, Moves[(FormEvolutions[c+2])]["MoveName"] .. ". ")
							elseif Encounters["Wild"][tostring(FormEvolutions[c+2])] then
								table.insert(wikitext, Encounters["Wild"][tostring(FormEvolutions[c+2])]["Name"] .. ". ")
							elseif Names[(FormEvolutions[c+2])] then
								table.insert(wikitext, Names[(FormEvolutions[c+2])] .. ". ")
							elseif Evolutions[c+1]=="Affection" then
								table.insert(wikitext, Types[(FormEvolutions[c+2])]["Name"] .. ". ")
							else
								if FormEvolutions[c+2] == "0" then
									table.insert(wikitext, ". ")
								else
									table.insert(wikitext, firstToUpper(FormEvolutions[c+2]) .. ". ")
								end
							end
							FormEvolutions[c] = nil
							FormEvolutions[c+1] = nil
							FormEvolutions[c+2] = nil
						end
					end
					FormEvolutions = {}
				end
			end
		end
	end
	--Faliron end
	return table.concat(wikitext)
end

------------------------------------------------ POKEDEX ENTRY ------------------------------------------------
function p.DexEntry(Frame)
	local Pokemon = Frame.args[1]
	if not Pokemon then
		Pokemon = mw.title.getCurrentTitle().text
	end
	Pokemon=Names[Pokemon]
	local wikitext = {}
	table.insert(wikitext, "== Pokédex entry ==\n")
	table.insert(wikitext, Frame:getParent():expandTemplate{title = "DexEntry", args = {
		["1"] = Species[Pokemon].Pokedex,
		type1 = firstToUpper(Species[Pokemon].Type1),
		type2 = firstToUpper(Species[Pokemon].Type2)
		}
	} .. "\n")
	if Forms[Pokemon] then
		for a,b in pairs(Forms[Pokemon]) do
			if Forms[Pokemon][a].Pokedex then
				table.insert(wikitext, "==== " .. Forms[Pokemon][a].FormName .. " ====\n")
				table.insert(wikitext, Frame:getParent():expandTemplate{title = "DexEntry", args = {
					["1"] = Forms[Pokemon][a].Pokedex,
					type1 = firstToUpper(Forms[Pokemon][a].Type1) or firstToUpper(Species[Pokemon].Type1),
					type2 = firstToUpper(Forms[Pokemon][a].Type2) or firstToUpper(Species[Pokemon].Type2)
					}
				} .. "\n")
			end
		end
	end
	return table.concat(wikitext)
end
------------------------------------------------ HELD ITEMS ------------------------------------------------
function p.HeldItems(Frame)
	local Pokemon = Frame.args[1]
	if not Pokemon then
		Pokemon = mw.title.getCurrentTitle().text
	end
	Pokemon=Names[Pokemon]
	local wikitext = {}
	local rare = "none"
	local common = "none"
	local uncommon = "none"
	if Species[Pokemon].WildItemRare then
		rare = Species[Pokemon].WildItemRare
	end
	if Species[Pokemon].WildItemCommon then
		common = Species[Pokemon].WildItemCommon
	end
	if Species[Pokemon].WildItemUncommon then
		uncommon = Species[Pokemon].WildItemUncommon
	end
	table.insert(wikitext, "== Held items ==\n")
	table.insert(wikitext, Frame:getParent():expandTemplate{title = "HeldItems", args = {
		rare = Names[rare],
		common = Names[common],
		uncommon = Names[uncommon],
		type1 = firstToUpper(Species[Pokemon].Type1),
		type2 = firstToUpper(Species[Pokemon].Type2)
		}
	} .. "\n")
	if Forms[Pokemon] then
		for a,b in pairs(Forms[Pokemon]) do
			if Forms[Pokemon][a].WildItemUncommon then
				table.insert(wikitext, "==== " .. Forms[Pokemon][a].FormName .. " ====\n")
				table.insert(wikitext, Frame:getParent():expandTemplate{title = "HeldItems", args = {
					uncommon = Names[Forms[Pokemon][a].WildItemUncommon],
					type1 = firstToUpper(Forms[Pokemon][a].Type1) or firstToUpper(Species[Pokemon].Type1),
					type2 = firstToUpper(Forms[Pokemon][a].Type2) or firstToUpper(Species[Pokemon].Type2)
					}
				} .. "\n")
			end
		end
	end
	return table.concat(wikitext)
end
------------------------------------------------ AVAILABILITY ------------------------------------------------

function p.location(Frame)
	local Pokemon = Frame.args[1]
	local availability = Frame.args[2]
	if not Pokemon then
		Pokemon = mw.title.getCurrentTitle().text
	end
	Pokemon=Names[Pokemon]
	local locations = {}
	local location = {}
	for a, b in pairs(Encounters["Wild"]) do
		for c, d in pairs(Encounters["Wild"][a]) do
			if c ~= "Name" then
			for e, f in pairs(Encounters["Wild"][a][c]) do
				if f[1] == Pokemon then
					location = {a, c, Encounters["Chances"][c][e], b["Name"]}
					table.insert(locations, location)
				end
			end
			end
		end
	end
	for a, b in pairs(locations) do
	if locations[a+1] then
		if locations[a][1] == locations[a+1][1] then
		if locations[a][2] == locations[a+1][2] then
		locations[a+1][3] = locations[a][3] + locations[a+1][3]
		locations[a] = nil
		end
		end
	end
	end

	local uncommon = ""
	local common = ""
	local rare = ""
	local wikitext = {}
	table.insert(wikitext, "== Game locations ==\n")
	for a, b in pairs(locations) do
		if locations[a] == nil then
		else
		if locations[a][2] == "Water" or locations[a][2] == "RockSmash" or locations[a][2] == "GoodRod" or locations[a][2] == "OldRod" then
			if locations[a][3] >= 40 then
				common = common .. locations[a][4] .. " (" .. locations[a][2] .. "), "
			elseif locations[a][3] >= 20 then
				uncommon = uncommon .. locations[a][4] .. " (" .. locations[a][2] .. "), "
			else
				rare = rare .. locations[a][4] .. " (" .. locations[a][2] .. "), "
			end
		else
			if locations[a][3] >= 20 then
				common = common .. locations[a][4] .. " (" .. locations[a][2] .. "), "
			elseif locations[a][3] >= 6 then
				uncommon = uncommon .. locations[a][4] .. " (" .. locations[a][2] .. "), "
			else
				rare = rare .. locations[a][4] .. " (" .. locations[a][2] .. "), "
			end
		end
		end
	end
	local one = ""
	if Encounters["Event"][Names[Pokemon]] then
		one = Encounters["Event"][Names[Pokemon]]
	end
	if availability ~= "none" then
		one = availability
	end
	table.insert(wikitext, Frame:getParent():expandTemplate{title = "Availability", args = {
		type1 = firstToUpper(Species[Pokemon].Type1),
		type2 = firstToUpper(Species[Pokemon].Type2),
		one = one,
		common = common,
		uncommon = uncommon,
		rare = rare
		}
	} .. "\n")
	return table.concat(wikitext)
end
------------------------------------------------ BASE STATS ------------------------------------------------
function p.BaseStats(Frame)
	local Pokemon = Frame.args[1]
	if not Pokemon then
		Pokemon = mw.title.getCurrentTitle().text
	end
	Pokemon=Names[Pokemon]
	local wikitext = {}
	table.insert(wikitext, "== Base stats ==\n")
	table.insert(wikitext, Frame:getParent():expandTemplate{title = "Stats", args = {
		HP = Species[Pokemon].BaseStats[1],
		Attack = Species[Pokemon].BaseStats[2],
		Defense = Species[Pokemon].BaseStats[3],
		SpAtk = Species[Pokemon].BaseStats[4],
		SpDef = Species[Pokemon].BaseStats[5],
		Speed = Species[Pokemon].BaseStats[6],
		type = firstToUpper(Species[Pokemon].Type1),
		type2 = firstToUpper(Species[Pokemon].Type2),
		}
	} .. "\n")
	if Forms[Pokemon] then
		for a,b in pairs(Forms[Pokemon]) do
			if Forms[Pokemon][a].BaseStats then
				table.insert(wikitext, "==== " .. Forms[Pokemon][a].FormName .. " ====\n")
				table.insert(wikitext, Frame:getParent():expandTemplate{title = "Stats", args = {
					HP = Forms[Pokemon][a].BaseStats[1],
					Attack = Forms[Pokemon][a].BaseStats[2],
					Defense = Forms[Pokemon][a].BaseStats[3],
					SpAtk = Forms[Pokemon][a].BaseStats[4],
					SpDef = Forms[Pokemon][a].BaseStats[5],
					Speed = Forms[Pokemon][a].BaseStats[6],
					type = firstToUpper(Forms[Pokemon][a].Type1) or firstToUpper(Species[Pokemon].Type1),
					type2 = firstToUpper(Forms[Pokemon][a].Type2) or firstToUpper(Species[Pokemon].Type2)
					}
				} .. "\n")
			end
		end
	end
	return table.concat(wikitext)
	
end
--------------------------------------------- TYPE EFFECTIVENESS ---------------------------------------------
function TypeEffectiveness(Pokemon, Type, Form)
	local Effectiveness = 1
	if Form == nil then
	local Type1 = firstToUpper(Species[Pokemon].Type1)
	local Type2 = firstToUpper(Species[Pokemon].Type2)
	
	if Types[Type1]["Weaknesses"] then
		for a,b in pairs(Types[Type1]["Weaknesses"]) do
			if b == Type then
			Effectiveness = Effectiveness * 2
			end
		end
	end
	if Types[Type1]["Resistances"] then
		for a,b in pairs(Types[Type1]["Resistances"]) do
			if b == Type then
			Effectiveness = Effectiveness * 0.5
			end
		end
	end
	if Types[Type1]["Immunities"] then
		for a,b in pairs(Types[Type1]["Immunities"]) do
			if b == Type then
			Effectiveness = 0
			end
		end
	end
	if Species[Pokemon].Type2 then
		if Types[Type2]["Weaknesses"] then
			for a,b in pairs(Types[Type2]["Weaknesses"]) do
				if b == Type then
				Effectiveness = Effectiveness * 2
				end
			end
		end
		if Types[Type2]["Resistances"] then
			for a,b in pairs(Types[Type2]["Resistances"]) do
				if b == Type then
				Effectiveness = Effectiveness * 0.5
				end
			end
		end
		if Types[Type2]["Immunities"] then
			for a,b in pairs(Types[Type2]["Immunities"]) do
				if b == Type then
				Effectiveness = 0
				end
			end
		end
	end
	
	else --if we are doing an alternate form

	local Type1 = firstToUpper(Forms[Pokemon][Form].Type1) or firstToUpper(Species[Pokemon].Type1)
	local Type2 = firstToUpper(Forms[Pokemon][Form].Type2) or firstToUpper(Species[Pokemon].Type2)

	if Forms[Pokemon][Form].Type1 or Forms[Pokemon][Form].Type2 then
		if Types[Type1]["Weaknesses"] then
			for a,b in pairs(Types[Type1]["Weaknesses"]) do
				if b == Type then
				Effectiveness = Effectiveness * 2
				end
			end
		end
		if Types[Type1]["Resistances"] then
			for a,b in pairs(Types[Type1]["Resistances"]) do
				if b == Type then
				Effectiveness = Effectiveness * 0.5
				end
			end
		end
		if Types[Type1]["Immunities"] then
			for a,b in pairs(Types[Type1]["Immunities"]) do
				if b == Type then
				Effectiveness = 0
				end
			end
		end
	end

	if Forms[Pokemon][Form].Type2 then
		if Types[Type2]["Weaknesses"] then
			for a,b in pairs(Types[Type2]["Weaknesses"]) do
				if b == Type then
				Effectiveness = Effectiveness * 2
				end
			end
		end
		if Types[Type2]["Resistances"] then
			for a,b in pairs(Types[Type2]["Resistances"]) do
				if b == Type then
				Effectiveness = Effectiveness * 0.5
				end
			end
		end
		if Types[Type2]["Immunities"] then
			for a,b in pairs(Types[Type2]["Immunities"]) do
				if b == Type then
				Effectiveness = 0
				end
			end
		end
	end
	end

	return Effectiveness * 100
end

function p.WeaknessAndResistance(Frame)
	local Pokemon = Frame.args[1]
	if not Pokemon then
		Pokemon = mw.title.getCurrentTitle().text
	end
	Pokemon=Names[Pokemon]
	local wikitext = {}
	table.insert(wikitext, "== Type effectiveness ==\n")
	table.insert(wikitext, Frame:getParent():expandTemplate{title = "TypeEffectiveness", args = {
		type1 = firstToUpper(Species[Pokemon].Type1),
		type2 = firstToUpper(Species[Pokemon].Type2),
		Bug = TypeEffectiveness(Pokemon, "BUG"),
		Dark = TypeEffectiveness(Pokemon, "DARK"),
		Dragon = TypeEffectiveness(Pokemon, "DRAGON"),
		Electric = TypeEffectiveness(Pokemon, "ELECTRIC"),
		Fairy = TypeEffectiveness(Pokemon, "FAIRY"),
		Fighting = TypeEffectiveness(Pokemon, "FIGHTING"),
		Fire = TypeEffectiveness(Pokemon, "FIRE"),
		Flying = TypeEffectiveness(Pokemon, "FLYING"),
		Ghost = TypeEffectiveness(Pokemon, "GHOST"),
		Grass = TypeEffectiveness(Pokemon, "GRASS"),
		Ground = TypeEffectiveness(Pokemon, "GROUND"),
		Ice = TypeEffectiveness(Pokemon, "ICE"),
		Normal = TypeEffectiveness(Pokemon, "NORMAL"),
		Poison = TypeEffectiveness(Pokemon, "POISON"),
		Psychic = TypeEffectiveness(Pokemon, "PSYCHIC"),
		Rock = TypeEffectiveness(Pokemon, "ROCK"),
		Steel = TypeEffectiveness(Pokemon, "STEEL"),
		Water = TypeEffectiveness(Pokemon, "WATER"),
		Shadow = TypeEffectiveness(Pokemon, "SHADOW"),
		}
	} .. "\n")

	if Forms[Pokemon] then
		for a,b in pairs(Forms[Pokemon]) do
			if Forms[Pokemon][a].Type1 or Forms[Pokemon][a].Type2 then
				table.insert(wikitext, "=== " .. Forms[Pokemon][a].FormName .. " ===\n")
				
				table.insert(wikitext, Frame:getParent():expandTemplate{title = "TypeEffectiveness", args = {
				type1 = firstToUpper(Forms[Pokemon][a].Type1 or Species[Pokemon].Type1),
				type2 = firstToUpper(Forms[Pokemon][a].Type2 or Species[Pokemon].Type2),
				Bug = TypeEffectiveness(Pokemon, "BUG", a),
				Dark = TypeEffectiveness(Pokemon, "DARK", a),
				Dragon = TypeEffectiveness(Pokemon, "DRAGON", a),
				Electric = TypeEffectiveness(Pokemon, "ELECTRIC", a),
				Fairy = TypeEffectiveness(Pokemon, "FAIRY", a),
				Fighting = TypeEffectiveness(Pokemon, "FIGHTING", a),
				Fire = TypeEffectiveness(Pokemon, "FIRE", a),
				Flying = TypeEffectiveness(Pokemon, "FLYING", a),
				Ghost = TypeEffectiveness(Pokemon, "GHOST", a),
				Grass = TypeEffectiveness(Pokemon, "GRASS", a),
				Ground = TypeEffectiveness(Pokemon, "GROUND", a),
				Ice = TypeEffectiveness(Pokemon, "ICE", a),
				Normal = TypeEffectiveness(Pokemon, "NORMAL", a),
				Poison = TypeEffectiveness(Pokemon, "POISON", a),
				Psychic = TypeEffectiveness(Pokemon, "PSYCHIC", a),
				-- Falirion start
				Rock = TypeEffectiveness(Pokemon, "ROCK", a),
				-- Falirion end
				Steel = TypeEffectiveness(Pokemon, "STEEL", a),
				Water = TypeEffectiveness(Pokemon, "WATER", a),
				Shadow = TypeEffectiveness(Pokemon, "SHADOW", a),
					}
				} .. "\n")
			end
		end
	end
	return table.concat(wikitext)
end

----------------------------------------------- START OF MOVES -----------------------------------------------
function GetEvolutions(Pokemon)
	local Evolution = {}
	if Species[Pokemon].Evolutions then
	for a, b in pairs(Species[Pokemon].Evolutions) do
		if Species[b] then
			table.insert(Evolution, b)
		end
	end
	end
	return Evolution
end

function p.CreateMovesSection(Frame)
	local Pokemon = Frame.args[1]
	Pokemon=Names[Pokemon]
	if not Species[Pokemon] then
		return '<span style="color:red">ERROR: ' .. Pokemon .. ' is not a valid Pokemon.</span>'
	end

	local Type1 = firstToUpper(Species[Pokemon].Type1)
	local Type2 = Type1
	if Species[Pokemon].Type2 then
		Type2 = firstToUpper(Species[Pokemon].Type2)
	end

	local wikitext = {}
	table.insert(wikitext, "== Moves ==\n")
	table.insert(wikitext, "=== By leveling up ===\n")
	table.insert(wikitext, Frame:getParent():expandTemplate{title = "Learnlist/header", args = {
		[1] = "Level"
		}
	} .. "\n|-")
	for _, move in pairs(Species[Pokemon].Moves) do
		if Moves[move] then
		Stab = nil
		Power = nil
		Accuracy = nil
		for a, b in pairs(GetEvolutions(Pokemon)) do
			if Species[b].Type2 then
				if Species[b].Type1 == Moves[move]["Type"] or Species[b].Type2 == Moves[move]["Type"] then
					Stab = "''"
				end
			elseif Species[b].Type1 == Moves[move]["Type"] then
				Stab = "''"
			end
		end
		if Species[Pokemon].Type1 == Moves[move]["Type"] or Species[Pokemon].Type2 == Moves[move]["Type"] then
			Stab = "'''"
		end
		if Moves[move]["Category"] == "Status" then
				Stab = nil
			end
		if (Moves[move]["Strength"] == "0") or (Moves[move]["Strength"] == "1") then
			Power = "—"
		else
			Power = Moves[move].Strength
		end
		if Moves[move]["Accuracy"] == "0" then
			Accuracy = "—"
		else
			Accuracy = Moves[move].Accuracy
		end
		table.insert(wikitext,
		Frame:getParent():expandTemplate{
			title = "Learnlist/Level",
			args = {
				[1] = Species[Pokemon].Moves[_-1],
				[2] = Moves[move].MoveName,
				[3] = firstToUpper(Moves[move].Type),
				[4] = Moves[move].Category,
				[5] = Power,
				[6] = Accuracy,
				[7] = Moves[move].PP,
				[8] = Stab
			}
		} .. "\n|-")
		end
	end
	table.insert(wikitext,Frame:getParent():expandTemplate{title = "Learnlist/footer", args = {
		[1] = Names[Pokemon]
		}
	} .. "\n")

	if Forms[Pokemon] then
		for a,b in pairs(Forms[Pokemon]) do
		if Forms[Pokemon][a].Moves then
		table.insert(wikitext, "==== " .. Forms[Pokemon][a].FormName .. " ====\n")
		table.insert(wikitext, Frame:getParent():expandTemplate{title = "Learnlist/header", args = {
			[1] = "Level"
			}
		} .. "\n|-")
			for _, move in pairs(Forms[Pokemon][a].Moves) do
			if Moves[move] then
			Stab = nil
			Power = nil
			Accuracy = nil
			for c, d in pairs(GetEvolutions(Pokemon)) do
				if Species[d].Type2 then
					if Species[d].Type1 == Moves[move]["Type"] or Species[d].Type2 == Moves[move]["Type"] then
						Stab = "''"
					end
				elseif Species[d].Type1 == Moves[move]["Type"] then
					Stab = "''"
				end
			end
			if Forms[Pokemon][a].Type1 == Moves[move]["Type"] or Forms[Pokemon][a].Type2 == Moves[move]["Type"] then
				Stab = "'''"
			end
			if Moves[move]["Category"] == "Status" then
					Stab = nil
				end
			if (Moves[move]["Strength"] == "0") or (Moves[move]["Strength"] == "1") then
				Power = "—"
			else
				Power = Moves[move].Strength
			end
			if Moves[move]["Accuracy"] == "0" then
				Accuracy = "—"
			else
				Accuracy = Moves[move].Accuracy
			end
			table.insert(wikitext,
			Frame:getParent():expandTemplate{
			title = "Learnlist/Level",
			args = {
				[1] = Forms[Pokemon][a].Moves[_-1],
				[2] = Moves[move].MoveName,
				[3] = firstToUpper(Moves[move].Type),
				[4] = Moves[move].Category,
				[5] = Power,
				[6] = Accuracy,
				[7] = Moves[move].PP,
				[8] = Stab
				}
			} .. "\n|-")
			end
			end
		table.insert(wikitext,Frame:getParent():expandTemplate{title = "Learnlist/footer", args = {
		[1] = Names[Pokemon]
		}
		} .. "\n")
		end
		end
	end

	table.insert(wikitext, "\n=== By TM ===\n")
	table.insert(wikitext, Frame:getParent():expandTemplate{title = "Learnlist/header", args = {
		[1] = "TM"
		}
	} .. "\n|-")
--Falirion start
--	for move,b in pairs(TMs) do
--		if TMs[move][1] ~= "Tutor" then
--		for c,d in pairs(TMs[move]) do
--		if d == Pokemon then
--		Stab = nil
--		Method = TMs[move][1]
	for a,b in ipairs(TMs) do
		if TMs[a][2] ~= "Tutor" then
		move = TMs[a][1]
		for c,d in pairs(TMs[a]) do
		if d == Pokemon then
		Stab = nil
		Power = nil
		Accuracy = nil
		Method = TMs[a][2]
--Falirion end
		for a, b in pairs(GetEvolutions(Pokemon)) do
			if Species[b].Type2 then
				if Species[b].Type1 == Moves[move]["Type"] or Species[b].Type2 == Moves[move]["Type"] then
					Stab = "''"
				end
			elseif Species[b].Type1 == Moves[move]["Type"] then
				Stab = "''"
			end
		end
		if Species[Pokemon].Type1 == Moves[move]["Type"] or Species[Pokemon].Type2 == Moves[move]["Type"] then
			Stab = "'''"
		end
		if Moves[move]["Category"] == "Status" then
			Stab = nil
		end
		if (Moves[move]["Strength"] == "0") or (Moves[move]["Strength"] == "1") then
			Power = "—"
		else
			Power = Moves[move].Strength
		end
		if Moves[move]["Accuracy"] == "0" then
			Accuracy = "—"
		else
			Accuracy = Moves[move].Accuracy
		end
		table.insert(wikitext,
		Frame:getParent():expandTemplate{
			title = "Learnlist/TM",
			args = {
				[1] = Method,
				[2] = Moves[move].MoveName,
				[3] = firstToUpper(Moves[move].Type),
				[4] = Moves[move].Category,
				[5] = Power,
				[6] = Accuracy,
				[7] = Moves[move].PP,
				[8] = Stab
			}
		} .. "\n|-")
		end
		end
		end
	end
	table.insert(wikitext,Frame:getParent():expandTemplate{title = "Learnlist/footer", args = {
		[1] = Names[Pokemon]
		}
	} .. "\n")

--Falirion start
	if Forms[Pokemon] then
		for a,b in pairs(Forms[Pokemon]) do
		if Forms[Pokemon][a].TMs then
		table.insert(wikitext, "==== " .. Forms[Pokemon][a].FormName .. " ====\n")
		table.insert(wikitext, Frame:getParent():expandTemplate{title = "Learnlist/header", args = {
			[1] = "TM"
			}
		} .. "\n|-")
			for _, move in pairs(Forms[Pokemon][a].TMs) do
			if Moves[move] then
			Stab = nil
			Power = nil
			Accuracy = nil
			Method = "none"
			for key,b in pairs(TMs) do
			if TMs[key][1] == move then
			Method = TMs[key][2]
			break
			end
			end
			for c, d in pairs(GetEvolutions(Pokemon)) do
				if Species[d].Type2 then
					if Species[d].Type1 == Moves[move]["Type"] or Species[d].Type2 == Moves[move]["Type"] then
						Stab = "''"
					end
				elseif Species[d].Type1 == Moves[move]["Type"] then
					Stab = "''"
				end
			end
			if Forms[Pokemon][a].Type1 == Moves[move]["Type"] or Forms[Pokemon][a].Type2 == Moves[move]["Type"] then
				Stab = "'''"
			end
			if Moves[move]["Category"] == "Status" then
				Stab = nil
			end
			if (Moves[move]["Strength"] == "0") or (Moves[move]["Strength"] == "1") then
			Power = "—"
			else
				Power = Moves[move].Strength
			end
			if Moves[move]["Accuracy"] == "0" then
				Accuracy = "—"
			else
				Accuracy = Moves[move].Accuracy
			end
			table.insert(wikitext,
			Frame:getParent():expandTemplate{
			title = "Learnlist/TM",
			args = {
				[1] = Method,
				[2] = Moves[move].MoveName,
				[3] = firstToUpper(Moves[move].Type),
				[4] = Moves[move].Category,
				[5] = Power,
				[6] = Accuracy,
				[7] = Moves[move].PP,
				[8] = Stab
				}
			} .. "\n|-")
			end
			end
		table.insert(wikitext,Frame:getParent():expandTemplate{title = "Learnlist/footer", args = {
		[1] = Names[Pokemon]
		}
		} .. "\n")
		end
		end
	end
--Falirion end

	table.insert(wikitext, "\n=== By Tutor ===\n")
	table.insert(wikitext, Frame:getParent():expandTemplate{title = "Learnlist/header", args = {
		[1] = "Tutor"
		}
	} .. "\n|-")
	for move,b in pairs(TMs) do
		if TMs[move][2] == "Tutor" then
		for c,d in pairs(TMs[move]) do
		if d == Pokemon then
		Stab = nil
		Power = nil
		Accuracy = nil
		Location = TMs[move][1]
		for a, b in pairs(GetEvolutions(Pokemon)) do
			if Species[b].Type2 then
				if Species[b].Type1 == Moves[move]["Type"] or Species[b].Type2 == Moves[move]["Type"] then
					Stab = "''"
				end
			elseif Species[b].Type1 == Moves[move]["Type"] then
				Stab = "''"
			end
		end
		if Species[Pokemon].Type1 == Moves[move]["Type"] or Species[Pokemon].Type2 == Moves[move]["Type"] then
			Stab = "'''"
		end
		if Moves[move]["Category"] == "Status" then
			Stab = nil
		end
		if (Moves[move]["Strength"] == "0") or (Moves[move]["Strength"] == "1") then
			Power = "—"
		else
			Power = Moves[move].Strength
		end
		if Moves[move]["Accuracy"] == "0" then
			Accuracy = "—"
		else
			Accuracy = Moves[move].Accuracy
		end
		table.insert(wikitext,
		Frame:getParent():expandTemplate{
			title = "Learnlist/Tutor",
			args = {
				[1] = Location,
				[2] = Moves[move].MoveName,
				[3] = firstToUpper(Moves[move].Type),
				[4] = Moves[move].Category,
				[5] = Power,
				[6] = Accuracy,
				[7] = Moves[move].PP,
				[8] = Stab
			}
		} .. "\n|-")
		end
		end
		end
	end
	table.insert(wikitext,Frame:getParent():expandTemplate{title = "Learnlist/footer", args = {
		[1] = Names[Pokemon]
		}
	} .. "\n")

--Falirion start
	if Forms[Pokemon] then
		for a,b in pairs(Forms[Pokemon]) do
		if Forms[Pokemon][a].Tutor then
		table.insert(wikitext, "==== " .. Forms[Pokemon][a].FormName .. " ====\n")
		table.insert(wikitext, Frame:getParent():expandTemplate{title = "Learnlist/header", args = {
			[1] = "Tutor"
			}
		} .. "\n|-")
			for _, move in pairs(Forms[Pokemon][a].Tutor) do
			if Moves[move] then
			Stab = nil
			Power = nil
			Accuracy = nil
			if TMs[move] then
			Location = TMs[move][1]
			for c, d in pairs(GetEvolutions(Pokemon)) do
				if Species[d].Type2 then
					if Species[d].Type1 == Moves[move]["Type"] or Species[d].Type2 == Moves[move]["Type"] then
						Stab = "''"
					end
				elseif Species[d].Type1 == Moves[move]["Type"] then
					Stab = "''"
				end
			end
			if Forms[Pokemon][a].Type1 == Moves[move]["Type"] or Forms[Pokemon][a].Type2 == Moves[move]["Type"] then
				Stab = "'''"
			end
			if Moves[move]["Category"] == "Status" then
				Stab = nil
			end
			if (Moves[move]["Strength"] == "0") or (Moves[move]["Strength"] == "1") then
			Power = "—"
			else
			Power = Moves[move].Strength
			end
			if Moves[move]["Accuracy"] == "0" then
				Accuracy = "—"
			else
				Accuracy = Moves[move].Accuracy
			end
			table.insert(wikitext,
			Frame:getParent():expandTemplate{
			title = "Learnlist/Tutor",
			args = {
				[1] = Location,
				[2] = Moves[move].MoveName,
				[3] = firstToUpper(Moves[move].Type),
				[4] = Moves[move].Category,
				[5] = Power,
				[6] = Accuracy,
				[7] = Moves[move].PP,
				[8] = Stab
				}
			} .. "\n|-")
			end
			end
			end
		table.insert(wikitext,Frame:getParent():expandTemplate{title = "Learnlist/footer", args = {
		[1] = Names[Pokemon]
		}
		} .. "\n")
		end
		end
	end
--Falirion end

	local FirstEvo=Pokemon
	local Preevo,z,y,FormName=getPreEvolution(FirstEvo,0)
	z,y= nil
	local FormNum = 0
	while (FirstEvo ~= Preevo) do
		FirstEvo=Preevo
		RegForm=FormName
		if (FormName ~= nil) then
			for a=1,5,1 do
				if Forms[Preevo][a]["FormName"] == FormName then
					Preevo,z,y,FormName=getPreEvolution(FirstEvo,a)
					FormNum = a
					break
				end
			end
		else
			Preevo,z,y,FormName=getPreEvolution(FirstEvo,0)
		end
	end
	if ((RegForm == nil) and (Species[FirstEvo].EggMoves)) or ((RegForm ~= nil) and (Forms[FirstEvo][FormNum].EggMoves)) then
		table.insert(wikitext, "\n=== By Breeding ===\n")
		table.insert(wikitext, Frame:getParent():expandTemplate{title = "Learnlist/header", args = {
			[1] = "Breed"
			}
		} .. "\n|-")
		if (Species[FirstEvo].EggMoves and (RegForm == nil)) then
			for _, move in pairs(Species[FirstEvo].EggMoves) do
				Stab = nil
				Power = nil
				Accuracy = nil
				for a, b in pairs(GetEvolutions(Pokemon)) do
					if Species[b].Type2 then
						if Species[b].Type1 == Moves[move]["Type"] or Species[b].Type2 == Moves[move]["Type"] then
							Stab = "''"
						end
					elseif Species[b].Type1 == Moves[move]["Type"] then
						Stab = "''"
					end
				end
				if Species[Pokemon].Type1 == Moves[move]["Type"] or Species[Pokemon].Type2 == Moves[move]["Type"] then
					Stab = "'''"
				end
				if Moves[move]["Category"] == "Status" then
					Stab = nil
				end
				if (Moves[move]["Strength"] == "0") or (Moves[move]["Strength"] == "1") then
					Power = "—"
				else
					Power = Moves[move].Strength
				end
				if Moves[move]["Accuracy"] == "0" then
					Accuracy = "—"
				else
					Accuracy = Moves[move].Accuracy
				end
				table.insert(wikitext,
				Frame:getParent():expandTemplate{
					title = "Learnlist/Breed",
					args = {
						[1] = " ",
						[2] = Moves[move].MoveName,
						[3] = firstToUpper(Moves[move].Type),
						[4] = Moves[move].Category,
						[5] = Power,
						[6] = Accuracy,
						[7] = Moves[move].PP,
						[8] = Stab
					}
				} .. "\n|-")
			end
		elseif (Forms[FirstEvo][FormNum].EggMoves and (RegForm ~= nil)) then
			for _, move in pairs(Forms[FirstEvo][FormNum].EggMoves) do
				Stab = nil
				Power = nil
				Accuracy = nil
				for a, b in pairs(GetEvolutions(Pokemon)) do
					if Species[b].Type2 then
						if Species[b].Type1 == Moves[move]["Type"] or Species[b].Type2 == Moves[move]["Type"] then
							Stab = "''"
						end
					elseif Species[b].Type1 == Moves[move]["Type"] then
						Stab = "''"
					end
				end
				if Species[Pokemon].Type1 == Moves[move]["Type"] or Species[Pokemon].Type2 == Moves[move]["Type"] then
					Stab = "'''"
				end
				if Moves[move]["Category"] == "Status" then
					Stab = nil
				end
				if (Moves[move]["Strength"] == "0") or (Moves[move]["Strength"] == "1") then
					Power = "—"
				else
					Power = Moves[move].Strength
				end
				if Moves[move]["Accuracy"] == "0" then
					Accuracy = "—"
				else
					Accuracy = Moves[move].Accuracy
				end
				table.insert(wikitext,
				Frame:getParent():expandTemplate{
					title = "Learnlist/Breed",
					args = {
						[1] = " ",
						[2] = Moves[move].MoveName,
						[3] = firstToUpper(Moves[move].Type),
						[4] = Moves[move].Category,
						[5] = Power,
						[6] = Accuracy,
						[7] = Moves[move].PP,
						[8] = Stab
					}
				} .. "\n|-")
			end
		end
		table.insert(wikitext,Frame:getParent():expandTemplate{title = "Learnlist/footer", args = {
			[1] = Names[Pokemon]
			}
		} .. "\n")
	end
	if Forms[Pokemon] then
		for a,b in pairs(Forms[Pokemon]) do
			local FirstEvo=Pokemon
			local RegForm = Forms[Pokemon][a]["FormName"]
			local Preevo,z,y,FormName=getPreEvolution(FirstEvo,a)
			z,y= nil
			local FormNum = a
			while (FirstEvo ~= Preevo) do
				FirstEvo=Preevo
				RegForm=FormName
				if (FormName ~= nil) then
					for k=1,5,1 do
						if Forms[Preevo][k]["FormName"] == FormName then
							Preevo,z,y,FormName=getPreEvolution(FirstEvo,k)
							FormNum = k
							break
						end
					end
				else
					Preevo,z,y,FormName=getPreEvolution(FirstEvo,0)
				end
			end
			if ((RegForm == nil) and (Species[FirstEvo].EggMoves)) or ((RegForm ~= nil) and (Forms[FirstEvo][FormNum].EggMoves)) then
				table.insert(wikitext, "==== " .. Forms[Pokemon][a].FormName .. " ====\n")
				table.insert(wikitext, Frame:getParent():expandTemplate{title = "Learnlist/header", args = {
					[1] = "Breed"
					}
				} .. "\n|-")
			if (Species[FirstEvo].EggMoves and (RegForm == nil)) then
				for _, move in pairs(Species[FirstEvo].EggMoves) do
					Stab = nil
					Power = nil
					Accuracy = nil
					for a, b in pairs(GetEvolutions(Pokemon)) do
						if Species[b].Type2 then
							if Species[b].Type1 == Moves[move]["Type"] or Species[b].Type2 == Moves[move]["Type"] then
								Stab = "''"
							end
						elseif Species[b].Type1 == Moves[move]["Type"] then
							Stab = "''"
						end
					end
					if Species[Pokemon].Type1 == Moves[move]["Type"] or Species[Pokemon].Type2 == Moves[move]["Type"] then
						Stab = "'''"
					end
					if Moves[move]["Category"] == "Status" then
						Stab = nil
					end
					if (Moves[move]["Strength"] == "0") or (Moves[move]["Strength"] == "1") then
						Power = "—"
					else
						Power = Moves[move].Strength
					end
					if Moves[move]["Accuracy"] == "0" then
						Accuracy = "—"
					else
						Accuracy = Moves[move].Accuracy
					end
					table.insert(wikitext,
					Frame:getParent():expandTemplate{
						title = "Learnlist/Breed",
						args = {
							[1] = " ",
							[2] = Moves[move].MoveName,
							[3] = firstToUpper(Moves[move].Type),
							[4] = Moves[move].Category,
							[5] = Power,
							[6] = Accuracy,
							[7] = Moves[move].PP,
							[8] = Stab
						}
					} .. "\n|-")
				end
			elseif (Forms[FirstEvo][FormNum].EggMoves and (RegForm ~= nil)) then
				for _, move in pairs(Forms[FirstEvo][FormNum].EggMoves) do
					Stab = nil
					Power = nil
					Accuracy = nil
					for a, b in pairs(GetEvolutions(Pokemon)) do
						if Species[b].Type2 then
							if Species[b].Type1 == Moves[move]["Type"] or Species[b].Type2 == Moves[move]["Type"] then
								Stab = "''"
							end
						elseif Species[b].Type1 == Moves[move]["Type"] then
							Stab = "''"
						end
					end
					if Species[Pokemon].Type1 == Moves[move]["Type"] or Species[Pokemon].Type2 == Moves[move]["Type"] then
						Stab = "'''"
					end
					if Moves[move]["Category"] == "Status" then
						Stab = nil
					end
					if (Moves[move]["Strength"] == "0") or (Moves[move]["Strength"] == "1") then
						Power = "—"
					else
						Power = Moves[move].Strength
					end
					if Moves[move]["Accuracy"] == "0" then
						Accuracy = "—"
					else
						Accuracy = Moves[move].Accuracy
					end
					table.insert(wikitext,
					Frame:getParent():expandTemplate{
						title = "Learnlist/Breed",
						args = {
							[1] = " ",
							[2] = Moves[move].MoveName,
							[3] = firstToUpper(Moves[move].Type),
							[4] = Moves[move].Category,
							[5] = Power,
							[6] = Accuracy,
							[7] = Moves[move].PP,
							[8] = Stab
						}
					} .. "\n|-")
				end
			end
			table.insert(wikitext,Frame:getParent():expandTemplate{title = "Learnlist/footer", args = {
				[1] = Names[Pokemon]
				}
			} .. "\n")
			end
		end
	end
	return table.concat(wikitext)
end

------------------------------------------------ SPRITES ------------------------------------------------

function p.Sprites(Frame)
	local Pokemon = Frame.args[1]
	if not Pokemon then
		Pokemon = mw.title.getCurrentTitle().text
	end
	Pokemon=Names[Pokemon]
	local wikitext = {}
	table.insert(wikitext, "== Sprites ==\n")
	table.insert(wikitext, Frame:getParent():expandTemplate{title = "Sprites", args = {
		["1"] = ("%03d"):format(tonumber(Species[Pokemon].ID)),
		type = firstToUpper(Species[Pokemon].Type1),
		type2 = firstToUpper(Species[Pokemon].Type2)
		}
	} .. "\n")
	if Forms[Pokemon] then
        for a,b in pairs(Forms[Pokemon]) do
            table.insert(wikitext, "==== " .. Forms[Pokemon][a].FormName .. " ====\n")
            table.insert(wikitext, Frame:getParent():expandTemplate{title = "Sprites", args = {
                ["1"] = ("%03d"):format(tonumber(Species[Pokemon].ID)),
                type = firstToUpper(Species[Pokemon].Type1),
                type2 = firstToUpper(Species[Pokemon].Type2),
                form = "_" .. a
                }
            } .. "\n")
        end
    end
	return table.concat(wikitext)
end

------------------------------------------------------------ Pokemon Pages END --------------------------------------------------------------
------------------------------------------------------------ Pokemon Pages END --------------------------------------------------------------
------------------------------------------------------------ Pokemon Pages END --------------------------------------------------------------
------------------------------------------------------------ Pokemon Pages END --------------------------------------------------------------
------------------------------------------------------------ Pokemon Pages END --------------------------------------------------------------
------------------------------------------------------------ Pokemon Pages END --------------------------------------------------------------
------------------------------------------------------------ Pokemon Pages END --------------------------------------------------------------
------------------------------------------------------------ Pokemon Pages END --------------------------------------------------------------
------------------------------------------------------------ Pokemon Pages END --------------------------------------------------------------

------------------------------------------------------------ Encounters --------------------------------------------------------------

function p.WildEncounters(Frame)
	Location = Frame.args[1]
	Type = Frame.args[2]
	IsSpecial = Frame.args[3]
	wikitext= {}
	for a, b in pairs(Encounters["Wild"]) do
		if b["Name"] == Location then
		table.insert(wikitext, Frame:getParent():expandTemplate{title = "catch/header", args = {
			["1"] = Type
			}
		} .. "\n")
		for c, d in pairs(b) do
			if c ~="Name" then
			table.insert(wikitext, Frame:getParent():expandTemplate{title = "catch/div", args = {
				["1"] = Type,
				["2"] = c
				}
			})
			for e, f in pairs(d) do
				if Species[(f[1])] then
					Switch = Species[(f[1])]
				else Switch = {}
				end
				if f[3] then
					level = " - " .. f[3]
				else level = ""
				end
				if Switch.Type2 then
					Type2=Switch.Type2
				else
					Type2=nil
				end
			table.insert(wikitext, Frame:getParent():expandTemplate{title = "catch/entry", args = {
				["1"] = ("%03d"):format(tonumber(Switch.ID)),
				["2"] = Names[(f[1])],
				["4"] = c,
				["5"] = f[2] .. level,
				["all"] = Encounters["Chances"][c][e] .. "%",
				["type1"] = firstToUpper(Switch.Type1),
				["type2"] = firstToUpper(Type2),
				}
			} .. "\n")
			end
			end
		end
	if IsSpecial == "yes" then
	table.insert(wikitext, Frame:getParent():expandTemplate{title = "catch/footer", args = {
		["1"] = Type
		}
	} .. "\n")
	else
	table.insert(wikitext, Frame:getParent():expandTemplate{title = "catch/div", args = {
		["1"] = "Road",
		["2"] = "Special"
		}
	})
		end
	end
	end
	return table.concat(wikitext)
end
------------------------------------------------------------ Search --------------------------------------------------------------
function p.Search(Frame)
	local Modul=Frame.args[1]
	local Pokemon=Frame.args[2]
	local InfoType=Frame.args[3]
	local InfoLocation=Frame.args[4]
	if Modul == "Species" then
		Modul = Species
	elseif Modul == "Moves" then
		Modul = Moves
	elseif Modul == "Encounters" then
		Modul = Encounters
	elseif Modul == "Forms" then
		Modul = Forms
	end
	if InfoLocation == "0" then
		if InfoType == "0" then
			return Modul[Pokemon]
		elseif InfoType == "Type" or InfoType == "Type1" or InfoType == "Type2" then
			return firstToUpper(Modul[Pokemon][InfoType])
		end
	else return Modul[Pokemon][InfoType][InfoLocation]
	end
end

return p
