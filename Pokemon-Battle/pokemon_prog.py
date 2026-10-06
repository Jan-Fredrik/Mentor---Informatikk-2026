import json
import random
from builtins import print
from time import sleep

import pygame



# ------------ Funksjoner -----------

def player_attack():
    print("\nChoose your attack:")

    for number, attack in enumerate(current_pokemon_player["attacks"], start=1):
        print(f"{number}: {attack["name"]}")

    while True:
        choice = int(input("\nChoice (number): "))

        if 1 <= choice <= len(current_pokemon_player["attacks"]):
            break

        print("Invalid choice! Try again.")

    chosen_attack = current_pokemon_player["attacks"][choice - 1]

    damage = chosen_attack["damage"]
    current_pokemon_rival["HP"] -= damage

    if current_pokemon_rival["HP"] < 0:
        current_pokemon_rival["HP"] = 0

    print(f"{current_pokemon_player['name']} used {chosen_attack['name']}!")
    print(f"It did {damage} damage!")


    print(f"{current_pokemon_rival["name"]} has {current_pokemon_rival['HP']} HP left.")



def rival_attack():
    attack = random.choice(current_pokemon_rival["attacks"])

    damage = attack["damage"]
    current_pokemon_player["HP"] -= damage

    print(f"\n{current_pokemon_rival['name']} used {attack['name']}!")
    print(f"It did {damage} damage!")

    if current_pokemon_player["HP"] < 0:
        current_pokemon_player["HP"] = 0


    if current_pokemon_player["HP"] > 0:
        print(f"{current_pokemon_player['name']} now has {current_pokemon_player['HP']} HP\n")


def HP_checks():

    player_hp1 = player_pokemon[0]["HP"]
    player_hp2 = player_pokemon[1]["HP"]

    rival_hp1 = rival_pokemon[0]["HP"]
    rival_hp2 = rival_pokemon[1]["HP"]

    if player_hp1 <= 0 and player_hp2 <= 0:
        print(f"{rival_player_name} has won !!")
        pygame.mixer.music.stop()
        pygame.mixer.music.load("music/lose.mp3")
        pygame.mixer.music.play()
        sleep(12)

        return True

    elif rival_hp1 <= 0 and rival_hp2 <= 0:
        print(f"{player_name} has won !!")

        pygame.mixer.music.stop()
        pygame.mixer.music.load("music/victory.mp3")
        pygame.mixer.music.play()
        sleep(13)
        return True

    return False

def pokemon_death_check():
    global current_pokemon_player
    global current_pokemon_rival

    if current_pokemon_player["HP"] <= 0:
        current_pokemon_player["HP"] = 0
        print(f"{current_pokemon_player['name']} has fainted!!")

        if current_pokemon_player == player_pokemon[0]:
            current_pokemon_player = player_pokemon[1]
            print(f"{current_pokemon_player['name']} has entered the field !!")

    if current_pokemon_rival["HP"] <= 0:
        current_pokemon_rival["HP"] = 0
        print(f"{current_pokemon_rival['name']} has fainted !!")

        if current_pokemon_rival == rival_pokemon[0]:
            current_pokemon_rival = rival_pokemon[1]
            print(f"{current_pokemon_rival['name']} has entered the field !!")

# -------------------------------------------------------------

pygame.mixer.init()
print()
print()
print("------ Welcome to Pokemon battle ------\n")

pygame.mixer.music.load("music/start_music.mp3")
pygame.mixer.music.play()

sleep(11)

pygame.mixer.music.load("music/lobby.mp3")
pygame.mixer.music.play()

player_name = input("Oak: What is your name?: ")
rival_player_name = input("Oak: What is my grandsons name? (excuse my dementia): ")



# Innlesning av pokemon fila
with open("pokemon.json", "r") as file:
    pokemon_data = json.load(file)

print("\nYou have to choose which 2 pokemon's you want to use!\n")


for number, pokemon in enumerate(pokemon_data["pokemon"], start=1):
    print(f"{number}: {pokemon["name"]}")

choice1 = int(input("\nChoose your first Pokemon: "))
choice2 = int(input("Choose your second Pokemon: "))



player_pokemon = []

player_pokemon.append(pokemon_data["pokemon"][choice1 - 1])
player_pokemon.append(pokemon_data["pokemon"][choice2 - 1])



# Shuffler dictsene i pokemon_data
random.shuffle(pokemon_data["pokemon"])

rival_pokemon = []

for pokemon in pokemon_data["pokemon"]:
    if len(rival_pokemon) == 2:
        break

    if pokemon not in player_pokemon:
        rival_pokemon.append(pokemon)

pygame.mixer.music.stop()

pygame.mixer.music.load("music/battle.mp3")
pygame.mixer.music.play()

print()
print(" ----- Commence battle! ----- \n")
print("BLRBRLLBRLBRLBLRLBRLblrblblrbr....")
print("dun dun, dun-dun dun DUH' dun dun..\n")

sleep(5)

current_pokemon_player = player_pokemon[0]
current_pokemon_rival = rival_pokemon[0]

print(f"{player_name}'s current pokemon is: {current_pokemon_player["name"]}")
print(f"{rival_player_name}'s current pokemon is: {current_pokemon_rival["name"]}\n")




while True:
    player_attack()
    pokemon_death_check()
    if HP_checks():
        break


    rival_attack()
    pokemon_death_check()
    if HP_checks():
        break

