import tkinter as tk
from tkinter import ttk, scrolledtext
import subprocess
import platform
import socket

def run():
    window = tk.Toplevel()
    window.title("Network Diagnostics")
    window.geometry("600x500")

    def execute_command(command):
        try:
            result = subprocess.check_output(command, shell=True, universal_newlines=True)
        except subprocess.CalledProcessError as e:
            result = e.output
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, result)

    def ping():
        target = entry.get()
        param = '-n' if platform.system().lower()=='windows' else '-c'
        command = f"ping {param} 4 {target}"
        execute_command(command)

    def traceroute():
        target = entry.get()
        cmd = "tracert" if platform.system().lower() == "windows" else "traceroute"
        command = f"{cmd} {target}"
        execute_command(command)

    def dns_lookup():
        target = entry.get()
        try:
            ip = socket.gethostbyname(target)
            result = f"DNS Lookup Result for {target}: {ip}"
        except socket.gaierror:
            result = "Invalid hostname"
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, result)

    ttk.Label(window, text="Enter IP or Domain:").pack(pady=5)
    entry = ttk.Entry(window, width=50)
    entry.pack(pady=5)

    btn_frame = ttk.Frame(window)
    btn_frame.pack(pady=10)
    ttk.Button(btn_frame, text="Ping", command=ping).pack(side=tk.LEFT, padx=5)
    ttk.Button(btn_frame, text="Traceroute", command=traceroute).pack(side=tk.LEFT, padx=5)
    ttk.Button(btn_frame, text="DNS Lookup", command=dns_lookup).pack(side=tk.LEFT, padx=5)

    output_box = scrolledtext.ScrolledText(window, width=70, height=20)
    output_box.pack(pady=10)