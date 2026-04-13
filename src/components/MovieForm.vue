<template>
  <div class="container mt-4">
    <h2>Add Movie</h2>

    <div v-if="successMessage" class="alert alert-success" role="alert">
      {{ successMessage }}
    </div>

    <div v-if="errorMessages.length" class="alert alert-danger" role="alert">
      <ul class="mb-0">
        <li v-for="(err, idx) in errorMessages" :key="idx">{{ err }}</li>
      </ul>
    </div>

    <form id="movieForm" @submit.prevent="saveMovie" enctype="multipart/form-data">
      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input type="text" id="title" name="title" class="form-control" />
      </div>

      <div class="form-group mb-3">
        <label for="description" class="form-label">Description</label>
        <textarea id="description" name="description" class="form-control"></textarea>
      </div>

      <div class="form-group mb-3">
        <label for="poster" class="form-label">Photo Upload</label>
        <input type="file" id="poster" name="poster" class="form-control" />
      </div>

      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

let csrf_token = ref("");
let successMessage = ref("");
let errorMessages = ref([]);

function getCsrfToken() {
  fetch("/api/v1/csrf-token")
    .then((response) => response.json())
    .then((data) => {
      csrf_token.value = data.csrf_token;
    })
    .catch((error) => {
      console.log(error);
    });
}

function saveMovie() {
  successMessage.value = "";
  errorMessages.value = [];

  let movieForm = document.getElementById("movieForm");
  let form_data = new FormData(movieForm);

  fetch("/api/v1/movies", {
    method: "POST",
    body: form_data,
    headers: {
      "X-CSRFToken": csrf_token.value
    }
  })
    .then(async (response) => {
      const data = await response.json();
      return { ok: response.ok, status: response.status, data };
    })
    .then(({ ok, data }) => {
      if (ok) {
        successMessage.value = data.message || "Movie Successfully added";
        movieForm.reset();
        return;
      }

      if (Array.isArray(data?.errors)) {
        errorMessages.value = data.errors;
        return;
      }

      errorMessages.value = ["An unexpected error occurred."];
    })
    .catch((error) => {
      console.log(error);
      errorMessages.value = ["Network error. Please try again."];
    });
}

onMounted(() => {
  getCsrfToken();
});
</script>