# dreadnoughtShipBonusLaserCapNeedA1
#
# Used by:
# Ships named like: Revelation (2 of 2)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Dreadnought").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Energy Turret"),
                                  "capacitorNeed", ship.getModifiedItemAttr("dreadnoughtShipBonusA1") * level)
