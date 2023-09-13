from characters import Erik
from characters import Mono
from characters import viki
from characters import Vladimir

def getQuotes(level):
    if level == 0:
        return Erik.getQuotes()
    if level == 1:
        return viki.getQuotes()
    if level == 2:
        return Mono.getQuotes()
    if level == 3:
        return Vladimir.getQuotes()

def getEnemySprite(level):
    if level == 0:
        return Erik.getArt()
    if level == 1:
        return viki.getArt()
    if level == 2:
        return Mono.getArt()
    if level == 3:
        return Vladimir.getArt()

def getAttackSprite(level, attack):
    if level == 0:
        if attack == 3:
            return Erik.getFinalAttack()
        return Erik.getAttack()
    if level == 1:
        if attack == 3:
            return viki.getFinalAttack()
        return viki.getAttack()
    if level == 2:
        if attack == 3:
            return Mono.getFinalAttack()
        return Mono.getAttack()
    if level == 3:
        if attack == 3:
            return Vladimir.getFinalAttack()
        return Vladimir.getAttack()

def getNumBullets(level, attack):
    if level == 0:
        if attack == 3:
            return Erik.getFinalNumBullets()
        return Erik.getNumBullets()
    if level == 1:
        if attack == 3:
            return viki.getFinalNumBullets()
        return viki.getNumBullets()
    if level == 2:
        if attack == 3:
            return Mono.getFinalNumBullets()
        return Mono.getNumBullets()
    if level == 3:
        if attack == 3:
            return Vladimir.getFinalNumBullets()
        return Vladimir.getNumBullets()