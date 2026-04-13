<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);
let errorMessage = ref("");

function fetchMovies() {
  errorMessage.value = "";

  fetch("/api/v1/movies")
    .then(async (response) => {
      const contentType = response.headers.get("content-type") || "";
      if (!contentType.includes("application/json")) {
        throw new Error("Non-JSON response from API.");
      }
      const data = await response.json();
      return { ok: response.ok, data };
    })
    .then(({ ok, data }) => {
      if (!ok) {
        errorMessage.value = data.error || "Unable to load movies.";
        movies.value = [];
        return;
      }
      movies.value = data.movies || [];
    })
    .catch((error) => {
      console.log(error);
      errorMessage.value = "Unable to load movies.";
    });
}

onMounted(() => {
  fetchMovies();
});
</script>

<template>
  <div class="container mt-4">
    <h2 class="mb-3">Movies</h2>

    <div v-if="errorMessage" class="alert alert-danger" role="alert">
      {{ errorMessage }}
    </div>

    <div v-if="!movies.length && !errorMessage" class="alert alert-info" role="alert">
      No movies found yet.
    </div>

    <div class="row g-3" v-if="movies.length">
      <div v-for="movie in movies" :key="movie.id" class="col-12 col-md-6 col-lg-4">
        <div class="card h-100">
          <img
            class="card-img-top"
            :src="movie.poster"
            :alt="movie.title"
            style="object-fit: cover; height: 360px"
          />
          <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>
            <p class="card-text">{{ movie.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

