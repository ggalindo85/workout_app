import json
import os
from datetime import datetime
from pathlib import Path


class WorkoutTracker:
    def __init__(self, data_file="workouts.json"):
        self.data_file = data_file
        self.workouts = self.load_workouts()

    def load_workouts(self):
        """Load workouts from JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                return json.load(f)
        return []

    def save_workouts(self):
        """Save workouts to JSON file."""
        with open(self.data_file, "w") as f:
            json.dump(self.workouts, f, indent=2)

    def add_workout(self, exercise, duration_minutes, sets=None, reps=None, weight=None, notes=""):
        """Add a new workout entry."""
        workout = {
            "date": datetime.now().isoformat(),
            "exercise": exercise,
            "duration_minutes": duration_minutes,
            "sets": sets,
            "reps": reps,
            "weight": weight,
            "notes": notes
        }
        self.workouts.append(workout)
        self.save_workouts()
        print(f"✓ Added {exercise} workout")
        return workout

    def list_workouts(self, limit=None):
        """Display all workouts or last N workouts."""
        if not self.workouts:
            print("No workouts recorded yet.")
            return

        workouts_to_show = self.workouts[-limit:] if limit else self.workouts
        print(f"\n{'Date':<20} {'Exercise':<15} {'Duration (min)':<15} {'Sets/Reps':<15} {'Weight':<10} {'Notes'}")
        print("-" * 95)

        for workout in workouts_to_show:
            date = datetime.fromisoformat(workout["date"]).strftime("%Y-%m-%d %H:%M")
            sets_reps = f"{workout['sets']}x{workout['reps']}" if workout['sets'] and workout['reps'] else "-"
            weight = f"{workout['weight']} lbs" if workout['weight'] else "-"
            print(f"{date:<20} {workout['exercise']:<15} {workout['duration_minutes']:<15} {sets_reps:<15} {weight:<10} {workout['notes']}")

    def get_stats(self):
        """Get workout statistics."""
        if not self.workouts:
            print("No workout data available.")
            return

        total_workouts = len(self.workouts)
        total_minutes = sum(w["duration_minutes"] for w in self.workouts)
        exercises = {}

        for workout in self.workouts:
            exercise = workout["exercise"]
            exercises[exercise] = exercises.get(exercise, 0) + 1

        print("\n=== WORKOUT STATS ===")
        print(f"Total Workouts: {total_workouts}")
        print(f"Total Minutes: {total_minutes}")
        print("\nExercise Breakdown:")
        for exercise, count in sorted(exercises.items(), key=lambda x: x[1], reverse=True):
            print(f"  - {exercise}: {count} times")

    def delete_workout(self, index):
        """Delete a workout by index."""
        if 0 <= index < len(self.workouts):
            removed = self.workouts.pop(index)
            self.save_workouts()
            print(f"✓ Deleted {removed['exercise']} workout")
        else:
            print("Invalid workout index.")


def main():
    tracker = WorkoutTracker()

    while True:
        print("\n=== WORKOUT TRACKER ===")
        print("1. Add workout")
        print("2. View workouts")
        print("3. View stats")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            exercise = input("Exercise name: ").strip()
            duration = int(input("Duration (minutes): "))
            sets = input("Sets (optional): ")
            reps = input("Reps (optional): ")
            weight = input("Weight in lbs (optional): ")
            notes = input("Notes (optional): ").strip()

            tracker.add_workout(
                exercise=exercise,
                duration_minutes=duration,
                sets=int(sets) if sets else None,
                reps=int(reps) if reps else None,
                weight=float(weight) if weight else None,
                notes=notes
            )

        elif choice == "2":
            limit = input("Show last N workouts (press Enter for all): ").strip()
            tracker.list_workouts(limit=int(limit) if limit else None)

        elif choice == "3":
            tracker.get_stats()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
