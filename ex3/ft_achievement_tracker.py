def main() -> None:
    print("=== Achievement Tracker System ===")

    alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    bob = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie = {"level_10", "treasure_hunter", "boss_slayer",
               "speed_demon", "perfectionist"}

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    unique_achievements = alice.union(bob, charlie)
    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    print()
    print(f"Common to all players: "
          f"{alice.intersection(bob).intersection(charlie)}")

    rare_1 = alice.difference(bob.union(charlie))
    rare_2 = bob.difference(charlie.union(alice))
    rare_3 = charlie.difference(alice.union(bob))

    rare = rare_1.union(rare_2, rare_3)
    print(f"Rare achievements (1 player): {rare}")

    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")

    print("\nwho's missing what achievements\n")
    print(f"\nAlice missing: {unique_achievements.difference(alice)}")
    print(f"Bob missing: {unique_achievements.difference(bob)}")
    print(f"Charlie missing: {unique_achievements.difference(charlie)}")

    print("\nshared accomplishments\n")
    print(f"Alice & Bob share: {alice.intersection(bob)}")
    print(f"Alice & Charlie share: {alice.intersection(charlie)}")
    print(f"Bob & Charlie share: {bob.intersection(charlie)}")


if __name__ == "__main__":
    main()
