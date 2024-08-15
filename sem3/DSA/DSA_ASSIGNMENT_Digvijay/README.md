# Assignment Guide

## Logical Units and Terminologies

1. **Song**: Each song is identified by a unique non-negative integer identifier.
2. **Playlist**: A playlist is a collection of songs. We can add songs, delete songs, and search for songs from it.
3. **Play Queue**: A song queue specifies the prioritized order in which the songs need to play next. If the queue is non-empty, the next song to be played is always from this queue and not from the playlist.
4. **Shuffling**: Shuffle the order of songs stored in the playlist. Shuffling is done by a combination of KSwap and reverse operations.
5. **KSwap**: Given an integer `k`, swap the node at position `i` with the node at position `i+k` up to the point where `i+k` is less than the size of the linked list. The swap is performed for nodes that satisfy `0 <= i+k < n` where `n` is the length of the linked list and `0 <= i < n` and `0 <= k < n`.

### Example of a Shuffle Operation

- The swaps and changes to the linked list should be done on nodes, not just values. Carefully observe the address values below the nodes at each iteration in the image provided.

## Choice of Data Structures

1. **Playlist**: The ideal data structure for modeling a playlist would be a doubly linked list. This is useful because new songs can be added, or old ones can be removed from the playlist at any point. Additionally, it should support playing (querying) the previous song, next song, and (current + i)’th song on the playlist.
2. **Play Queue**: A queue abstract data type (ADT) to follow FIFO. The ADT can be implemented using either a linked list or an array. For this assignment, we use the linked list implementation of the queue as it allows for dynamic resizing of the data structure.

## Files to Complete

### 1. `dll.c`

Implementation file for all the basic doubly linked list operations:

- `void insert_front(list_t* list, int data);`  
  Inserts data at the beginning of the linked list.
  
- `void insert_back(list_t* list, int data);`  
  Inserts data at the end of the linked list.
  
- `void insert_after(list_t* list, int data, int prev);`  
  Inserts data after the node with `data` as “prev”.
  
- `void delete_front(list_t* list);`  
  Deletes the start node from the linked list.
  
- `void delete_back(list_t* list);`  
  Deletes the end node from the linked list.
  
- `void delete_node(list_t* list, int data);`  
  Deletes the first occurrence of the node with `data` as “data” from the linked list.
  
- `node_t* search(list_t* list, int data);`  
  Returns the pointer to the node with `data` as “data” field.

### 2. `queue.c`

Implementation file for all the basic queue operations (using the functions from `dll.c`):

- `void enqueue(queue_t* q, int data);`  
  Insert data into the queue.
  
- `int dequeue(queue_t* q);`  
  Return the data at the front of the queue and delete it. Return `-1` if the queue is empty.
  
- `int front(queue_t* q);`  
  Return the data at the front of the queue. Return `-1` if the queue is empty.

### 3. `music_player.c`

Implementation file for all the music player platform operations (using the functions from `dll.c` and `queue.c`):

- `void add_song(playlist_t* list, int song_id, int where);`  
  Add a song to the playlist:
  - If `where` is `-1`, add the song to the start of the playlist.
  - If `where` is `-2`, add the song to the end of the playlist.
  - If `where` is non-negative, add the song after the song with `id = where` in the playlist.
  
- `void delete_song(playlist_t* playlist, int song_id);`  
  Remove the song with the given song id from the playlist.
  
- `song_t* search_song(playlist_t* playlist, int song_id);`  
  Return a pointer to the node where the `song_id` is present in the playlist.
  
- `void play_next(playlist_t* playlist, music_queue_t* q);`  
  Play the next song in the linked list with reference to the last played song or play from the queue, considering the following rules:
  1. Play the next song in the linked list if the queue is empty.
  2. If the queue is not empty, play from the queue rather than the next song in the list.
  3. If there was no song that was played last, play the first song on the list.
  4. If there is no next song in the playlist, play the first song of the playlist and follow the list order for further `play_next` calls.
  5. If there are no songs yet in the playlist, return from the function without doing anything.
  
- `void play_previous(playlist_t* playlist);`  
  Play the previous song in the linked list with reference to the last played song:
  1. If the previous song in the playlist is not present, play the last song of the list and follow the reverse order of the list from the last song for further `play_previous` calls.
  2. No need to check for previously played songs from the queue (they would have been removed from the queue), i.e., always play the previous song from the playlist when this function is called.
  3. If there was no song that was played last, play the last song on the list.
  4. If there are no songs yet in the playlist, return from the function without doing anything.
  
- `void search_and_play(playlist_t* playlist, int song_id);`  
  Play the song with the given `song_id` from the list (no need to bother about the queue). A call to this function should always play the given song, and further calls to `play_next` and `play_previous`.
  
- `void play_from_queue(playlist_t* q);`  
  Play a song from the queue.
  
- `void insert_to_queue(music_queue_t* q, int song_id);`  
  Insert a song id into the queue.
  
- `void reverse(playlist_t* playlist);`  
  Reverse the order of the songs in the given playlist (swap the nodes, not data).
  
- `void k_swap(playlist_t* playlist);`  
  Swap the node at position `i` with the node at position `i+k` up to the point where `i+k` is less than the size of the linked list.
  
- `void shuffle(playlist_t* playlist, int k);`  
  Perform `k_swap` and `reverse` in the order: `k_swap` first and `reverse` next.
  
- `song_t* debug(playlist_t* playlist);`  
  If the given linked list has a cycle, return the start of the cycle; else return `null`. Check cycles only in the forward direction (i.e., with the `next` pointer). No need to check for cycles in the backward pointer.

## Extra Tips

- Playing a song should be simulated by calling the `void play_song(int song_id);` function, which is already implemented.
- Any boundary conditions where you feel that you need to include a print statement (e.g., underflow, overflow, linked list is empty, etc.) should not print anything to `STDOUT`. Instead, just return from the function without doing anything, unless explicitly specified.
- Do not take any inputs from `STDIN` and do not print anything to `STDOUT`.

## Running the Makefile

### For OSes Except Windows:

1. `make compile` - Creates an executable.
2. `make run` - Runs the executable.
3. `make clean` - Deletes the executable and object files.

### For Windows OS:

1. `make -f makefile.mk compile` - Creates an executable.
2. `make -f makefile.mk run` - Runs the executable.
3. `make -f makefile.mk clean` - Deletes the executable and object files.


Credits: PESU University