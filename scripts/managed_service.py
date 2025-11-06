# in terminal run: pip install pandas sqlalchemy pymysql python-dotenv
# Run this file top-to-bottom OR run it cell-by-cell in VS Code.

import os, time
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# --- 0) Load environment ---
load_dotenv("assignment_4/.env")  # reads .env in current working directory

MAN_DB_HOST = os.getenv("MAN_DB_HOST")
MAN_DB_PORT = os.getenv("MAN_DB_PORT", "3306")
MAN_DB_USER = os.getenv("MAN_DB_USER")
MAN_DB_PASS = os.getenv("MAN_DB_PASS")
MAN_DB_NAME = os.getenv("MAN_DB_NAME")

print("[ENV] MAN_DB_HOST:", MAN_DB_HOST)
print("[ENV] MAN_DB_PORT:", MAN_DB_PORT)
print("[ENV] MAN_DB_USER:", MAN_DB_USER)
print("[ENV] MAN_DB_NAME:", MAN_DB_NAME)

# --- 1) Connect to server (no DB) and ensure database exists ---
server_url = f"mysql+pymysql://{MAN_DB_USER}:{MAN_DB_PASS}@{MAN_DB_HOST}:{MAN_DB_PORT}/{MAN_DB_NAME}?ssl=false"
print("[STEP 1] Connecting to Managed MySQL (no DB):", server_url.replace(MAN_DB_PASS, "*****"))
t0 = time.time()

engine_server = create_engine(server_url, pool_pre_ping=True)
with engine_server.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS `{MAN_DB_NAME}`"))
    conn.commit()
print(f"[OK] Ensured database `{MAN_DB_NAME}` exists on managed instance.")

# --- 2) Connect to the target database ---
db_url = f"mysql+pymysql://{MAN_DB_USER}:{MAN_DB_PASS}@{MAN_DB_HOST}:{MAN_DB_PORT}/{MAN_DB_NAME}?ssl=false"
engine = create_engine(db_url, pool_pre_ping=True)

# --- 3) Create a DataFrame and write to a table ---
table_name = "visits"
df = pd.DataFrame(
    [
        {"patient_id": 1, "visit_date": "2025-09-01", "bp_sys": 118, "bp_dia": 76, "HR": 72, "RR": 16, "Temp_C": 36.6},
        {"patient_id": 2, "visit_date": "2025-09-02", "bp_sys": 78, "bp_dia": 35, "HR": 88, "RR": 20, "Temp_C": 37.0},
        {"patient_id": 3, "visit_date": "2025-09-03", "bp_sys": 121, "bp_dia": 79, "HR": 95, "RR": 18, "Temp_C": 38.2},
        {"patient_id": 4, "visit_date": "2025-09-04", "bp_sys": 210, "bp_dia": 105, "HR": 110, "RR": 22, "Temp_C": 39.0},
        {"patient_id": 5, "visit_date": "2025-09-05", "bp_sys": 125, "bp_dia": 82, "HR": 76, "RR": 17, "Temp_C": 36.8},
    ]
)
print("[STEP 3] Writing DataFrame to table:", table_name)
with engine.begin() as conn:
    df.to_sql(table_name, con=conn, if_exists="replace", index=False)
print("[OK] Wrote DataFrame to table.")

# --- 4) Read back a quick check ---
print("[STEP 4] Reading back row count ...")
with engine.connect() as conn:
    count_df = pd.read_sql(f"SELECT COUNT(*) AS n_rows FROM `{table_name}`", con=conn)
print(count_df)

elapsed = time.time() - t0
print(f"[DONE] Managed path completed in {elapsed:.1f}s at {datetime.utcnow().isoformat()}Z")