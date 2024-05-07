from datetime import datetime

from fastapi import FastAPI
from loguru import logger

from boilerplate.schemas.status import Status  # TODO: Replace with your app

app = FastAPI(
    # swagger_ui_parameters={"docExpansion": "none"},
)

start_time = datetime.now()


@app.get(path="/", response_model=Status)
async def get_status():
    """
    Retrieves the status of the application.

    This function first calculates the uptime of the application by subtracting
    the start time from the current time. It then removes the microseconds from
    the uptime and converts it to a string. It retrieves the current stage of
    the application from the configuration and sets the health status of the
    application to 'healthy'. It then creates a Status object with the current
    stage, uptime, and health status, logs the status, and returns it.

    :returns: The status of the application.
    :rtype: Status
    """

    # Calculate uptime
    current_time = datetime.now()
    uptime_duration = current_time - start_time

    # Convert to string and remove microseconds
    uptime_str = str(uptime_duration).split(".")[0]

    # Define the health status of your application
    # (e.g., healthy, degraded, down)
    health_status = "healthy"

    status = Status(uptime=uptime_str, health=health_status)
    logger.info(status)

    return status


# app.include_router(routes.router, prefix="/route")
