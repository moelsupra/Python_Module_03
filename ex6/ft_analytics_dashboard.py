def main() -> None:
    print("=== Game Analytics Dashboard ===")
    players = [
        {"name": "alice", "score": 2300, "active": True, 'region': 'north',
            "achievements": ["first_kill", "level_10", "boss_slayer",
                             "speed_demon", "collector"]},
        {"name": "bob", "score": 1800, "active": True, 'region': 'central',
         "achievements": ["first_kill", "level_10", "collector"]},
        {"name": "charlie", "score": 2150, "active": True, 'region': 'central',
         "achievements": ["boss_slayer", "speed_demon", "perfectionist",
                          "level_10", "first_kill", "collector",
                          "treasure_hunter"]},
        {"name": "diana",   "score": 2050, "active": False, 'region': 'east',
         "achievements": ["first_kill", "level_10"]}
    ]
    print()

    print("=== List Comprehension Examples ===")

    high_scorers = [p["name"] for p in players if p["score"] > 2000]
    doubled_scores = [p["score"] * 2 for p in players]
    active_players = [p["name"] for p in players if p["active"]]
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {doubled_scores}")
    print(f"Active players: {active_players}")
    print()

    print("=== Dict Comprehension Examples ===")
    player_scores = {p["name"]: p["score"] for p in players}

    categories = ["high" if p["score"] > 2000
                  else "medium" if p["score"] > 1500
                  else "low" for p in players]
    score_categories = {
        "high":   len([c for c in categories if c == "high"]),
        "medium": len([c for c in categories if c == "medium"]),
        "low":    len([c for c in categories if c == "low"])
    }
    achievement_counts = {p["name"]: len(p["achievements"]) for p in players}
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}")
    print()

    print("=== Set Comprehension Examples ===")
    unique_players = {p["name"] for p in players}
    unique_achievements = {a for p in players for a in p["achievements"]}
    active_regions = {p["region"] for p in players}
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}")
    print()

    print("=== Combined Analysis ===")
    total_players = len(players)
    total_achievements = len(unique_achievements)
    average_score = sum([p["score"] for p in players]) / total_players
    top_score = max([p["score"] for p in players])
    best_player = [p for p in players if p["score"] == top_score]
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_achievements}")
    print(f"Average score: {average_score}")
    print(f"Top performer: {best_player[0]['name']} "
          f"({best_player[0]['score']} points, "
          f"{len(best_player[0]['achievements'])} achievements)")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected error: {e}")
