## Movie Buffer Simulator
    I built a tiny simulator to understand how streaming apps (like Netflix) buffer video in small chunks.
    This is a beginner-friendly version — simple and clear — so you can see the sliding-window idea in action.

## What this project does
    The simulator treats a video as a list of chunks (1, 2, 3, ...). The player has a small buffer that holds a fixed number of chunks.
    We load chunks until the buffer is full, then play the first chunk and repeat — sliding the buffer forward as we go.

## Files
    movie_buffer.py — the Python script.
    movie_buffer_run.py - the python script to run

## How it uses the sliding window idea
    1. The buffer (a range of chunk indices) is our sliding window.
  
    2. add to the right (load new chunks) and remove from the left (play watched chunks).
  
    3. Start and end pointers move forward only — efficient and simple.

## License
    Feel free to use and tweak this however you want. (MIT-style, go ahead and share!)



## Quick start (run locally)
     **in your terminal
    python movie_buffer_run.py
## Example output
    This is what you should see when you run the script with video_chunks = [1,2,3,4,5] and buffer_size = 2:

    Loading chunk 1...
    Loading chunk 2...
    Playing chunk 1...
    Loading chunk 3...
    Playing chunk 2...
    Loading chunk 4...
    Playing chunk 3...
    Loading chunk 5...
    Playing chunk 4...
    Playing chunk 5...
    Movie finished! 🍿
## What I learned building this
    1. Real streaming apps don’t load a whole movie at once — they load parts ahead of what you’re watching.
    
    2.How to implement a fixed-size sliding window (very handy!).
    
    3. Reusing work (update the window) instead of recalculating from scratch saves time and makes the logic clean.
