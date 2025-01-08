import psutil
from rich.console import Console
from rich.table import Table
import main

console = Console()

def system_health_monitoringg():
    
 
    cpu_cores = psutil.cpu_count(logical=True)
    cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
    total_cpu_usage = psutil.cpu_percent(interval=1)
    table1 = Table(title="CPU Usage Information", style="bold cyan")
    table1.add_column("Metric", style="bold yellow", justify="left")
    table1.add_column("Value", style="bold white", justify="right")
    table1.add_row("Number of CPU Cores", str(cpu_cores))
    table1.add_row("usage total", str( total_cpu_usage))
    j = 0
    for i in cpu_usage:
     j += 1
     table1.add_row(f"Usage Core {j}", f"{i}%")
    console.print(table1)


    memory = psutil.virtual_memory()
    table2 = Table(title="memoire info", style="bold cyan")
    table2.add_column("Metric", style="bold yellow", justify="left")
    table2.add_column("Value ", style="bold white", justify="right")
    table2.add_row("Total Memory:", f"{memory.total / (1024 ** 3):.2f} GB")
    table2.add_row("Used Memory", f"{memory.used / (1024 ** 3):.2f} GB")
    table2.add_row("Available Memory", f"{memory.available / (1024 ** 3):.2f} GB")
    console.print(table2)

    

    disk = psutil.disk_usage('/')
    table3 = Table(title="Disk Information", style="bold cyan")
    table3.add_column("Metric", style="bold yellow", justify="left")
    table3.add_column("Value ", style="bold white", justify="right")
    table3.add_row("Total Disk Space:", f"{disk.total / (1024 ** 3):.2f} GB")
    table3.add_row("Used Disk Space:", f"{disk.used / (1024 ** 3):.2f} GB")
    table3.add_row("Free Disk Space:", f"{disk.free / (1024 ** 3):.2f} GB")
    console.print(table3)
    

    net = psutil.net_io_counters()
    table4 = Table(title="Network Information", style="bold cyan")
    table4.add_column("Metric", style="bold yellow", justify="left")
    table4.add_column("Value ", style="bold white", justify="right")
    table4.add_row("Total Data Sent:", f"{net.bytes_sent / (1024 ** 2):.2f} MB")
    table4.add_row("Total Data Received:", f"{net.bytes_recv / (1024 ** 2):.2f} MB")
    console.print(table4)
    
    
    main.main()