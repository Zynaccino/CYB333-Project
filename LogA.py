try:
    webapp = open("webapp.log", "r")
    failed_attempt_count = 0
    UNA_count = 0
    failed_users = {}
    API_error_count = 0

    for line in webapp:
            
        if "login failed" in line.lower():
            failed_attempt_count += 1
            print(line.strip())
            data_part = line.split(":")[-1]
            pairs = data_part.split(", ")
            user_id = None
            print(pairs)

            for item in pairs:
                key, value = item.split("=")
                if key.strip() == "user_id":
                    user_id = value.strip()
            
            if user_id:
                if user_id in failed_users:
                    failed_users[user_id] += 1
                else:
                    failed_users[user_id] = 1
        
        if "unauthorized access" in line.lower():
           UNA_count += 1
           print(line.strip())
           data_part = line.split(":")[-1]
           pairs = data_part.split(", ")
           print(pairs)

           for item in pairs:
                key, value = item.split("=")
                print(key.strip(), value.strip())

        if "api error" in line.lower():
            API_error_count += 1
            print( line.strip())
            data_part = line.split("API error:")[-1].strip()
            pairs = data_part.split(", message=", 1)

            print(pairs)


     
    print(f"Total failed attempts: {failed_attempt_count}")
    print(f"Total Unauthorized access attempts: {UNA_count}")
    print(f"Total API error: {API_error_count}")

    for user_id, attempts in failed_users.items():
        print(f"User {user_id} failed {attempts} times")

except FileNotFoundError:
    print("The file webapp.log was not found.")
