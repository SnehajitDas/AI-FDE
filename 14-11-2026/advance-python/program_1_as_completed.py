from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def check_service(service_name, delay):
    time.sleep(delay)
    return f"{service_name}: healthy"

services = {
    "Customer API": 2.0,
    "Payment API": 0.5,
    "Inventory API": 1.0
}

with ThreadPoolExecutor(max_workers=3) as executor:
    future_to_service = {
        executor.submit(check_service, service, delay): service
        for service, delay in services.items()
    }

    for future in as_completed(future_to_service):
        service = future_to_service[future]

        try:
            print(future.result())
        except Exception as error:
            print(f"{service} failed: {error}")

