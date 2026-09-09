import time


def wait_for_network() -> None:
    time.sleep(0.7)


def crunch_numbers() -> None:
    total = 0
    for i in range(15_000_000):
        total += i


def step(name: str, function) -> None:
    wall_start = time.perf_counter()
    cpu_start = time.process_time()
    function()
    wall = time.perf_counter() - wall_start
    cpu = time.process_time() - cpu_start
    print(f"{name:<16} wall {wall:.2f} s   cpu {cpu:.2f} s")


print("Everything below runs in ONE thread, top to bottom:\n")

program_start = time.perf_counter()
step("wait_network", wait_for_network)
step("crunch", crunch_numbers)
step("wait_network", wait_for_network)
step("crunch", crunch_numbers)
print(f"\ntotal wall time: {time.perf_counter() - program_start:.2f} s")