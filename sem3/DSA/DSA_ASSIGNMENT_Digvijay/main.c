#include "queue.h"
#include "dll.h"
#include "music_player.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

playlist_t *create_buggy_playlist(int n, int s)
{
    playlist_t *pl = create_playlist();
    node_t *start = NULL;
    for (int i = 0; i < n; i++)
    {
        add_song(pl, i, -1);
        if (i == s)
        {
            start = pl->list->head;
        }
    }

    pl->list->tail->next = start;

    return pl;
}

int main()
{
    int lines;
    FILE *fptr;

    if ((fptr = fopen("sample_input2.txt", "r")) == NULL)
    {
        printf("Error! opening file");
        exit(1);
    }

    fscanf(fptr, "%d", &lines);
    char operation[20];
    char ops[2];
    playlist_t *p;
    music_queue_t *mq;
    int id, where, song_id, k, s, n;
    song_t *song;

    for (int i = 0; i < lines; i++)
    {
        fscanf(fptr, "%s", operation);
        if (strcmp(operation, "create_playlist") == 0)
        {
            p = create_playlist();
        }
        else if (strcmp(operation, "delete_playlist") == 0)
        {
            delete_playlist(p);
        }
        else if (strcmp(operation, "create_music_queue") == 0)
        {
            mq = create_music_queue();
        }
        else if (strcmp(operation, "clear_music_queue") == 0)
        {
            clear_music_queue(mq);
        }
        else if (strcmp(operation, "add_song") == 0)
        {
            fscanf(fptr, "%d %d", &id, &where);
            add_song(p, id, where);
        }
        else if (strcmp(operation, "delete_song") == 0)
        {
            fscanf(fptr, "%d", &id);
            delete_song(p, id);
        }
        else if (strcmp(operation, "search_and_play") == 0)
        {
            fscanf(fptr, "%d", &song_id);
            search_and_play(p, song_id);
        }
        else if (strcmp(operation, "play_next") == 0)
        {
            play_next(p, mq);
        }
        else if (strcmp(operation, "play_previous") == 0)
        {
            play_previous(p);
        }
        else if (strcmp(operation, "insert_to_queue") == 0)
        {
            fscanf(fptr, "%d", &id);
            insert_to_queue(mq, id);
        }
        else if (strcmp(operation, "shuffle") == 0)
        {
            fscanf(fptr, "%d", &k);

            shuffle(p, k);
        }
        else if (strcmp(operation, "debug") == 0)
        {
            fscanf(fptr, "%d %d", &n, &s);
            playlist_t *bp = create_buggy_playlist(n, s);
            song = debug(bp);
            if (song != NULL)
            {
                printf("Found cycle at: %d\n", song->data);
            }
            else
            {
                printf("No loop!\n");
            }
        }
        else if (strcmp(operation, "display_playlist") == 0)
        {
            display_playlist(p);
        }
        else
        {
            printf("Invalid Input Format!\n");
            exit(0);
        }
    }

    fclose(fptr);
    return 0;
}
