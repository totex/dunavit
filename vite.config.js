import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
    plugins: [tailwindcss()],

    build: {
        outDir: 'dunavit/static',

        watch: {
            exclude: [
                'dunavit/static/**',
            ],
        },

        rollupOptions: {
            input: {
                main: 'frontend/js/main.js',
            },

            output: {
                entryFileNames: 'js/dunavit.min.js',
                assetFileNames: 'css/dunavit.min.css',
            },
        },
    },
})