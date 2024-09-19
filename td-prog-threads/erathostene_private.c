#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <stdbool.h>

#define MAX_THREADS 10
#define FINISH_VALUE -10
#define FILTERED_VALUE = -1

int createdThread = 0;

typedef struct {
    int filter;
    int *values;
    int value_len;
} thread_data;

void *thread_fall(void *data) {
    int *InputPipe = (int *)data;
    int pipeR = InputPipe[0];
    int value;
    read(pipeR, &value, sizeof(value));
    if (value == FINISH_VALUE) {
        return NULL;
    } else {
        printf("No more filter available, %d fall.\n", value);
    }
}

void *thread_filter(void *data) {
    int *InputPipe = (int *)data;
    int pipeR = InputPipe[0];
    int filter;
    read(pipeR, &filter, sizeof(filter));
    printf("%d, ", filter);

    int nextPipe[2];
    bool nextInit = false;
    pthread_t next;

    int value;
    while (value != FINISH_VALUE) {
        read(pipeR, &value, sizeof(value));
        // printf("filter %d, read=%d\n", filter, value);
        if (value == FINISH_VALUE) {
            write(nextPipe[1], &value, sizeof(value));
            break;
        } else if (value % filter == 0) {
            continue;
        } else if (!nextInit) {
            pipe(nextPipe);

            if (createdThread >= MAX_THREADS)
            {

                pthread_create(&next, NULL, *thread_fall, (void *)nextPipe);
            }
            else
            {
                pthread_create(&next, NULL, *thread_filter, (void *)nextPipe);
            }

            write(nextPipe[1], &value, sizeof(value));
            nextInit = true;
        } else {
            write(nextPipe[1], &value, sizeof(value));
        }
    }

    if (nextInit) {
        pthread_join(next, NULL);
    }
    return 0;
}

int main(void) {
    // parse input
    int number;
    int nbvalue = 0;
    int *values = malloc(sizeof(int) * nbvalue);

    while (scanf("%d", &number) == 1) {
        nbvalue++;
        values = realloc(values, sizeof(int) * nbvalue);
        values[nbvalue - 1] = number;
    }

    pthread_t thread;
    int firstFilterPipe[2];
    pipe(firstFilterPipe);

    pthread_create(&thread, NULL, *thread_filter, (void *)firstFilterPipe);

    for (int i = 2; i < nbvalue + 2; i++) {
        write(firstFilterPipe[1], &i, sizeof(i));
    }
    
    int stop = FINISH_VALUE;
    write(firstFilterPipe[1], &stop, sizeof(stop));

    pthread_join(thread, NULL);
    printf("\n");
    free(values);
    return EXIT_SUCCESS;
}