#ifndef MUSIC_PLAYER_H
#define MUSIC_PLAYER_H
#include "dll.h"
#include "queue.h"

typedef node_t song_t;
typedef queue_t music_queue_t;

struct playlist
{
	list_t* list;
	int num_songs;
	song_t* last_song; // last played song		
};

typedef struct playlist playlist_t;

playlist_t* create_playlist(); // return a newly created doubly linked list
void delete_playlist(playlist_t* playlist); // delete the playlist
music_queue_t* create_music_queue(); // return a newly created queue
void clear_music_queue(music_queue_t* q); // clear the queue q
void add_song(playlist_t* playlist, int id, int where); // add a song id to playlist
void delete_song(playlist_t* playlist, int id); // remove song id from the playlist
song_t* search_song(playlist_t* playlist, int id); // return a pointer to the node where the song id is present in the playlist
void search_and_play(playlist_t* playlist, int song_id) ; // play the song with given song_id from the list(no need to bother about the queue. Call to this function should always play the given song and further calls to play_next and play_previous)
void play_next(playlist_t* playlist, music_queue_t* q); // play the next song in the linked list if the queue is empty. If the queue if not empty, play from the queue
void play_previous(playlist_t* playlist); // play the previous song from the linked list
void play_from_queue(music_queue_t* q); // play a song from the queue
void insert_to_queue(music_queue_t* q, int id); // insert a song id to the queue
void reverse(playlist_t* playlist); // reverse the order of the songs in the given playlist. (Swap the nodes, not data)
void k_swap(playlist_t* playlist, int k); // swap the node at position i with node at position i+k upto the point where i+k is less than the size of the linked list
void shuffle(playlist_t* playlist, int k); // perform k_swap and reverse
song_t* debug(playlist_t* playlist); // if the given linked list has a cycle, return the start of the cycle, else return null. Check cycles only in forward direction i.e with the next pointer. No need to check for cycles in the backward pointer.
void display_playlist(playlist_t* p); // Displays the playlist
void play_song(int song_id); // DO NOT MODIFY: Call this function, to simulate playing of a song


#endif
