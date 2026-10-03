from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException

load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
os.makedirs(user_data_dir, exist_ok=True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

URL = "https://github.io"


def retry(func, retries=7, delay=2, description="Action"):
    for attempt in range(1, retries + 1):
        try:
            return func()
        except (WebDriverException, NoSuchElementException, TimeoutException) as e:
            print(
                f"⚠️ [Attempt {attempt}/{retries}] {description} failed due to network chaos. Retrying in {delay}s...")
            time.sleep(delay)
            if attempt == retries:
                print(f"❌ [CRITICAL] {description} completely failed after {retries} attempts.")
                raise e


def login_user(driver, wait):
    driver.get(URL)
    enter_bottom = driver.find_element(By.CLASS_NAME, "Home_heroButton__3eeI3")
    enter_bottom.click()

    email_entry = driver.find_element(By.ID, "email-input")
    email_entry.clear()
    email_entry.send_keys(os.getenv("EMAIL"))

    password_entry = driver.find_element(By.ID, "password-input")
    password_entry.clear()
    password_entry.send_keys(os.getenv("PASSWORD"))

    login_button = driver.find_element(By.ID, "submit-button")
    login_button.click()

    wait.until(EC.presence_of_all_elements_located((By.ID, "schedule-page")))
    print("✓ Login Successful")


def process_single_class_card(driver, card, stats_dict):
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    if "Tue" in day_title or "Thu" in day_title:
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            button_text = button.text

            stats_dict["total"] += 1

            if button_text in ["Booked", "Waitlisted"]:
                print(f"✓ Already processed: {class_name} on {day_title} ({button_text})")
                stats_dict["already"] += 1
                stats_dict["log"].append(f"[Already Booked/Waitlisted] {class_name} on {day_title}")
                return

            def execute_click_action():
                current_btn = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
                current_text = current_btn.text

                if current_text in ["Booked", "Waitlisted"]:
                    return current_text

                current_btn.click()

                inner_wait = WebDriverWait(driver, 3)
                inner_wait.until(
                    lambda d: card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']").text in ["Booked",
                                                                                                        "Waitlisted"])
                return card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']").text

            final_status = retry(
                execute_click_action,
                retries=7,
                description=f"Booking {class_name} on {day_title}"
            )

            if final_status == "Booked":
                print(f"✓ Successfully booked: {class_name} on {day_title}")
                stats_dict["booked"] += 1
                stats_dict["log"].append(f"[New Booking] {class_name} on {day_title}")
            elif final_status == "Waitlisted":
                print(f"✓ Joined waitlist for: {class_name} on {day_title}")
                stats_dict["waitlist"] += 1
                stats_dict["log"].append(f"[New Waitlist] {class_name} on {day_title}")


def navigate_and_fetch_bookings(driver):
    bookings_nav_button = driver.find_element(By.LINK_TEXT, "My Bookings")
    bookings_nav_button.click()

    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "booking-item")))

    my_bookings_list = driver.find_elements(By.CSS_SELECTOR, ".booking-item")

    extracted_data = []
    for booking in my_bookings_list:
        name_text = booking.find_element(By.CSS_SELECTOR, ".booking-name").text
        status_text = booking.find_element(By.CSS_SELECTOR, ".booking-status").text
        extracted_data.append({"name": name_text, "status": status_text})

    return extracted_data


def run_resilient_booking_pipeline():
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    stats = {"booked": 0, "waitlist": 0, "already": 0, "total": 0, "log": []}

    try:
        retry(lambda: login_user(driver, wait), retries=7, description="User Authentication Portal")

        class_cards = driver.find_elements(By.CSS_SELECTOR, ".card, .class-box")
        for card in class_cards:
            process_single_class_card(driver, card, stats)

        print("\n--- BOOKING SUMMARY ---")
        print(f"New bookings: {stats['booked']}")
        print(f"New waitlist entries: {stats['waitlist']}")
        print(f"Already booked/waitlisted: {stats['already']}")
        print(f"Total Tuesday & Thursday 6pm classes: {stats['total']}")

        print("\n--- DETAILED CLASS LIST ---")
        for log_entry in stats["log"]:
            print(f"  • {log_entry}")
        print(f"\n--- Total Tuesday/Thursday 6pm classes: {stats['total']} ---\n")

        print("--- VERIFYING ON MY BOOKINGS PAGE ---")

        verified_rows = retry(
            lambda: navigate_and_fetch_bookings(driver),
            retries=7,
            description="Navigating & Extracting Profile Dashboard Data"
        )

        found_bookings = 0
        for row in verified_rows:
            if "Waitlist" in row["status"]:
                print(f"  ✓ Verified: {row['name']} (Waitlist)")
            else:
                print(f"  ✓ Verified: {row['name']}")
            found_bookings += 1

        print("\n--- VERIFICATION RESULT ---")
        expected_label = "booking" if stats['total'] == 1 else "bookings"
        found_label = "booking" if found_bookings == 1 else "bookings"

        print(f"Expected: {stats['total']} {expected_label}")
        print(f"Found: {found_bookings} {found_label}")

        if stats['total'] == found_bookings:
            print("✅ SUCCESS: All bookings verified with zero structural data loss!")
        else:
            mismatch = stats['total'] - found_bookings
            print(f"❌ MISMATCH: Missing {mismatch} bookings")

    finally:
        driver.quit()


if __name__ == "__main__":
    run_resilient_booking_pipeline()
