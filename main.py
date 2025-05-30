from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Operation(BaseModel):
    operation_id: str  # e.g. "AX5T1S-112"
    code_trailer: str  # e.g. "TA487PZ"
    code_container: str  # e.g. "BSE1212"
    cod_prov: str  # e.g. "TO"
    cod_comune: str  # e.g. "A388"
    destination_port: str  # e.g. "A01"
    gps_position: tuple[float, float]  # e.g. (38.12312, 38.12312)
    documents: None  # optional, not needed

    # e.g. "2025-06-03T13:22:31"
    start_date: str
    # e.g. "2025-06-03T13:22:31"
    operation_date: str
    # e.g. "2025-06-03T15:35:12", start_date + operation_total_time
    estimated_arrival_time: str
    # e.g. 31 (fixed HH)
    operation_total_time: int


class OperationStatus(BaseModel):
    operation_id: str  # e.g. "AX5T1S-112"
    status_code: str  # e.g. "01" activated, "02" disactivated, "03" anomaly
    description: str | None  # used when there's an anomaly


STATUS_CODE_MAP: dict[str, str] = {
    "01": "activated",
    "02": "disactivated",
    "03": "anomaly",
}


@app.post("/api/operations")
async def create_operation(operation: Operation):
    print(f"Created operation: {operation}")
    return {"status": "ok"}


@app.put("/api/operations/{operation_id}")
async def update_operation(operation_id: str, status: OperationStatus):
    op_msg = STATUS_CODE_MAP.get(status.status_code, "unknown")
    print(f"Operation {operation_id}: {op_msg}")
    return {"status": "ok"}
