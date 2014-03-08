"""splitting script"""

from subprocess import call
import inspect
import lesson2

ALLFUNCS = inspect.getmembers(lesson2, inspect.isfunction)
for current_func in ALLFUNCS:
    call(["mkdir", current_func[0]])
    current_file = open(current_func[0] + "/solution.py", "w")
    current_source = inspect.getsource(current_func[1])
    current_file.write(current_source)
    current_file.close()
    call(["touch", current_func[0] + "/test.py"])
