"""splitting script"""

from subprocess import call
import inspect
import lesson1

ALLFUNCS = inspect.getmembers(lesson1, inspect.isfunction)
for current_func in ALLFUNCS:
    call(["mkdir", current_func[0]])
    current_file = open(current_func[0] + "/solution.py", "w")
    current_source = inspect.getsource(current_func[1])
    current_file.write(current_source)
    current_file.close()
    call(["touch", current_func[0] + "/test.py"])
