from rich.console import Console
from rich.table import Table
import calendar
from datetime import datetime

console = Console()
现在 = datetime.now()
cal = calendar.monthcalendar(now.year, now.month)
month_name = calendar.month_name[now.month]

table = Table(title=f"{month_name} {now.year}", show_header=True, header_style="bold magenta")
days = ["日", "一", "二", "三", "四", "五", "六"]
for day in days:
    table.add_column(day, justify="center")

for week in cal:
    # 将 0 替换为空格，方便阅读
    week_str = [str(d) if d != 0 else "" for d in week]
    table.add_row(*week_str)

console.print(table)
