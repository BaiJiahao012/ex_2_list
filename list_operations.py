participants = [
    "Alice Wong",
    "Chen Wei",
    "David Kim",
    "Fatima Ali",
    "George Smith",
    "Hana Lee",
    "Audrey Hepburn",
    "James Stewart",
    "George Scott"
]
scores = [78, 92, 64, 87, 55, 73, 69, 96, 90]
qualification_score = 70
distinction_score = 90


# 1. Display all existing participants together with their scores using zip()
for name, scr in zip(participants, scores):
    print(f"{name}: {scr}")


# 2. Logic to add a new participant with multiple validation checks
new_name = input("Please enter new participant's name: ").strip()

# Check if the input name is empty
if not new_name:
    print("Error: Name cannot be empty. Participant will not be added.")
else:
    # Check if participant already exists in the list
    if new_name in participants:
        print(f"Notice: {new_name} is already registered. Participant will not be added.")
    else:
        score_input = input("Please enter the participant's score: ").strip()
        # Check whether the score input is a valid number
        if not score_input.isdigit():
            print("Error: Score must be a number. Participant will not be added.")
        else:
            new_score = int(score_input)
            # Validate score is within valid range 0‑100
            if new_score < 0 or new_score > 100:
                print("Error: Score must be between 0 and 100. Participant will not be added.")
            else:
                # All validations passed, append new data to lists
                participants.append(new_name)
                scores.append(new_score)
                print(f"{new_name} has been registered successfully!")


# 3. Logic to search for a specific participant and show qualification status
search_name = input("Enter the name of participant to search: ").strip()
if search_name in participants:
    idx = participants.index(search_name)
    found_score = scores[idx]
    print(f"Name: {search_name}, Score: {found_score}")
    if found_score > distinction_score:
        print("Result: DISTINCTION")
    elif found_score > qualification_score:
        print("Result: QUALIFIED")
    else:
        print("Result: NOT QUALIFIED")
else:
    print(f"{search_name} is not found.")


# 4. Display every participant's name, score and qualification status
for name, scr in zip(participants, scores):
    status = ""
    if scr > distinction_score:
        status = "DISTINCTION"
    elif scr > qualification_score:
        status = "QUALIFIED"
    else:
        status = "NOT QUALIFIED"
    print(f"{name} | Score:{scr} | {status}")


# 5. Check if at least one participant has distinction AND if all participants scored 50 or above
has_any_distinction = any(s > distinction_score for s in scores)
all_passed = all(s >= 50 for s in scores)

print(f"Is there any participant with DISTINCTION: {has_any_distinction}")
print(f"Do all participants have score >=50 (all passed): {all_passed}")


# 6. Logic to update an existing participant's score with validation
update_name = input("Enter name of participant to update score: ").strip()
if update_name not in participants:
    print(f"Error: {update_name} does not exist, cannot perform update.")
else:
    new_scr_input = input("Enter new score: ").strip()
    if not new_scr_input.isdigit():
        print("Error: Score must be a number, update aborted.")
    else:
        updated_score = int(new_scr_input)
        if updated_score < 0 or updated_score > 100:
            print("Error: Score must be between 0‑100, update aborted.")
        else:
            pos = participants.index(update_name)
            scores[pos] = updated_score
            print(f"{update_name}'s score has been updated to {updated_score}")


# 7. Logic to withdraw / remove participant, remove corresponding score entry
remove_name = input("Enter name of participant to remove: ").strip()
if remove_name not in participants:
    print(f"{remove_name} is not in participant list, cannot remove.")
else:
    remove_idx = participants.index(remove_name)
    participants.pop(remove_idx)
    scores.pop(remove_idx)
    print(f"{remove_name} has been removed from the list.")


# 8. Create scoreboard sorted by score descending, display rank together with name and score
paired_list = list(zip(participants, scores))
# Sort the paired list by score value in descending order
paired_list.sort(key=lambda x: x[1], reverse=True)

for rank, (p_name, p_scr) in enumerate(paired_list, start=1):
    print(f"Rank {rank} | {p_name} | {p_scr}")


# 9. Calculate all required statistics values
score_list = scores
highest = max(score_list)
lowest = min(score_list)
avg = sum(score_list) / len(score_list)

count_highest = score_list.count(highest)
count_lowest = score_list.count(lowest)

count_distinction = 0
count_qualified = 0
count_not_qualified = 0

for s in score_list:
    if s > distinction_score:
        count_distinction += 1
    elif s > qualification_score:
        count_qualified += 1
    else:
        count_not_qualified += 1


# 10. Generate and print final complete report
print("Rank | Name               | Score | Qualification")
for rank, (p_name, p_scr) in enumerate(paired_list, start=1):
    if p_scr > distinction_score:
        stat = "DISTINCTION"
    elif p_scr > qualification_score:
        stat = "QUALIFIED"
    else:
        stat = "NOT QUALIFIED"
    print(f"{rank:2d} | {p_name:<18} | {p_scr:3d} | {stat}")



print("Highest score: {highest}, Number of participants with highest score: {count_highest}".format(highest=highest,count_highest=count_highest))
print("Lowest score: {lowest}, Number of participants with lowest score: {count_lowest}".format(lowest=lowest,count_lowest=count_lowest))
print(f"Average score: {avg:.2f}")
print(f"Number of DISTINCTION participants: {count_distinction}")
print(f"Number of QUALIFIED participants: {count_qualified}")
print(f"Number of NOT QUALIFIED participants: {count_not_qualified}")
print(f"Any participant achieved DISTINCTION: {has_any_distinction}")
print(f"All participants scored 50 or above: {all_passed}")
