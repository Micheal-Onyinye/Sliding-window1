# movie Buffer Simulator 


def movie_buffer(video_chunks,window_size):
  start=0 #starting point of the window
  end = 0 #end point of the window
  loaded_chunks = 0

  while start < len(video_chunks):
    #load until buffer is full or has ran out of chunks
    while loaded_chunks < window_size and end < len(video_chunks):
      print(f"Loading chunk{video_chunks[end]} ...")

      end += 1
      loaded_chunks += 1

      # Play the first chunk in buffer
    print(f"Playing chunk {video_chunks[start]}...")

    start += 1

    loaded_chunks -= 1



  print("Movie finished! 🍿")




