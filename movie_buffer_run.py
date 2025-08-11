from movie_buffer import movie_buffer


video_chunks = [1, 2, 3, 4, 5] # movie chunks

window_size = 2 # can hold 2 chunks at once

movie_buffer(video_chunks, window_size)