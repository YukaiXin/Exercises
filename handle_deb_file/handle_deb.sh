
sort -k 1,1 -k2,2n regions.bed  >  sort_regions.bed

python3 chr_position_arg.py sort_regions.bed > all_position.txt
