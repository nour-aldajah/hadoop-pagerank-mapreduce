# Hadoop PageRank with MapReduce

## About the project
This project implements one iteration of the PageRank algorithm using Hadoop Streaming and Python MapReduce. The mapper distributes each page's rank across its outgoing links, and the reducer combines the contributions to calculate updated page ranks.

## Files
- `mapper.py` — distributes PageRank contributions to linked pages.
- `reducer.py` — combines contributions and calculates updated ranks.

## Requirements
- Hadoop with Hadoop Streaming
- Python 3
- An input text file where each line contains a page ID followed by its outgoing links, separated by commas.

## Run
Upload the input file to HDFS, then run the mapper and reducer with Hadoop Streaming. Update `TOTAL_PAGES` in both scripts to match the number of pages in the input.

## Output
The output lists each page and its calculated PageRank for one iteration.

## Note
This is an educational implementation. The result depends on the input graph and the `TOTAL_PAGES` value.
