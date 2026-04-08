import requests
import concurrent.futures
import time
from collections import Counter

API_URL = "http://127.0.0.1:8000/chat"

PAYLOAD = {
    "user_id": "user_admin",         
    "message": "Say exactly 'test'",
    "model": "gpt-4o-mini",
    "use_fallback": False,
    "temperature": 0.7,
    "max_tokens": 1024
}

def make_request(request_id: int):
    start = time.time()
    try:
        response = requests.post(API_URL, json=PAYLOAD, timeout=15)
        duration = time.time() - start

        if response.status_code == 200:
            data = response.json()
            actual_response = data.get("response", "").strip()
            success = actual_response.lower() == "test"
            return {
                "id": request_id,
                "status": response.status_code,
                "duration": round(duration, 3),
                "success": success,
                "response": actual_response[:50]
            }
        else:
            return {
                "id": request_id,
                "status": response.status_code,
                "duration": round(duration, 3),
                "success": False,
                "error": response.text[:100]
            }
    except Exception as e:
        return {
            "id": request_id,
            "status": "ERROR",
            "duration": round(time.time() - start, 3),
            "success": False,
            "error": str(e)
        }

if __name__ == "__main__":
    print(" Starting API stress test — 20 concurrent users...")
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(make_request, range(20)))

    total_time = time.time() - start_time

    # Summary
    successes = sum(1 for r in results if r["success"])
    status_counts = Counter(r["status"] for r in results)
    avg_duration = sum(r["duration"] for r in results) / len(results)

    print(f"\n✅ Finished in {total_time:.2f} seconds\n")
    print(f"Success rate : {successes}/20 ({successes/20*100:.1f}%)")
    print(f"Avg latency   : {avg_duration:.3f}s")
    print(f"Status codes  : {dict(status_counts)}")

    # Show failures (if any)
    for r in results:
        if not r["success"]:
            print(f"  ❌ Request {r['id']:02d} → {r.get('error', r.get('response', ''))}")