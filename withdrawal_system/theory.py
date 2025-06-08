# The code is simulation of an withdrawal system with custom exception handling for:

Incorrect PIN attempts (with a maximum of 3 tries).

Low balance during withdrawal (if the remaining balance drops below ₹1000).

 Key Components:
Custom Exceptions:
  LowBalanceException: Raised when withdrawal would leave balance below ₹1000.
  AttemptException: Raised after 3 failed PIN attempts.

Global Variable:
  attempt: Tracks how many times the user has entered an incorrect PIN.

Function withdraw():
  Prompts the user to enter a PIN.
  If correct:
    Accepts the withdrawal amount.
    Checks if the resulting balance is below ₹1000.
    If so, raises LowBalanceException.

If incorrect:
    Offers retry option up to 3 times.
    Raises AttemptException after 3 failed attempts.

Error Handling:
    Uses try-except to catch and display exception messages.
