import threading
import time
import requests


TARGET_URL = "http://localhost:8000/orders/"
TOTAL_THREADS = 100


success_count = 0
rejected_count = 0
error_count = 0



stats_lock = threading.Lock()

def dispatch_single_order(thread_id: int):
    """Worker task function executed by each independent parallel thread."""
    global success_count, rejected_count, error_count
    
    payload = {
        "product_id": 1,
        "email": f"stress_buyer_{thread_id}@amazon-test.com"
    }
    
    try:
        
        response = requests.post(TARGET_URL, json=payload, timeout=5)
        
        with stats_lock:
            if response.status_code == 222 or response.status_code == 202:
                success_count += 1
                print(f"🟩 Thread #{thread_id:03d}: SECURED STOCK! Order ID: {response.json().get('order_id')}")
            elif response.status_code == 400:
                rejected_count += 1
                print(f"🟥 Thread #{thread_id:03d}: BLOCKED! Status 400 (Sold Out Managed Safely)")
            else:
                error_count += 1
                print(f"⚠️ Thread #{thread_id:03d}: Unexpected Status {response.status_code} -> {response.text}")
                
    except Exception as e:
        with stats_lock:
            error_count += 1
            print(f"❌ Thread #{thread_id:03d}: Connection Failed -> {str(e)}")

def run_flash_sale_simulation():
    """Orchestrates 100 concurrent threads to bombard the server at once."""
    print("==============================================================")
    print(f"🚀 INITIALIZING BRUTAL FLASH SALE STRESS SIMULATION")
    print(f"💥 Spawning {TOTAL_THREADS} Concurrent Threads in Process Memory...")
    print("==============================================================")
    
    threads = []
    
    
    for i in range(1, TOTAL_THREADS + 1):
        t = threading.Thread(target=dispatch_single_order, args=(i,))
        threads.append(t)
        
    print("🏁 Ready... Thread barrier unlocked! Launching load storm...")
    start_time = time.time()
    
    
    for t in threads:
        t.start()
        
    
    for t in threads:
        t.join()
        
    end_time = time.time()
    duration = end_time - start_time
    
    print("\n==============================================================")
    print("📊 FINAL CONCURRENCY BENCHMARK DIAGNOSTICS")
    print("==============================================================")
    print(f"⏱️ Total Load Wave Execution Time: {duration:.2f} seconds")
    print(f"✅ Successful Transactions Secured : {success_count}  (Should be exactly 4!)")
    print(f"❌ Handled Out-Of-Stock Rejections: {rejected_count} (Should be exactly 96!)")
    print(f"⚠️ Broken System Fault Crashes     : {error_count}    (Should be exactly 0!)")
    print("==============================================================")
    
    if error_count == 0 and success_count == 4:
        print(" RESULT: PASSED! Your Custom Embedded Mutex Engine is 100% Thread-Safe.")
    else:
        print(" RESULT: FAILED! Concurrency leak or race condition detected.")

if __name__ == "__main__":
    run_flash_sale_simulation()