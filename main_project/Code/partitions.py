def main():
    IP = [0] * 20
    
    for N in range(1, 21):
        print(f"{N:10d}")
        
        # Initialize: N followed by zeros
        IP = [N] + [0] * 19
        print("".join(f"{val:3d}" for val in IP))
        
        while True:
            # Find rightmost part > 1 (Fortran uses 1-based indexing)
            J = 0
            while J < 20 and IP[J] > 1:
                J += 1
            
            # J now points to first part <= 1 or end of array
            # In Fortran, J would be the index where we stop
            
            if J == 0:  # All parts are 1, we're done
                break
            
            # The part to modify is at position J-1 (since we overshot by 1)
            part_to_modify = J - 1
            
            # Calculate sum of parts before the one we're modifying
            sum_before = sum(IP[:part_to_modify])
            remaining = N - sum_before
            
            current_value = IP[part_to_modify]
            new_value = current_value - 1
            
            # How many times we can use the new value
            count = remaining // new_value
            remainder = remaining % new_value
            
            # Update the partition
            for i in range(count):
                if part_to_modify + i < 20:
                    IP[part_to_modify + i] = new_value
            
            if part_to_modify + count < 20:
                IP[part_to_modify + count] = remainder
            
            # Zero out the rest
            next_position = part_to_modify + count + (1 if remainder > 0 else 0)
            for i in range(next_position, 20):
                IP[i] = 0
            
            print("".join(f"{val:3d}" for val in IP))
        
        print()
    
    print("Program completed")

if __name__ == "__main__":
    main()