#!/bin/bash

file="in.txt"

declare -a arr

while read w; do
      arr+=("$w")
done <<< ( sort in.txt | uniq -c )

for item in "${arr[@]}"; do
  echo "$item"
done


# words=()
# echo "Type words (type x to stop). Ctrl-D to finish."

# while read -r -a input; do        # read a line and split into words (default IFS)
#     for w in "${input[@]}"; do
#         if [[ "$w" == "x" ]]; then
#             echo "Stopping input."
#             printf '%s\n' "${words[@]}"
#             exit 0
#         fi
#         words+=("$w")
#     done
# done
# while IFS= read -r -a input; do
#     for w in "${input[@]}"; do
#         if [[ $w == "x" ]]; then
#             echo "Stopping input."
#             echo "Collected words: ${words[*]}"
#             exit 0
#         fi
#         words+=("$w")
#     done
# done

# # If we reach EOF (Ctrl-D), print collected words:
# echo "EOF reached. Collected words:"
# printf '%s\n' "${words[@]}