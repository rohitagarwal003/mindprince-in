package main

import (
	"log"
	"net/http"
	"os"
)

func redirect(w http.ResponseWriter, r *http.Request) {
	http.Redirect(w, r, "https://www.rohitagarwal.org"+r.URL.Path, 301)
}

func main() {
	http.HandleFunc("/", redirect)

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}

	if err := http.ListenAndServe(":"+port, nil); err != nil {
		log.Fatal(err)
	}
}
