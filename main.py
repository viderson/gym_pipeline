import argparse
from database import init_db
from data_loader import load_data

def main():
    parser = argparse.ArgumentParser(
        description="Gym Project: initialize DB, load data, export CSV"
    )
    parser.add_argument(
        "--init",
        action="store_true",
        help="Initialize the SQLite database (create tables)"
    )
    parser.add_argument(
        "--load",
        metavar="JSON_PATH",
        help="Path to the JSON file to load into the database"
    )
    parser.add_argument(
        "--export-csv",
        metavar="OUTPUT_CSV",
        help="Export user data to CSV (requires --user)"
    )
    parser.add_argument(
        "--user",
        type=int,
        metavar="USER_ID",
        help="User ID to export or inspect"
    )

    args = parser.parse_args()

    if args.init:
        init_db()
        print("✅ Database schema created.")

    if args.load:
        load_data(args.load)
        print(f"✅ Data loaded from {args.load}")

    if args.export_csv:
        if not args.user:
            parser.error("--export-csv requires --user USER_ID")
        from analysis.dataframe_builder import build_user_dataframe
        df = build_user_dataframe(args.user)
        df.to_csv(args.export_csv, index=False)
        print(f"✅ User {args.user} data exported to {args.export_csv}")

if __name__ == "__main__":
    main()
