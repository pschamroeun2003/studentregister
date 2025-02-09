<template>
  <div class="full-screen">
    <h1 id="topic" class="text-2xl font-semibold mb-4">Course</h1>
    <div class="overflow-x-auto">
      <table class="min-w-full table-auto bg-white shadow-md rounded-lg overflow-hidden">
        <thead>
          <tr class="bg-gray-100 text-left text-sm font-semibold text-gray-600">
            <th class="py-2 px-4 border">Name</th>
            <th class="py-2 px-4 border">Code</th>
            <th class="py-2 px-4 border">Credits</th>
            <th class="py-2 px-4 border">Department</th>
            <th class="py-2 px-4 border">Created At</th>
            <th class="py-2 px-4 border">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr class="hover:bg-gray-50">
            <td class="py-2 px-4 border">John</td>
            <td class="py-2 px-4 border">Doe</td>
            <td class="py-2 px-4 border">01/01/2000</td>
            <td class="py-2 px-4 border">Male</td>
            <td class="py-2 px-4 border">johndoe@example.com</td>
            <td class="py-2 px-4 border">+123456789</td>
            <td class="py-2 px-4 border">123 Street, City</td>
            <td class="py-2 px-4 border">01/01/2022</td>
            <td class="py-2 px-4 border text-center">
              <button class="bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600">
                Update
              </button>
              <button
                class="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600 ml-2"
              >
                Delete
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import axios from "axios"; // Import Axios
import VITE_APP_BASE_URL from "VITE_APP_BASE_URL"
export default defineComponent({
  name: "CoursePage",
  setup() {
    const courses = ref([]);
    const errorMessage = ref(""); // To handle error messages
    const loading = ref(true); // To handle loading state

    onMounted(async () => {
      try {
         const baseUrl = import.meta.env.VITE_APP_BASE_URL || "http://127.0.0.1:5000";

        // Make an Axios GET request
        const response = await axios.get(`${baseUrl}/api/courses/course`);

        // Assuming the response structure is { courses: [...] }
        courses.value = response.data.courses || []; // Store courses in the ref
        console.log(courses.value); // Log the courses to the console
      } catch (error) {
        // Handle error if the request fails
        errorMessage.value = `Error fetching courses: ${error.message}`;
        console.error("Error fetching courses:", error);
      } finally {
        loading.value = false; // Stop loading once the data is fetched
      }
    });

    return {
      courses,
      errorMessage,
      loading,
    };
  },
});
</script>

<style scoped>
@font-face {
  font-family: "ArialCustom";
  src: url("@/assets/fonts/arialceb.ttf") format("truetype");
}

html,
body {
  height: 100%;
  margin: 0;
  font-family: "ArialCustom", Arial, sans-serif;
}
#topic {
  font-family: "ArialCustom", Arial, sans-serif;
}
.full-screen {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  padding: 10px;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th,
td {
  padding: 10px;
  text-align: left;
  border: 1px solid #e5e7eb;
  font-family: "ArialCustom", Arial, sans-serif;
}

/* Striped rows */
tr:nth-child(even) {
  background-color: #f9fafb;
}

/* Hover effect */
tr:hover {
  background-color: #f1f5f9;
}
</style>
