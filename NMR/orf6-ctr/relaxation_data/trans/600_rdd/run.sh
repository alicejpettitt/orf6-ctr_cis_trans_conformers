## create script to sort all the files, need tau, intensity and esd in blocks of 8 (8 delay times) 
# make a file for the 4 columns 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#!/bin/bash

# with help from my pal chatgpt 

# List of input files - might be an easier way to do this but i cba right now - 11th aug 23 
files="S43N-HN.out L44N-HN.out T45N-HN.out E46N-HN.out N47N-HN.out K48N-HN.out Y49N-HN.out S50N-HN.out Q51N-HN.out L52N-HN.out D53N-HN.out E54N-HN.out E55N-HN.out Q56N-HN.out M58N-HN.out E59N-HN.out I60N-HN.out D61N-HN.out"

# Iterate over each file
for filename in $files; do
    # Extract the numeric part from the filename
    file_number=$(echo "$filename" | grep -oE '[0-9]+')

    # Remove lines starting with a '#' from the start and save to a new file
    sed '/^#/d' "$filename" > temp.txt

    # Rearrange the data and output to output.txt
    entries_per_column=8
    output_file="Four_rates_${file_number}.out"  # Use the extracted number in the output filename

    # Clear the output file
    > "$output_file"

    # Loop to rearrange data
    for ((i = 0; i < entries_per_column; i++)); do
        sed -n "$((i + 1))p;$((i + entries_per_column + 1))p;$((i + 2*entries_per_column + 1))p;$((i + 3*entries_per_column + 1))p" temp.txt \
            | awk '{printf "%s\t\t%s\t\t%s\t\t", $1, $2, $3}' \
            >> "$output_file"
        echo "" >> "$output_file"  # Add newline after each line of data
    done

    # Remove temp.txt - adios 
    rm temp.txt

    # lmk what happened 
    echo "Data from $filename has been rearranged and saved to $output_file"
done
~     
