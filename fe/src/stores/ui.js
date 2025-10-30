import { defineStore } from 'pinia'

export const useUiStore = defineStore('ui', {
    state: () => ({
        loadingCount: 0
    }),
    getters: {
        isLoading: (state) => state.loadingCount > 0
    },
    actions: {
        incrementLoading() {
            this.loadingCount += 1
        },
        decrementLoading() {
            if (this.loadingCount > 0) this.loadingCount -= 1
        },
        resetLoading() {
            this.loadingCount = 0
        }
    }
})


