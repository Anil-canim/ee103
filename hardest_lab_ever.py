# Python file for user: anilcanguler
# =============================================
# EE103 - LAB 7: Galactic Pet Health System
# Topic: Try/Except, Raising Errors,
#        Custom Exceptions, Assertions
#
# INSTRUCTIONS FOR STUDENTS:
#   * Only fill the regions marked with "TODO".
#   * Do NOT change function names, parameters, or main().
#   * Do NOT remove any given code except the 'pass' lines
#     that are explicitly marked with TODO.
# =============================================

# ---------- AUTO INPUT CONFIG (NO MANUAL TYPING) ----------

USE_TEST_INPUT = True

# This sequence matches the sample output in the lab sheet:
#   3 pets:
#     Pet 1: Lumu, 40 -> 38
#     Pet 2: Zorp, 50 -> 70  (CRITICAL gain)
#     Pet 3: Blip, 60 -> 61
test_inputs = iter([
    "3",
    "Lumu",
    "40",
    "38",
    "Zorp",
    "50",
    "70",
    "Blip",
    "60",
    "61"
])


def test_input(prompt=""):
    """
    Replacement for built-in input() when USE_TEST_INPUT is True.
    It takes values from test_inputs and prints them as if the user
    had typed them.
    """
    try:
        value = next(test_inputs)
    except StopIteration:
        value = ""
    # Ekranda normal input gibi görünmesi için:
    if prompt:
        print(f"{prompt}{value}")
    else:
        print(value)
    return value


# built-in input() fonksiyonunu override et
if USE_TEST_INPUT:
    import builtins
    builtins.input = test_input


# ---------- PART 1: SAFE INTEGER INPUT (15 pts) ----------

def get_int(prompt):
    """
    TODO (Part 1):
      - Continuously ask the user for input using the given prompt.
      - Try to convert the input text to an integer.
      - If conversion fails (ValueError):
            * print an error message
              (for example: "Invalid integer, please try again.")
            * and ask again.
      - If conversion succeeds:
            * return the integer value.

    You may use a while-loop with try/except.
    """

    # WRITE YOUR CODE BELOW
    # ---------------------
    
    while True:
        text=input(prompt)
        try:
            integer_value=int(text)
            return integer_value

        except ValueError:
            print("Invalid integer, please try again")
        # TODO: remove this pass after implementing your solution
    # ---------------------


# ---------- HELPER FUNCTION: SAFE DIVISION (GIVEN) ----------

def safe_divide(a, b):
    """
    Safely compute a / b.

    Returns:
        - result of a / b if no error occurs,
        - None if division by zero or wrong type occurs.

    You can use this function in other parts of the lab.
    DO NOT modify this function.
    """
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers.")
        return None


# ---------- PART 2: WEIGHT VALIDATION (10 pts) ----------

def validate_weight(w):
    """
    TODO (Part 2):
      - A valid Galactic pet weight is between 1 and 300 (inclusive).
      - If w is OUTSIDE this range:
            * raise ValueError("Invalid weight range.")
      - Do NOT print anything in this function.
    """

    # WRITE YOUR CODE BELOW
    # ---------------------
    if w<1 or w>300:
        raise ValueError("Invalid weight range")# TODO: remove this pass after implementing your solution
    # ---------------------


# ---------- CUSTOM EXCEPTION (GIVEN) ----------

class CriticalHealthError(Exception):
    """
    Custom exception used for dangerous weight changes.

    This class is already provided.
    DO NOT modify this class.
    """
    pass


# ---------- PART 3: EVALUATE A PET (30 pts) ----------

def evaluate_pet(prev_w, curr_w):
    """
    TODO (Part 3):
      - Use validate_weight(prev_w) and validate_weight(curr_w)
        to ensure both weights are in the valid range.
      - Compute the percentage change of weight using safe_divide:
            percent = (curr_w - prev_w) / prev_w * 100
      - If safe_divide returns None:
            * raise CriticalHealthError("Unable to compute change.")
      - If the weight change is critical:
            * percent < -12   OR   percent > 25
            * raise CriticalHealthError with a short message.
      - Otherwise, set a status string:
            * -12 <= percent < -4  -> "loss"
            *  4 <= percent <= 25  -> "gain"
            *  otherwise           -> "stable"
      - Return a tuple (percent, status) for non-critical cases.

    Only this function should classify the change as loss/gain/stable.
    """

    validate_weight(prev_w)
    validate_weight(curr_w)

   

    raw=safe_divide(curr_w-prev_w,prev_w)
    if raw==None:
        raise CriticalHealthError("Unable to compute the change")
    
    percent=raw*100
    if percent<-12 or percent>25:
        raise CriticalHealthError("percent is out of the range")

    if -12<= percent<-4:
        status="loss"
    elif 4<= percent <= 25:
        status="gain"
    else:
        status="stable"

    return (percent,status)
    # WRITE YOUR CODE BELOW
    # ---------------------
      # TODO: remove this pass after implementing your solution
    # ---------------------


# ---------- PART 4: READING MULTIPLE PETS (25 pts) ----------

def read_pets():
    """
    TODO (Part 4):
      - Ask the user (using get_int) how many alien pets will
        be checked today.
      - Use an assertion to enforce:
            1 <= number_of_pets <= 40
      - For each pet:
            * read the pet name (using input).
              If the user enters an empty string, replace it with
              a default name such as "Pet_1", "Pet_2", ...
            * repeatedly:
                  - read previous and current weights using get_int
                  - try to validate and evaluate the pet:
                        validate_weight(...)
                        evaluate_pet(...)
                    using try/except:
                        · on ValueError (invalid range):
                              print the error message and
                              ask for the weights again.
                        · on CriticalHealthError:
                              print the error message,
                              set the pet's status to "CRITICAL",
                              choose a reasonable percent value
                              (for example, you may store None),
                              then stop asking weights for this pet.
            * create a dictionary for each pet with keys such as:
                  "name", "previous", "current",
                  "percent", "status"
              and append it to a list.
      - Return the list that contains all pet dictionaries.
    """
    number_of_pets=get_int("how many cats will be checked today? ")
    assert 1<= number_of_pets <= 40
    pet_names=[]
    pet_data=[]
    

   
    for i in range((number_of_pets)):
        pet_names.append(input(f"'what is the name of {i+1}. pet name'"))
        if pet_names[i]=="":
            pet_names[i]=f"Pet_{i+1}"
                
        while True:
            previous_weights=get_int("Enter the previous weight")
            current_weights=get_int("Enter the current_weight")
            try:
                validate_weight(previous_weights)
                validate_weight(current_weights)
                percent, status=evaluate_pet(previous_weights,current_weights)
                break
            except ValueError:
                print("wrong weight")
            except CriticalHealthError:
                print("wrong weight")
                status="CRITICAL"
                percent=None
                break

        pet_dictionary={
            "name":pet_names[i],
            "previous":previous_weights,
            "current":current_weights,
            "percent":percent,
            "status":status
        }
        pet_data.append(pet_dictionary)
    return pet_data
        

    # WRITE YOUR CODE BELOW
    # ---------------------
      # TODO: remove this pass after implementing your solution
    # ---------------------


# ---------- PART 5: ANALYZE PETS (20 pts) ----------

def analyze_pets(pets):
    """
    TODO (Part 5):
      - Use assertions to check:
            * pets list is not empty,
            * each pet["current"] is positive.
      - Compute and/or determine:
            * total number of pets,
            * total of current weights,
            * average current weight (use safe_divide),
            * heaviest pet  (maximum current weight),
            * lightest pet  (minimum current weight),
            * number of pets whose status is "CRITICAL".
      - Print a summary similar to the lab sheet example:

            === Summary ===
            Total pets: ...
            Average current weight: ... kg
            Heaviest pet : <name> (<weight> kg)
            Lightest pet : <name> (<weight> kg)
            Number of CRITICAL cases: ...

      - The exact wording can differ slightly, but the
        information and structure should be similar.
    """
    assert len(pets) > 0
    
    for pet in pets:
        assert pet["current"] > 0
    
    total_pets = len(pets)
    total_weight = 0
    critical_count = 0
        
        # En ağır ve en hafifi bulmak için geçici değişkenler
        # Başlangıçta ilk hayvanı "en ağır" ve "en hafif" varsayalım
    heaviest_pet = pets[0] 
    lightest_pet = pets[0]
    for pet in pets:
        # 1. Toplam ağırlığı ekle
        total_weight += pet["current"]
        
        # 2. Kritik mi diye bak (Senin takıldığın yer burası)
        if pet["status"] == "CRITICAL":
            critical_count += 1
            
        # 3. En ağır mı? (Şu anki max'tan büyükse yeni max bu olur)
        if pet["current"] > heaviest_pet["current"]:
            heaviest_pet = pet
            
        # 4. En hafif mi?
        if pet["current"] < lightest_pet["current"]:
            lightest_pet = pet

        # Bölünen: Toplam Ağırlık, Bölen: Hayvan Sayısı
    average_weight = safe_divide(total_weight, total_pets)
    print("=== Summary ===")
    print(f"Total pets: {total_pets}")
    # {:.2f} koyarak virgülden sonra 2 basamak gösterirsin, şık durur
    print(f"Average current weight: {average_weight:.2f} kg") 
    
    print(f"Heaviest pet: {heaviest_pet['name']} ({heaviest_pet['current']} kg)")
    print(f"Lightest pet: {lightest_pet['name']} ({lightest_pet['current']} kg)")
    
    print(f"Number of CRITICAL cases: {critical_count}")

        
    # WRITE YOUR CODE BELOW
    # ---------------------
     # TODO: remove this pass after implementing your solution
    # ---------------------


# ---------- MAIN PROGRAM (DO NOT MODIFY) ----------

def main():
    print("=== Galactic Pet Health System ===")
    try:
        pets = read_pets()
        analyze_pets(pets)
    except AssertionError as e:
        print("Assertion failed:", e)
    finally:
        print("\nProgram finished. (finally block executed.)")


if __name__ == "__main__":
    main()
