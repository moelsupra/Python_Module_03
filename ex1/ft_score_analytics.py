import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) > 1:
        try:
            scores = []
            for arg in sys.argv[1:]:
                scores.append(int(arg))
            length = len(scores)
            total = sum(scores)
            high = max(scores)
            low = min(scores)
            print(f"Scores processed: {scores}")
            print(f"Total players: {length}")
            print(f"Total score: {total}")
            print(f"Average score: {total / length}")
            print(f"High score: {high}")
            print(f"Low score: {low}")
            print(f"Score range: {high - low}")
        except ValueError:
            print(f"oops, I typed {arg} instead of a number "
                  f"for example '1000'")
    else:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ..."
              )


if __name__ == "__main__":
    main()
