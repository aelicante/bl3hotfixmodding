#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

def set_pool(mod, pool_to_set, balances, char=None):

    parts = []
    for bal in balances:
        if type(bal) is tuple:
            (bal1, bal2) = bal
        else:
            bal1 = bal
            bal2 = bal
        part = '(InventoryBalanceData={},ResolvedInventoryBalanceData=InventoryBalanceData\'"{}"\',Weight=(BaseValueConstant=1))'.format(
                bal1,
                bal2,
                )
        parts.append(part)
    if char is None:
        hf_subtype = Mod.PATCH
        hf_pkg = ''
    else:
        hf_subtype = Mod.CHAR
        hf_pkg = char
    mod.reg_hotfix(hf_subtype, hf_pkg,
            pool_to_set,
            'BalancedItems',
            '({})'.format(','.join(parts)))

mod = Mod('testing_loot_drops.txt',
        'Testing loot drops...',
        [],
        'Drops',
        )

do_pool_set = True

# This one's my usual 'rotating' pool that gets used
pool_to_set = '/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SnipeRifles_Legendary'
#pool_to_set = '/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Legendary'
#pool_to_set = '/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_05_Legendary'
#pool_to_set = '/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_05_Legendary'
#pool_to_set = '/Game/Gear/Artifacts/_Design/ItemPools/ItemPool_Artifacts_05_Legendary'
#pool_to_set = '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_05_Legendary'
#pool_to_set = '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Beastmaster_05_Legendary'
#pool_to_set = '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Gunner_05_Legendary'
#pool_to_set = '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Operative_05_Legendary'
#pool_to_set = '/Game/Gear/Artifacts/_Design/ItemPools/ItemPool_Artifacts_03_Rare'
#pool_to_set = '/Game/Gear/Artifacts/_Design/ItemPools/ItemPool_Artifacts'

# Hoovering up cosmetics
#pool_to_set = '/Game/GameData/Loot/ItemPools/ItemPool_SkinsAndMisc'
#pool_to_set = '/Game/Pickups/Customizations/_Design/ItemPools/Heads/ItemPool_Customizations_Heads_Loot_Siren'
#pool_to_set = '/Game/Pickups/Customizations/_Design/ItemPools/Heads/ItemPool_Customizations_Heads_Loot_Beastmaster'
#pool_to_set = '/Game/Pickups/Customizations/_Design/ItemPools/Heads/ItemPool_Customizations_Heads_Loot_Gunner'
#pool_to_set = '/Game/Pickups/Customizations/_Design/ItemPools/PlayerRoomDeco/ItemPool_Customizations_RoomDeco_Loot'
#pool_to_set = '/Game/Gear/WeaponTrinkets/_Design/ItemPools/ItemPool_Customizations_WeaponTrinkets_Loot'
#pool_to_set = '/Game/PlayerCharacters/_Customizations/EchoDevice/ItemPools/ItemPool_Customizations_Echo_Loot'
#pool_to_set = '/Game/Gear/WeaponSkins/_Design/ItemPools/ItemPool_Customizations_WeaponSkins_Loot'

balances = [
        #'/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Devestator/Balance/Balance_PS_TOR_Devestator.Balance_PS_TOR_Devestator',
        #'/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Sabre/Balance/Balance_PS_Tediore_Sabre.Balance_PS_Tediore_Sabre',
        #'/Game/Gear/GrenadeMods/_Design/_Unique/ObviousTrap/Balance/InvBalD_GM_ObviousTrap.InvBalD_GM_ObviousTrap',
        #'/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Balance/Balance_MAL_SR_LGD_Storm.Balance_MAL_SR_LGD_Storm',
        #'/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Magnificent/Balance/Balance_PS_VLA_Magnificent.Balance_PS_VLA_Magnificent',

        # Bloody Harvest shenanigans
        #'/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Maggie/Balance/Balance_PS_JAK_Maggie.Balance_PS_JAK_Maggie',
        #'/Game/PatchDLC/BloodyHarvest/Gear/Weapons/SniperRifles/Dahl/_Design/_Unique/Frostbolt/Balance/Balance_SR_DAL_ETech_Frostbolt.Balance_SR_DAL_ETech_Frostbolt',
        #'/Game/Gear/GrenadeMods/_Design/_Unique/ObviousTrap/Balance/InvBalD_GM_ObviousTrap.InvBalD_GM_ObviousTrap',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/westergun/Balance/Balance_SM_MAL_westergun.Balance_SM_MAL_westergun',

        # Playing around with modding Maliwan charge times, here's some spawns for Maliwan guns
        #'/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/BalanceState/Balance_PS_MAL_04_VeryRare.Balance_PS_MAL_04_VeryRare',
        #'/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/BalanceState/Balance_SG_MAL_04_VeryRare.Balance_SG_MAL_04_VeryRare',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/BalanceState/Balance_SM_MAL_04_VeryRare.Balance_SM_MAL_04_VeryRare',
        #'/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Balance/Balance_MAL_SR_04_VeryRare.Balance_MAL_SR_04_VeryRare',
        #'/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/MAL/Balance/Balance_PS_MAL_ETech_Rare.Balance_PS_MAL_ETech_Rare',
        #'/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Maliwan/Balance/Balance_SG_MAL_ETech_VeryRare.Balance_SG_MAL_ETech_VeryRare',
        #'/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SMGs/Maliwan/Balance/Balance_SM_MAL_ETech_VeryRare.Balance_SM_MAL_ETech_VeryRare',
        #'/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SniperRifles/Maliwan/Balance/Balance_SR_MAL_ETech_VeryRare.Balance_SR_MAL_ETech_VeryRare',

        # Maliwan uniques/legendaries
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/E3/Balance_SM_MAL_E3.Balance_SM_MAL_E3',
        #'/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Hellshock/Balance/Balance_PS_MAL_Hellshock.Balance_PS_MAL_Hellshock',
        #'/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Plumber/Balance/Balance_PS_MAL_Plumber.Balance_PS_MAL_Plumber',
        #'/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/ThunderballFist/Balance/Balance_PS_MAL_ThunderballFists.Balance_PS_MAL_ThunderballFists',
        #'/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/HyperHydrator/Balance/Balance_PS_MAL_HyperHydrator.Balance_PS_MAL_HyperHydrator',
        #'/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Starkiller/Balance/Balance_PS_MAL_Starkiller.Balance_PS_MAL_Starkiller',
        #'/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/SuckerPunch/Balance/Balance_PS_MAL_SuckerPunch.Balance_PS_MAL_SuckerPunch',
        #'/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Recursion/Balance/Balance_SG_MAL_Recursion.Balance_SG_MAL_Recursion',
        #'/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Trev/Balance/Balance_SG_MAL_Trev.Balance_SG_MAL_Trev',
        #'/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Wisp/Balance/Balance_SG_MAL_Wisp.Balance_SG_MAL_Wisp',
        #'/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/MouthPiece2/Balance/Balance_SG_MAL_Mouthpiece2.Balance_SG_MAL_Mouthpiece2',
        #'/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Shriek/Balance/Balance_SG_MAL_Shriek.Balance_SG_MAL_Shriek',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Cutsman/Balance/Balance_SM_MAL_Cutsman.Balance_SM_MAL_Cutsman',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/DestructoSpin/Balance/Balance_SM_MAL_DestructoSpin.Balance_SM_MAL_DestructoSpin',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Devoted/Balance/Balance_SM_MAL_Devoted.Balance_SM_MAL_Devoted',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Balance/Balance_SM_MAL_CloudKill.Balance_SM_MAL_CloudKill',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Crit/Balance/Balance_SM_MAL_Crit.Balance_SM_MAL_Crit',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Egon/Balance/Balance_SM_MAL_Egon.Balance_SM_MAL_Egon',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Emporer/Balance/Balance_SM_MAL_Emporer.Balance_SM_MAL_Emporer',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Kevins/Balance/Balance_SM_MAL_Kevins.Balance_SM_MAL_Kevins',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Tsunami/Balance/Balance_SM_MAL_Tsunami.Balance_SM_MAL_Tsunami',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/VibraPulse/Balance/Balance_SM_MAL_VibraPulse.Balance_SM_MAL_VibraPulse',
        #'/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/westergun/Balance/Balance_SM_MAL_westergun.Balance_SM_MAL_westergun',
        #'/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Balance/Balance_MAL_SR_ASMD.Balance_MAL_SR_ASMD',
        #'/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Krakatoa/Balance/Balance_MAL_SR_Krakatoa.Balance_MAL_SR_Krakatoa',
        #'/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Balance/Balance_MAL_SR_LGD_Storm.Balance_MAL_SR_LGD_Storm',
        #'/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Soleki/Balance/Balance_MAL_SR_Soleki.Balance_MAL_SR_Soleki',

        # Ha ha!  Figured out getting head/skin drops!
        #'/Game/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_1.InvBal_CustomSkin_Siren_1',

        # Weird, orphaned ECHO skin, not sure if this is droppable.
        '/Game/UI/_Shared/CustomIconsEcho/ECHOTheme_35.InvBal_ECHOTheme_35',

        # Bloody Harvest rewards:
        #'/Game/PatchDLC/BloodyHarvest/Gear/Weapons/WeaponTrinkets/_Shared/Trinket_League_BloodyHarvest_1.InvBal_Trinket_League_BloodyHarvest_1',
        #'/Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_11.InvBal_ECHOTheme_11',
        #'/Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/Beastmaster/Skins/CustomSkin_Beastmaster_40.InvBal_CustomSkin_Beastmaster_40',
        #'/Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/Gunner/Skins/CustomSkin_Gunner_40.InvBal_CustomSkin_Gunner_40',
        #'/Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/Operative/Skins/CustomSkin_Operative_40.InvBal_CustomSkin_Operative_40',
        #'/Game/PatchDLC/BloodyHarvest/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_40.InvBal_CustomSkin_Siren_40',
        #'/Game/PatchDLC/BloodyHarvest/Gear/Weapons/WeaponSkins/WeaponSkin_BloodyHarvest_01.InvBal_WeaponSkin_BloodyHarvest_01',

        # NOG Heads:
        #'/Game/PlayerCharacters/_Customizations/Beastmaster/Heads/CustomHead_Beastmaster_22.InvBal_CustomHead_Beastmaster_22',
        #'/Game/PlayerCharacters/_Customizations/Gunner/Heads/CustomHead_Gunner_22.InvBal_CustomHead_Gunner_22',
        #'/Game/PlayerCharacters/_Customizations/Operative/Heads/CustomHead_Operative_22.InvBal_CustomHead_Operative_22',
        #'/Game/PlayerCharacters/_Customizations/SirenBrawler/Heads/CustomHead_Siren_22.InvBal_CustomHead_Siren_22',

        # Golden weapon skin + trinket.  Technically we already have these, as it turns out, but they're not
        # active unless you actually have the preorder "DLC" or whatever.
        #'/Game/Gear/WeaponSkins/_Design/SkinParts/WeaponSkin_21.InvBal_WeaponSkin_21',
        #'/Game/Gear/WeaponTrinkets/_Design/TrinketParts/WeaponTrinket_51.InvBal_WeaponTrinket_51',

        # Maliwan Takedown weapons
        # Redistributor
        #'/Game/PatchDLC/Raid1/Gear/Weapons/Fork2/Balance/Balance_SM_HYP_Fork2.Balance_SM_HYP_Fork2',
        # Moonfire
        #'/Game/PatchDLC/Raid1/Gear/Weapons/HandCannon/Balance/Balance_PS_TOR_HandCannon.Balance_PS_TOR_HandCannon',
        # Kyb's Worth
        #'/Game/PatchDLC/Raid1/Gear/Weapons/KybsWorth/Balance/Balance_SM_MAL_KybsWorth.Balance_SM_MAL_KybsWorth',
        # P2P Networker
        #'/Game/PatchDLC/Raid1/Gear/Weapons/Link/Balance/Balance_SM_MAL_Link.Balance_SM_MAL_Link',
        # Tiggs' Boom
        #'/Game/PatchDLC/Raid1/Gear/Weapons/TiggsBoom/Balance/Balance_SG_Torgue_TiggsBoom.Balance_SG_Torgue_TiggsBoom',

        # Maliwan Takedown Shields
        # Version 0.m
        #'/Game/PatchDLC/Raid1/Gear/Shields/VersionOmNom/Balance/InvBalD_Shield_Legendary_VersionOmNom.InvBalD_Shield_Legendary_VersionOmNom',
        # Re-Charger Berner
        #'/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/ReCharger_Berner/InvBalD_Shield_LGD_ReCharger_Berner.InvBalD_Shield_LGD_ReCharger_Berner',
        # Frozen Snowshoe
        #'/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_FrozenHeart/Balance/InvBalD_Shield_SlideKickFrozenHeart.InvBalD_Shield_SlideKickFrozenHeart',
        # Re-Charger variant
        #'/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_Recharger/InvBalD_Shield_SlideKickRecharger.InvBalD_Shield_SlideKickRecharger',

        # Maliwan Takedown COMs
        # R4kk P4k
        #'/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/InvBalD_CM_Beastmaster_Raid1.InvBalD_CM_Beastmaster_Raid1',
        # Raging Bear
        #'/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/GUN/InvBalD_CM_Gunner_Raid1.InvBalD_CM_Gunner_Raid1',
        # Antifreeze
        #'/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/OPE/InvBalD_CM_Operative_Raid1.InvBalD_CM_Operative_Raid1',
        # Spiritual Driver
        #'/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/SRN/InvBalD_CM_Siren_Raid1.InvBalD_CM_Siren_Raid1',

        # Mayhem 4 Gear:
        # Crader's EM-P5
        #'/Game/PatchDLC/Raid1/Re-Engagement/Weapons/CraderMP5/Balance/Balance_SM_DAHL_CraderMP5.Balance_SM_DAHL_CraderMP5',
        # Vosk's Deathgrip
        #'/Game/PatchDLC/Raid1/Re-Engagement/Weapons/DeathGrip/Balance/Balance_SG_MAL_DeathGrip.Balance_SG_MAL_DeathGrip',
        # S3RV-80S-EXECUTE
        #'/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Execute/Balance/Balance_PS_TED_Execute.Balance_PS_TED_Execute',
        # Good Juju
        #'/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juju/Balance/Balance_DAL_AR_ETech_Juju.Balance_DAL_AR_ETech_Juju',
        # Juliet's Dazzle
        #'/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juliet/Balance/Balance_AR_TOR_Juliet.Balance_AR_TOR_Juliet',
        #'/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juliet/Balance/Balance_AR_TOR_Juliet_WorldDrop.Balance_AR_TOR_Juliet_WorldDrop',
        # Tankman's Shield
        #'/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Tankman/Balance/Balance_SR_HYP_Tankman.Balance_SR_HYP_Tankman',
        # Zheitsev's Eruption
        #'/Game/PatchDLC/Raid1/Re-Engagement/Weapons/ZheitsevEruption/Balance/Balance_AR_COV_Zheitsev.Balance_AR_COV_Zheitsev',

        # More Maliwan Takedown patch additions, dunno what's up with these.  They seem to be basically identical
        # to their non-Maliwan-Takedown counterparts.
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/CommanderPlanetoid/InvBalD_Artifact_CommanderPlanetoid.InvBalD_Artifact_CommanderPlanetoid',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/CosmicCrater/InvBalD_Artifact_CosmicCrater.InvBalD_Artifact_CosmicCrater',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/Deathless/InvBalD_Artifact_Deathless.InvBalD_Artifact_Deathless',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/LoadedDice/InvBalD_Artifact_LoadedDice.InvBalD_Artifact_LoadedDice',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/MoxxisEndowment/InvBalD_Artifact_MoxxisEndowment.InvBalD_Artifact_MoxxisEndowment',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/OttoIdol/InvBalD_Artifact_OttoIdol.InvBalD_Artifact_OttoIdol',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/PullOutMethod/InvBalD_Artifact_PullOutMethod.InvBalD_Artifact_PullOutMethod',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/RocketBoots/InvBalD_Artifact_RocketBoots.InvBalD_Artifact_RocketBoots',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/Safegaurd/InvBalD_Artifact_Safegaurd.InvBalD_Artifact_Safegaurd',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/Salvo/InvBalD_Artifact_Salvo.InvBalD_Artifact_Salvo',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/SplatterGun/InvBalD_Artifact_SplatterGun.InvBalD_Artifact_SplatterGun',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/StaticTouch/InvBalD_Artifact_StaticTouch.InvBalD_Artifact_StaticTouch',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/VictoryRush/InvBalD_Artifact_VictoryRush.InvBalD_Artifact_VictoryRush',
        #'/Game/PatchDLC/Raid1/Gear/Artifacts/WhiteElephant/InvBalD_Artifact_WhiteElephant.InvBalD_Artifact_WhiteElephant',

        # Probably the same story, just with Siren COMs this time...
        #'/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Breaker.InvBalD_ClassMod_Siren_Breaker',
        #'/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Dragon.InvBalD_ClassMod_Siren_Dragon',
        #'/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Elementalist.InvBalD_ClassMod_Siren_Elementalist',
        #'/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Nimbus.InvBalD_ClassMod_Siren_Nimbus',
        #'/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Phasezerker.InvBalD_ClassMod_Siren_Phasezerker',

        # DLC1 (Dandelion) weapons
        #'/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/AutoAime/Balance/Balance_SR_DAL_AutoAime.Balance_SR_DAL_AutoAime',
        #'/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Boomer/Balance/Balance_SM_DAL_Boomer.Balance_SM_DAL_Boomer',
        #'/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/CheapTips/Balance/Balance_SM_HYP_CheapTips.Balance_SM_HYP_CheapTips',
        #'/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Craps/Balance/Balance_PS_TOR_Craps.Balance_PS_TOR_Craps',
        #'/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Creamer/Balance/Balance_HW_TOR_Creamer.Balance_HW_TOR_Creamer',
        #'/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Digby/Balance/Balance_DAL_AR_Digby.Balance_DAL_AR_Digby',
        #'/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/EmbersPurge/Balance/Balance_SM_MAL_EmbersPurge.Balance_SM_MAL_EmbersPurge',
        #'/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/HeartBreaker/Balance/Balance_SG_HYP_HeartBreaker.Balance_SG_HYP_HeartBreaker',
        #'/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonCannon/Balance/Balance_HW_VLA_IonCannon.Balance_HW_VLA_IonCannon',
        #'/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonLaser/Balance/Balance_SM_MAL_IonLaser.Balance_SM_MAL_IonLaser',
        #'/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/JustCaustic/Balance/Balance_SM_HYP_JustCaustic.Balance_SM_HYP_JustCaustic',
        #'/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Lucky7/Balance/Balance_PS_JAK_Lucky7.Balance_PS_JAK_Lucky7',
        #'/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/MeltFacer/Balance/Balance_SG_HYP_MeltFacer.Balance_SG_HYP_MeltFacer',
        #'/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Nukem/Balance/Balance_HW_TOR_Nukem.Balance_HW_TOR_Nukem',
        #'/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/RoboMasher/Balance/Balance_PS_JAK_RoboMasher.Balance_PS_JAK_RoboMasher',
        #'/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Scoville/Balance/Balance_PS_TOR_Scoville.Balance_PS_TOR_Scoville',
        #'/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/SlowHand/Balance/Balance_SG_HYP_SlowHand.Balance_SG_HYP_SlowHand',
        #'/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Trash/Balance/Balance_AR_COV_Trash.Balance_AR_COV_Trash',
        #'/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Varlope/Balance/Balance_AR_TOR_Varlope.Balance_AR_TOR_Varlope',

        # DLC1 (Dandelion) Shields
        #'/Game/PatchDLC/Dandelion/Gear/Shield/Clover/Balance/InvBalD_Shield_Clover.InvBalD_Shield_Clover',
        #'/Game/PatchDLC/Dandelion/Gear/Shield/DoubleDowner/Balance/InvBalD_Shield_DoubleDowner.InvBalD_Shield_DoubleDowner',
        #'/Game/PatchDLC/Dandelion/Gear/Shield/Ember/Balance/InvBalD_Shield_Ember.InvBalD_Shield_Ember',
        #'/Game/PatchDLC/Dandelion/Gear/Shield/Rico/Balance/InvBalD_Shield_Rico.InvBalD_Shield_Rico',

        # DLC1 (Dandelion) Grenades
        #'/Game/PatchDLC/Dandelion/Gear/Grenade/AcidBurn/Balance/InvBalD_GM_AcidBurn.InvBalD_GM_AcidBurn',
        #'/Game/PatchDLC/Dandelion/Gear/Grenade/Slider/Balance/InvBalD_GM_TED_Slider.InvBalD_GM_TED_Slider',
        ]

# Set the pool, if we've been told to
if do_pool_set:
    last_bit = pool_to_set.split('/')[-1]
    set_pool(mod, '{}.{}'.format(pool_to_set, last_bit), balances)

# TODO: Would like to get trash piles back in here too, though I think we'd
# have to have a level hotfix for each level, and I don't feel like scripting
# that out yet.
#
# These definitions *should* be pretty thorough, though note that bosses and
# minibosses have been left alone, since I'm only gonna be mobbing while
# testing this stuff.

for (pool, chars) in [

        # Base-game Standard Enemy drop list
        ('/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear', [

            # TODO: This isn't always sufficient; if you spawn in Floodmoor Basin, for
            # instance, the enemies around the lodge area don't trigger it, nor do Saurians
            # in Floodmoor Basin.  Saurians in particular have proven difficult; even
            # enumerating all the BPChar* entries which reference the "Shared" one didn't
            # seem to do it.  Hrmph.  Giving up for now!
            'BPChar_Ape',
            'BPChar_EnforcerShared',
            'BPChar_Frontrunner',
            'BPChar_Goon',
            'BPChar_GuardianShared',
            'BPChar_Heavy_Shared',
            'BPChar_Nekrobug_Shared',
            'BPChar_Nog',
            'BPChar_OversphereShared',
            'BPChar_PsychoShared',
            'BPChar_PunkShared',
            'BPChar_Rakk',
            'BPChar_Ratch',
            'BPChar_Saurian_Shared',

            # These are all the BPChars which reference BPChar_Saurian_Shared...
            #'BPChar_Saurian_Grog_Poison_Fodder',
            #'BPChar_SaurianLaser',
            #'BPChar_SaurianShield',
            #'BPChar_Saurian_SlaughterBoss',
            #'BPChar_Saurian_TrialBoss',
            #'BPChar_Saurian_Grog',
            #'BPChar_Saurian_Grog_Fire',
            #'BPChar_Saurian_Grog_Poison',
            #'BPChar_Saurian_Hamtaurus',
            #'BPChar_Saurian_Hamtaurus_Badass',
            #'BPChar_Saurian_Predator',
            #'BPChar_Saurian_Predator_X',
            #'BPChar_Saurian_Pygmimus',
            #'BPChar_SaurianShiny',
            #'BPChar_Saurian_Slinger',
            #'BPChar_Saurian_Tyrant',
            #'BPChar_SaurianForager',

            'BPChar_ServiceBot',
            'BPChar_SkagShared',
            'BPChar_Spiderant',
            'BPChar_Tink',
            'BPChar_Tink_Turret',
            'BPChar_Trooper',
            'BPChar_VarkidShared',
            'BPChar_LootTracker',

            # Maliwan Takedown
            'BPChar_MechBasicMini',
            'BPChar_MechMeleeMini',

            # Moxxi's Heist
            'BPChar_EnforcerShared_Stripped',
            'BPChar_Goon_Stripped',
            'BPChar_PsychoShared_Stripped',
            'BPChar_PunkShared_Stripped',
            'BPChar_TinkStripped',
            ]),

        # Goliaths
        ('/Game/GameData/Loot/ItemPools/Goliath/ItemPoolList_Goliath_Godliath', ['BPChar_Goliath', 'BPChar_Goliath_Stripped']),
        ('/Game/GameData/Loot/ItemPools/Goliath/ItemPoolList_Goliath_NonEnraging', ['BPChar_Goliath', 'BPChar_Goliath_Stripped']),
        ('/Game/GameData/Loot/ItemPools/Goliath/ItemPoolList_Goliath_Ultimate', ['BPChar_Goliath', 'BPChar_Goliath_Stripped']),
        ('/Game/GameData/Loot/ItemPools/Goliath/ItemPoolList_Goliath_SuperRaging', ['BPChar_Goliath', 'BPChar_Goliath_Stripped']),
        ('/Game/GameData/Loot/ItemPools/Goliath/ItemPoolList_Goliath_MegaRaging', ['BPChar_Goliath', 'BPChar_Goliath_Stripped']),

        # Dandelion standard-enemy drop list
        ('/Game/PatchDLC/Dandelion/GameData/Loot/EnemyPools/ItemPoolList_StandardEnemyGunsandGear_Dandelion', [
            'BPChar_AcidTrip_EarlyPrototype',
            'BPChar_EnforcerBruiser_Looter',
            'BPChar_GoliathBasic_Looter',
            'BPChar_GoliathMidget_Looter',
            'BPChar_GoonBasic_looter',
            'BPChar_GoonVortex_Looter',
            'BPChar_PsychoBasic_Looter',
            'BPChar_PsychoFirebrand_Looter',
            'BPChar_PsychoSlugger_Looter',
            'BPChar_PsychoSuicide_Looter',
            'BPChar_PunkAssaulter_Looter',
            'BPChar_PunkBasic_Looter',
            'BPChar_PunkShotgunner_Looter',
            'BPChar_PunkSniper_Looter',
            'BPChar_TinkBasic_Looter',
            'BPChar_TinkPsycho_Looter',
            'BPChar_TinkShotgun_Looter',
            'BPChar_TinkSuicide_Looter',
            'BPChar_CasinoBot_BigJanitor',
            ]),

        # Dandelion standard-loader drop list
        ('/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/ItemPools/ItemPoolList_StandardEnemyGunsandGearLoader', [
            # Moxxi's Heist
            'BPChar_HyperionTurretBasic',
            'BPChar_LoaderShared',
            'BPChar_WeeLoaderBasic',
            ]),

        # Base game badass enemy drop list
        ('/Game/GameData/Loot/ItemPools/ItemPoolList_BadassEnemyGunsGear', [

            # Base Game (don't actually care about the unique enemies in here, but
            # it was less work to just leave 'em in)
            'BPChar_Ape_Hunt01',
            'BPChar_ApeJungleMonarch',
            'BPChar_ApeBadass',
            'BPChar_ApeLoot',
            'BPChar_Enforcer_BountyPrologue',
            'BPChar_EnforcerUrist',
            'BPChar_EnforcerBadass',
            'BPChar_Frontrunner_Badass',
            'BPChar_Goliath_Badass',
            'BPChar_GoonBadass',
            'BPChar_GuardianGemGoblin',
            'BPChar_GuardianWraithBadass',
            'BPChar_Heavy_Badass',
            'BPChar_Mech',
            'BPChar_Nekrobug_Badass',
            'BPChar_NogBadass',
            'BPChar_NogNogromancer',
            'BPChar_OversphereBadass',
            'BPChar_PsychoBadass',
            'BPChar_Punk_Bounty01a',
            'BPChar_Punk_Bounty01b',
            'BPChar_Punk_Bounty01c',
            'BPChar_Punk_Bounty01d',
            'BPChar_PunkBrewHag',
            'BPChar_PunkMotherOfDragons',
            'BPChar_PunkBadass',
            'BPChar_Rakk_Dragon',
            'BPChar_Rakk_DragonCryo',
            'BPChar_Rakk_Hunt01',
            'BPChar_Rakk_HuntSkrakk',
            'BPChar_RakkBadassCryo',
            'BPChar_RakkChromatic',
            'BPChar_RakkQueen',
            'BPChar_RatchBadass',
            'BPChar_RatchHive',
            'BPChar_Saurian_Grog_Poison',
            'BPChar_Saurian_Hamtaurus_Badass',
            'BPChar_Saurian_Tyrant',
            'BPChar_ServiceBot_SWAT',
            'BPChar_Skag_Rare01',
            'BPChar_SkagBadass',
            'BPChar_SpiderantKing',
            'BPChar_SpiderantQueen',
            'BPChar_Tink_Bounty01',
            'BPChar_TinkRare02',
            'BPChar_TinkUndertaker',
            'BPChar_TinkBadass',
            'BPChar_Tink_SentryRocketPodBigD',
            'BPChar_TrooperBadass',
            'BPChar_VarkidBadass',
            'BPChar_AtlasSoldier_Bounty01',

            # Maliwan Takedown
            'BPChar_Behemoth',

            # Moxxi's Heist
            'BPChar_EnforcerBadass_Stripped',
            'BPChar_Goliath_Badass_Stripped',
            'BPChar_GoonBadass_Stripped',
            'BPChar_PunkBadass_Stripped',
            'BPChar_TinkBadass_Stripped',
            'BPChar_Mimic',
            'BPChar_WeeLoaderShared',
            ]),

        # Dandelion Badass enemy list
        ('/Game/PatchDLC/Dandelion/GameData/Loot/EnemyPools/ItemPoolList_BadassEnemyGunsGear_Dandelion', [
            'BPChar_SisterlyLove_DebtCollectorLoader',
            'BPChar_GreatEscape_Rudy',
            'BPChar_RagingBot_MachineGunMikey',
            'BPChar_EnforcerBadass_Looter',
            'BPChar_Enforcer_PrettyBoy',
            'BPChar_GoliathBadass_Looter',
            'BPChar_GoonBadass_Looter',
            'BPChar_PsychoBadass_Looter',
            'BPChar_PunkArmored_LooterVIP',
            'BPChar_PunkBadass_Looter',
            'BPChar_TinkBadass_Looter',
            'BPChar_TinkBadassArmored_Looter',
            # /Dandelion/Missions/Plot/Ep05_ThePlan/SpawnOption_TricksyNick_Farmable but eh.
            ]),

        # Dandelion Badass loader list
        ('/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/ItemPools/ItemPoolList_BadassEnemyGunsGearLoader1', [
            'BPChar_HyperionTurretBadass',
            'BPChar_LoaderBadass',
            ]),

        # Dandelion Constructors
        ('/Game/PatchDLC/Dandelion/Enemies/Constructor/_Shared/_Design/Balance/ItemPoolList_Constructor', [
            'BPChar_Constructor',
            ]),

        # Anointed Enemies
        ('/Game/GameData/Loot/ItemPools/ItemPoolList_AnointedEnemyGunsGear', [

            'BPChar_EnforcerAnointed',
            'BPChar_Goliath_Anointed',
            'BPChar_GoonAnointed',
            'BPChar_PsychoAnointed',
            'BPChar_Punk_Anointed',
            'BPChar_TinkAnointed',
            'BPChar_VarkidHunt02_LarvaA',
            'BPChar_VarkidHunt02_LarvaB',
            'BPChar_VarkidHunt02_LarvaC',
            'BPChar_VarkidHunt02_LarvaD',
            'BPChar_VarkidSuperBadass',
            ]),

        ]:

    last_bit = pool.split('/')[-1]
    full_pool = '{}.{}'.format(pool, last_bit)

    for char in chars:
        mod.reg_hotfix(Mod.CHAR, char,
                full_pool,
                'ItemPools',
                """(
                    (
                        ItemPool=ItemPoolData'"{}"'
                        PoolProbability=(
                            BaseValueConstant=1,
                            DataTableValue=(DataTable=None,RowName="",ValueName=""),
                            BaseValueAttribute=None,
                            AttributeInitializer=None,
                            BaseValueScale=1
                        ),
                        NumberOfTimesToSelectFromThisPool=(
                            BaseValueConstant=5,
                            DataTableValue=(DataTable=None,RowName="",ValueName=""),
                            BaseValueAttribute=None,
                            AttributeInitializer=None,
                            BaseValueScale=1
                        )
                    )
                )""".format(pool_to_set))

mod.close()
