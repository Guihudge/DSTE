#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

typedef struct {
    int filter;
    int *values;
    int value_len;
} thread_data;

void *thread_filter(void *thdata) {
    thread_data *data;
    data = (thread_data *)thdata;
    int next_filter = -1;
    pthread_t me = pthread_self();
    pthread_t child;
    printf("Hi from thread %lu, with filter=%d\n", me, data->filter);
    // Crible
    for (int i = 0; i < data->value_len; i++) {
        if (data->values[i] == -1 || data->values[i] <= data->filter) {
            continue;
        } else if (data->values[i] % data->filter == 0) {
            data->values[i] = -1;
        } else if (next_filter == -1) {
            next_filter = data->values[i];
            thread_data *next_data = malloc(sizeof(thread_data));
            next_data->filter = next_filter;
            next_data->values = data->values;
            next_data->value_len = data->value_len;

            pthread_create(&child, NULL, *thread_filter, (void *)next_data);
        }
    } 
    
    if (next_filter != -1) {
        pthread_join(child, NULL);
    }
    free(data);
    printf("Goodbye from thread %lu\n", me, data->filter);
    return 0;
}

int main(void) {
    // parse input
    int number;
    int nbvalue = 0;
    int * values = malloc(sizeof(int)*nbvalue);

    while (scanf("%d", &number) == 1) {
        nbvalue ++;
        values = realloc(values, sizeof(int)*nbvalue);
        values[nbvalue-1] = number;
    }

    pthread_t thread;
    thread_data *start_data = malloc(sizeof(thread_data));
    start_data->filter = 2;
    start_data->values = values;
    start_data->value_len = nbvalue;

    pthread_create(&thread, NULL, *thread_filter, (void *)start_data);
    pthread_join(thread, NULL);

    for (int i = 0; i < nbvalue; i++) {
        if (values[i] != -1) {
            printf("%d, ", values[i]);
        }
    }
    printf("\n");

    return EXIT_SUCCESS;
}