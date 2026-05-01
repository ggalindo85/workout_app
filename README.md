# Workout Tracker

A simple command-line Python workout tracker to log, view, and analyze your fitness workouts.

## Features

- **Add Workouts**: Log exercise name, duration, sets, reps, weight, and notes
- **View Workouts**: Display all workouts or just the most recent ones
- **View Statistics**: See total workouts, total minutes, and exercise breakdown
- **Persistent Storage**: All workouts are saved to `workouts.json`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ggalindo85/workout_app.git
cd workout_app
```

2. Install dependencies (minimal):
```bash
pip install -r requirements.txt
```

## Usage

Run the tracker:
```bash
python workout_tracker.py
```

### Menu Options

1. **Add Workout** - Log a new exercise session
   - Exercise name (required)
   - Duration in minutes (required)
   - Sets, reps, weight, notes (optional)

2. **View Workouts** - See your workout history
   - View all workouts or just the last N workouts

3. **View Stats** - Get a summary of your training
   - Total workouts
   - Total minutes trained
   - Breakdown by exercise type

4. **Exit** - Close the application

## Data Storage

All workouts are stored in `workouts.json` in the following format:

```json
{
  "date": "2026-05-01T20:30:00",
  "exercise": "Bench Press",
  "duration_minutes": 45,
  "sets": 4,
  "reps": 8,
  "weight": 225,
  "notes": "Great workout!"
}
```

## Example Session

```
=== WORKOUT TRACKER ===
1. Add workout
2. View workouts
3. View stats
4. Exit
Choose an option: 1
Exercise name: Squats
Duration (minutes): 30
Sets (optional): 5
Reps (optional): 5
Weight in lbs (optional): 315
Notes (optional): Felt strong today
✓ Added Squats workout
```

## Future Enhancements

- Export workouts to CSV
- Weight tracking over time
- Workout routine templates
- Rest day tracking
- Progress graphs

## License

MIT
