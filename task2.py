import tkinter as tk
import winsound
import threading
import datetime

class AlarmClock:
    def __init__(self, master):
        self.master = master
        master.title("Alarm Clock")

        self.label = tk.Label(master, text="Set Alarm (HH:MM)")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.set_button = tk.Button(master, text="Set Alarm", command=self.set_alarm)
        self.set_button.pack()

        self.cancel_button = tk.Button(master, text="Cancel", command=self.cancel_alarm)
        self.cancel_button.pack()

    def set_alarm(self):
        alarm_time = self.entry.get()
        try:
            alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
            now = datetime.datetime.now()
            alarm_datetime = datetime.datetime(now.year, now.month, now.day, alarm_hour, alarm_minute)

            if alarm_datetime <= now:
                alarm_datetime += datetime.timedelta(days=1)  # set alarm for next day if it's already passed
            self.alert_thread = threading.Thread(target=self.alert, args=(alarm_datetime,))
            self.alert_thread.start()
        except ValueError:
            messagebox.showerror("Error", "Invalid time format! Please use HH:MM")

    def alert(self, alarm_time):
        while True:
            now = datetime.datetime.now()
            if now >= alarm_time:
                self.play_beep()
                break

    def play_beep(self):
        winsound.Beep(1000, 1000)  # Beep sound for 1 second

    def cancel_alarm(self):
        self.entry.delete(0, tk.END)


def main():
    root = tk.Tk()
    clock = AlarmClock(root)
    root.mainloop()


if __name__ == "__main__":
    main()
