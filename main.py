# main.py - CTI Pipeline Launcher

from datetime import datetime
from modules.alerts import check_auction_alerts
from modules.svgscan import scan_svg_files
from modules.social import dummy_scrape_social
from modules.correlation import correlate, activate_playbooks
import json

def main():
    print("\n[CTI PIPELINE STARTED] ", datetime.now())
    alerts = check_auction_alerts()
    svg_hits = scan_svg_files()
    mentions = dummy_scrape_social()

    correlation = correlate(alerts, svg_hits, mentions)
    print("\n--- CORRELATION ---")
    print(json.dumps(correlation, indent=2))
    actions = activate_playbooks(correlation['risk_level'])
    print("\n--- ACTIONS TRIGGERED ---")
    for action in actions:
        print(f"[+] {action}")

if __name__ == "__main__":
    main()
