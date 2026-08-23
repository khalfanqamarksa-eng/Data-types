def process_payment(ticket_amount):
    accepted_coins = [1, 5, 10, 25]
    total_inserted = 0

    print(f"Ticket Amount Due: {ticket_amount} cents")

    # Simulated inserted coins (including invalid ones like 2 and 7)
    coins_inserted = [1, 2, 5, 7, 10, 25]

    for coin in coins_inserted:
        if coin not in accepted_coins:
            print(f"Invalid coin: {coin} cent(s). Skipping...")
            continue  # Skip invalid coin

        total_inserted += coin
        print(f"Inserted: {coin} cent(s). Total so far: {total_inserted}")

        if total_inserted >= ticket_amount:
            print("Required amount reached!")
            break  # Stop collecting coins once paid

    change = total_inserted - ticket_amount

    if change == 0:
        pass  # No change needed
    else:
        print(f"Returning change: {change} cent(s)")

    return change


# Run test
process_payment(15)