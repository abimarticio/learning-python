# error handling
try: 
    quotient = 1/ 0
    print(quotient)
except Exception as error:
    print(f"Error: {error}")
finally:
    print("done")

answer = 4
output = 4 + 1
assert answer == output, f"[ERROR] answer != output: answer={answer}, output={output}"