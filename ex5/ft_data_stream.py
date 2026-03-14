import typing


def game_event_generator(count: int) -> typing.Generator:
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]
    levels = [5, 12, 8]
    i = 0
    while i < count:
        yield {
            "player": players[i % 3],
            "level": levels[i % 3],
            "action": actions[i % 3]
        }
        i += 1


def filter_high_level(
    generator: typing.Generator, min_level: int
) -> typing.Generator:
    for event in generator:
        if event["level"] >= min_level:
            yield event


def fibonacci_generator() -> typing.Generator:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_generator() -> typing.Generator:
    num = 2
    while True:
        is_prime = True
        i = 2
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            yield num
        num += 1


def main() -> None:
    print("=== Game Data Stream Processor ===")
    print("Processing 1000 game events...\n")

    events = game_event_generator(1000)

    i = 0
    while i < 3:
        event = next(events)
        print(f"Event {i + 1}: Player {event['player']}"
              f" (level {event['level']}) {event['action']}")
        i += 1
    print("...")

    total = 0
    high_level = 0
    treasure = 0
    levelup = 0
    for event in events:
        total += 1
        if event["level"] >= 10:
            high_level += 1
        if event["action"] == "found treasure":
            treasure += 1
        if event["action"] == "leveled up":
            levelup += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total + 3}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {levelup}")

    print("\n=== Memory Efficiency ===")
    list_size = 1000 * 3
    generator_size = 1
    print(f"List approach: ~{list_size} values in memory at once")
    print(f"Generator approach: ~{generator_size} value in memory at once")
    print("Memory saved: generators use constant O(1) space!")

    print("\n=== Batch Processing (High Level Events) ===")
    batch = game_event_generator(1000)
    high_events = filter_high_level(batch, 10)
    count = 0
    for event in high_events:
        count += 1
    print(f"High level events (level >= 10): {count}")

    print("\n=== Generator Demonstration ===")
    fib = fibonacci_generator()
    print("Fibonacci sequence (first 10): ", end="")
    i = 0
    while i < 10:
        val = next(fib)
        if i < 9:
            print(val, end=", ")
        else:
            print(val)
        i += 1

    prime = prime_generator()
    print("Prime numbers (first 5): ", end="")
    i = 0
    while i < 5:
        val = next(prime)
        if i < 4:
            print(val, end=", ")
        else:
            print(val)
        i += 1


if __name__ == "__main__":
    main()

    # *Test*
    # events = []
    # i = 0
    # while i < 10000000:
    #     events.append({'player': 'alice', 'level': 1, 'action': 'kill'})
    #     i += 1
    # print('list done')
    # def gen(n):
    #     i = 0
    #     while i < n:
    #         yield {'player': 'alice', 'level': 1, 'action': 'kill'}
    #         i += 1
    # for e in gen(10000000):
    #     pass
    # print('generator done')
