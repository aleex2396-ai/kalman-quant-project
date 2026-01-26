import yfinance as yf
import pandas as pd
import os


def download_data(start_date="2018-01-01", end_date="2022-01-01"):
    """
    Downloads EWA (Australia) and EWC (Canada) data.
    These are classic 'Commodity Currency' pairs that usually move together.
    """
    tickers = ["EWA", "EWC"]
    print(f"Downloading data for {tickers}...")

    # Download close prices only
    try:
        data = yf.download(tickers, start=start_date, end=end_date)['Close']
    except Exception as e:
        print(f"Error downloading data: {e}")
        return

    # Drop any days where one market was open but the other was closed
    data = data.dropna()

    # --- PATH FIX: Ensure we save to the project root's 'data' folder ---
    # Get the directory where this script (data_loader.py) is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to the project root, then into 'data'
    data_folder = os.path.join(current_dir, '..', 'data')

    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
        print(f"Created folder: {data_folder}")

    file_path = os.path.join(data_folder, "ewa_ewc_pairs.csv")

    # Save to CSV
    data.to_csv(file_path)
    print(f"Data saved successfully to: {file_path}")
    print(f"Rows downloaded: {len(data)}")


if __name__ == "__main__":
    download_data()