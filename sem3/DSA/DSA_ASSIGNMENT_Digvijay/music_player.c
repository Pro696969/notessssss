#include "queue.h"
#include "dll.h"
#include "music_player.h"
#include <stdio.h>
#include <stdlib.h>

playlist_t *create_playlist() // return a newly created doubly linked list
{
	// DO NOT MODIFY!!!
	playlist_t *playlist = (playlist_t *)malloc(sizeof(playlist_t));
	playlist->list = create_list();
	playlist->num_songs = 0;
	playlist->last_song = NULL;
	return playlist;
}

void delete_playlist(playlist_t *playlist) // delete the playlist
{
	// DO NOT MODIFY!!!
	delete_list(playlist->list);
	free(playlist);
}

music_queue_t *create_music_queue() // return a newly created queue
{
	// DO NOT MODIFY!!!
	return create_queue();
}

void clear_music_queue(music_queue_t *q) // clear the queue q
{
	// DO NOT MODIFY!!!
	delete_queue(q);
}

void add_song(playlist_t *playlist, int song_id, int where) // TODO: add a song id to the playlist
{

}

void delete_song(playlist_t *playlist, int song_id) // TODO: remove song id from the playlist
{

}

song_t *search_song(playlist_t *playlist, int song_id) // TODO: return a pointer to the node where the song id is present in the playlist
{

}

void play_next(playlist_t *playlist, music_queue_t *q) // TODO: play the next song in the linked list if the queue is empty. If the queue if not empty, play from the queue
{
	
}

void play_previous(playlist_t *playlist) // TODO: play the previous song from the linked list
{
	
}

void search_and_play(playlist_t *playlist, int song_id) // TODO: play the song with given song_id from the list(no need to bother about the queue. Call to this function should always play the given song and further calls to play_next and play_previous)
{
	
}

void play_from_queue(music_queue_t *q) // TODO: play a song from the queue
{
	
}

void insert_to_queue(music_queue_t *q, int song_id) // TODO: insert a song id to the queue
{
	
}

void reverse(playlist_t *playlist) // TODO: reverse the order of the songs in the given playlist. (Swap the nodes, not data)
{
	
}

void k_swap(playlist_t *playlist, int k) // TODO: swap the node at position i with node at position i+k upto the point where i+k is less than the size of the linked list
{
	
}

void shuffle(playlist_t *playlist, int k) // TODO: perform k_swap and reverse
{

}

song_t *debug(playlist_t *playlist) // TODO: if the given linked list has a cycle, return the start of the cycle, else return null. Check cycles only in forward direction i.e with the next pointer. No need to check for cycles in the backward pointer.
{
	
}

void display_playlist(playlist_t *p) // Displays the playlist
{
	// DO NOT MODIFY!!!
	display_list(p->list);
}

void play_song(int song_id)
{
	// DO NOT MODIFY!!!
	printf("Playing: %d\n", song_id);
}
