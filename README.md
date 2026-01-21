# Canvas Assignment Notifier 🎓

A simple automation tool that sends a daily morning briefing of your Canvas assignments directly to your phone. 

This script was designed to run entirely for **free** on GitHub Actions every morning to notify yourself of upcoming assignments for the day.


## 🚀 How It Works

1.  **Trigger:** GitHub Actions wakes up every day at a scheduled time.
2.  **Fetch:** The script downloads your private Canvas Calendar (`.ics` file).
3.  **Parse:** It filters for assignments that are due **today**.
4.  **Notify:** It sends a push notification to your phone via [ntfy.sh](https://ntfy.sh).

## 🛠️ Setup Guide

### 1. Get your Canvas Calendar Feed
1.  Log in to Canvas web.
2.  Click **Calendar** in the sidebar.
3.  Find the **"Calendar Feed"** button (usually bottom right).
4.  Copy the URL (it starts with `https://canvas.instructure.com/feeds/...`).

At first my idea was to use Canvas' API, but since my University restricts access token generation, I had to take a different approach by using the calendar feed.

### 2. Set up Notifications
1.  Download the **ntfy** app on your phone (iOS/Android).
2.  Subscribe to a unique topic name (e.g., `my-canvas-alerts-8392`).

*Note: No account signup is required.*

### 3. Enable the Automation
The workflow is defined in `.github/workflows/daily_sync.yml`. It is scheduled to run automatically, but you can force a test run:
* Set environment variables on repository setting.
* Go to the **Actions** tab in GitHub.
* Select **Daily Canvas Sync**.
* Click **Run workflow**.

## 🔮 Roadmap

* [ ] Add a weekly summary workflow (Sunday nights).
* [ ] Integrate Google Tasks/Calendar for long-term planning.